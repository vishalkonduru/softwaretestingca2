"""Create a MantisBT issue and retrieve it through the REST API.

Set MANTIS_URL and MANTIS_API_TOKEN as environment variables.
"""
import os
import requests

BASE_URL = os.environ["MANTIS_URL"].rstrip("/")
API_TOKEN = os.environ["MANTIS_API_TOKEN"]

headers = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json",
}
payload = {
    "summary": "Login validation issue reported by API",
    "description": "Steps to reproduce: open login, submit test data, observe result.",
    "project": {"name": "TestProject"},
    "category": {"name": "General"},
}

create_response = requests.post(
    f"{BASE_URL}/issues/", headers=headers, json=payload, timeout=30
)
create_response.raise_for_status()
issue_id = create_response.json()["issue"]["id"]
print("Bug Created:", issue_id)

details_response = requests.get(
    f"{BASE_URL}/issues/{issue_id}", headers=headers, timeout=30
)
details_response.raise_for_status()
print("Bug Details:", details_response.json())
