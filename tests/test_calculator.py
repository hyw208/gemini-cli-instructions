from scripts.calculator import calculate
import json

def test_calculate_addition():
    result = calculate("2+2")
    result = json.loads(result)
    assert result["status"] == "success"
    assert result["result"] == 4

def test_calculate_error():
    result = calculate("2+")
    result = json.loads(result)
    assert result["status"] == "error"
