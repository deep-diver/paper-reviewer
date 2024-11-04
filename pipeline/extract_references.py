import json
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import prompts
from configs.gemini_configs import extract_references_config

def ask_gemini_for_references(pdf_file_in_gemini, section_infos):

    model = genai.GenerativeModel(
        model_name=extract_references_config["model_name"],
        generation_config=extract_references_config["generation_config"],
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

    prompt = prompts["extract_references"]["prompt"]
    prompt = Template(prompt).substitute(target_sections=section_infos)
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_references(pdf_file_in_gemini, section_infos):
    return ask_gemini_for_references(pdf_file_in_gemini, section_infos)
