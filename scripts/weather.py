#!/usr/bin/env python3
import sys
import json
import argparse
import requests
from datetime import datetime

# WMO Weather codes mapping
WMO_WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

def get_coordinates(city: str) -> tuple:
    """
    Geocode city name to coordinates using Open-Meteo geocoding API.
    Returns (latitude, longitude, city_name) or raises exception.
    """
    try:
        response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1, "language": "en", "format": "json"},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        
        if not data.get("results"):
            raise ValueError(f"City '{city}' not found")
        
        result = data["results"][0]
        return result["latitude"], result["longitude"], result["name"]
    except requests.exceptions.RequestException as e:
        raise Exception(f"Geocoding request failed: {str(e)}")

def get_current_weather(city: str) -> dict:
    """
    Fetches current weather data from Open-Meteo and returns structured data.
    """
    try:
        lat, lon, city_name = get_coordinates(city)
        
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,apparent_temperature"
            },
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        current = data['current']
        
        weather_code = current.get('weather_code', 0)
        conditions = WMO_WEATHER_CODES.get(weather_code, "Unknown")
        
        return {
            "status": "success",
            "action": "current",
            "city": city_name,
            "temperature": int(current['temperature_2m']),
            "unit": "C",
            "conditions": conditions,
            "humidity": int(current.get('relative_humidity_2m', 0)),
            "wind_speed_kmph": int(current.get('wind_speed_10m', 0)),
            "feels_like": int(current.get('apparent_temperature', 0)),
            "timestamp": datetime.now().isoformat()
        }
    except ValueError as e:
        return {"status": "error", "message": str(e)}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Request failed: {str(e)}"}
    except (KeyError, IndexError) as e:
        return {"status": "error", "message": "Could not parse weather data."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_forecast(city: str, days: int = 3) -> dict:
    """
    Fetches weather forecast from Open-Meteo.
    """
    try:
        lat, lon, city_name = get_coordinates(city)
        
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "daily": "temperature_2m_max,temperature_2m_min,weather_code",
                "forecast_days": days,
                "timezone": "auto"
            },
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        daily = data['daily']
        
        forecast_data = []
        for i in range(len(daily['time'])):
            weather_code = daily['weather_code'][i]
            conditions = WMO_WEATHER_CODES.get(weather_code, "Unknown")
            max_temp = int(daily['temperature_2m_max'][i])
            min_temp = int(daily['temperature_2m_min'][i])
            
            forecast_data.append({
                "date": daily['time'][i],
                "max_temp_c": max_temp,
                "min_temp_c": min_temp,
                "avg_temp_c": int((max_temp + min_temp) / 2),
                "conditions": conditions
            })
        
        return {
            "status": "success",
            "action": "forecast",
            "city": city_name,
            "days": days,
            "forecast": forecast_data
        }
    except ValueError as e:
        return {"status": "error", "message": str(e)}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Request failed: {str(e)}"}
    except (KeyError, IndexError) as e:
        return {"status": "error", "message": "Could not parse forecast data."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Weather information tool - Get current weather or forecasts for any city using Open-Meteo API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Get current weather:
    %(prog)s --city "Beijing"
  
  Get 7-day forecast:
    %(prog)s --city "Beijing" --forecast 7
  
  Get 3-day forecast (default):
    %(prog)s --city "London" --forecast

Data source: Open-Meteo API (https://open-meteo.com)
Supports up to 16-day forecasts, no API key required.
"""
    )
    parser.add_argument("--city", required=True, help="City name to get weather for")
    parser.add_argument("--forecast", nargs='?', const=3, type=int, metavar="DAYS",
                       help="Get weather forecast for N days (default: 3, max: 16)")
    
    args = parser.parse_args()
    
    if args.forecast is not None:
        result = get_forecast(args.city, args.forecast)
    else:
        result = get_current_weather(args.city)
    
    print(json.dumps(result))
