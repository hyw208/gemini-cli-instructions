#!/usr/bin/env python3
import sys
import json
import argparse
import requests

def weather(city: str) -> str:
    """
    Fetches weather data from wttr.in and returns a JSON string.
    """
    try:
        print("city: " + city)
        response = requests.get(f"https://wttr.in/{city}?format=j1")
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return json.dumps({"status": "success", "result": data['current_condition'][0]['temp_C'] + "C"})
    except requests.exceptions.RequestException as e:
        return json.dumps({"status": "error", "message": str(e)})
    except (KeyError, IndexError) as e:
        return json.dumps({"status": "error", "message": "Could not parse weather data."})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True)
    args = parser.parse_args()
    print(weather(args.city))
