import os
import argparse
import json
import asyncio
from functools import reduce
import operator
from tqdm import tqdm

from utils import download_pdf
from utils import pdf_to_images
from utils import crop_figures
from utils import crop_figures_upstage
from utils import associate_description
from utils import double_check_figure
from utils import upload_to_gemini
from utils import wait_for_files_active

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arxiv-id', type=str, help='arXiv ID')
    parser.add_argument('--workers', type=int, default=10, help='Number of workers')
    parser.add_argument('--use-upstage', action='store_true', help='Use Upstage to extract figures from images')
    return parser.parse_args()

async def process_image(i, image_path, root_path, pbar):
    figure_path = crop_figures(i, image_path, root_path)
    pbar.update(1)
    if isinstance(figure_path, list):
        return figure_path
    else:
        return [figure_path]

async def process_image_upstage(i, image_path, root_path, pbar):
    figure_path = crop_figures_upstage(i, image_path, root_path)
    pbar.update(1)
    if isinstance(figure_path, list):
        return figure_path
    else:
        return [figure_path]

async def process_figure_and_table(figure_path, pdf_file_in_gemini, pbar):
    associated_description = associate_description(pdf_file_in_gemini, figure_path)
    pbar.update(1)
    return {
        "figure_path": figure_path,
        "description": associated_description
    }

async def process_figure_double_check(figure_path, pbar):
    figure_included = double_check_figure(figure_path)
    pbar.update(1)
    if figure_included:
        return figure_path
    else:
        return None

async def main(args):
    root_path = args.arxiv_id

    # download pdf
    print(f"Downloading PDF from arXiv: {args.arxiv_id}")
    pdf_file_path = download_pdf(root_path, args.arxiv_id)

    # convert pdf to images
    print(f"Converting PDF to images")
    image_paths = pdf_to_images(pdf_file_path, root_path)

    # crop figures from images
    print(f"Cropping figures from images")
    figure_paths = []
    cropping_tasks = []

    # Create a semaphore to limit the number of concurrent tasks
    semaphore = asyncio.Semaphore(args.workers) #num_workers)
    with tqdm(total=len(image_paths)) as pbar:
        async def worker(i, image_path):
            async with semaphore:
                if args.use_upstage:
                    return await process_image_upstage(i, image_path, root_path, pbar)
                else:
                    return await process_image(i, image_path, root_path, pbar)

        # Gather tasks and execute concurrently
        cropping_tasks = [worker(i, image_path) for i, image_path in enumerate(image_paths)]
        results = await asyncio.gather(*cropping_tasks)
        figure_paths.extend(result for result in results)  # Flatten the results

    figure_paths = list(filter(None, figure_paths))
    figure_paths = reduce(operator.add, figure_paths)
    print(f"{len(figure_paths)} number of figures are extracted and saved {figure_paths}.")

    # Double check if figure image file contians figure
    print(f"Double checking if figure image file contians figure")
    double_checking_tasks = []
    double_checking_results = []

    semaphore = asyncio.Semaphore(args.workers)
    with tqdm(total=len(figure_paths)) as pbar:
        async def worker(figure_path):
            async with semaphore:
                return await process_figure_double_check(figure_path, pbar)

        double_checking_tasks = [worker(figure_path) for figure_path in figure_paths]
        results = await asyncio.gather(*double_checking_tasks)
        for result in results:
            if result is not None:
                double_checking_results.append(result)

    figures_to_be_removed = list(set(figure_paths) - set(double_checking_results))
    for figure_path in figures_to_be_removed:
        os.remove(figure_path)

    # associate each figure and table with description
    print(f"Associating each figure and table with description")
    association_results = []
    association_tasks = []

    pdf_file_in_gemini = upload_to_gemini(pdf_file_path)
    wait_for_files_active([pdf_file_in_gemini])

    semaphore = asyncio.Semaphore(args.workers)
    with tqdm(total=len(double_checking_results)) as pbar:
        async def worker(figure_path):
            async with semaphore:
                return await process_figure_and_table(figure_path, pdf_file_in_gemini, pbar)

        association_tasks = [worker(figure_path) for figure_path in double_checking_results]
        results = await asyncio.gather(*association_tasks)
        association_results.extend(result for result in results)

    # save the results
    print(f"Saving the results")
    with open(f"{root_path}/association_results.json", "w") as f:
        json.dump(association_results, f)

if __name__ == "__main__":
    args = parse_args() 
    print(args)
    asyncio.run(main(args))
