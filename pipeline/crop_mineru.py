import copy
import json
import os
import shutil

def crop_media(pdf_path, root_path):
    from magic_pdf.data.data_reader_writer import FileBasedDataWriter
    from magic_pdf.pipe.UNIPipe import UNIPipe

    figure_paths = []
    table_paths = []

    tmp_path = os.path.join(root_path, "tmp")
    os.makedirs(tmp_path, exist_ok=True)

    pdf_bytes = open(pdf_path, 'rb').read()
    image_writer = FileBasedDataWriter(tmp_path)

    pipe = UNIPipe(
        pdf_bytes, 
        {'_pdf_type': '', 'model_list': []}, 
        image_writer
    )

    pipe.pipe_classify()
    pipe.pipe_analyze()
    pipe.pipe_parse()

    content_list = pipe.pipe_mk_uni_format(tmp_path, drop_mode='none')
    with open(f"{root_path}/content_list.json", "w") as f:
        json.dump(content_list, f)

    page_counter = {"image": {}, "table": {}}
    for content in content_list:
        content_type = content['type']
        page_idx = content['page_idx']

        if content_type == 'image':
            if content['img_path'].strip():
                page_counter["image"][page_idx] = page_counter["image"].get(page_idx, 0) + 1 # count the number of contents in each page
                current_image_count = page_counter["image"][page_idx]

                filename = os.path.basename(content['img_path'])
                filepath = f"{root_path}/figures/figures_{page_idx}_{current_image_count}.jpg"
                dest_filepath = f"{root_path}/figures/figures_{page_idx}_{current_image_count}.jpg"

                shutil.move(f"{tmp_path}/{filename}", dest_filepath)
                figure_paths.append(dest_filepath)

        elif content_type == 'table':
            if content['img_path'].strip():
                page_counter["table"][page_idx] = page_counter["table"].get(page_idx, 0) + 1 # count the number of contents in each page
                current_image_count = page_counter["table"][page_idx]

                filename = os.path.basename(content['img_path'])
                dest_filepath = f"{root_path}/tables/tables_{page_idx}_{current_image_count}.jpg"

                shutil.move(f"{tmp_path}/{filename}", dest_filepath)
                table_paths.append(dest_filepath)

    shutil.rmtree(tmp_path)
    return figure_paths, table_paths