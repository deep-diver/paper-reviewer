import os
import requests
from PIL import Image

def ask_upstage_document_parse(image_path):
    results = {}

    figure_coordinates = []
    chart_coordinates = []
    tables = []

    UPSTAGE_API_KEY = os.environ["UPSTAGE_API_KEY"]
    
    url = "https://api.upstage.ai/v1/document-ai/document-parse"
    headers = {"Authorization": f"Bearer {UPSTAGE_API_KEY}"}
    files = {"document": open(image_path, "rb")}
    data = {"output_formats": "['markdown', 'html']"} # in case you need both text and html
    
    response = requests.post(url, headers=headers, files=files, data=data)
    response = response.json()

    for element in response["elements"]:
        category = element["category"]

        if "figure" in category:
            figure_coordinates.append(element["coordinates"])
        elif "chart" in category:
            chart_coordinates.append(element["coordinates"])
        elif "table" in category:
            tables.append(element["content"]["html"])

    results["figure_coordinates"] = figure_coordinates
    results["chart_coordinates"] = chart_coordinates
    results["tables"] = tables
    return results

def calc_original_coordinates(coordinate, width, height):
    x_coords = [coord['x'] for coord in coordinate]
    y_coords = [coord['y'] for coord in coordinate]

    # Calculate top-left and bottom-right
    top_left = {'x': min(x_coords), 'y': min(y_coords)}
    bottom_right = {'x': max(x_coords), 'y': max(y_coords)}

    left = int(top_left['x'] * width)
    top = int(top_left['y'] * height)
    right = int(bottom_right['x'] * width)
    bottom = int(bottom_right['y'] * height)

    return left, top, right, bottom

def _crop_figures(coordinates, image, width, height, root_path, idx, prefix="figure"):
    cropped_img_paths = []
    for i, coordinate in enumerate(coordinates):
        left, top, right, bottom = calc_original_coordinates(coordinate, width, height)

        try:
            cropped_img = image.crop((left, top, right, bottom))
            cropped_img_path = f"{root_path}/{prefix}/{prefix}_{idx}_{i}.png"
            cropped_img.save(cropped_img_path)
            cropped_img_paths.append(cropped_img_path)
        except:
            continue

    return cropped_img_paths    

def _crop_tables(tables, root_path, idx):
    table_paths = []
    for i, table in enumerate(tables):
        table_path = f"{root_path}/tables/table_{idx}_{i}.html"
        with open(table_path, "w") as f:
            f.write(table)
        table_paths.append(table_path)

    return table_paths

def crop_figures(idx, image_path, root_path):
    image = Image.open(image_path)  # Replace "image.jpg" with your image file
    width, height = image.size

    # call Upstage's Document Parse to obtain left, top, right, bottom coordinates
    results = ask_upstage_document_parse(image_path)
    fig_coordinates, chart_coordinates, tables = results["figure_coordinates"], results["chart_coordinates"], results["tables"]
    fig_img_paths = _crop_figures(fig_coordinates, image, width, height, root_path, idx, prefix="figures")
    chart_img_paths = _crop_figures(chart_coordinates, image, width, height, root_path, idx, prefix="charts")
    table_paths = _crop_tables(tables, root_path, idx)

    return fig_img_paths, chart_img_paths, table_paths