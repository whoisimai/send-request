import os
import requests


url = os.getenv("SERVER_URL")

if not url:
    print("SERVER_URL is not set in the environment variables.")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Ping successful: {response.status_code}")
    else:
        print(f"Ping failed: {response.status_code}")

except requests.exceptions.RequestException as e:

    print(f"An error occurred: {e}")