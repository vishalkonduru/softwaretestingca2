"""Create a Bugzilla issue and fetch its details using the REST API.

Set BUGZILLA_URL and BUGZILLA_API_KEY as environment variables before running.
"""
import os
import requests

BASE_URL = os.environ["BUGZILLA_URL"].rstrip("/")
API_KEY = os.environ["BUGZILLA_API_KEY"]

payload = {
    "product": "TestProduct",
    "component": "TestComponent",
    "summary": "Login validation issue reported by API",
    "version": "unspecified",
    "description": "Steps to reproduce: open login, submit test data, observe result.",
    "op_sys": "All",
    "platform": "All",
    "api_key": API_KEY,
}

create_response = requests.post(f"{BASE_URL}/bug", data=payload, timeout=30)
create_response.raise_for_status()
bug_id = create_response.json()["id"]
print("Bug Created:", bug_id)

details_response = requests.get(
    f"{BASE_URL}/bug/{bug_id}",
    params={"api_key": API_KEY},
    timeout=30,
)
details_response.raise_for_status()
print("Bug Details:", details_response.json())
