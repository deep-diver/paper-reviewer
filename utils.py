import os
import json
import requests
import time
from PIL import Image
from pdf2image import convert_from_path

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def download_pdf(root_path, arxiv_id):
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    response = requests.get(pdf_url)

    if response.status_code == 200:
        os.mkdir(root_path)
        file_path = f"{root_path}/{arxiv_id}.pdf"

        with open(file_path, "wb") as f:
            f.write(response.content)

        return file_path
    else:
        print(f"Failed to download PDF from arXiv: {response.status_code}")
        return None

def pdf_to_images(pdf_file_path, root_path):
    images = convert_from_path(pdf_file_path)
    image_paths = []

    for i, image in enumerate(images):
        image_path = f"{root_path}/{i}.png"
        image.save(image_path)
        image_paths.append(image_path)

    return image_paths

def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini.

    See https://ai.google.dev/gemini-api/docs/prompting_with_media
    """
    file = genai.upload_file(path, mime_type=mime_type)
    return file

def wait_for_files_active(files):
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            time.sleep(10)
            file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")

def ask_gemini_for_coordinates(image_path):
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
        model_name="gemini-1.5-pro-002",
        generation_config=generation_config,
    )

    files = [
        upload_to_gemini(image_path, mime_type="image/png"),
    ]

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    files[0],
                    "extract the coordinates of figure 2 in a given image.\n(x_min, y_min, x_max, y_max)\n\nthe coordinate should cover the entire figure.\nthe coordinate should be represented in integer from 0 to 1 (floating point number)",
                ],
            },
        ]
    )

    prompt = """extract the coordinates(x_min, y_min, x_max, y_max) of figures in a given image.

the coordinate should cover the entire figure with margin.
the coordinate should be represented in integer from 0 to 1

only figures and tables are allowed to be included. no math formula.
if there is no figure, return empty array.
"""

    response = chat_session.send_message(prompt)
    return response.text

def ask_gemini_for_description(pdf_path, figure_path):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-002",
            generation_config=generation_config,
    )

    files = [
        upload_to_gemini(pdf_path, mime_type="application/pdf"),
        upload_to_gemini(figure_path, mime_type="image/png"),
    ]

    wait_for_files_active(files)

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    files[0],
                    files[1],
                ],
            }            
        ]
    )

    prompt = "based on the paper, describe the given image in detail in two paragraphs."
    response = chat_session.send_message(prompt)
    return response.text

def crop_figures(idx, image_path, root_path):
    cropped_img_paths = []
    image = Image.open(image_path)  # Replace "image.jpg" with your image file
    width, height = image.size

    # call Gemini 1.5 Pro to obtain left, top, right, bottom coordinates
    coordinates_json = ask_gemini_for_coordinates(image_path)
    coordinates = json.loads(coordinates_json)

    norm_lefts, norm_tops, norm_rights, norm_bottoms = coordinates["x_min"], coordinates["y_min"], coordinates["x_max"], coordinates["y_max"]
    for i, (norm_left, norm_top, norm_right, norm_bottom) in enumerate(zip(norm_lefts, norm_tops, norm_rights, norm_bottoms)):
        # scale the coordinates to the original image size
        left = int(norm_left * width)
        top = int(norm_top * height)
        right = int(norm_right * width)
        bottom = int(norm_bottom * height)

        try:
            cropped_img = image.crop((left, top, right, bottom))
            cropped_img_path = f"{root_path}/figure_{idx}_{i}.png"
            cropped_img.save(cropped_img_path)
            cropped_img_paths.append(cropped_img_path)
        except:
            continue

    return cropped_img_paths

def associate_description(pdf_path, figure_path):
    desc = ask_gemini_for_description(pdf_path, figure_path)
    return desc