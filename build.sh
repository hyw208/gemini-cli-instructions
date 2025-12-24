#!/bin/bash
set -e

echo "Building the project..."

# Create a virtual environment using uv
uv venv

# Install dependencies from pyproject.toml
uv pip install -e .[dev]

echo "Build complete. The virtual environment is ready in .venv"
