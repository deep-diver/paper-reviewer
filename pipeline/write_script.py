import json
import google.generativeai as genai

from pipeline.utils import prompts
from configs.gemini_configs import write_script_config

def write_script_first_half(pdf_in_gemini):
    """
    pdf_in_gemini: the pdf file in Gemini
    """
    model = genai.GenerativeModel(
        model_name=write_script_config["model_name"],
        generation_config=write_script_config["generation_config"],
    )

    history=[
        {
            "role": "user",
            "parts": [
                pdf_in_gemini,
            ],
        }
    ]

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [pdf_in_gemini],
            }
        ]
    )

    prompt = prompts["write_script"]["first_prompt"]
    response = chat_session.send_message(prompt)

    later_history = [
        {
            "role": "user",
            "parts": [prompt],
        },
        {
            "role": "assistant",
            "parts": [response.text],
        }
    ]
    history = history + later_history

    return history, json.loads(response.text)

def write_script_second_half(history):
    """
    history: the history of the chat session
    """
    model = genai.GenerativeModel(
        model_name=write_script_config["model_name"],
        generation_config=write_script_config["generation_config"],
    )

    chat_session = model.start_chat(history=history)

    prompt = prompts["write_script"]["second_prompt"]
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def write_script(pdf_in_gemini):
    """
    pdf_in_gemini: the pdf file in Gemini
    """
    history, first_half_script = write_script_first_half(pdf_in_gemini)
    second_half_script = write_script_second_half(history)
    return first_half_script["conversations"] + second_half_script["conversations"]
