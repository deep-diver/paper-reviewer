#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <start_date> <end_date>"
  echo "Example: $0 2024-10-20 2024-10-24"
  exit 1
fi

start_date="$1"
end_date="$2"

# Loop through the date range
while [[ "$start_date" <= "$end_date" ]]; do
  echo "Processing papers for $start_date"

  # Fetch the list of papers for the current date
  curl "https://huggingface.co/api/daily_papers?date=$start_date" -o daily_papers.json

  # Extract the "id"s and process them line by line
  jq -r '.[].paper.id' daily_papers.json | while read -r id; do
    rm -rf articles/$id
    if [ -d "$id" ]; then
      python gen_article.py --arxiv-id $id --hf-daily-papers-date-tag $start_date
    fi  
  done

  # Increment the date (Linux compatible)
  start_date=$(date -d "$start_date + 1 day" +%Y-%m-%d)
done