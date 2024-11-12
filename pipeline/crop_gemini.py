import json
import glob
import toml
from PIL import Image
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import upload_to_gemini, wait_for_files_active, prompts
from configs.gemini_configs import crop_config

def ask_gemini_for_coordinates(image_path, correct_examples, wrong_examples):
    model = genai.GenerativeModel(
        model_name=crop_config["model_name"],
        generation_config=crop_config["generation_config"],
    )

    target_file = upload_to_gemini(image_path, mime_type="image/png")
    wait_for_files_active([target_file])

    correct_parts = correct_examples + ["These images are examples of figures present in the image. Refer to the RED rectangle's coordinate to understand which region to extract."]
    wrong_parts = wrong_examples + ["These images are examples that there is no figure."]
    target_parts = [target_file]

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": correct_parts,
            },
            {
                "role": "user",
                "parts": wrong_parts,
            },
            {
                "role": "user",
                "parts": target_parts,
            },
        ]
    )

    prompt = prompts["extract_coordinate"]["prompt"]
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def crop_figures(idx, image_path, root_path, correct_examples, wrong_examples):
    image = Image.open(image_path)  # Replace "image.jpg" with your image file
    width, height = image.size

    # call Gemini 1.5 Pro to obtain left, top, right, bottom coordinates
    coordinate  = ask_gemini_for_coordinates(image_path, correct_examples, wrong_examples)
    norm_left, norm_top, norm_right, norm_bottom = coordinate["x_min"], coordinate["y_min"], coordinate["x_max"], coordinate["y_max"]
    
    if norm_left == 0 and norm_top == 0 and norm_right == 0 and norm_bottom == 0:
        return None

    left = int(norm_left * width)
    top = int(norm_top * height)
    right = int(norm_right * width)
    bottom = int(norm_bottom * height)

    cropped_img = image.crop((left, top, right, bottom))
    cropped_img_path = f"{root_path}/figures/figures_{idx}_0.png"
    cropped_img.save(cropped_img_path)
    return cropped_img_path


## Table extraction
def ask_gemini_for_tables(image_path):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["tables"],
            properties = {
                "tables": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                        type = content.Type.OBJECT,
                        required = ["table_html"],
                        properties = {
                            "table_html": content.Schema(
                                type = content.Type.STRING,
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

    target_file = upload_to_gemini(image_path, mime_type="image/png")
    wait_for_files_active([target_file])

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [target_file],
            },
        ]
    )

    prompt = prompts["extract_tables"]["prompt"]
    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def extract_tables(idx, image_path, root_path):
    tables = ask_gemini_for_tables(image_path)

    table_paths = []
    for i, table in enumerate(tables["tables"]):
        table_path = f"{root_path}/tables/table_{idx}_{i}.html"
        with open(table_path, "w") as f:
            f.write(table['table_html'])
        table_paths.append(table_path)

    return table_paths    
