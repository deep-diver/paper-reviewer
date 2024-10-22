import json

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from pipeline.utils import prompts

MODEL_NAME = "gemini-1.5-flash-002"

def ask_gemini_for_sections(pdf_file_in_gemini):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["sections"],
            properties = {
                "sections": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                        type = content.Type.OBJECT,
                        required = ["section_title", "page_start_idx", "page_end_idx", "section_number"],
                        properties = {
                            "section_title": content.Schema(
                                type = content.Type.STRING,
                            ),
                            "page_start_idx": content.Schema(
                                type = content.Type.INTEGER,
                            ),
                            "page_end_idx": content.Schema(
                                type = content.Type.INTEGER,
                            ),
                            "section_number": content.Schema(
                                type = content.Type.INTEGER,
                            ),
                        },
                    ),
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

    prompt = prompts["extract_sections"]["prompt"]
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_sections(pdf_file_in_gemini):
    return ask_gemini_for_sections(pdf_file_in_gemini)
