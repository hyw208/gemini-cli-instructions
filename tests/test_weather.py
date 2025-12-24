from scripts.weather import weather
import json
from unittest.mock import patch

@patch("scripts.weather.requests.get")
def test_weather_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current_condition": [{"temp_C": "10"}]
    }

    result = weather("London")
    result = json.loads(result)
    assert result["status"] == "success"
    assert result["result"] == "10C"

@patch("scripts.weather.requests.get")
def test_weather_error(mock_get):
    mock_get.side_effect = Exception("API error")

    result = weather("London")
    result = json.loads(result)
    assert result["status"] == "error"
