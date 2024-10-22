import json
import asyncio
from tqdm import tqdm

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from pipeline.utils import prompts, upload_to_gemini, wait_for_files_active

MODEL_NAME = "gemini-1.5-flash-002"

def ask_gemini_for_description(pdf_file_in_gemini, figure_path):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["description", "section"],
            properties = {
                "description": content.Schema(
                    type = content.Type.STRING,
                ),
                "section": content.Schema(
                    type = content.Type.STRING,
                ),
            },
        ),
        "response_mime_type": "application/json",        
    }

    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
            generation_config=generation_config,
    )

    figure_in_gemini = upload_to_gemini(figure_path, mime_type="image/png")
    wait_for_files_active([figure_in_gemini])

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    pdf_file_in_gemini,
                    figure_in_gemini,
                ],
            }            
        ]
    )

    prompt = prompts["describe_figure"]["prompt"]
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

async def process_figure_and_table(figure_path, pdf_file_in_gemini, pbar):
    associated_description = ask_gemini_for_description(pdf_file_in_gemini, figure_path)
    pbar.update(1)
    return {
        "figure_path": figure_path,
        "description": associated_description["description"],
        "section": associated_description["section"],
    }

async def associate_description(figure_paths, pdf_file_path, workers):
    association_results = []
    association_tasks = []

    pdf_file_in_gemini = upload_to_gemini(pdf_file_path)
    wait_for_files_active([pdf_file_in_gemini])

    semaphore = asyncio.Semaphore(workers)
    with tqdm(total=len(figure_paths)) as pbar:
        async def worker(figure_path):
            async with semaphore:
                return await process_figure_and_table(figure_path, pdf_file_in_gemini, pbar)

        association_tasks = [worker(figure_path) for figure_path in figure_paths]
        results = await asyncio.gather(*association_tasks)
        association_results.extend(result for result in results)

    return association_results, pdf_file_in_gemini