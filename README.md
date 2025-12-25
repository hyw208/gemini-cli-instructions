# Gemini CLI Extensibility

This project is a template for extending the Gemini CLI with custom commands.

## Project Structure

This project is structured as a standard Python project.

-   `commands/`: Contains the `.toml` configuration files for the custom commands.
-   `skills/`: A symbolic link to `commands/`, providing an alternative name for the custom commands (skills).
-   `scripts/`: A Python package containing the implementation of the custom commands.
-   `tests/`: Contains tests for the custom commands.
-   `pyproject.toml`: Defines the project dependencies.
-   `build.sh`: A script to build the project, create a virtual environment, and install dependencies.
-   `test.sh`: A script to run the tests.
-   `clean.sh`: A script to clean up temporary files.
-   `symlink.sh`: A script to create symbolic links to the `~/.gemini` directory.

## Getting Started

### Installation

After cloning this project, you need to link the project files to the Gemini CLI's configuration directory (`~/.gemini`).

1.  **Build the project:**

    Run the `build.sh` script to create the virtual environment (`.venv`) and install the necessary dependencies.

    ```bash
    ./build.sh
    ```

2.  **Create symbolic links:**

    Run the `symlink.sh` script to automatically create the necessary symbolic links.

    ```bash
    ./symlink.sh
    ```

    This script will:
    -   Create the `~/.gemini` directory if it doesn't exist.
    -   Prompt you if an existing `GEMINI.md` file is found.
    -   Create symbolic links for the `commands`, `scripts`, `.venv`, and `GEMINI.md` directories and files.

    Now, the Gemini CLI will be able to find and use the custom commands from this project.

### Development

This project includes scripts to help with development:

*   `build.sh`: Creates a virtual environment in `.venv/` and installs the required dependencies from `pyproject.toml`.
*   `test.sh`: Runs the test suite using `pytest`. It will also run `build.sh` first to ensure the environment is set up correctly.
*   `clean.sh`: Removes temporary files and directories, such as `.pytest_cache`, `__pycache__`, and `gemini-scripts.egg-info`.

To use these scripts, run them from the root of the project:

```bash
./build.sh
./test.sh
./clean.sh
```

## Creating Custom Commands

To create a new custom command, you need to:

1.  **Create a `.toml` file** in the `commands/` directory. This file defines the command's `description` and `prompt`. The `prompt` should execute your Python script.

    Example: `commands/calculator.toml`

    ```toml
    description = "Simple Calculator"
    prompt = """
    Calculates mathematical expressions:
    !{ ./.venv/bin/python -m scripts.calculator --expression "{{expression}}"}
    """
    ```

2.  **Create a Python script** in the `scripts/` directory. This script should contain the logic for your command and use `argparse` to handle command-line arguments.

    Example: `scripts/calculator.py`

    ```python
    #!/usr/bin/env python3
    import sys
    import json
    import argparse

    def calculate(expression: str) -> str:
        # ... your logic here ...

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--expression", required=True)
        args = parser.parse_args()
        print(calculate(args.expression))
    ```

3.  **Add tests** for your new command in the `tests/` directory.

4.  **Add any new dependencies** to `pyproject.toml`.