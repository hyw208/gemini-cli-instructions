---
skillId: weather
description: Get temperature for a given city
interactions:
  - weather
  - temperature
  - forecast
  - how hot
  - how cold
---

# Instructions

Use this skill when the user asks about weather, temperature, or climate conditions for a specific city.

## Command

Run: `./.venv/bin/python -m scripts.weather --city "CITY_NAME"`

Replace `CITY_NAME` with the name of the city (e.g., "Taipei", "Tokyo", "London").

## Output Format

The command returns JSON:
- Success: `{"status": "success", "result": "TEMPERATURE"}`
- Error: `{"status": "error", "message": "ERROR_MESSAGE"}`

Example: For city "Taipei", the result might be `{"status": "success", "result": "17C"}`


