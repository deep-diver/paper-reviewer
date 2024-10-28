#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 3 ]; then
  echo "Usage: $0 <start_date> <end_date> <num_threads>"
  echo "Example: $0 2024-10-20 2024-10-24 4"
  exit 1
fi

start_date="$1"
end_date="$2"
num_threads="$3"

# Loop through the date range
while [[ $(date -d "$start_date" +%s) -le $(date -d "$end_date" +%s) ]]; do
  echo "Processing papers for $start_date"

  # Fetch the list of papers for the current date
  curl "https://huggingface.co/api/daily_papers?date=$start_date" -o daily_papers.json

  # Remove existing directories
  jq -r '.[].paper.id' daily_papers.json | while read -r id; do
    rm -rf "$id"
  done

  # Run your Python script in parallel for each paper
  jq -r '.[].paper.id' daily_papers.json | xargs -I {} -P "$num_threads" sh -c "python main.py --arxiv-id {} --use-upstage"

  # Increment the date (Linux compatible)
  start_date=$(date -d "$start_date + 1 day" +%Y-%m-%d)
done