import argparse
import json
import asyncio
from functools import reduce
import operator
from tqdm import tqdm

from utils import download_pdf
from utils import pdf_to_images
from utils import crop_figures
from utils import associate_description

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arxiv-id', type=str, help='arXiv ID')
    parser.add_argument('--workers', type=int, default=10, help='Number of workers')
    return parser.parse_args()

async def process_image(i, image_path, root_path, pbar):
    figure_path = crop_figures(i, image_path, root_path)
    pbar.update(1)
    if isinstance(figure_path, list):
        return figure_path
    else:
        return [figure_path]

async def process_figure_and_table(figure_path, pdf_file_path, pbar):
    associated_description = associate_description(pdf_file_path, figure_path)
    pbar.update(1)
    return {
        "figure_path": figure_path,
        "description": associated_description
    }

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
                return await process_image(i, image_path, root_path, pbar)

        # Gather tasks and execute concurrently
        cropping_tasks = [worker(i, image_path) for i, image_path in enumerate(image_paths)]
        results = await asyncio.gather(*cropping_tasks)
        figure_paths.extend(result for result in results)  # Flatten the results

    figure_paths = list(filter(None, figure_paths))
    figure_paths = reduce(operator.add, figure_paths)
    print(f"{len(figure_paths)} number of figures are extracted and saved {figure_paths}.")

    # associate each figure and table with description
    print(f"Associating each figure and table with description")
    association_results = []
    association_tasks = []

    semaphore = asyncio.Semaphore(args.workers)

    with tqdm(total=len(figure_paths)) as pbar:
        async def worker(i, figure_path):
            async with semaphore:
                return await process_figure_and_table(pdf_file_path, figure_path, pbar)

        association_tasks = [worker(i, figure_path) for i, figure_path in enumerate(figure_paths)]
        results = await asyncio.gather(*association_tasks)
        association_results.extend(result for result in results)

    association_results = list(filter(None, association_results))
    association_results = reduce(operator.add, association_results)
    print(association_results)

    # save the results
    print(f"Saving the results")
    with open(f"{root_path}/association_results.json", "w") as f:
        json.dump(association_results, f)

if __name__ == "__main__":
    args = parse_args() 
    asyncio.run(main(args))
