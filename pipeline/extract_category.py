import json
from string import Template
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from pipeline.utils import prompts

MODEL_NAME = "gemini-1.5-flash-8b"

def ask_gemini_for_category(pdf_file_in_gemini, known_categories):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["main_category", "sub_category"],
            properties = {
                "main_category": content.Schema(
                    type = content.Type.STRING,
                ),
                "sub_category": content.Schema(
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

    prompt = prompts["extract_category"]["prompt"]
    prompt = Template(prompt).safe_substitute(known_categories=str(known_categories))
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_category(pdf_file_in_gemini, known_categories_path):
    with open(known_categories_path, "r") as f:
        known_categories = json.load(f)

    return ask_gemini_for_category(pdf_file_in_gemini, known_categories)
