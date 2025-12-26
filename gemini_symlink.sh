#!/bin/bash
set -e

echo "Creating symbolic links to ~/.gemini..."

# Create the ~/.gemini directory if it doesn't exist
mkdir -p ~/.gemini

# Backup existing GEMINI.md if it exists, then create symlink
if [ -e ~/.gemini/GEMINI.md ]; then
    mv ~/.gemini/GEMINI.md ~/.gemini/GEMINI.md.bk
    echo "Backed up existing GEMINI.md to GEMINI.md.bk"
fi
ln -s "$(pwd)/commands/GEMINI.md" ~/.gemini/GEMINI.md
echo "Created symlink for GEMINI.md"

# Remove other conflicting files or symlinks
rm -rf ~/.gemini/commands

# Create the rest of the symbolic links
ln -s "$(pwd)/commands" ~/.gemini/commands
ln -s "$(pwd)/scripts" ~/.gemini/commands/scripts
ln -s "$(pwd)/.venv" ~/.gemini/commands/.venv

echo "Symbolic links created successfully."
