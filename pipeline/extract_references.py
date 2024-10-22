import json
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from pipeline.utils import prompts

MODEL_NAME = "gemini-1.5-flash-002"

def ask_gemini_for_references(pdf_file_in_gemini, section_infos):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["references"],
            properties = {
                "references": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                        type = content.Type.OBJECT,
                        required = ["paper_title", "fullname_first_author", " publication_date", "reason", "section_number"],
                        properties = {
                            "paper_title": content.Schema(
                                type = content.Type.STRING,
                            ),
                            "fullname_first_author": content.Schema(
                                type = content.Type.STRING,
                            ),
                            " publication_date": content.Schema(
                                type = content.Type.STRING,
                            ),
                            "reason": content.Schema(
                                type = content.Type.STRING,
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

    prompt = prompts["extract_references"]["prompt"]
    prompt = Template(prompt).substitute(target_sections=section_infos)
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_references(pdf_file_in_gemini, section_infos):
    return ask_gemini_for_references(pdf_file_in_gemini, section_infos)
