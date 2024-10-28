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


def remove_root_path_part(item):
  item["figure_path"] = '/'.join(item["figure_path"].split('/')[1:])
  return item

def replace_double_quotes_to_single_quotes(item):
  item["caption"] = item["caption"].replace('"', "'")
  item["description"] = item["description"].replace('"', "'")

  item["caption"] = item["caption"].replace("\n", " ")
  item["description"] = item["description"].replace("\n", " ")  
  return item

def read_md(item):
    item["content"] = open(item["figure_path"], 'r').read()
    return item

def sort_and_extract(data, to_remove_root_path_part=True, markdown=False):
    def extract_fn_sn(figure_path):
        """Extracts fn and sn from a figure_path string."""
        parts = figure_path.split('/')[0].split('.')
        return int(parts[0]), int(parts[1])

    data.sort(key=lambda item: extract_fn_sn(item['figure_path']))
    if to_remove_root_path_part:
        data = [remove_root_path_part(item) for item in data]

    if markdown:
        data = [read_md(item) for item in data]

    data = [replace_double_quotes_to_single_quotes(item) for item in data]

    if len(data) == 0:
        return None, []
    elif len(data) == 1:
        return data[0], []
    else:
        return data[0], data[1:]

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_paper_imgs(args):
    paper_imgs_dir = os.path.join(args.arxiv_id, 'paper_images')
    paper_imgs = []
    
    if os.path.exists(paper_imgs_dir):
        for file in sorted(os.listdir(paper_imgs_dir), key=lambda x: int(x.split('.')[0])):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                paper_imgs.append(f"paper_images/{file}")
    
    return paper_imgs

def main(args):
    essential_json = load_json(f'{args.arxiv_id}/essential.json')
    figures_json = load_json(f'{args.arxiv_id}/figures.json')
    tables_json = load_json(f'{args.arxiv_id}/tables.json')
    charts_json = load_json(f'{args.arxiv_id}/charts.json')
    paper_imgs = get_paper_imgs(args)

    # 0. copy the directory
    copy_directory(args.arxiv_id, f"articles/{args.arxiv_id}")
    os.remove(f'articles/{args.arxiv_id}/{args.arxiv_id}.pdf')
    first_figure, other_figures = sort_and_extract(figures_json, to_remove_root_path_part=True)
    first_chart, other_charts = sort_and_extract(charts_json, to_remove_root_path_part=True)
    first_table, other_tables = sort_and_extract(tables_json, to_remove_root_path_part=False, markdown=True)
    
    if first_figure is not None:
        shutil.copy(f"{args.arxiv_id}/{first_figure['figure_path']}", f"articles/{args.arxiv_id}/cover.png")

    paper_info = get_paper_info(args.arxiv_id)
    paper_summary = essential_json["summary"].replace('"', "'")
    if len(paper_summary) > 200:
        paper_summary = f"{paper_summary[:200]}..."

    # Create a Jinja2 environment
    env = Environment(loader=FileSystemLoader(''))  # 'templates' is your template directory
    template = env.get_template('article_tmpl.md')
    data = {
        'hf_daily_papers_date_tag': args.hf_daily_papers_date_tag,
        'paper_title': f"\"{paper_info['title']}\"",
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



