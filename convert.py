import os
import json
import arxiv
import shutil
import argparse
from jinja2 import Environment, FileSystemLoader

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arxiv-id', type=str, help='arXiv ID')
    parser.add_argument('--hf-daily-papers-date-tag', type=str, default=None)
    parser.add_argument('--upload-images-r2', action='store_true', help='Cloudflare R2 to upload images')
    return parser.parse_args()

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
        "publish_date": paper.published.strftime('%Y-%m-%d')
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

def upload_images_from_json(arxiv_id, json_data, target="r2"):
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

def main(args):
    # 0. copy the directory
    shutil.rmtree(f'articles/{args.arxiv_id}')
    copy_directory(args.arxiv_id, f"articles/{args.arxiv_id}")
    os.remove(f'articles/{args.arxiv_id}/{args.arxiv_id}.pdf')

    # 1. load essential.json, figures.json, tables.json, charts.json
    try:
        figures_json = load_json(f'{args.arxiv_id}/figures.json')
        tables_json = load_json(f'{args.arxiv_id}/tables.json')
        charts_json = load_json(f'{args.arxiv_id}/charts.json')
        essential_json = load_json(f'{args.arxiv_id}/essential.json')
    except:
        os.remove(f'articles/{args.arxiv_id}')
        return
    
    # 2. get paper imgs
    if args.upload_images_r2:
        paper_imgs = upload_paper_imgs(args.arxiv_id)
        shutil.rmtree(f'articles/{args.arxiv_id}/paper_images', ignore_errors=True)
    else:
        paper_imgs = get_paper_imgs(args.arxiv_id)

    # 3. sort the json by paths
    figures_json = sort_json_by_paths(figures_json)
    charts_json = sort_json_by_paths(charts_json)
    tables_json = sort_json_by_paths(tables_json)

    # 4. rebase the paths
    figures_json = rebase_paths_from_json(figures_json)
    charts_json = rebase_paths_from_json(charts_json)
    tables_json = rebase_paths_from_json(tables_json)
    tables_json = read_add_table_content(args.arxiv_id, tables_json)

    # 5. replace double quotes to single quotes
    figures_json = replace_double_quotes_to_single_quotes(figures_json)
    charts_json = replace_double_quotes_to_single_quotes(charts_json)
    tables_json = replace_double_quotes_to_single_quotes(tables_json)

    # 6. upload images to r2
    if args.upload_images_r2:
        figures_json = upload_images_from_json(args.arxiv_id, figures_json)
        charts_json = upload_images_from_json(args.arxiv_id, charts_json)

        shutil.rmtree(f'articles/{args.arxiv_id}/figures', ignore_errors=True)
        shutil.rmtree(f'articles/{args.arxiv_id}/charts', ignore_errors=True)

    first_figure, other_figures = get_first_and_rest(figures_json)
    first_chart, other_charts = get_first_and_rest(charts_json)
    first_table, other_tables = get_first_and_rest(tables_json)
    
    if first_figure is not None:
        shutil.copy(
            os.path.join("articles", args.arxiv_id, first_figure["figure_path"]),
            os.path.join("articles", args.arxiv_id, "cover.png")
        )

    paper_info = get_paper_info(args.arxiv_id)
    paper_summary = essential_json["summary"].replace('"', "'")
    if len(paper_summary) > 200:
        paper_summary = f"{paper_summary[:200]}..."

    essentials_json = linebreaks_for_essentials(essential_json)

    env = Environment(loader=FileSystemLoader(''))  # 'templates' is your template directory
    template = env.get_template('article_tmpl.md')
    data = {
        'hf_daily_papers_date_tag': args.hf_daily_papers_date_tag,
        'paper_title': f"\"{paper_info['title']}\"",
        'arxiv_id': args.arxiv_id,
        'paper_summary': f"\"{paper_summary}\"",
        'publish_date': paper_info["publish_date"],
        'arxiv_url': f'https://arxiv.org/abs/{args.arxiv_id}',
        'hf_url': f'https://huggingface.co/papers/{args.arxiv_id}',
        'tldr': essential_json["tldr"],
        'reason_why_matter': essential_json["importance"],
        'takeaways': essential_json["takeaways"],
        'first_figure': first_figure,
        'first_chart': first_chart,
        'first_table': first_table,
        'other_figures': other_figures,
        'other_charts': other_charts,
        'other_tables': other_tables,
        'paper_imgs': paper_imgs
    }
    output = template.render(data)

    with open(f"articles/{args.arxiv_id}/index.md", "w") as f:
        f.write(output)

if __name__ == "__main__":
    args = parse_args() 
    main(args)



