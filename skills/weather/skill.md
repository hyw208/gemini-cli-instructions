---
skillId: weather
description: Get current weather and forecasts for any city
interactions:
  - weather
  - temperature
  - forecast
  - how hot
  - how cold
---

# Instructions

Use this skill when the user asks about weather, temperature, or climate conditions for a specific city.

## Commands

**Get current weather:**
```bash
.github/skills/.venv/bin/python -m scripts.weather --city "CITY_NAME"
```

**Get forecast:**
```bash
.github/skills/.venv/bin/python -m scripts.weather --city "CITY_NAME" --forecast [DAYS]
```

Replace `CITY_NAME` with the city name (e.g., "Taipei", "Tokyo", "London").
Optional: `DAYS` for forecast (default: 3, max: 16)

## Output Format

**Current weather:**
```json
{
  "status": "success",
  "action": "current",
  "city": "Taipei",
  "temperature": 14,
  "unit": "C",
  "conditions": "Slight rain",
  "humidity": 89,
  "wind_speed_kmph": 10,
  "feels_like": 13,
  "timestamp": "2025-12-26T14:17:17.597917"
}
```

**Forecast:**
```json
{
  "status": "success",
  "action": "forecast",
  "city": "Taipei",
  "days": 3,
  "forecast": [
    {"date": "2025-12-27", "max_temp_c": 18, "min_temp_c": 13, "avg_temp_c": 15, "conditions": "Slight rain"},
    {"date": "2025-12-28", "max_temp_c": 20, "min_temp_c": 16, "avg_temp_c": 18, "conditions": "Overcast"}
  ]
}
```

**Error:**
```json
{"status": "error", "message": "ERROR_MESSAGE"}
```

## Data Source

Uses Open-Meteo API (https://open-meteo.com) - free, no API key required, fast and reliable


