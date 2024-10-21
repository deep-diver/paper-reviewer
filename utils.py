import os
import toml
import json
import requests
import time
from PIL import Image
from pdf2image import convert_from_path

import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

prompt_tmpl_path='configs/prompts.toml'
prompts = toml.load(prompt_tmpl_path)

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

    response = chat_session.send_message(prompt)
    return response.text

def ask_upstage_document_parse(image_path):
    coordinates = []
    UPSTAGE_API_KEY = os.environ["UPSTAGE_API_KEY"]
    
    url = "https://api.upstage.ai/v1/document-ai/document-parse"
    headers = {"Authorization": f"Bearer {UPSTAGE_API_KEY}"}
    files = {"document": open(image_path, "rb")}
    data = {"output_formats": "['markdown']"} # in case you need both text and html
    
    response = requests.post(url, headers=headers, files=files, data=data)
    response = response.json()

    for element in response["elements"]:
        if element["category"] == "figure" or element["category"] == "chart":
            coordinates.append(element["coordinates"])

    return coordinates

def ask_gemini_for_description(pdf_file_in_gemini, figure_path):
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

    figure_in_gemini = upload_to_gemini(figure_path, mime_type="image/png")
    wait_for_files_active([figure_in_gemini])

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    pdf_file_in_gemini,
                    figure_in_gemini,
                ],
            }            
        ]
    )

    prompt = prompts["describe_figure"]["prompt"]
    response = chat_session.send_message(prompt)
    return response.text

def ask_gemini_for_double_check(figure_path):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            required = ["response"],
            properties = {
                "response": content.Schema(
                    type = content.Type.BOOLEAN,
                ),
            },
        ),
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-8b",
        generation_config=generation_config,
    )

    files = [
        upload_to_gemini(figure_path, mime_type="image/png"),
    ]
    wait_for_files_active(files)

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    files[0],
                ],
            },
        ]
    )

    prompt = prompts["double_check_figure"]["prompt"]
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

def crop_figures_upstage(idx, image_path, root_path):
    cropped_img_paths = []
    image = Image.open(image_path)  # Replace "image.jpg" with your image file
    width, height = image.size

    # call Upstage's Document Parse to obtain left, top, right, bottom coordinates
    coordinates = ask_upstage_document_parse(image_path)

    for i, coordinate in enumerate(coordinates):
        x_coords = [coord['x'] for coord in coordinate]
        y_coords = [coord['y'] for coord in coordinate]

        # Calculate top-left and bottom-right
        top_left = {'x': min(x_coords), 'y': min(y_coords)}
        bottom_right = {'x': max(x_coords), 'y': max(y_coords)}

        left = int(top_left['x'] * width)
        top = int(top_left['y'] * height)
        right = int(bottom_right['x'] * width)
        bottom = int(bottom_right['y'] * height)

        try:
            cropped_img = image.crop((left, top, right, bottom))
            cropped_img_path = f"{root_path}/figure_{idx}_{i}.png"
            cropped_img.save(cropped_img_path)
            cropped_img_paths.append(cropped_img_path)
        except:
            continue        

    return cropped_img_paths

def associate_description(pdf_file_in_gemini, figure_path):
    desc = ask_gemini_for_description(pdf_file_in_gemini, figure_path)
    return desc

def double_check_figure(figure_path):
    include_figure = ask_gemini_for_double_check(figure_path)
    include_figure = json.loads(include_figure)["response"]
    return include_figure
