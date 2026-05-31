import csv
import json
import os
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv("backend/.env")

SPLUNK_HEC_URL = os.getenv("SPLUNK_HEC_URL")
SPLUNK_HEC_TOKEN = os.getenv("SPLUNK_HEC_TOKEN")
SPLUNK_INDEX = os.getenv("SPLUNK_INDEX", "main")

HEADERS = {
    "Authorization": f"Splunk {SPLUNK_HEC_TOKEN}",
    "Content-Type": "application/json"
}

def send_event(event, sourcetype, source):
    payload = {
        "index": SPLUNK_INDEX,
        "sourcetype": sourcetype,
        "source": source,
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
        print("ERROR:", r.status_code, r.text)

def import_csv(file_path, sourcetype, source, limit=None):
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return

    print(f"🚀 Importing {file_path.name} as {sourcetype}")

    with file_path.open("r", encoding="utf-8-sig", errors="ignore") as f:
        reader = csv.DictReader(f)
        count = 0

        for row in reader:
            clean_row = {}

            for k, v in row.items():
                if k is None:
                    continue

                key = k.strip().replace(" ", "_").replace("/", "_")
                value = v.strip() if isinstance(v, str) else v

                if value == "":
                    value = None

                clean_row[key] = value

            clean_row["app"] = "OncoConnect AI"
            clean_row["dataset_source"] = source
            clean_row["ingested_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

            send_event(clean_row, sourcetype, source)

            count += 1

            if count % 1000 == 0:
                print(f"✅ {count} events sent from {file_path.name}")

            if limit and count >= limit:
                break

    print(f"🎉 Finished {file_path.name}: {count} events sent")

if __name__ == "__main__":
    import_csv(
        "ThyroTrack-MV Processed Dataset.csv",
        "oncoconnect:thyroid",
        "thyrotrack_multi_visit",
        limit=10000
    )

    import_csv(
        "chemotherapy_patient_data.csv",
        "oncoconnect:chemotherapy",
        "chemotherapy_regimens",
        limit=10000
    )

    print("✅ Dataset import completed.")
