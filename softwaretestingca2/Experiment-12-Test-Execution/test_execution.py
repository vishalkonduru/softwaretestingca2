"""Simulate login test execution and report mismatches as defects."""

def login(username, password):
    # Mock application behavior for a lab demonstration.
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Login Failed"


test_cases = [
    {
        "id": 1,
        "username": "admin",
        "password": "admin123",
        "expected": "Login Successful",
    },
    {
        "id": 2,
        "username": "admin",
        "password": "wrongpass",
        "expected": "Login Successful",  # Intentional mismatch for demonstration
    },
]

for test in test_cases:
    actual = login(test["username"], test["password"])
    print(f"Test Case ID: {test['id']}")
    print(f"Expected: {test['expected']}, Actual: {actual}")

    if actual == test["expected"]:
        print("Result: PASSED\n")
    else:
        print("Result: FAILED")
        print("Log Defect: Mismatch in login result\n")
