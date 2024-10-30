import json
from string import Template
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from pipeline.utils import prompts

MODEL_NAME = "gemini-1.5-flash-8b"

def ask_gemini_for_affiliation(pdf_file_in_gemini, known_affiliations):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["affiliation"],
            properties = {
                "affiliation": content.Schema(
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

    prompt = prompts["extract_affiliation"]["prompt"]
    prompt = Template(prompt).safe_substitute(known_affiliations=known_affiliations)
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_affiliation(pdf_file_in_gemini, known_affiliations_path):
    with open(known_affiliations_path, "r") as f:
        file_content = f.read()
        known_affiliations = file_content.splitlines()

    return ask_gemini_for_affiliation(pdf_file_in_gemini, known_affiliations)
