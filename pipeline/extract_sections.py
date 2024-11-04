import json

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import prompts
from configs.gemini_configs import extract_sections_config

def ask_gemini_for_sections(pdf_file_in_gemini):
    model = genai.GenerativeModel(
        model_name=extract_sections_config["model_name"],
        generation_config=extract_sections_config["generation_config"],
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

    prompt = prompts["extract_sections"]["prompt"]
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_sections(pdf_file_in_gemini):
    return ask_gemini_for_sections(pdf_file_in_gemini)
