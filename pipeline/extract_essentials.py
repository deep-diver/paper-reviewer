import json

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from pipeline.utils import prompts

MODEL_NAME = "gemini-1.5-flash-002"

def ask_gemini_for_essentials(pdf_file_in_gemini):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["tldr", "takeaways", "reason"],
            properties = {
                "tldr": content.Schema(
                    type = content.Type.STRING,
                ),
                "takeaways": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                        type = content.Type.STRING,
                    ),
                ),
                "reason": content.Schema(
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

    prompt = prompts["extract_essentials"]["prompt"]
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_essentials(pdf_file_in_gemini):
    return ask_gemini_for_essentials(pdf_file_in_gemini)
