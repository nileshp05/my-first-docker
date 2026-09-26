import os
from datetime import date
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

app = FastAPI(title="Vendor Risk Demo API")

VENDORS = [
    {
        "vendor_id": "V001",
        "vendor_name": "ABC Technologies",
        "availability_score": 95,
        "cyber_incidents": 1,
        "audit_score": 88
    },
    {
        "vendor_id": "V002",
        "vendor_name": "Global Services Ltd",
        "availability_score": 72,
        "cyber_incidents": 6,
        "audit_score": 55
    },
    {
        "vendor_id": "V003",
        "vendor_name": "Secure Systems Inc",
        "availability_score": 98,
        "cyber_incidents": 0,
        "audit_score": 96
    },
    {
        "vendor_id": "V004",
        "vendor_name": "Data Solutions",
        "availability_score": 80,
        "cyber_incidents": 3,
        "audit_score": 67
    },
    {
        "vendor_id": "V005",
        "vendor_name": "Cloud Partners",
        "availability_score": 60,
        "cyber_incidents": 8,
        "audit_score": 42
    }
]


@app.get("/vendor-risk")
def get_vendor_risk(x_api_key: str = Header(default=None)):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    return {
        "report_date": date.today().isoformat(),
        "records": VENDORS
    }