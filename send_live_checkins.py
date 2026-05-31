import requests
import random
import time

patients = [
    {"patientId": "P010", "cancerType": "Breast Cancer", "treatmentStage": "Chemotherapy", "city": "Istanbul"},
    {"patientId": "P011", "cancerType": "Lung Cancer", "treatmentStage": "Radiotherapy", "city": "Ankara"},
    {"patientId": "P012", "cancerType": "Colon Cancer", "treatmentStage": "Follow-up", "city": "Izmir"},
    {"patientId": "P013", "cancerType": "Lymphoma", "treatmentStage": "Immunotherapy", "city": "Bursa"},
]

for i in range(10):
    p = random.choice(patients)

    payload = {
        **p,
        "fatigue": random.randint(3, 10),
        "nausea": random.randint(1, 9),
        "pain": random.randint(1, 9),
        "mood": random.randint(1, 8),
        "note": "Automated live demo check-in from VS Code."
    }

    r = requests.post(
        "http://localhost:5050/checkin",
        json=payload,
        timeout=10
    )

    print(i + 1, payload["patientId"], r.status_code, r.text)
    time.sleep(1)
