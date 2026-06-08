# OncoConnect AI — Splunk Observability MVP

OncoConnect AI is a hackathon MVP designed to support cancer patients and caregivers through structured daily symptom check-ins and real-time observability.

The platform allows patients to submit fatigue, nausea, pain, mood, treatment stage, cancer type, city, and notes. The backend computes a lightweight risk score and sends each structured check-in event to Splunk through HTTP Event Collector.

Splunk is used as the observability and analytics layer. It enables real-time dashboards for patient check-in volume, risk distribution, symptom trends, city-level patterns, and high-risk patient alerts.

## Core Components

- React / Vite frontend for patient check-ins
- Node.js / Express backend
- Risk scoring logic
- Splunk HEC integration
- Splunk dashboard for monitoring and analytics
- Synthetic oncology dataset import for demo-scale observability

## Hackathon Value

This MVP demonstrates how Splunk can be used beyond traditional IT logs, as a real-time health observability layer for patient-reported outcomes, early risk detection, and social impact monitoring.
