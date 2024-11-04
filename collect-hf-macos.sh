#!/bin/sh

# Check if two arguments are provided
if [ $# -lt 2 ] || [ $# -gt 4 ]; then
  echo "Usage: $0 <start_date> <end_date> [<num_threads>] [<existing_articles_dir>]"
  echo "Example: $0 2024-10-20 2024-10-24 4 /path/to/articles"
  exit 1
fi

start_date="$1"
end_date="$2"
num_threads="$3"
existing_articles_dir="$4"

existing_articles=()

if [ -n "$existing_articles_dir" ]; then
  existing_articles=$(ls -d $existing_articles_dir/*/ | xargs -I {} basename {})
fi
# Loop through the date range
while [[ $(date -j -f "%Y-%m-%d" "$start_date" +%s) -le $(date -j -f "%Y-%m-%d" "$end_date" +%s) ]]; do
  echo "Processing papers for $start_date"

  # Fetch the list of papers for the current date
  curl "https://huggingface.co/api/daily_papers?date=$start_date" -o daily_papers.json
  
  jq -r '.[].paper.id' daily_papers.json | xargs -I {} -P "$num_threads" sh -c '
    id={}; 
    rm -rf "$id"; 
    if echo "${existing_articles[@]}" | grep -qw "$id"; then 
      echo "Skipping $id - already exists"; 
    else 
      python collect.py --arxiv-id "$id" --stop-at-no-html;
    fi
  '

  # python collect.py --arxiv-id "$id" --use-upstage
  # jq -r '.[].paper.id' daily_papers.json | xargs -I {} -P "$num_threads" sh -c "python collect.py --arxiv-id {} --use-upstage"

  # Increment the date (macOS compatible)
  start_date=$(date -j -v+1d -f "%Y-%m-%d" "$start_date" +%Y-%m-%d)
done