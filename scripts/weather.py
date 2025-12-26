#!/usr/bin/env python3
import sys
import json
import argparse
import requests
from datetime import datetime

def get_current_weather(city: str) -> dict:
    """
    Fetches current weather data from wttr.in and returns structured data.
    """
    try:
        response = requests.get(f"https://wttr.in/{city}?format=j1")
        response.raise_for_status()
        data = response.json()
        current = data['current_condition'][0]
        
        return {
            "status": "success",
            "action": "current",
            "city": city,
            "temperature": int(current['temp_C']),
            "unit": "C",
            "conditions": current.get('weatherDesc', [{}])[0].get('value', 'Unknown'),
            "humidity": int(current.get('humidity', 0)),
            "wind_speed_kmph": int(current.get('windspeedKmph', 0)),
            "feels_like": int(current.get('FeelsLikeC', 0)),
            "timestamp": datetime.now().isoformat()
        }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Request failed: {str(e)}"}
    except (KeyError, IndexError) as e:
        return {"status": "error", "message": "Could not parse weather data."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_forecast(city: str, days: int = 3) -> dict:
    """
    Fetches weather forecast from wttr.in.
    """
    try:
        response = requests.get(f"https://wttr.in/{city}?format=j1")
        response.raise_for_status()
        data = response.json()
        
        forecast_data = []
        for day in data['weather'][:days]:
            forecast_data.append({
                "date": day['date'],
                "max_temp_c": int(day['maxtempC']),
                "min_temp_c": int(day['mintempC']),
                "avg_temp_c": int(day['avgtempC']),
                "conditions": day['hourly'][0]['weatherDesc'][0]['value'] if day.get('hourly') else "Unknown"
            })
        
        return {
            "status": "success",
            "action": "forecast",
            "city": city,
            "days": days,
            "forecast": forecast_data
        }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Request failed: {str(e)}"}
    except (KeyError, IndexError) as e:
        return {"status": "error", "message": "Could not parse forecast data."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Weather information tool - Get current weather or forecasts for any city",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Get current weather:
    %(prog)s --city "Beijing"
  
  Get 7-day forecast:
    %(prog)s --city "Beijing" --forecast 7
  
  Get 3-day forecast (default):
    %(prog)s --city "London" --forecast
"""
    )
    parser.add_argument("--city", required=True, help="City name to get weather for")
    parser.add_argument("--forecast", nargs='?', const=3, type=int, metavar="DAYS",
                       help="Get weather forecast for N days (default: 3)")
    
    args = parser.parse_args()
    
    if args.forecast is not None:
        result = get_forecast(args.city, args.forecast)
    else:
        result = get_current_weather(args.city)
    
    print(json.dumps(result))
