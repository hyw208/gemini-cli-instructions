---
skillId: calculator
description: Safely evaluates a mathematical expression
interactions:
  - calculate
  - math
  - evaluate expression
  - compute
  - solve
---

# Instructions

Use this skill when the user asks to perform mathematical calculations or evaluate mathematical expressions.

## Command

Run: `.github/skills/.venv/bin/python .github/skills/scripts/calculator.py --expression "EXPRESSION"`

Replace `EXPRESSION` with the mathematical expression to evaluate (e.g., "2+3*4").

## Output Format

The command returns JSON:
- Success: `{"status": "success", "result": VALUE}`
- Error: `{"status": "error", "message": "ERROR_MESSAGE"}`

Example: For expression "2+3*4", the result will be `{"status": "success", "result": 14}`

