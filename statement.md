# Problem Statement

**Project:** Attendance Scenario Calculator
**Course:** Python Essentials, Fall Semester 2026-27
**Submitted by:** Raj Gupta (26BCY10108)

## Problem

Students commonly calculate attendance by hand using formulas and repeated trial-and-error. This leads to calculation mistakes and makes it hard to answer practical questions such as:

- "How many classes do I need to attend to reach 75%?"
- "What happens if I miss two more classes?"
- "What will my attendance be after attending the next ten classes?"

## Proposed Solution

A Python command-line application that takes total classes conducted and classes attended, then calculates the current attendance percentage and gives scenario-based results for future attendance decisions.

## Objectives

1. Calculate current attendance percentage accurately.
2. Estimate the classes needed to reach a target percentage.
3. Predict attendance after future attended or missed classes.
4. Validate user input and prevent invalid calculations.
5. Provide simple, readable terminal output suitable for a beginner.

## Functional Requirements

| ID  | Requirement |
|-----|-------------|
| FR1 | Accept total classes conducted and classes attended |
| FR2 | Calculate current attendance percentage |
| FR3 | Calculate classes needed to reach a target percentage |
| FR4 | Calculate future attendance after upcoming attended classes |
| FR5 | Calculate the effect of upcoming missed classes |
| FR6 | Display clear results in the terminal |

## Non-Functional Requirements

- **Usability:** simple enough for a beginner to use from a terminal.
- **Reliability:** invalid, negative or inconsistent inputs are rejected with a clear message.
- **Maintainability:** calculation and validation logic are separated into functions.
- **Portability:** runs on Python 3 with the standard library only, no GUI dependency.

## Formulas

- Current: `Attendance % = (Attended / Total) x 100`
- Future: `Future % = (Attended + Future Attended) / (Total + Future Attended + Future Missed) x 100`
- Target: the number of future attended classes is increased until the percentage reaches the target.

## Example

Total = 60, Attended = 42, Target = 75%
Current attendance = 70%. Classes that must be attended consecutively: **12**.

## Validation Rules

1. Total classes must be greater than zero.
2. Attended classes cannot be negative.
3. Attended classes cannot exceed total classes.
4. Target must be between 0% and 100%.
5. Future attended/missed counts cannot be negative.
6. Non-numeric input must not crash the program.

## Scope and Limitations

- Calculations use only user-entered values.
- No access to official college attendance records.
- Results are for planning only and are not an official academic decision. University rules may use different policies, rounding or exclusions.
