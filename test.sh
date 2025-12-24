#!/bin/bash
set -e

echo "Running tests..."

# Ensure the project is built and dependencies are installed
./build.sh

# Run pytest
./.venv/bin/pytest

echo "Tests passed."
