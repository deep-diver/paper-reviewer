import json
import toml
from PIL import Image
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import upload_to_gemini, wait_for_files_active, prompts

MODEL_NAME = "gemini-1.5-pro-002"

def ask_gemini_for_coordinates(image_path, media_type):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["x_min", "y_min", "x_max", "y_max"],
            properties = {
                "x_min": content.Schema(
                        type = content.Type.ARRAY,
                        items = content.Schema(
                            type = content.Type.NUMBER,
                        ),
                ),
                "y_min": content.Schema(
                        type = content.Type.ARRAY,
                        items = content.Schema(
                            type = content.Type.NUMBER,
                        ),
                ),
                "x_max": content.Schema(
                        type = content.Type.ARRAY,
                        items = content.Schema(
                            type = content.Type.NUMBER,
                        ),
                ),
                "y_max": content.Schema(
                        type = content.Type.ARRAY,
                        items = content.Schema(
                            type = content.Type.NUMBER,
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

    files = [
        upload_to_gemini(image_path, mime_type="image/png"),
    ]

    wait_for_files_active(files)

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    files[0]
                ],
            },
        ]
    )

    prompt = prompts["extract_coordinates"]["prompt"]
    prompt = Template(prompt).safe_substitute(type=media_type)

    response = chat_session.send_message(prompt)
    return json.loads(response.text)

def crop_figures(idx, image_path, root_path, media_type):
    cropped_img_paths = []
    image = Image.open(image_path)  # Replace "image.jpg" with your image file
    width, height = image.size

    # call Gemini 1.5 Pro to obtain left, top, right, bottom coordinates
    coordinates = ask_gemini_for_coordinates(image_path, media_type)

    norm_lefts, norm_tops, norm_rights, norm_bottoms = coordinates["x_min"], coordinates["y_min"], coordinates["x_max"], coordinates["y_max"]
    for i, (norm_left, norm_top, norm_right, norm_bottom) in enumerate(zip(norm_lefts, norm_tops, norm_rights, norm_bottoms)):
        # scale the coordinates to the original image size
        left = int(norm_left * width)
        top = int(norm_top * height)
        right = int(norm_right * width)
        bottom = int(norm_bottom * height)

        try:
            cropped_img = image.crop((left, top, right, bottom))
            cropped_img_path = f"{root_path}/{media_type}/{media_type}_{idx}_{i}.png"
            print(cropped_img_path)
            cropped_img.save(cropped_img_path)
            cropped_img_paths.append(cropped_img_path)
        except:
            continue

    return cropped_img_paths
