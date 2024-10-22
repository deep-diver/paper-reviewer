import os
import requests
from PIL import Image

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

def crop_figures(idx, image_path, root_path):
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