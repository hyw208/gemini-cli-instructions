# Gemini CLI Extensibility

This project is a template for extending the Gemini CLI with custom commands and making them available to both Gemini CLI and GitHub Copilot agents.

## Project Structure

This project is structured as a standard Python project with integrations for both Gemini CLI and GitHub Copilot.

### Python Core
-   `scripts/`: A Python package containing the implementation of custom commands (shared by both Gemini CLI and Copilot).
-   `tests/`: Contains tests for the custom commands.
-   `pyproject.toml`: Defines the project dependencies.
-   `build.sh`: A script to build the project, create a virtual environment, and install dependencies.
-   `test.sh`: A script to run the tests.
-   `clean.sh`: A script to clean up temporary files.

### Gemini CLI Integration
-   `commands/`: Contains the `.toml` configuration files for Gemini CLI custom commands.
-   `gemini_symlink.sh`: A script to create symbolic links to the `~/.gemini` directory.

### GitHub Copilot Integration
-   `skills/`: Contains skill definitions (`.md` files) for GitHub Copilot agents.
-   `copilot_symlink.sh`: A script to create symbolic links to a project's `.github/skills` directory.

## Getting Started

### Installation

After cloning this project, you need to build it and link the files to make them available.

1.  **Build the project:**

    Run the `build.sh` script to create the virtual environment (`.venv`) and install the necessary dependencies.

    ```bash
    ./build.sh
    ```

2.  **Test the project:**

    Run the `test.sh` script to verify everything works correctly.

    ```bash
    ./test.sh
    ```

### Integration with Gemini CLI

To use the custom commands with Gemini CLI:

1.  **Create symbolic links:**

    Run the `gemini_symlink.sh` script to automatically create the necessary symbolic links.

    ```bash
    ./gemini_symlink.sh
    ```

    This script will:
    -   Create the `~/.gemini` directory if it doesn't exist.
    -   Prompt you if an existing `GEMINI.md` file is found.
    -   Create symbolic links for the `commands`, `scripts`, `.venv`, and `GEMINI.md` directories and files.

    Now, the Gemini CLI will be able to find and use the custom commands from this project.

### Integration with GitHub Copilot

To make skills available to GitHub Copilot agents in any project:

1.  **Link skills to your project:**

    Run the `copilot_symlink.sh` script with the path to your target project.

    ```bash
    ./copilot_symlink.sh --project-folder /path/to/your/project
    ```

    This script will:
    -   Create a `.github` directory in the target project if it doesn't exist.
    -   Create a symbolic link from `<project>/.github/skills` to this project's `skills/` directory.

    Now, Copilot agents in that project can discover and use the skills defined in this repository.

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

## Creating Custom Commands and Skills

### For Gemini CLI

To create a new custom command for Gemini CLI:

1.  **Create a `.toml` file** in the `commands/` directory. This file defines the command's `description` and `prompt`. The `prompt` should execute your Python script.

    Example: `commands/calculator.toml`

    ```toml
    description = "Simple Calculator"
    prompt = """
    Calculates mathematical expressions:
    !{ ./.venv/bin/python -m scripts.calculator --expression "{{expression}}"}
    """
    ```

2.  **Create a Python script** in the `scripts/` directory. This script should contain the logic for your command and use `argparse` to handle command-line arguments. Output should be JSON format.

    Example: `scripts/calculator.py`

    ```python
    #!/usr/bin/env python3
    import sys
    import json
    import argparse

    def calculate(expression: str) -> str:
        # ... your logic here ...
        return json.dumps({"status": "success", "result": result})

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--expression", required=True)
        args = parser.parse_args()
        print(calculate(args.expression))
    ```

3.  **Add tests** for your new command in the `tests/` directory.

### For GitHub Copilot Agents

To create a new skill for Copilot agents:

1.  **Create a folder** in the `skills/` directory with your skill name (e.g., `skills/calculator/`).

2.  **Create a `skill.md` file** in that folder with YAML front matter and instructions:

    Example: `skills/calculator/skill.md`

    ```markdown
    ---
    skillId: calculator
    description: Safely evaluates a mathematical expression
    interactions:
      - calculate
      - math
      - evaluate expression
    ---

    # Instructions

    Use this skill when the user asks to perform mathematical calculations.

    ## Command

    Run: `./.venv/bin/python -m scripts.calculator --expression "EXPRESSION"`

    ## Output Format

    The command returns JSON:
    - Success: `{"status": "success", "result": VALUE}`
    - Error: `{"status": "error", "message": "ERROR_MESSAGE"}`
    ```

3.  **Reuse the same Python script** from `scripts/` - this way both Gemini CLI and Copilot agents use the same tested implementation.

## Available Commands/Skills

-   **calculator**: Evaluates mathematical expressions
-   **weather**: Gets temperature for a given city

4.  **Add any new dependencies** to `pyproject.toml`.