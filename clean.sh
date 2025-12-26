#!/bin/bash
set -e

echo "Cleaning up project..."

# Remove .pytest_cache
if [ -d ".pytest_cache" ]; then
    echo "Removing .pytest_cache..."
    rm -rf .pytest_cache
fi

# Remove __pycache__ directories
echo "Removing __pycache__ directories and *.pyc files..."
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Remove egg-info directory
if [ -d "gemini-scripts.egg-info" ]; then
    echo "Removing gemini-scripts.egg-info..."
    rm -rf gemini-scripts.egg-info
fi

# Remove local virtual environment
if [ -d ".venv" ]; then
    echo "Removing .venv..."
    rm -rf .venv
fi

echo "Cleanup complete."
