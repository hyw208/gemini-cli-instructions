# Available Skills

Before responding to user requests, always check the skills listed below and use them to fulfill the request.

## Skills Summary

| Skill | Description | Command | Interactions |
|-------|-------------|---------|--------------|
| **calculator** | Safely evaluates a mathematical expression | `.github/skills/.venv/bin/python .github/skills/scripts/calculator.py --expression "EXPRESSION"` | calculate, math, evaluate expression, compute, solve |
| **weather** | Get temperature and conditions for a given city | `.github/skills/.venv/bin/python .github/skills/scripts/weather.py --city "CITY_NAME"` | weather, temperature, forecast, how hot, how cold |

## Usage

When the user's request matches any of the interaction keywords, use the corresponding skill by running the command provided. Replace placeholders like `EXPRESSION` or `CITY_NAME` with the actual values from the user's request.

For detailed instructions on each skill, see the individual `skill.md` files in each skill folder.
