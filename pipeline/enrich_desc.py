import json
import asyncio
from tqdm import tqdm
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from pipeline.utils import prompts, upload_to_gemini, wait_for_files_active

MODEL_NAME = "gemini-1.5-flash-002"

def ask_gemini_description_from_image(pdf_file_in_gemini, media_path, media_type):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["caption", "description", "section"],
            properties = {
                "caption": content.Schema(
                    type = content.Type.STRING,
                ),
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

    if media_type == "figure" or media_type == "chart":
        media_in_gemini = upload_to_gemini(media_path, mime_type="image/png")
        wait_for_files_active([media_in_gemini])
    elif media_type == "table":
        with open(media_path, "r") as f:
            media_in_gemini = f.read()

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    pdf_file_in_gemini,
                    media_in_gemini,
                ],
            }            
        ]
    )

    prompt = prompts["describe_figure"]["prompt"]
    prompt = Template(prompt).substitute(type=media_type)
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

async def process_figure_and_table(figure_path, pdf_file_in_gemini, pbar, media_type):
    associated_description = ask_gemini_description_from_image(pdf_file_in_gemini, figure_path, media_type)
    pbar.update(1)
    return {
        "figure_path": figure_path,
        "caption": associated_description["caption"],
        "description": associated_description["description"],
        "section": associated_description["section"],
    }

async def enrich_description_from_images(media_paths, pdf_file_in_gemini, workers, media_type):
    association_results = []
    association_tasks = []

    semaphore = asyncio.Semaphore(workers)
    with tqdm(total=len(media_paths)) as pbar:
        async def worker(media_path):
            async with semaphore:
                return await process_figure_and_table(media_path, pdf_file_in_gemini, pbar, media_type)

        association_tasks = [worker(media_path) for media_path in media_paths]
        results = await asyncio.gather(*association_tasks)
        association_results.extend(result for result in results)

    return association_results


## HTML
def ask_gemini_description_from_html(pdf_file_in_gemini, figure, media_type):
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

    prompt = prompts["describe_figure_from_html"]["prompt"]
    prompt = Template(prompt).substitute(
        type=media_type,
        caption=figure["caption"],
    )
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

async def process_figure_and_table_from_html(media, pdf_file_in_gemini, pbar, media_type):
    associated_description = ask_gemini_description_from_html(pdf_file_in_gemini, media, media_type)
    pbar.update(1)
    if media_type == "figure":
        return {
            "figure_path": media["figure_path"],
            "caption": media["caption"],
            "description": associated_description["description"],
            "section": associated_description["section"],
        }
    elif media_type == "table":
        return {
            "content": media["content"],
            "caption": media["caption"],
            "description": associated_description["description"],
            "section": associated_description["section"],
        }

async def enrich_description_from_html(media_list, pdf_file_in_gemini, workers, media_type):
    association_results = []
    association_tasks = []

    semaphore = asyncio.Semaphore(workers)
    with tqdm(total=len(media_list)) as pbar:
        async def worker(media):
            async with semaphore:
                return await process_figure_and_table_from_html(media, pdf_file_in_gemini, pbar, media_type)

        association_tasks = [worker(media) for media in media_list]
        results = await asyncio.gather(*association_tasks)
        association_results.extend(result for result in results)

    return association_results