import re
import os

def download_pdf_from_arxiv(root_path, arxiv_id):
    import arxiv

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

def download_pdf_from_openreview(root_path, openreview_id):
    import requests
    import openreview

    os.mkdir(root_path)
    os.mkdir(f"{root_path}/paper_images")
    os.mkdir(f"{root_path}/figures")
    os.mkdir(f"{root_path}/charts")
    os.mkdir(f"{root_path}/tables")

    filepath = f"{root_path}/{openreview_id}.pdf"

    client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")
    paper_info = client.get_note(id=openreview_id)
    pdf_sub_url = paper_info.content["pdf"]["value"]
    pdf_url = f"https://openreview.net{pdf_sub_url}"

    response = requests.get(pdf_url)
    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath

def _get_title_from_openreview(openreview_id):
    import openreview

    client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")
    paper_info = client.get_note(id=openreview_id)
    return paper_info.content["title"]["value"]

def _get_paper_info_from_arxiv(paper_title):
    import arxiv
    from urllib.parse import quote

    query = f"ti:{quote(paper_title)}"

    client = arxiv.Client()
    search = arxiv.Search(
        query=query,  # Query specifically for the title
        max_results=1,  # Limit to one result for efficiency
        sort_by=arxiv.SortCriterion.Relevance
    )

    return list(client.results(search))[0]

def remove_version_from_string(string):
    return re.sub(r"v\d+", "", string)

def get_paper_from_arxiv_by_openreview(openreview_id):
    openreview_title = _get_title_from_openreview(openreview_id)
    arxiv_paper_info = _get_paper_info_from_arxiv(openreview_title)

    if openreview_title != arxiv_paper_info.title:
        return False, None
    else:
        arxiv_id = arxiv_paper_info.entry_id.split("/")[-1]
        arxiv_id = remove_version_from_string(arxiv_id)
        return True, arxiv_id