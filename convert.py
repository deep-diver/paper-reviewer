import os
import shutil
import argparse
from jinja2 import Environment, FileSystemLoader

from convert_utils import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arxiv-id', type=str, help='arXiv ID')
    parser.add_argument('--template', type=str, default='templates/article_tmpl.md', help='Template file')
    parser.add_argument('--hf-daily-papers-date-tag', type=str, default=None)
    parser.add_argument('--upload-images-r2', action='store_true', help='Cloudflare R2 to upload images')
    parser.add_argument('--stop-at-no-html', action='store_true', help='Stop if no HTML is found')
    return parser.parse_args()

def main(args):
    use_html = True
    url = f"https://arxiv.org/html/{args.arxiv_id}"
    response = requests.get(url)
    if response.status_code != 200:
        if args.stop_at_no_html:
            print(f"No HTML is found. Skip this paper.")
            return
        else:
            use_html = False

    # 0. copy the directory
    if os.path.isdir(f'articles/{args.arxiv_id}'):
        shutil.rmtree(f'articles/{args.arxiv_id}')

    copy_directory(args.arxiv_id, f"articles/{args.arxiv_id}")
    if os.path.exists(f'articles/{args.arxiv_id}/{args.arxiv_id}.pdf'):
        os.remove(f'articles/{args.arxiv_id}/{args.arxiv_id}.pdf')

    # 1. load essential.json, figures.json, tables.json, charts.json
    try:
        figures_json = load_json(f'articles/{args.arxiv_id}/figures.json')
        tables_json = load_json(f'articles/{args.arxiv_id}/tables.json')
        essential_json = load_json(f'articles/{args.arxiv_id}/essential.json')
    except:
        shutil.rmtree(f'articles/{args.arxiv_id}')
        return
    
    # 2. get paper imgs
    podcast_path = f'articles/{args.arxiv_id}/podcast.wav'
    if args.upload_images_r2:
        paper_imgs = upload_paper_imgs(args.arxiv_id)
        shutil.rmtree(f'articles/{args.arxiv_id}/paper_images', ignore_errors=True)

        if os.path.exists(podcast_path):
            podcast = upload_podcast(args.arxiv_id, podcast_path)
            os.remove(podcast_path)
    else:
        paper_imgs = get_paper_imgs(args.arxiv_id)

        if not os.path.exists(podcast_path):
            podcast = None

    # 3. sort the json by paths
    if not use_html:
        figures_json = sort_json_by_paths(figures_json)
        tables_json = sort_json_by_paths(tables_json)

    # 4. rebase the paths
    if not use_html:
        figures_json = rebase_paths_from_json(figures_json)
        tables_json = rebase_paths_from_json(tables_json)
        tables_json = read_add_table_content(args.arxiv_id, tables_json)

    # 5. replace double quotes to single quotes
    figures_json = replace_double_quotes_to_single_quotes(figures_json)
    tables_json = replace_double_quotes_to_single_quotes(tables_json)

    # 6. get the first figure, chart, table
    first_figure, other_figures = get_first_and_rest(figures_json)
    first_table, other_tables = get_first_and_rest(tables_json)

    # 7. copy the first figure to cover.png
    if first_figure is not None:
        if not use_html:
            shutil.copy(
                os.path.join("articles", args.arxiv_id, first_figure["figure_path"]),
                os.path.join("articles", args.arxiv_id, "cover.png")
            )
        else:
            download_image(first_figure["figure_path"], os.path.join("articles", args.arxiv_id, "cover.png"))

    # 8. upload images to r2
    if not use_html:    
        if args.upload_images_r2:
            first_figure = upload_images_from_json(args.arxiv_id, [first_figure])[0]
            other_figures = upload_images_from_json(args.arxiv_id, other_figures)

            shutil.rmtree(f'articles/{args.arxiv_id}/figures', ignore_errors=True)

    # 9. get the paper info
    paper_info = get_paper_info(args.arxiv_id)
    paperswithcode_url = get_paperswithcode_url(args.arxiv_id)
    paper_summary = essential_json["summary"].replace('"', "'")
    if len(paper_summary) > 200:
        paper_summary = f"{paper_summary[:200]}..."

    essential_json = linebreaks_for_essentials(essential_json)

    with open(f"articles/{args.arxiv_id}/sections.json", "r") as f:
        sections_info = json.load(f)

    # 10. render the template
    env = Environment(loader=FileSystemLoader(''))  # 'templates' is your template directory
    template = env.get_template(args.template)
    data = {
        'hf_daily_papers_date_tag': args.hf_daily_papers_date_tag,
        'paper_title': f"\"{paper_info['title']}\"",
        'arxiv_id': args.arxiv_id,
        "author": paper_info["author"],
        "affiliation": essential_json["affiliation"],
        "category": essential_json["categories"]["main_category"],
        "sub_category": essential_json["categories"]["sub_category"],
        'paper_summary': f"\"{paper_summary}\"",
        'publish_date': paper_info["publish_date"],
        'arxiv_url': f'https://arxiv.org/abs/{args.arxiv_id}',
        'hf_url': f'https://huggingface.co/papers/{args.arxiv_id}',
        'paperswithcode_url': paperswithcode_url,
        'podcast': podcast,
        'tldr': essential_json["tldr"],
        'reason_why_matter': essential_json["importance"],
        'takeaways': essential_json["takeaways"],
        "sections": sections_info,
        'first_figure': first_figure,
        'first_table': first_table,
        'other_figures': other_figures,
        'other_tables': other_tables,
        'paper_imgs': paper_imgs[:20]
    }
    output = template.render(data)

    # 11. write the output to index.md
    with open(f"articles/{args.arxiv_id}/index.md", "w") as f:
        f.write(output)

if __name__ == "__main__":
    args = parse_args() 
    main(args)



