from scripts.weather import weather
import json
from unittest.mock import patch, MagicMock

@patch("scripts.weather.requests.get")
def test_weather_success(mock_get):
    # Mock the geocoding response
    geo_response = MagicMock()
    geo_response.json.return_value = {
        "results": [{
            "latitude": 51.5074,
            "longitude": -0.1278,
            "name": "London"
        }]
    }
    geo_response.raise_for_status = MagicMock()
    
    # Mock weather response
    weather_response = MagicMock()
    weather_response.json.return_value = {
        "current": {
            "temperature_2m": 10,
            "relative_humidity_2m": 75,
            "weather_code": 0,
            "wind_speed_10m": 5,
            "apparent_temperature": 9
        }
    }
    weather_response.raise_for_status = MagicMock()
    
    mock_get.side_effect = [geo_response, weather_response]

    result = weather("London")
    result = json.loads(result)
    assert result["status"] == "success"
    assert result["temperature"] == 10
    assert result["city"] == "London"

@patch("scripts.weather.requests.get")
def test_weather_error(mock_get):
    mock_get.side_effect = Exception("API error")

    result = weather("London")
    result = json.loads(result)
    assert result["status"] == "error"
