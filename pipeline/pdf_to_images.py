from pdf2image import convert_from_path

def pdf_to_images(pdf_file_path, root_path):
    images = convert_from_path(pdf_file_path)
    image_paths = []

    for i, image in enumerate(images):
        image_path = f"{root_path}/{i+1}.png"
        image.save(image_path)
        image_paths.append(image_path)

    return image_paths