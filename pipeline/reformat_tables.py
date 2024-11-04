import json
import asyncio
from tqdm import tqdm
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import prompts
from configs.gemini_configs import reformat_table_config

def ask_gemini_reformat_table(arxiv_id, table):
    model = genai.GenerativeModel(
        model_name=reformat_table_config["model_name"],
        generation_config=reformat_table_config["generation_config"],
    )

    chat_session = model.start_chat(history=[])

    prompt = prompts["reformat_table"]["prompt"]
    prompt = Template(prompt).substitute(
        html_table=table["content"],
        arxiv_id=arxiv_id,
    )
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

async def process_table(arxiv_id, table, pbar):
    try:
        reformated_table = ask_gemini_reformat_table(arxiv_id, table)
        pbar.update(1)
        return {
            "content": reformated_table["reformat"],
            "caption": table["caption"],
        }
    except Exception as e:
        print(f"Error reformatting table {table['caption']} on {arxiv_id}: {e}")
        pbar.update(1)
        return {
            "content": table["content"],
            "caption": table["caption"],
        }

async def reformat_tables_from_html(arxiv_id, tables, workers):
    reformat_results = []
    reformat_tasks = []

    semaphore = asyncio.Semaphore(workers)
    with tqdm(total=len(tables)) as pbar:
        async def worker(table):
            async with semaphore:
                return await process_table(arxiv_id, table, pbar)

        reformat_tasks = [worker(table) for table in tables]
        results = await asyncio.gather(*reformat_tasks)
        reformat_results.extend(result for result in results)

    return reformat_results
