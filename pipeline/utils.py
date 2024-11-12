import os
import time
import toml

import google.generativeai as genai

def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini.

    See https://ai.google.dev/gemini-api/docs/prompting_with_media
    """
    file = genai.upload_file(path, mime_type=mime_type)
    return file

def wait_for_files_active(files):
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            time.sleep(10)
            file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")

class UploadedFiles:
    def __init__(self, *paths):
        self.paths = paths
        self.uploaded_files = []

    def __enter__(self):
        for path in self.paths:
            uploaded_file = genai.upload_file(path=path)
            self.uploaded_files.append(uploaded_file)

        self.wait_for_files_active(self.uploaded_files)
        return self.uploaded_files

    def __exit__(self, exc_type, exc_value, traceback):
        for uploaded_file in self.uploaded_files:
            genai.delete_file(uploaded_file.name)

    def wait_for_files_active(self, files):
        """Wait for files to become active."""
        for name in (file.name for file in files):
            file = genai.get_file(name)
            while file.state.name == "PROCESSING":
                time.sleep(10)
                file = genai.get_file(name)
            if file.state.name != "ACTIVE":
                raise RuntimeError(f"File {file.name} failed to process")

def _prompts(tmpl_path='configs/prompts.toml'):
    return toml.load(tmpl_path)

prompts = _prompts()