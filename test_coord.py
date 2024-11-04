import os
import json
import toml
from PIL import Image
from string import Template

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from pipeline.utils import upload_to_gemini, wait_for_files_active, prompts

MODEL_NAME = "gemini-1.5-pro-002"

def ask_gemini_for_coordinates(image_path, example_path, example_path2, example_path3, example_path4, example_path5, media_type):
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
                    type = content.Type.NUMBER,
                ),
                "y_min": content.Schema(
                    type = content.Type.NUMBER,
                ),
                "x_max": content.Schema(
                    type = content.Type.NUMBER,
                ),
                "y_max": content.Schema(
                    type = content.Type.NUMBER,
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
        upload_to_gemini(example_path, mime_type="image/png"),
        upload_to_gemini(example_path2, mime_type="image/png"),
        upload_to_gemini(example_path5, mime_type="image/png"),
        upload_to_gemini(example_path3, mime_type="image/png"),
        upload_to_gemini(example_path4, mime_type="image/png"),
        upload_to_gemini(image_path, mime_type="image/png"),
    ]

    wait_for_files_active(files)

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    files[0],
                    files[1],
                    files[2],
                    "These images are examples of figures present in the image. Refer to the RED rectangle's coordinate to understand which region to extract.",
                ],
            },
            {
                "role": "user",
                "parts": [
                    files[3],
                    files[4],
                    "These images are examples that there is no figure.",
                ],
            },
            {
                "role": "user",
                "parts": [
                    files[5],
                ],
            },
        ]
    )

    prompt = prompts["extract_coordinate"]["prompt"]
    prompt = Template(prompt).safe_substitute(type=media_type)

    response = chat_session.send_message(prompt)
    return json.loads(response.text)

image_path = "test_assets/imgs/4.png"
example_path = "test_assets/imgs/example.png"
example_path2 = "test_assets/imgs/example2.png"
example_path3 = "test_assets/imgs/example3.png"
example_path4 = "test_assets/imgs/example4.png"
example_path5 = "test_assets/imgs/example5.png"
image = Image.open(image_path)  # Replace "image.jpg" with your image file
width, height = image.size

coordinate  = ask_gemini_for_coordinates(image_path, example_path, example_path2, example_path3, example_path4, example_path5, "figure")
print(coordinate)

norm_left, norm_top, norm_right, norm_bottom = coordinate["x_min"], coordinate["y_min"], coordinate["x_max"], coordinate["y_max"]

if norm_left != 0 or norm_top != 0 or norm_right != 0 or norm_bottom != 0:
    left = int(norm_left * width)
    top = int(norm_top * height)
    right = int(norm_right * width)
    bottom = int(norm_bottom * height)
    # left = int(norm_left)
    # top = int(norm_top)
    # right = int(norm_right)
    # bottom = int(norm_bottom)
    print(left, top, right, bottom)

    cropped_img = image.crop((left, top, right, bottom))
    cropped_img.save(f"test_assets/cropped/{os.path.basename(image_path)}")
else:
    print("Figure not found")
