import json
import asyncio
from tqdm import tqdm
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import prompts
from configs.gemini_configs import extract_section_details_config

def ask_gemini_for_section_details(pdf_file_in_gemini, section_info):
    model = genai.GenerativeModel(
        model_name=extract_section_details_config["model_name"],
        generation_config=extract_section_details_config["generation_config"],
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    pdf_file_in_gemini,
                ],
            }            
        ]
    )

    prompt = prompts["extract_section_details"]["prompt"]
    prompt = Template(prompt).substitute(section_title=section_info["heading_title"])
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

async def process_section_info(pdf_file_in_gemini, section_info, pbar):
    section_details = ask_gemini_for_section_details(pdf_file_in_gemini, section_info)
    pbar.update(1)
    return section_details

async def extract_section_details(pdf_file_in_gemini, section_infos, workers):
    section_detail_list = []
    section_details_tasks = []

    semaphore = asyncio.Semaphore(workers)
    with tqdm(total=len(section_infos)) as pbar:
        async def worker(section_info):
            async with semaphore:
                return await process_section_info(pdf_file_in_gemini, section_info, pbar)

        section_details_tasks = [worker(section_info) for section_info in section_infos]
        results = await asyncio.gather(*section_details_tasks)
        section_detail_list.extend(result for result in results)

    return section_detail_list
