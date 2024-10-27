import asyncio
import operator
from tqdm import tqdm
from functools import reduce

from pipeline.crop_gemini import crop_figures as crop_figures_gemini
from pipeline.crop_upstage import crop_figures as crop_figures_upstage

async def process_images_upstage(image_paths, root_path, workers):
    pass

async def worker(semaphore, i, image_path, root_path, pbar, media_type=None):
    async with semaphore:
        return await process_image(i+1, image_path, root_path, pbar, media_type)

async def process_images(image_paths, root_path, workers, media_type):
    semaphore = asyncio.Semaphore(workers)
    with tqdm(total=len(image_paths)) as pbar:
        cropping_tasks = [worker(semaphore, i, image_path, root_path, pbar, media_type) for i, image_path in enumerate(image_paths)]
        results = await asyncio.gather(*cropping_tasks)
    return results

async def process_image(i, image_path, root_path, pbar, media_type):
    figure_path = crop_figures_gemini(i, image_path, root_path, media_type)
    pbar.update(1)
    if isinstance(figure_path, list):
        return figure_path
    else:
        return [figure_path]

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

    else:
        all_figure_paths = await process_images(image_paths, root_path, workers, "figures")
        all_chart_paths = await process_images(image_paths, root_path, workers, "charts")
        all_table_paths = await process_images(image_paths, root_path, workers, "tables")


    all_figure_paths = list(filter(None, all_figure_paths))
    all_chart_paths = list(filter(None, all_chart_paths))
    all_table_paths = list(filter(None, all_table_paths))

    return all_figure_paths, all_chart_paths, all_table_paths

