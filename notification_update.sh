#!/usr/bin/env zsh
# notification_update.sh
# Usage: ./notification_update.sh <n>   where <n> is an integer 1–10

# Exit on error and undefined vars
set -euo pipefail

# Check argument count
if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <integer 1–10>"
  exit 1
fi

# Validate argument (integer between 1 and 10)
if ! [[ "$1" =~ ^[0-9]+$ ]] || (( $1 < 1 || $1 > 10 )); then
  echo "Error: Argument must be an integer between 1 and 10."
  exit 1
fi

# Define directories
src_dir="$HOME/GitHub/anisotropela.github.io/pics/notification-badges"
dest_dir="$HOME/GitHub/anisotropela.github.io/pics"

# Format the number with leading zeros (001–010)
num=$(printf "%03d" "$1")

# Build filenames
src_file="$src_dir/notification-badges.${num}.png"
dest_file="$dest_dir/notification.png"

# Check that source file exists
if [[ ! -f "$src_file" ]]; then
  echo "Error: File $src_file not found."
  exit 1
fi

# Copy and move
cp "$src_file" "$dest_file"

echo "✅ Updated notification image to badge #$1"
