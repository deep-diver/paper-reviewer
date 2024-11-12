import glob
import asyncio
import operator
from tqdm import tqdm
from functools import reduce

from pipeline.crop_gemini import crop_figures as crop_figures_gemini
from pipeline.crop_gemini import extract_tables as extract_tables_gemini
from pipeline.crop_upstage import crop_figures as crop_figures_upstage
from pipeline.utils import UploadedFiles

async def gemini_process_image(i, image_path, root_path, pbar, media_type, correct_examples, wrong_examples):
    if media_type == "figures":
        figure_paths = crop_figures_gemini(i, image_path, root_path, correct_examples, wrong_examples)
    else:
        figure_paths = extract_tables_gemini(i, image_path, root_path)
    pbar.update(1)
    if isinstance(figure_paths, list):
        return figure_paths
    else:
        return [figure_paths]


async def gemini_worker(semaphore, i, image_path, root_path, pbar, media_type=None, correct_examples=None, wrong_examples=None):
    async with semaphore:
        return await gemini_process_image(i+1, image_path, root_path, pbar, media_type, correct_examples, wrong_examples)

async def gemini_process_images(image_paths, root_path, workers, media_type, correct_examples, wrong_examples):
    semaphore = asyncio.Semaphore(workers)
    with tqdm(total=len(image_paths)) as pbar:
        cropping_tasks = [
            gemini_worker(
                semaphore,
                i,
                image_path,
                root_path,
                pbar,
                media_type,
                correct_examples,
                wrong_examples
            )
            for i, image_path in enumerate(image_paths)
        ]
        results = await asyncio.gather(*cropping_tasks)
    return results

async def process_image_upstage(i, image_path, root_path, pbar):
    figure_paths, chart_paths, table_paths = crop_figures_upstage(i, image_path, root_path)
    pbar.update(1)

    if not isinstance(figure_paths, list):
        figure_paths = [figure_paths]
    if not isinstance(chart_paths, list):
        chart_paths = [chart_paths]
    if not isinstance(table_paths, list):
        table_paths = [table_paths]

    return figure_paths, chart_paths, table_paths

async def crop_figures(image_paths, root_path, use_upstage, workers):
    all_figure_paths = []
    all_chart_paths = []
    all_table_paths = []
    cropping_tasks = []

    # Create a semaphore to limit the number of concurrent tasks
    if use_upstage:
        semaphore = asyncio.Semaphore(workers)
        with tqdm(total=len(image_paths)) as pbar:
            async def worker(i, image_path):
                async with semaphore:
                    return await process_image_upstage(i+1, image_path, root_path, pbar)

            # Gather tasks and execute concurrently
            cropping_tasks = [worker(i, image_path) for i, image_path in enumerate(image_paths)]
            results = await asyncio.gather(*cropping_tasks)

        for result in results:
            figure_paths, chart_paths, table_paths = result
            all_figure_paths.extend(figure_paths)
            all_chart_paths.extend(chart_paths)
            all_table_paths.extend(table_paths)

        all_figure_paths = all_figure_paths + all_chart_paths

    else:
        correct_example_paths = glob.glob("assets/rect_example*.png")
        wrong_example_paths = glob.glob("assets/no_rect_example*.png")
        
        with UploadedFiles(correct_example_paths) as correct_examples:
            with UploadedFiles(wrong_example_paths) as wrong_examples:
                all_figure_paths = await gemini_process_images(image_paths, root_path, workers, "figures", correct_examples, wrong_examples)
                all_figure_paths = [item for sublist in all_figure_paths for item in sublist if item is not None]

                all_table_paths = await gemini_process_images(image_paths, root_path, workers, "tables", None, None)
                all_table_paths = [item for sublist in all_table_paths for item in sublist if item is not None]

    all_figure_paths = list(filter(None, all_figure_paths))
    all_table_paths = list(filter(None, all_table_paths))

    return all_figure_paths, all_table_paths

