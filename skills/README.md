# Available Skills

Before responding to user requests, always check the skills listed below and use them to fulfill the request.

## Skills Summary

| Skill | Description | Command | Interactions |
|-------|-------------|---------|--------------|
| **calculator** | Safely evaluates a mathematical expression | `.github/skills/.venv/bin/python -m scripts.calculator --expression "EXPRESSION"` | calculate, math, evaluate expression, compute, solve |
| **weather** | Get current weather and forecasts for any city using Open-Meteo API | `.github/skills/.venv/bin/python -m scripts.weather --city "CITY_NAME" [--forecast DAYS]` | weather, temperature, forecast, how hot, how cold |

## Usage

When the user's request matches any of the interaction keywords, use the corresponding skill by running the command provided. Replace placeholders like `EXPRESSION` or `CITY_NAME` with the actual values from the user's request.

For detailed instructions on each skill, see the individual `skill.md` files in each skill folder.
