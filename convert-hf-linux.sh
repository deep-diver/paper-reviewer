#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 3 ]; then
  echo "Usage: $0 <start_date> <end_date>"
  echo "Example: $0 2024-10-20 2024-10-24"
  exit 1
fi

start_date="$1"
end_date="$2"
upload_images_r2="$3"

if [[ "$upload_images_r2" == "true" ]]; then
  upload_images_r2_flag="--upload-images-r2"
else
  upload_images_r2_flag=""
fi

# Loop through the date range
while [[ $(date -d "$start_date" +%s) -le $(date -d "$end_date" +%s) ]]; do
  echo "Processing papers for $start_date"

  # Fetch the list of papers for the current date
  curl "https://huggingface.co/api/daily_papers?date=$start_date" -o daily_papers.json

  # Extract the "id"s and process them line by line
  jq -r '.[].paper.id' daily_papers.json | while read -r id; do
    rm -rf articles/$id
    if [ -d "$id" ]; then
      python convert.py --arxiv-id $id --hf-daily-papers-date-tag $start_date $upload_images_r2_flag --stop-at-no-html
    fi  
  done

  # Increment the date (Linux compatible)
  start_date=$(date -d "$start_date + 1 day" +%Y-%m-%d)
done
