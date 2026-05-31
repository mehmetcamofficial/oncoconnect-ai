import csv
import json
import os
import time
import requests
import urllib3
from pathlib import Path
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv("backend/.env")

SPLUNK_HEC_URL = os.getenv("SPLUNK_HEC_URL")
SPLUNK_HEC_TOKEN = os.getenv("SPLUNK_HEC_TOKEN")
SPLUNK_INDEX = os.getenv("SPLUNK_INDEX", "main")

HEADERS = {
    "Authorization": f"Splunk {SPLUNK_HEC_TOKEN}",
    "Content-Type": "application/json"
}

CSV_FILE = Path("chemotherapy_patient_data.csv")

if not CSV_FILE.exists():
    print("❌ chemotherapy_patient_data.csv bulunamadı")
    raise SystemExit

count = 0

with CSV_FILE.open("r", encoding="utf-8-sig", errors="ignore") as f:
    reader = csv.DictReader(f)

    print("Columns:", reader.fieldnames)

    for row in reader:
        event = {}

        for k, v in row.items():
            if not k:
                continue

            key = k.strip().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
            value = v.strip() if isinstance(v, str) else v

            if value == "":
                value = None

            event[key] = value

        event["app"] = "OncoConnect AI"
        event["dataset_source"] = "chemotherapy_regimens"
        event["ingested_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        payload = {
            "index": SPLUNK_INDEX,
            "sourcetype": "oncoconnect:chemotherapy",
            "source": "chemotherapy_regimens",
            "event": event
        }

        r = requests.post(
            SPLUNK_HEC_URL,
            headers=HEADERS,
            data=json.dumps(payload),
            verify=False,
            timeout=10
        )

        if r.status_code != 200:
            print("❌ ERROR:", r.status_code, r.text)
            break

        count += 1

        if count % 1000 == 0:
            print(f"✅ {count} chemotherapy events sent")

        if count >= 10000:
            break

print(f"🎉 Finished. Total sent: {count}")
