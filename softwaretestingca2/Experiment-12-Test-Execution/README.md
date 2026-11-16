# Experiment 12: Test Case Execution and Defect Tracking

## Objective
Execute test cases, compare actual results with expected results, and record a defect whenever they differ.

## Prerequisites
- Python 3

## Run
Open PowerShell in this folder and execute:

```powershell
py .\test_execution.py
```

## Expected output
```text
Test Case ID: 1
Expected: Login Successful, Actual: Login Successful
Result: PASSED

Test Case ID: 2
Expected: Login Successful, Actual: Login Failed
Result: FAILED
Log Defect: Mismatch in login result
```

## Explanation
- Test case 1 passes because actual and expected results match.
- Test case 2 intentionally contains an incorrect expected result to demonstrate defect logging.
- Use `defect_report_template.md` to record the title, steps, expected result, actual result, priority, and status.

## Note
This is a mock Python simulation. It does not connect to a real login application or automatically create an issue in Bugzilla/MantisBT.
