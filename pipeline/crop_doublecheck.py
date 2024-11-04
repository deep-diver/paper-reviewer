import json
import asyncio
from tqdm import tqdm
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import prompts, upload_to_gemini, wait_for_files_active
from configs.gemini_configs import double_check_config

def read_md(path):
    with open(path, 'r') as f:
        return f.read()

def ask_gemini_for_double_check(figure_path, pdf_file_in_gemini, media_type):
    model = genai.GenerativeModel(
        model_name=double_check_config["model_name"],
        generation_config=double_check_config["generation_config"],
    )

    if media_type == "table":
        media = [read_md(figure_path)]

        prompt = prompts["double_check_table"]["prompt"]
        prompt = Template(prompt).safe_substitute(table=media[0])

        parts = [pdf_file_in_gemini]

        history=[
            {
                "role": "user",
                "parts": parts
            },
        ]        
    else:
        media = [upload_to_gemini(figure_path, mime_type="image/png")]
        wait_for_files_active(media)
        parts = [pdf_file_in_gemini, media[0]]

        history=[
            {
                "role": "user",
                "parts": [
                    pdf_file_in_gemini,
                    "This is the paper PDF. Use it as a reference.",
                    media[0],
                ]
            },
        ]

        prompt = prompts["double_check_figure"]["prompt"]
        prompt = Template(prompt).safe_substitute(type=media_type)

    chat_session = model.start_chat(history=history)

    response = chat_session.send_message(prompt)
    return response.text

def double_check_figure(figure_path, pdf_file_in_gemini, media_type):
    include_figure = ask_gemini_for_double_check(figure_path, pdf_file_in_gemini, media_type)
    include_figure = json.loads(include_figure)["return"]
    return include_figure

async def process_figure_double_check(figure_path, pdf_file_in_gemini, pbar, media_type):
    figure_included = double_check_figure(figure_path, pdf_file_in_gemini, media_type)
    pbar.update(1)
    if figure_included:
        return figure_path
    else:
        return None

async def doublecheck_figures(media_paths, pdf_file_in_gemini, workers, media_type):
    double_checking_tasks = []
    double_checking_results = []

    semaphore = asyncio.Semaphore(workers)
    with tqdm(total=len(media_paths)) as pbar:
        async def worker(media_path):
            async with semaphore:
                return await process_figure_double_check(media_path, pdf_file_in_gemini, pbar, media_type)

        double_checking_tasks = [worker(media_path) for media_path in media_paths]
        results = await asyncio.gather(*double_checking_tasks)
        for result in results:
            if result is not None:
                double_checking_results.append(result)

    return double_checking_results