import os
from dotenv import load_dotenv
import requests

load_dotenv()

url = os.getenv("SERVER_URL")

if not url:
    print("SERVER_URL is not set in the environment variables.")