#!/bin/sh

# Check if two arguments are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <start_date> <end_date>"
  echo "Example: $0 2024-10-20 2024-10-24"
  exit 1
fi

start_date="$1"
end_date="$2"

# Loop through the date range
while [[ $(date -j -f "%Y-%m-%d" "$start_date" +%s) -le $(date -j -f "%Y-%m-%d" "$end_date" +%s) ]]; do
  echo "Processing papers for $start_date"

  # Fetch the list of papers for the current date
  curl "https://huggingface.co/api/daily_papers?date=$start_date" -o daily_papers.json

  # Remove existing directories
  jq -r '.[].paper.id' daily_papers.json | while read -r id; do
    rm -rf "$id"
  done

  # Run your Python script in parallel for each paper
  jq -r '.[].paper.id' daily_papers.json | xargs -I {} -P 4 sh -c "python main.py --arxiv-id {} --use-upstage"

  # Increment the date (macOS compatible)
  start_date=$(date -j -v+1d -f "%Y-%m-%d" "$start_date" +%Y-%m-%d)
done