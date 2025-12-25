#!/bin/bash
set -e

# Parse arguments
PROJECT_FOLDER=""

while [[ $# -gt 0 ]]; do
  case $1 in
    --project-folder)
      PROJECT_FOLDER="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: $0 --project-folder <path-to-project>"
      exit 1
      ;;
  esac
done

# Validate project folder argument
if [ -z "$PROJECT_FOLDER" ]; then
  echo "Error: --project-folder argument is required"
  echo "Usage: $0 --project-folder <path-to-project>"
  exit 1
fi

# Resolve absolute path
PROJECT_FOLDER=$(cd "$PROJECT_FOLDER" && pwd)

echo "Creating .github folder and symbolic links in: $PROJECT_FOLDER"

# Create .github directory if it doesn't exist
mkdir -p "$PROJECT_FOLDER/.github"

# Remove existing skills symlink/folder if it exists
rm -rf "$PROJECT_FOLDER/.github/skills"

# Create symbolic link to skills
ln -s "$(pwd)/skills" "$PROJECT_FOLDER/.github/skills"

echo "Symbolic link created successfully at: $PROJECT_FOLDER/.github/skills"



