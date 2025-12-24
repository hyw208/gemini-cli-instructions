#!/bin/bash
set -e

echo "Creating symbolic links to ~/.gemini..."

# Create the ~/.gemini directory if it doesn't exist
mkdir -p ~/.gemini

# Check if GEMINI.md exists and prompt for deletion
if [ -e ~/.gemini/GEMINI.md ]; then
    read -p "An existing GEMINI.md was found in ~/.gemini. Do you want to replace it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf ~/.gemini/GEMINI.md
        ln -s "$(pwd)/GEMINI.md" ~/.gemini/GEMINI.md
        echo "Replaced GEMINI.md"
    else
        echo "Skipped replacing GEMINI.md"
    fi
else
    ln -s "$(pwd)/GEMINI.md" ~/.gemini/GEMINI.md
    echo "Created symlink for GEMINI.md"
fi

# Remove other conflicting files or symlinks
rm -rf ~/.gemini/commands ~/.gemini/scripts ~/.gemini/.venv

# Create the rest of the symbolic links
ln -s "$(pwd)/commands" ~/.gemini/commands
ln -s "$(pwd)/scripts" ~/.gemini/scripts
ln -s "$(pwd)/.venv" ~/.gemini/.venv

echo "Symbolic links created successfully."
