import os
import argparse
import json
import asyncio

from pipeline.download import download_pdf
from pipeline.pdf_to_images import pdf_to_images
from pipeline.crop import crop_figures
from pipeline.crop_doublecheck import doublecheck_figures
from pipeline.associate_desc import associate_description
from pipeline.extract_sections import extract_sections
from pipeline.extract_section_details import extract_section_details
from pipeline.extract_references import extract_references
from pipeline.utils import upload_to_gemini, wait_for_files_active

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arxiv-id', type=str, help='arXiv ID')
    parser.add_argument('--workers', type=int, default=10, help='Number of workers')
    parser.add_argument('--use-upstage', action='store_true', help='Use Upstage to extract figures from images')
    return parser.parse_args()

async def main(args):
    print(args)
    root_path = args.arxiv_id

    # 1. download pdf
    print(f"Downloading PDF from arXiv: {args.arxiv_id}")
    pdf_file_path = download_pdf(root_path, args.arxiv_id)

    # 2. convert pdf to images
    print(f"Converting PDF to images")
    image_paths = pdf_to_images(pdf_file_path, root_path)

    # 3. crop figures from images
    print(f"Cropping figures from images")
    figure_paths = await crop_figures(image_paths, root_path, args.use_upstage, args.workers)
    print(f"{len(figure_paths)} number of figures are extracted and saved {figure_paths}.")

    # 4. Double check if figure image file contians figure
    print(f"Double checking if figure image file contians figure")
    double_checking_results = await doublecheck_figures(figure_paths, args.workers)

    figures_to_be_removed = list(set(figure_paths) - set(double_checking_results))
    for figure_path in figures_to_be_removed:
        os.remove(figure_path)

    print(f"{len(double_checking_results)} number of figures are remained. {len(figures_to_be_removed)} is removed. {double_checking_results}.")

    # 5. associate each figure and table with description
    print(f"Associating each figure and table with description")
    association_results, pdf_file_in_gemini = await associate_description(double_checking_results, pdf_file_path, args.workers)

    # 6. save the results
    print(f"Saving the image descriptions")
    results_path = f"{root_path}/image_descriptions.json"
    with open(results_path, "w") as f:
        json.dump(association_results, f)
    print(f"Image descriptions are saved to {results_path}")

    # 7. extract sections from the pdf  
    print(f"Extracting section list from the pdf")
    sections = extract_sections(pdf_file_in_gemini)["sections"]

    # 8. extract section details from the pdf
    print(f"Extracting section details from the pdf")
    section_detail_list = await extract_section_details(pdf_file_in_gemini, sections, args.workers)
    print(len(sections))
    print(len(section_detail_list))

    for i in range(len(section_detail_list)):
        sections[i]["details"] = section_detail_list[i]

    print(f"Saving section details")
    results_path = f"{root_path}/sections.json"
    with open(results_path, "w") as f:
        json.dump(sections, f)
    print(f"Section details are saved to {results_path}")    

    # 9. extract references from the pdf
    print(f"Extracting references from the pdf")
    references = extract_references(pdf_file_in_gemini, sections)

    print(f"Saving references")
    results_path = f"{root_path}/references.json"
    with open(results_path, "w") as f:
        json.dump(references, f)
    print(f"References are saved to {results_path}")

if __name__ == "__main__":
    args = parse_args() 
    asyncio.run(main(args))
