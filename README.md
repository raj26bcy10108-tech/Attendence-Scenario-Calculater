# Attendance Scenario Calculator

A Python command-line tool that helps students plan their attendance: check the current percentage, find how many classes are needed to hit a target, and predict the effect of attending or missing future classes.

Made for the **Python Essentials** course (Fall 2026-27) by Raj Gupta (26BCY10108).

## Features

- Current attendance percentage
- Classes required to reach a target percentage
- Predicted attendance after upcoming attended and/or missed classes
- Input validation (negative values, attended > total, bad text, invalid target)
- Standard library only, no installation needed

## Requirements

- Python 3.6 or newer

## How to Run

```bash
python main.py
```

## Sample Session

```
ATTENDANCE SCENARIO CALCULATOR
1. Calculate current attendance
2. Find classes needed for target
3. Predict future attendance
4. Exit
Enter choice: 2
Total classes: 60
Classes attended: 42
Target percentage: 75

Current attendance: 70.00%
Classes required to reach target: 12
```

## Formulas

```
Current %  = (Attended / Total) x 100
Future %   = (Attended + Future Attended) / (Total + Future Attended + Future Missed) x 100
```

## Project Structure

`main.py` is organised into four sections:

| Module | Purpose |
|--------|---------|
| Input & Validation | Reads values and checks they are valid |
| Attendance Calculator | Current and future percentage formulas |
| Scenario Engine | Classes needed for target, future scenarios |
| Report / Output | Menu and formatted terminal results |

## Testing

| Test case | Expected result |
|-----------|-----------------|
| 40/50 attendance | 80.00% displayed |
| Attended > Total | Validation error |
| Negative value | Validation error |
| Target below current | No extra classes required |
| Future attended classes | New percentage calculated |
| Future missed classes | Reduced percentage calculated |

## Limitations

- Uses only values entered by the user; no access to official records.
- Results are for planning, not an official academic decision. Your university may use different rules or rounding.

## Future Enhancements

GUI, database storage, multiple subjects and monthly history, charts, CSV/PDF export, and configurable institutional rules.
