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

# Remove and recreate commands directory
rm -rf ~/.gemini/commands
mkdir -p ~/.gemini/commands

# Symlink individual command files
for file in "$(pwd)"/commands/*.toml; do
  ln -s "$file" ~/.gemini/commands/$(basename "$file")
done

# Symlink scripts and .venv inside commands folder
ln -s "$(pwd)/scripts" ~/.gemini/commands/scripts
ln -s "$(pwd)/.venv" ~/.gemini/commands/.venv

echo "Symbolic links created successfully."
