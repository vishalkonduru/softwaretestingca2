# Test Summary Report: Login Module

> The figures below reproduce the lab-manual example and are illustrative.

## Test details
- **Module tested:** Login
- **Test period:** 5–8 July 2025
- **Total test cases:** 10
- **Passed:** 9
- **Failed:** 1

## Defects
- **Open critical defects:** 1
- **Description:** SQL injection attempt was not blocked.

## Observations
The login functionality works for the tested cases, but the application has a critical security weakness.

## Recommendation
Fix and retest the SQL injection defect before production deployment.

## Exit criteria
Not met. A critical defect remains open.

## Sign-off
**Not Ready**
