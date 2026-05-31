import requests

payload = {
    "patientId": "P999",
    "cancerType": "Breast Cancer",
    "treatmentStage": "Chemotherapy",
    "city": "Istanbul",
    "fatigue": 10,
    "nausea": 9,
    "pain": 9,
    "mood": 1,
    "note": "Critical symptom escalation detected during demo."
}

r = requests.post("http://localhost:5050/checkin", json=payload)
print(r.status_code, r.text)
