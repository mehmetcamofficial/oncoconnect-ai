from pathlib import Path

Path("backend/server.js").write_text("""
const express = require("express");
const cors = require("cors");
const axios = require("axios");
const https = require("https");
require("dotenv").config();

const app = express();

app.use(cors());
app.use(express.json());

const splunkClient = axios.create({
  httpsAgent: new https.Agent({
    rejectUnauthorized: false
  }),
  headers: {
    Authorization: `Splunk ${process.env.SPLUNK_HEC_TOKEN}`
  }
});

app.get("/", (req, res) => {
  res.send("OncoConnect Backend Running");
});

app.post("/test-splunk", async (req, res) => {
  try {
    const payload = {
      sourcetype: "oncoconnect:test",
      index: process.env.SPLUNK_INDEX || "main",
      event: {
        app: "OncoConnect AI",
        message: "First event from OncoConnect",
        timestamp: new Date().toISOString()
      }
    };

    const response = await splunkClient.post(
      process.env.SPLUNK_HEC_URL,
      payload
    );

    res.json({
      success: true,
      splunk: response.data
    });
  } catch (error) {
    console.log(error.response?.data || error.message);

    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

app.post("/checkin", async (req, res) => {
  try {
    const data = req.body;

    const fatigue = Number(data.fatigue || 0);
    const nausea = Number(data.nausea || 0);
    const pain = Number(data.pain || 0);
    const mood = Number(data.mood || 0);

    const risk_score = fatigue + nausea + pain + (10 - mood);

    const payload = {
      sourcetype: "oncoconnect:symptom",
      source: "oncoconnect-patient-app",
      index: process.env.SPLUNK_INDEX || "main",
      event: {
        app: "OncoConnect AI",
        event_type: "patient_symptom_checkin",

        patientId: data.patientId || "unknown",
        cancerType: data.cancerType || "not_specified",
        treatmentStage: data.treatmentStage || "not_specified",
        city: data.city || "not_specified",

        fatigue,
        nausea,
        pain,
        mood,
        risk_score,

        note: data.note || "",
        created_at: new Date().toISOString(),

        safety_note:
          "This event is for support and monitoring only. It does not provide diagnosis or treatment advice."
      }
    };

    const response = await splunkClient.post(
      process.env.SPLUNK_HEC_URL,
      payload
    );

    res.json({
      success: true,
      message: "Patient check-in sent to Splunk",
      risk_score,
      splunk: response.data
    });
  } catch (error) {
    console.log(error.response?.data || error.message);

    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

app.listen(5050, () => {
  console.log("Server running on port 5050");
});
""", encoding="utf-8")

print("✅ /checkin endpoint added successfully.")
