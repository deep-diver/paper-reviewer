import shutil
import json
import os
import arxiv
import requests
from paperswithcode import PapersWithCodeClient

def get_paperswithcode_url(arxiv_id):
    client = PapersWithCodeClient()
    papers = client.paper_list(arxiv_id=arxiv_id).results
    if len(papers) == 0:
        return None
    paper = papers[0]
    return f"https://paperswithcode.com/paper/{paper.id}"

def copy_directory(src, dst):
  try:
    shutil.copytree(src, dst)
    print(f"Directory '{src}' copied to '{dst}' successfully.")
  except OSError as e:
    print(f"Error copying directory: {e}")

def get_paper_info(arxiv_id):
  try:
    client = arxiv.Client()  # Create a Client instance
    search = arxiv.Search(id_list=[arxiv_id])
    paper = next(client.results(search))
    return {
        "title": paper.title,
        "publish_date": paper.published.strftime('%Y-%m-%d'),
        "author": f"{str(paper.authors[0])} et el."
    }
  except Exception as e:
    print(f"Error fetching paper information: {e}")
    return None

def sort_json_by_paths(json_data):
    def extract_fn_sn(figure_path):
        """Extracts fn and sn from a figure_path string."""
        parts = figure_path.split('/')[0].split('.')
        return int(parts[0]), int(parts[1])
    
    json_data.sort(key=lambda item: extract_fn_sn(item['figure_path']))
    return json_data

def rebase_paths_from_json(json_data):
    """
    "2410.07722/figures/figures_1_0.png" -> "figures/figures_1_0.png"
    """
    def remove_root_path_part(item):
        item["figure_path"] = '/'.join(item["figure_path"].split('/')[1:])
        return item
        
    return [remove_root_path_part(item) for item in json_data]

def read_add_table_content(arxiv_id, json_data):
    def read_table_content(item):
        filename = os.path.join("articles", arxiv_id, item["figure_path"])
        item["content"] = open(filename, 'r').read()
        return item

    return [read_table_content(item) for item in json_data]

def replace_double_quotes_to_single_quotes(json_data):
    def _replace_double_quotes_to_single_quotes(item):
        item["caption"] = item["caption"].replace('"', "'")
        item["description"] = item["description"].replace('"', "'")

        item["caption"] = item["caption"].replace("\n", " ")
        item["description"] = item["description"].replace("\n", " ")  
        return item

    json_data = [_replace_double_quotes_to_single_quotes(item) for item in json_data]
    return json_data

def get_first_and_rest(json_data):
    if len(json_data) == 0:
        return None, []
    elif len(json_data) == 1:
        return json_data[0], []
    else:
        return json_data[0], json_data[1:]

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_paper_imgs(arxiv_id):
    paper_imgs_dir = os.path.join("articles", arxiv_id, 'paper_images')
    paper_imgs = []
    
    if os.path.exists(paper_imgs_dir):
        for file in sorted(os.listdir(paper_imgs_dir), key=lambda x: int(x.split('.')[0])):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                paper_imgs.append(f"paper_images/{file}")
    
    return paper_imgs

def upload_paper_imgs(arxiv_id, target="r2"):
    paper_imgs_dir = os.path.join("articles", arxiv_id, 'paper_images')
    paper_imgs = []

    if target == "r2":
        from r2_utils import upload_to_r2, remove_r2_directory
        remove_r2_directory("ai-paper-reviews", arxiv_id)

    if os.path.exists(paper_imgs_dir):
        for file in sorted(os.listdir(paper_imgs_dir), key=lambda x: int(x.split('.')[0])):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                if target == "r2":
                    url = upload_to_r2(f"ai-paper-reviews", arxiv_id, f"articles/{arxiv_id}/paper_images/{file}")
                paper_imgs.append(url)
    
    return paper_imgs

def upload_podcast(arxiv_id, podcast_path, target="r2"):
    if target == "r2":
        from r2_utils import upload_to_r2
        url = upload_to_r2(f"ai-paper-reviews", arxiv_id, podcast_path)
        return url
    else:
        return None

def upload_images_from_json(arxiv_id, json_data, target="r2"):
    if len(json_data) == 1 and json_data[0] is None:
        return [None]

    for i in range(len(json_data)):
        data = json_data[i]
        figure_path = os.path.join("articles", arxiv_id, data["figure_path"])
        if target == "r2":
            from r2_utils import upload_to_r2
            url = upload_to_r2(f"ai-paper-reviews", arxiv_id, figure_path)
        json_data[i]["figure_path"] = url

    return json_data

def linebreaks_for_essentials(essentials_json):
    essentials_json["tldr"] = essentials_json["tldr"].replace("\n", "\n\n")
    # essentials_json["importance"] = essentials_json["importance"].replace("\n", "<br>")
    return essentials_json

def download_image(image_url, to_path):
  try:
    response = requests.get(image_url, stream=True)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    with open(to_path, 'wb') as file:
      for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)

    print(f"Image downloaded successfully as {to_path}")

  except requests.exceptions.RequestException as e:
    print(f"Error downloading image: {e}")