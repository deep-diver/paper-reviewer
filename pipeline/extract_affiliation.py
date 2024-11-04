import json
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import prompts
from configs.gemini_configs import extract_affiliation_config

def ask_gemini_for_affiliation(pdf_file_in_gemini, known_affiliations):
    model = genai.GenerativeModel(
        model_name=extract_affiliation_config["model_name"],
        generation_config=extract_affiliation_config["generation_config"],
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

    prompt = prompts["extract_affiliation"]["prompt"]
    prompt = Template(prompt).safe_substitute(known_affiliations=known_affiliations)
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_affiliation(pdf_file_in_gemini, known_affiliations_path):
    with open(known_affiliations_path, "r") as f:
        file_content = f.read()
        known_affiliations = file_content.splitlines()

    return ask_gemini_for_affiliation(pdf_file_in_gemini, known_affiliations)
