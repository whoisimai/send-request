import os
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def validate_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
        return bool(parsed.scheme and parsed.netloc)
    except ValueError:
        return False


load_dotenv(Path(__file__).resolve().with_name(".env"), override=False)
url = os.getenv("SERVER_URL")

if not url:
    print("ERROR: SERVER_URL is not set in the environment variables.")
    sys.exit(1)

if not validate_url(url):
    print(f"ERROR: SERVER_URL is not a valid URL: {url}")
    sys.exit(1)

max_attempts = 3
for attempt in range(1, max_attempts + 1):
    print(f"Ping attempt {attempt}/{max_attempts}", flush=True)
    try:
        response = requests.get(url, timeout=(10, 90))
        status = response.status_code
        reason = response.reason
        response.close()
        if status == 200:
            print(f"Ping successful: {status}")
            sys.exit(0)

        print(f"Ping failed: {status} {reason} - URL: {url}")
        if status not in (502, 503, 504):
            sys.exit(1)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        print(f"Temporary error while pinging {url}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while pinging {url}: {e}")
        sys.exit(1)

    if attempt < max_attempts:
        print("Retrying in 10 seconds...", flush=True)
        time.sleep(10)

print(f"Ping failed after {max_attempts} attempts.")
sys.exit(1)
