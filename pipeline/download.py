import os
import requests

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