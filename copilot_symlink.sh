#!/bin/bash
set -e

echo "Creating symbolic links to ~/skills..."

# Remove other conflicting files or symlinks
rm -rf ~/skills

# Create the rest of the symbolic links
ln -s "$(pwd)/skills" ~/skills

echo "Symbolic links created successfully."



