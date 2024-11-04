import json
import requests
from bs4 import BeautifulSoup

arxiv_id = "2410.24175"
url = f"https://arxiv.org/html/{arxiv_id}"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# Find all the links on the page
figures = []
tables = []

figure_images = soup.select('.ltx_figure > img')
figure_captions = soup.select('.ltx_figure > figcaption') 
for figure_image, figure_caption in zip(figure_images, figure_captions):
    figure = {
        'figure_path': f"https://arxiv.org/html/{arxiv_id}/{figure_image.get('src')}",
        'figure_caption': figure_caption.text.strip()
    }
    figures.append(figure)


table_contents = soup.select('table.ltx_tabular')
table_captions = soup.select('.ltx_table > figcaption')
for table_content, table_caption in zip(table_contents, table_captions):
    table = {
        'table_content': str(table_content),
        'table_caption': table_caption.text.strip()
    }
    tables.append(table)

with open('figures.json', 'w') as f:
    json.dump(figures, f)

with open('tables.json', 'w') as f:
    json.dump(tables, f)