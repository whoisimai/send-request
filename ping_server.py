import os
from dotenv import load_dotenv
import requests

load_dotenv()

url = os.getenv("SERVER_URL")

print(f"Pinging {url}...")