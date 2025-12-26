#!/bin/bash
set -e

# Parse arguments (require --project-folder, no default)
PROJECT_FOLDER=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --project-folder)
            PROJECT_FOLDER="$2"
            shift 2
            ;;
        *)
            echo "Unknown argument: $1"
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

echo "Creating symbolic links to $PROJECT_FOLDER..."

# Create the project folder if it doesn't exist
mkdir -p "$PROJECT_FOLDER"

# Backup existing GEMINI.md if it exists, then create symlink
if [ -e "$PROJECT_FOLDER/GEMINI.md" ]; then
    mv "$PROJECT_FOLDER/GEMINI.md" "$PROJECT_FOLDER/GEMINI.md.bk"
    echo "Backed up existing GEMINI.md to GEMINI.md.bk"
fi
ln -s "$(pwd)/commands/GEMINI.md" "$PROJECT_FOLDER/GEMINI.md"
echo "Created symlink for GEMINI.md"

# Remove and recreate commands directory
rm -rf "$PROJECT_FOLDER/commands"
mkdir -p "$PROJECT_FOLDER/commands"

# Symlink all non-hidden entries under commands (files and folders)
for entry in "$(pwd)"/commands/*; do
  name=$(basename "$entry")
  ln -sf "$entry" "$PROJECT_FOLDER/commands/$name"
done

# Symlink scripts and .venv inside commands folder
ln -s "$(pwd)/scripts" "$PROJECT_FOLDER/commands/scripts"
ln -s "$(pwd)/.venv" "$PROJECT_FOLDER/commands/.venv"

echo "Symbolic links created successfully in $PROJECT_FOLDER"
