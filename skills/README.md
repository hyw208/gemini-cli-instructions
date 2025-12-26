# .github/skills README

This directory contains reusable skills for automation and workflow enhancement. Each skill is organized in its own subdirectory with a `skill.md` file describing its usage, commands, and output format.

## Available Skills

### calculator
- **Description:** Safely evaluates a mathematical expression.
- **Interactions:** calculate, math, evaluate expression, compute, solve
- **Usage:**
  - Use when a user requests mathematical calculations or expression evaluation.
  - Command: `./.venv/bin/python -m scripts.calculator --expression "EXPRESSION"`
  - Output: JSON with `status` and `result` or `error` message.

### weather
- **Description:** Get temperature for a given city.
- **Interactions:** weather, temperature, forecast, how hot, how cold
- **Usage:**
  - Use when a user asks about weather, temperature, or climate for a city.
  - Command: `./.venv/bin/python -m scripts.weather --city "CITY_NAME"`
  - Output: JSON with `status` and `result` (temperature) or `error` message.

---

To add a new skill, create a subdirectory with a `skill.md` file following the same format.
