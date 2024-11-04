import json
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import prompts
from configs.gemini_configs import extract_category_config

def ask_gemini_for_category(pdf_file_in_gemini, known_categories):
    model = genai.GenerativeModel(
        model_name=extract_category_config["model_name"],
        generation_config=extract_category_config["generation_config"],
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

    prompt = prompts["extract_category"]["prompt"]
    prompt = Template(prompt).safe_substitute(known_categories=str(known_categories))
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_category(pdf_file_in_gemini, known_categories_path):
    with open(known_categories_path, "r") as f:
        known_categories = json.load(f)

    return ask_gemini_for_category(pdf_file_in_gemini, known_categories)
