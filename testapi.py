import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8080/vendor-risk")
API_KEY = os.getenv("API_KEY")

headers = {
    "x-api-key": API_KEY
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Report Date: {data['report_date']}")
    print(f"Total Vendors: {len(data['records'])}")
    print(data["records"])
else:
    print(f"Failed with status {response.status_code}: {response.json()}")