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

# Create .github/skills directory (fresh)
mkdir -p "$PROJECT_FOLDER/.github"
rm -rf "$PROJECT_FOLDER/.github/skills"
mkdir -p "$PROJECT_FOLDER/.github/skills"

# Link each skill folder so they can be edited independently if needed
for entry in "$(pwd)"/skills/*; do
  name=$(basename "$entry")
  ln -s "$entry" "$PROJECT_FOLDER/.github/skills/$name"
done

# Copy copilot-instructions.md to .github folder (this seems to be the most effective way to get GitHub Copilot to pick it up)
ln -s "$(pwd)/skills/README.md" "$PROJECT_FOLDER/.github/copilot-instructions.md"

# Also surface scripts and virtualenv under the skills folder for execution
ln -s "$(pwd)/scripts" "$PROJECT_FOLDER/.github/skills/scripts"
ln -s "$(pwd)/.venv" "$PROJECT_FOLDER/.github/skills/.venv"

echo "Symbolic links created successfully under: $PROJECT_FOLDER/.github/skills"



