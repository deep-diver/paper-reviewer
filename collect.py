import os
import argparse
import json
import asyncio
import shutil

from pipeline.download import download_pdf
from pipeline.pdf_to_images import pdf_to_images
from pipeline.parse_media_html import get_media_from_html
from pipeline.crop import crop_figures
from pipeline.crop_doublecheck import doublecheck_figures
from pipeline.enrich_desc import enrich_description_from_images, enrich_description_from_html
from pipeline.reformat_tables import reformat_tables_from_html
from pipeline.extract_sections import extract_sections
from pipeline.extract_section_details import extract_section_details
from pipeline.extract_references import extract_references
from pipeline.extract_essentials import extract_essentials
from pipeline.extract_affiliation import extract_affiliation
from pipeline.extract_category import extract_category
from pipeline.write_script import write_script
from pipeline.script_to_speech import script_to_speech
from pipeline.utils import UploadedFiles

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arxiv-id', type=str, help='arXiv ID')
    parser.add_argument('--workers', type=int, default=10, help='Number of workers')
    parser.add_argument('--use-upstage', action='store_true', help='Use Upstage to extract figures from images')
    parser.add_argument('--stop-at-no-html', action='store_true', help='Stop if no HTML is found')
    parser.add_argument('--known-affiliations-path', type=str, default='configs/known_affiliations.txt', help='Path to known affiliations')
    parser.add_argument('--known-categories-path', type=str, default='configs/known_categories.json', help='Path to known categories')
    parser.add_argument('--voice-synthesis', type=str, default=None, choices=['vertexai', 'local'], help='Voice synthesis service to use')
    return parser.parse_args()

async def main(args):
    print(args)
    use_html = True
    root_path = args.arxiv_id

    # 1. download pdf
    print(f"Downloading PDF from arXiv: {args.arxiv_id}")
    pdf_file_path = download_pdf(root_path, args.arxiv_id)

    with UploadedFiles(pdf_file_path) as uploaded_files:
        pdf_file_in_gemini = uploaded_files[0]

        # 2. convert pdf to images
        print(f"Converting PDF to images")
        image_paths = pdf_to_images(pdf_file_path, f"{root_path}/paper_images")
        if len(image_paths) > 50:
            print(f"Too many images: {len(image_paths)}. Skip this paper.")
            shutil.rmtree(root_path)
            return

        # 3. crop figures from images
        print(f"Using HTML to extract figures and tables")
        figures, tables = get_media_from_html(args.arxiv_id)
        if figures is None or tables is None:
            if args.stop_at_no_html:
                print(f"No HTML is found. Skip this paper.")
                shutil.rmtree(root_path)
                return
            else:
                use_html = False

        if not use_html:
            print(f"Cropping figures from images")
            figure_paths, table_paths = await crop_figures(image_paths, root_path, args.use_upstage, args.workers)
            print(f"{len(figure_paths)} number of figures are extracted and saved {figure_paths}.")
            print(f"{len(table_paths)} number of tables are extracted and saved {table_paths}.")

        # 4. Double check if figure image file contians figure
        if not use_html:
            print(f"Double checking if figure image file actually contians figure")
            # Filter out invalid figures and clean up files
            valid_figure_paths = await doublecheck_figures(figure_paths, pdf_file_in_gemini, args.workers, "figure")
            valid_figure_paths = [figure_paths[0]] if len(valid_figure_paths) == 0 else valid_figure_paths
            invalid_paths = set(figure_paths) - set(valid_figure_paths)
            for path in invalid_paths:
                os.remove(path)
            figure_paths = valid_figure_paths
            print(f"{len(figure_paths)} number of figures are remained. {figure_paths}.")

            print(f"Double checking if table file actually contians table")
            valid_table_paths = await doublecheck_figures(table_paths, pdf_file_in_gemini, args.workers, "table")
            valid_table_paths = [table_paths[0]] if len(valid_table_paths) == 0 else valid_table_paths
            invalid_paths = set(table_paths) - set(valid_table_paths)
            for path in invalid_paths:
                os.remove(path)
            table_paths = valid_table_paths
            print(f"{len(table_paths)} number of tables are remained. {table_paths}.")
        else:
            print(f"Reformatting tables")
            tables = await reformat_tables_from_html(args.arxiv_id, tables, args.workers)

        # 5. associate each figure and table with description
        print(f"Associating each figure with relevant information")
        if not use_html:
            association_figure_results = await enrich_description_from_images(figure_paths, pdf_file_in_gemini, args.workers, "figure")
            association_table_results = await enrich_description_from_images(table_paths, pdf_file_in_gemini, args.workers, "table")
        else:
            association_figure_results = await enrich_description_from_html(figures, pdf_file_in_gemini, args.workers, "figure")
            association_table_results = await enrich_description_from_html(tables, pdf_file_in_gemini, args.workers, "table")

        # 6. save the results
        print(f"Saving the figure information")
        association_figure_path = f"{root_path}/figures.json"
        with open(association_figure_path, "w") as f:
            json.dump(association_figure_results, f)
        print(f"Figure information is saved to {association_figure_path}")

        print(f"Saving the table information")
        association_table_path = f"{root_path}/tables.json"
        print(association_table_path)
        try:
            with open(association_table_path, "w") as f:
                json.dump(association_table_results, f)
        except Exception as e:
            print(e)
        print(f"Table information is saved to {association_table_path}")

        # 7. extract fundamental information from the pdf
        print(f"Extracting essential information from the pdf")
        essential_info = extract_essentials(pdf_file_in_gemini)

        # 8. extract affiliation from the pdf
        print(f"Extracting affiliation from the pdf")
        affiliation = extract_affiliation(pdf_file_in_gemini, args.known_affiliations_path)
        essential_info["affiliation"] = affiliation["affiliation"]

        categories = extract_category(pdf_file_in_gemini, args.known_categories_path)
        essential_info["categories"] = categories

        if args.voice_synthesis == "vertexai":
            print("Generating podcast")
            print("Writing script")
            raw_script_path = f"{root_path}/raw_script.wav"
            script = write_script(pdf_file_in_gemini)
            with open(raw_script_path, "w", encoding="utf-8") as f:
                json.dump(script, f)
                
            podcast = script_to_speech(script, use_vertexai=True)
            podcast_path = f"{root_path}/podcast.wav"
            podcast.export(podcast_path, format="wav")
            print(f"Podcast is saved to {podcast_path}")
            essential_info["podcast_path"] = podcast_path
            
        elif args.voice_synthesis == "local":
            pass

        print(f"Saving essential information")
        results_path = f"{root_path}/essential.json"
        with open(results_path, "w") as f:
            json.dump(essential_info, f)
        print(f"Essential information is saved to {results_path}")

        # 9. extract sections from the pdf  
        print(f"Extracting section list from the pdf")
        sections = extract_sections(pdf_file_in_gemini)["sections"]

        # 10. extract section details from the pdf
        print(f"Extracting section details from the pdf")
        section_detail_list = await extract_section_details(pdf_file_in_gemini, sections, args.workers)

        for i in range(len(section_detail_list)):
            sections[i]["details"] = section_detail_list[i]

        print(f"Saving section details")
        results_path = f"{root_path}/sections.json"
        with open(results_path, "w") as f:
            json.dump(sections, f)
        print(f"Section details are saved to {results_path}")

        # 11. extract references from the pdf
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
