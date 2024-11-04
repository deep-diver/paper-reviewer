import json
import requests
from bs4 import BeautifulSoup

def get_html_content(arxiv_id):
    url = f"https://arxiv.org/html/{arxiv_id}"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    return response.status_code, soup

def parse_figures(soup, arxiv_id):
    figures = []

    figure_images = soup.select('.ltx_figure > img')
    figure_captions = soup.select('.ltx_figure > figcaption')
    for figure_image, figure_caption in zip(figure_images, figure_captions):
        figure = {
            'figure_path': f"https://arxiv.org/html/{arxiv_id}/{figure_image.get('src')}",
            'caption': figure_caption.text.strip()
        }
        figures.append(figure)
    return figures

def parse_tables(soup):
    tables = []

    table_contents = soup.select('table.ltx_tabular')
    table_captions = soup.select('.ltx_table > figcaption')
    for table_content, table_caption in zip(table_contents, table_captions):
        table = {
            'content': str(table_content),
            'caption': table_caption.text.strip()
        }
        tables.append(table)
    return tables

def get_media_from_html(arxiv_id):
    status_code, soup = get_html_content(arxiv_id)
    if status_code != 200:
        return None, None

    figures = parse_figures(soup, arxiv_id)
    tables = parse_tables(soup)
    return figures, tables
