# Test Plan: Login Module

## 1. Objective
Verify login functionality with valid and invalid credentials.

## 2. Scope
- **In scope:** Web login form, valid login, invalid username/password, and empty fields.
- **Out of scope:** Forgot Password and account registration.

## 3. Features to be tested
- Username and password input
- Login button
- Successful login redirect
- Error message for invalid credentials

## 4. Test deliverables
- Test cases
- Test execution results
- Defect reports
- Test summary report

## 5. Entry criteria
- Development is complete.
- Test environment is available.
- Test data and test accounts are ready.

## 6. Exit criteria
- All planned test cases have been executed.
- No critical defects remain open.
- Results are reviewed and documented.

## 7. Roles and responsibilities
- Tester: prepare cases, execute tests, report defects.
- Developer: investigate and fix defects.
- Test lead: review results and provide sign-off.

## 8. Schedule
Plan and record the actual testing dates before execution.

## 9. Risks and mitigations
- Test environment unavailable: confirm access before testing.
- Test data invalid: prepare and verify test accounts.
- Critical defect found: report immediately and block release pending review.

## Tools
Selenium WebDriver, JUnit, and a defect tracker such as Bugzilla or MantisBT.
