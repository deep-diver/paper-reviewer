import asyncio
import operator
from tqdm import tqdm
from functools import reduce

from pipeline.crop_gemini import crop_figures as crop_figures_gemini
from pipeline.crop_upstage import crop_figures as crop_figures_upstage

async def process_image(i, image_path, root_path, pbar):
    figure_path = crop_figures_gemini(i, image_path, root_path)
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

async def crop_figures(image_paths, root_path, use_upstage, workers):
    figure_paths = []
    cropping_tasks = []

    # Create a semaphore to limit the number of concurrent tasks
    semaphore = asyncio.Semaphore(workers) #num_workers)
    with tqdm(total=len(image_paths)) as pbar:
        async def worker(i, image_path):
            async with semaphore:
                if use_upstage:
                    return await process_image_upstage(i, image_path, root_path, pbar)
                else:
                    return await process_image(i, image_path, root_path, pbar)

        # Gather tasks and execute concurrently
        cropping_tasks = [worker(i, image_path) for i, image_path in enumerate(image_paths)]
        results = await asyncio.gather(*cropping_tasks)
        figure_paths.extend(result for result in results)  # Flatten the results

    figure_paths = list(filter(None, figure_paths))
    figure_paths = reduce(operator.add, figure_paths)
    return figure_paths

