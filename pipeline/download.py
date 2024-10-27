import os
import arxiv
import requests

def download_pdf(root_path, arxiv_id):
    os.mkdir(root_path)
    os.mkdir(f"{root_path}/paper_images")
    os.mkdir(f"{root_path}/figures")
    os.mkdir(f"{root_path}/charts")
    os.mkdir(f"{root_path}/tables")

    filepath = f"{root_path}/{arxiv_id}.pdf"

    client = arxiv.Client()  # Create a Client instance
    search = arxiv.Search(id_list=[arxiv_id])
    paper = next(client.results(search))
    paper.download_pdf(filename=f"{root_path}/{arxiv_id}.pdf")

    return filepath