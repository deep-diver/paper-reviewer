# Paper Reviewer

https://github.com/user-attachments/assets/4ee19af5-107e-4ae7-95fe-67f6227eb5b0

Generate a comprehensive review of papers from [arXiv](https://arxiv.org) and [OpenReview](https://openreview.net), then turn it into a blog post. That is the goal of this project, and it comes with a set of tools to accomplish that. If you are curious how to build your own paper reviewing blog, check out [AI Paper Reviewer](https://deep-diver.github.io/ai-paper-reviewer) which is powered by this project to auto-generate blog posts on the [Hugging Face Daily Papers](https://huggingface.co/papers). The video above is the demo of it. As of Dec. 2024, this project also powers [AI Paper Reviewer for NeurIPS 2024](https://deep-diver.github.io/neurips2024/) web page.

## How it works

At high level, there are two Python scripts, [`collect.py`](./collect.py) and [`convert.py`](./convert.py). 
- `collect.py`: Collect and generate reviews for a given arXiv ID.
- `convert.py`: Convert the collected reviews into a blog post. The blog post follows a [fixed design template](https://deep-diver.github.io/ai-paper-reviewer).

## How to use

### Setup 

```bash
# mendatory
$ export GEMINI_API_KEY="..."

# optional, only if you want to use Upstage's Document Parse
$ export UPSTAGE_API_KEY="..." 

# optional, only if you want to upload images to R2
$ export R2_ACCESS_KEY_ID="..." 
$ export R2_SECRET_ACCESS_KEY="..."
$ export R2_S3_ENDPOINT_URL="..."
$ export R2_DOMAIN_NAME="..."

# install dependencies
$ pip install -r requirements.txt

# poppler is required to convert pdf to images
# for Ubuntu, use apt install poppler-utils 
$ brew install poppler
```

### When using MinerU

- When using [MinerU](https://github.com/opendatalab/MinerU), python version should be set to `3.10`. If your current environment is not `3.10`, make one with `$ conda create -n paper-reviewer-mineru python=3.10` or something similar.
- When using MinerU with GPU enabled, you need to modify the `~/magic-pdf.json` config file. Update `"device-mode": "cpu"` to `"device-mode": "cuda"` or `"device-mode": "cuda:0"` if you want to use specific GPU # in your system. If you want to keep multiple JSON files, switch between them by modifying the `MINERU_TOOLS_CONFIG_JSON` environment variable.

```bash
# create a new environment with python 3.10
$ conda create -n paper-reviewer-mineru python=3.10
$ conda activate paper-reviewer-mineru

# install dependencies
$ pip install -r requirements.txt

# install magic-pdf
$ pip install -U 'magic-pdf[full]==0.10.5' --extra-index-url https://wheels.myhloli.com

# update ~/magic-pdf.json to use GPU
$ vim ~/magic-pdf.json
```

### Collect and generate reviews for a given arXiv ID

To collect and generate reviews for a given arXiv ID, run the `collect.py` script with the following options:

```bash
usage: collect.py [-h] [--arxiv-id ARXIV_ID] [--openreview-id OPENREVIEW_ID] [--skip-comparision-openreview-arxiv] [--skip-page-threshold SKIP_PAGE_THRESHOLD] [--workers WORKERS] [--use-upstage]
                  [--use-mineru] [--stop-at-no-html] [--known-affiliations-path KNOWN_AFFILIATIONS_PATH] [--known-categories-path KNOWN_CATEGORIES_PATH] [--voice-synthesis {vertexai,local}]

options:
  -h, --help            show this help message and exit
  --arxiv-id ARXIV_ID   arXiv ID
  --openreview-id OPENREVIEW_ID
                        OpenReview ID
  --skip-comparision-openreview-arxiv
                        Skip downloading the PDF file
  --skip-page-threshold SKIP_PAGE_THRESHOLD
                        Skip the paper if the number of pages is greater than the threshold
  --workers WORKERS     Number of workers
  --use-upstage         Use Upstage to extract figures from images
  --use-mineru          Use MinerU to extract figures from images
  --stop-at-no-html     Stop if no HTML is found
  --known-affiliations-path KNOWN_AFFILIATIONS_PATH
                        Path to known affiliations
  --known-categories-path KNOWN_CATEGORIES_PATH
                        Path to known categories
  --voice-synthesis {vertexai,local}
                        Voice synthesis service to use
```

To minimize the cost, it is recommended to run the `collect.py` script with `--stop-at-no-html` option. This will make sure to run the workflow on the paper that is its dedicated HTML page(arXiv's experimental HTML page). 

```bash
$ python collect.py --arxiv-id "..." --stop-at-no-html
```

If you want to run the workflow on the paper which does not have its dedicated HTML page, you need to extract visual information(i.e. figures, tables, charts) from the imaged version of the paper. For this case, `--use-upstage` option as in the following command will give you the best results. 

```bash
$ python collect.py --arxiv-id "..." --use-upstage 
```

If you are not a user of Upstage, or if you don't want to be charged for the Upstage APIs, you can remove the `--use-upstage` option. In this case, the script will use Gemini to extract the visual information from the imaged version of paper. However, this approach is the best effort and not recommended if you care about how accurately visual information is parsed. Gemini is not optimized to determine the coordinates of the visual information on given images.

```bash
$ python collect.py --arxiv-id "..." 
```

### Convert the collected reviews into a blog post.

To convert the collected reviews into a blog post, run the `convert.py` script with the following options:

```bash
$ python convert.py --help
usage: convert.py [-h] [--arxiv-id ARXIV_ID] [--openreview-id OPENREVIEW_ID] [--template TEMPLATE] [--hf-daily-papers-date-tag HF_DAILY_PAPERS_DATE_TAG] [--upload-images-r2] [--stop-at-no-html]

options:
  -h, --help            show this help message and exit
  --arxiv-id ARXIV_ID   arXiv ID
  --openreview-id OPENREVIEW_ID
                        OpenReview ID
  --template TEMPLATE   Template file
  --hf-daily-papers-date-tag HF_DAILY_PAPERS_DATE_TAG
  --upload-images-r2    Cloudflare R2 to upload images
  --stop-at-no-html     Stop if no HTML is found
```

The blog post follows the [fixed design template](https://deep-diver.github.io/ai-paper-reviewer). If you want to customize the design, you have to modify the template by yourself. 
