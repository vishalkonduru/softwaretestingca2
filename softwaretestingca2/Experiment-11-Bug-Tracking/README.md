# Experiment 11: Bug Reporting and Tracking using Bugzilla or MantisBT

## Objective
Create a bug report and retrieve its details using either Bugzilla REST API or MantisBT REST API.

## Prerequisites
- Python 3
- A configured Bugzilla or MantisBT server
- API key/token and permission to create issues

## Install dependency
Run in PowerShell from this folder:

```powershell
py -m pip install -r requirements.txt
```

## Option 1: Bugzilla
Set your own server URL and API key. Do not commit real API keys.

```powershell
$env:BUGZILLA_URL = "https://your-bugzilla-host/rest"
$env:BUGZILLA_API_KEY = "YOUR_API_KEY"
py .\bugzilla_report.py
```

The script creates a bug, reads the returned ID, and retrieves the bug details.

## Option 2: MantisBT
Set the REST API base URL and token:

```powershell
$env:MANTIS_URL = "https://your-mantis-host/api/rest"
$env:MANTIS_API_TOKEN = "YOUR_API_TOKEN"
py .\mantis_report.py
```

The script creates an issue and retrieves it using its ID.

## Expected result
A successful run prints a created bug/issue ID followed by the returned issue details. Exact response fields and IDs depend on your server.

## Important
The URLs, product/component names, project/category names, and credentials are examples. Replace them with values that exist in your installation. Never commit API tokens.
