# Custom Gemini Commands

This document provides instructions for the custom commands available in this project. These GEMINI custom commands are under ./commands folder where there are multiple *.toml files containing explicit instructions on how to use/invoke/execute them.

| GEMINI Command      | Description                                                 | Usage                                                              | Run |
|--------------|-------------------------------------------------------------|--------------------------------------------------------------------|------|
| `/calculator` | A simple calculator that evaluates mathematical expressions. | `calculator [expression]` (e.g., `calculator 2+2`) | `!{ ./commands/.venv/bin/python -m scripts.calculator --expression {{args}}}` |
| `/weather`    | Get weather information for a city.                         | `weather --city "CITY" [--forecast [DAYS]]` (e.g., `weather --city "London" --forecast 7`) | `!{ ./commands/.venv/bin/python -m scripts.weather {{args}}}` |
