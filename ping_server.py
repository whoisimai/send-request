import os
import sys
from urllib.parse import urlparse

import requests


def validate_url(value: str) -> bool:
    parsed = urlparse(value)
    return bool(parsed.scheme and parsed.netloc)


url = os.getenv("SERVER_URL")

if not url:
    print("ERROR: SERVER_URL is not set in the environment variables.")
    sys.exit(1)

if not validate_url(url):
    print(f"ERROR: SERVER_URL is not a valid URL: {url}")
    sys.exit(1)

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        print(f"Ping successful: {response.status_code}")
        sys.exit(0)

    print(
        f"Ping failed: {response.status_code} {response.reason}"
        f" - URL: {url}"
    )
    sys.exit(1)

except requests.exceptions.RequestException as e:
    print(f"An error occurred while pinging {url}: {e}")
    sys.exit(1)
