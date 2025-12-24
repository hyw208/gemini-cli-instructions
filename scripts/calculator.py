#!/usr/bin/env python3
import sys
import json
import argparse

def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression and returns a JSON string.
    """
    try:
        allowed_names = {"__builtins__": {}}
        result = eval(expression, allowed_names, {})
        # Return a structured success response
        return json.dumps({"status": "success", "result": result})
    except Exception as e:
        # Return a structured error
        return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--expression", required=True)
    args = parser.parse_args()
    print(calculate(args.expression))
