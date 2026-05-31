from pathlib import Path

app = r'''
import { useState } from "react";
import "./App.css";

const API_URL = "http://localhost:5050";

const patientPresets = {
  P999: {
    patientId: "P999",
    label: "Critical Demo Patient",
    cancerType: "Breast Cancer",
    treatmentStage: "Chemotherapy",
    city: "Istanbul",
    fatigue: 10,
    nausea: 9,
    pain: 9,
    mood: 1,
    note: "Critical symptom escalation detected during demo."
  },
  P001: {
    patientId: "P001",
    label: "High fatigue after chemotherapy",
    cancerType: "Breast Cancer",
    treatmentStage: "Chemotherapy",
    city: "Izmir",
    fatigue: 8,
    nausea: 7,
    pain: 3,
    mood: 2,
    note: "Kemoterapi sonrası halsizlik ve bulantı arttı."
  },
  P002: {
    patientId: "P002",
    label: "Radiotherapy follow-up",
    cancerType: "Lung Cancer",
    treatmentStage: "Radiotherapy",
    city: "Ankara",
    fatigue: 6,
    nausea: 4,
    pain: 5,
    mood: 5,
    note: "Fatigue continues after radiotherapy."
  },
  P012: {
    patientId: "P012",
    label: "Stable follow-up",
    cancerType: "Colon Cancer",
    treatmentStage: "Follow-up",
    city: "Izmir",
    fatigue: 4,
    nausea: 3,
    pain: 2,
    mood: 7,
    note: "Stable follow-up condition."
  },
  P013: {
    patientId: "P013",
    label: "Improving condition",
    cancerType: "Lymphoma",
    treatmentStage: "Immunotherapy",
    city: "Bursa",
    fatigue: 5,
    nausea: 3,
    pain: 2,
    mood: 6,
    note: "Feeling better today."
  }
};

function App() {
  const [form, setForm] = useState(patientPresets.P999);
  const [result, setResult] = useState(null);
  const [aiSummary, setAiSummary] = useState(null);
  const [loading, setLoading] = useState(false);
  const [timeline, setTimeline] = useState([
    "Ready: select a patient scenario or adjust symptoms."
  ]);

  const update = (key, value) => {
    setForm({ ...form, [key]: value });
    setResult(null);
    setAiSummary(null);
  };

  const selectPatient = (patientId) => {
    setForm(patientPresets[patientId]);
    setResult(null);
    setAiSummary(null);
    setTimeline([
      `Scenario loaded: ${patientId} — ${patientPresets[patientId].label}`,
      "Next step: send check-in to Splunk."
    ]);
  };

  const riskScore = () => {
    return Number(form.fatigue) + Number(form.nausea) + Number(form.pain) + (10 - Number(form.mood));
  };

  const riskLabel = (score) => {
    if (score >= 25) return "Critical";
    if (score >= 20) return "High";
    if (score >= 12) return "Medium";
    return "Low";
  };

  const submitCheckin = async () => {
    setLoading(true);
    setResult(null);
    setTimeline([
      "Step 1: collecting patient-reported symptoms...",
      "Step 2: backend calculates operational risk score...",
      "Step 3: event is sent to Splunk HEC as oncoconnect:symptom..."
    ]);

    try {
      const res = await fetch(`${API_URL}/checkin`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      const data = await res.json();
      setResult(data);

      if (data.success) {
        setTimeline([
          "Check-in received by Node backend.",
          `Risk score calculated: ${data.risk_score} (${riskLabel(data.risk_score)}).`,
          "Splunk HEC accepted the event successfully.",
          "Refresh the Splunk dashboard to see the live update."
        ]);
      } else {
        setTimeline(["Backend responded, but check-in failed."]);
      }
    } catch (e) {
      setResult({ success: false, message: "Backend connection failed." });
      setTimeline(["Backend connection failed. Make sure node server.js is running."]);
    }

    setLoading(false);
  };

  const generateAISummary = async () => {
    setLoading(true);
    setAiSummary(null);
    setTimeline([
      "AI agent is reading symptom severity...",
      "AI agent is classifying operational risk...",
      "AI summary event is being streamed into Splunk..."
    ]);

    try {
      const res = await fetch(`${API_URL}/ai-summary`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      const data = await res.json();
      setAiSummary(data.summary);

      if (data.success) {
        setTimeline([
          `AI Summary created for ${data.summary.patientId}.`,
          `Risk level: ${data.summary.riskLevel}.`,
          "Recommended action generated.",
          "AI event sent to Splunk as oncoconnect:ai_summary."
        ]);
      }
    } catch (e) {
      setAiSummary({ ai_summary: "AI summary endpoint failed." });
      setTimeline(["AI summary endpoint failed. Check backend server."]);
    }

    setLoading(false);
  };

  const currentScore = result?.risk_score ?? riskScore();
  const currentLabel = riskLabel(currentScore);

  return (
    <div className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">SPLUNK AI HACKATHON PROJECT</p>
          <h1>OncoConnect AI</h1>
          <p className="subtitle">
            AI-powered oncology support console that converts patient-reported
            symptoms into Splunk operational events, risk scores, AI summaries,
            and dashboard intelligence.
          </p>

          <div className="pipeline">
            <span>Patient Check-In</span>
            <b>→</b>
            <span>Risk API</span>
            <b>→</b>
            <span>AI Summary Agent</span>
            <b>→</b>
            <span>Splunk HEC</span>
            <b>→</b>
            <span>Command Center</span>
          </div>
        </div>

        <div className="hero-card">
          <h3>What this console does</h3>
          <p>
            This screen is not a full patient database browser. It is a live
            demo console for creating new patient check-in events and AI
            summaries. Population-scale analytics are shown in Splunk dashboards.
          </p>
        </div>
      </section>

      <section className="metrics">
        <div>
          <strong>15K+</strong>
          <span>Splunk Events</span>
        </div>
        <div>
          <strong>10K</strong>
          <span>Chemotherapy Cases</span>
        </div>
        <div>
          <strong>5.2K</strong>
          <span>Monitoring Events</span>
        </div>
        <div>
          <strong>Live</strong>
          <span>HEC Ingestion</span>
        </div>
      </section>

      <section className="workspace">
        <div className="panel form-panel">
          <div className="section-title">
            <div>
              <span>1. Select Patient Scenario</span>
              <small>Choose a demo case, then adjust symptoms if needed.</small>
            </div>
          </div>

          <select
            className="wide-select"
            value={form.patientId}
            onChange={(e) => selectPatient(e.target.value)}
          >
            {Object.values(patientPresets).map((p) => (
              <option key={p.patientId} value={p.patientId}>
                {p.patientId} — {p.label} / {p.city}
              </option>
            ))}
          </select>

          <div className="grid">
            <select value={form.cancerType} onChange={(e) => update("cancerType", e.target.value)}>
              <option>Breast Cancer</option>
              <option>Lung Cancer</option>
              <option>Colon Cancer</option>
              <option>Lymphoma</option>
              <option>Leukemia</option>
            </select>

            <select value={form.city} onChange={(e) => update("city", e.target.value)}>
              <option>Istanbul</option>
              <option>Izmir</option>
              <option>Ankara</option>
              <option>Bursa</option>
            </select>

            <select value={form.treatmentStage} onChange={(e) => update("treatmentStage", e.target.value)}>
              <option>Chemotherapy</option>
              <option>Radiotherapy</option>
              <option>Immunotherapy</option>
              <option>Follow-up</option>
              <option>Post-surgery follow-up</option>
            </select>

            <div className={`risk-preview ${currentLabel.toLowerCase()}`}>
              <small>Predicted Risk</small>
              <b>{currentScore}</b>
              <span>{currentLabel}</span>
            </div>
          </div>

          <div className="section-title compact">
            <div>
              <span>2. Adjust Symptoms</span>
              <small>Risk = fatigue + nausea + pain + (10 - mood)</small>
            </div>
          </div>

          <div className="sliders">
            {[
              ["fatigue", "Fatigue"],
              ["nausea", "Nausea"],
              ["pain", "Pain"],
              ["mood", "Mood"]
            ].map(([key, label]) => (
              <div key={key} className="slider-row">
                <label>{label}: <b>{form[key]}</b></label>
                <input
                  type="range"
                  min="0"
                  max="10"
                  value={form[key]}
                  onChange={(e) => update(key, Number(e.target.value))}
                />
              </div>
            ))}
          </div>

          <textarea
            value={form.note}
            onChange={(e) => update("note", e.target.value)}
            placeholder="Patient note"
          />

          <div className="actions">
            <button onClick={submitCheckin} disabled={loading}>
              3. Send Check-In to Splunk
            </button>
            <button className="secondary" onClick={generateAISummary} disabled={loading}>
              4. Generate AI Summary
            </button>
          </div>
        </div>

        <div className="panel output-panel">
          <div className="section-title">
            <div>
              <span>AI Copilot</span>
              <small>Explains what happened after each action.</small>
            </div>
          </div>

          <div className={`risk-card ${currentLabel.toLowerCase()}`}>
            <p>Current Risk Score</p>
            <h2>{currentScore}</h2>
            <span>{currentLabel}</span>
          </div>

          <div className="timeline">
            {timeline.map((item, idx) => (
              <div key={idx} className="timeline-item">
                <b>{idx + 1}</b>
                <p>{item}</p>
              </div>
            ))}
          </div>

          {aiSummary && (
            <div className="ai-card">
              <h3>AI Patient Summary</h3>
              <p>{aiSummary.ai_summary}</p>
              <strong>Recommended action</strong>
              <p>{aiSummary.recommended_action}</p>
              <small>{aiSummary.safety_note}</small>
            </div>
          )}
        </div>
      </section>

      <section className="explain">
        <div>
          <h2>How to demo it</h2>
          <p>
            Select a patient scenario, send the check-in, generate the AI
            summary, then refresh the Splunk Command Center and AI Insights
            dashboards. The new events appear in real time.
          </p>
        </div>

        <div className="cards">
          <div>
            <strong>Live event</strong>
            <span>oncoconnect:symptom</span>
          </div>
          <div>
            <strong>AI event</strong>
            <span>oncoconnect:ai_summary</span>
          </div>
          <div>
            <strong>Population data</strong>
            <span>15K+ historical records</span>
          </div>
          <div>
            <strong>Splunk layer</strong>
            <span>Dashboards + risk analytics</span>
          </div>
        </div>
      </section>
    </div>
  );
}

export default App;
'''

css = r'''
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  background: #f4f7fb;
  color: #111827;
}

.page {
  min-height: 100vh;
}

.hero {
  min-height: 48vh;
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  align-items: center;
  gap: 34px;
  padding: 40px 56px 100px;
  color: white;
  background:
    radial-gradient(circle at top right, rgba(168, 85, 247, 0.55), transparent 35%),
    linear-gradient(135deg, #06182f, #1e3a8a 52%, #6d28d9);
}

.eyebrow {
  letter-spacing: 3px;
  font-size: 12px;
  font-weight: 900;
  opacity: 0.85;
}

h1 {
  font-size: 58px;
  margin: 10px 0;
  line-height: 1;
}

.subtitle {
  font-size: 18px;
  line-height: 1.55;
  max-width: 900px;
  color: rgba(255,255,255,0.92);
}

.pipeline {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-top: 24px;
}

.pipeline span {
  background: rgba(255,255,255,0.13);
  border: 1px solid rgba(255,255,255,0.24);
  padding: 9px 13px;
  border-radius: 999px;
  font-weight: 800;
  font-size: 14px;
}

.hero-card {
  padding: 22px;
  border-radius: 24px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.18);
  backdrop-filter: blur(14px);
}

.hero-card h3 {
  margin-top: 0;
  font-size: 28px;
}

.hero-card p {
  line-height: 1.65;
  color: rgba(255,255,255,0.9);
}

.metrics {
  max-width: 1180px;
  margin: -70px auto 24px;
  padding: 0 24px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  position: relative;
  z-index: 2;
}

.metrics div {
  background: white;
  border-radius: 20px;
  padding: 18px 20px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 18px 50px rgba(15, 23, 42, 0.12);
}

.metrics strong {
  display: block;
  font-size: 28px;
}

.metrics span {
  color: #64748b;
  font-weight: 700;
}

.workspace {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 24px;
  max-width: 1180px;
  margin: 0 auto 38px;
  padding: 0 24px;
}

.panel {
  background: white;
  border-radius: 26px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 28px 70px rgba(15, 23, 42, 0.14);
  padding: 24px;
}

.section-title {
  display: flex;
  justify-content: space-between;
  margin-bottom: 16px;
}

.section-title.compact {
  margin-top: 20px;
}

.section-title span {
  display: block;
  font-weight: 950;
  font-size: 22px;
}

.section-title small {
  color: #64748b;
}

.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-top: 12px;
}

input,
select,
textarea {
  width: 100%;
  border: 1px solid #cbd5e1;
  border-radius: 14px;
  padding: 13px;
  font-size: 15px;
  background: white;
}

select {
  cursor: pointer;
}

.wide-select {
  font-weight: 800;
}

.risk-preview {
  border-radius: 16px;
  padding: 12px 14px;
  color: white;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
}

.risk-preview small {
  opacity: 0.9;
}

.risk-preview b {
  font-size: 32px;
}

.risk-preview span {
  grid-column: 1 / 3;
  font-weight: 900;
}

.risk-preview.critical,
.risk-card.critical {
  background: #dc2626;
}

.risk-preview.high,
.risk-card.high {
  background: #ea580c;
}

.risk-preview.medium,
.risk-card.medium {
  background: #ca8a04;
}

.risk-preview.low,
.risk-card.low {
  background: #16a34a;
}

.sliders {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.slider-row label {
  display: block;
  font-weight: 850;
  margin-bottom: 8px;
}

textarea {
  min-height: 95px;
  margin-top: 18px;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 16px;
}

button {
  border: none;
  background: #1d4ed8;
  color: white;
  padding: 14px 17px;
  border-radius: 14px;
  font-weight: 950;
  cursor: pointer;
}

button.secondary {
  background: #7c3aed;
}

button:disabled {
  opacity: 0.55;
}

.risk-card {
  color: white;
  border-radius: 22px;
  padding: 22px;
}

.risk-card p {
  margin: 0;
  opacity: 0.9;
}

.risk-card h2 {
  font-size: 74px;
  margin: 4px 0;
}

.risk-card span {
  font-size: 20px;
  font-weight: 950;
}

.timeline {
  margin-top: 18px;
}

.timeline-item {
  display: grid;
  grid-template-columns: 34px 1fr;
  gap: 10px;
  padding: 10px 0;
  border-bottom: 1px solid #e5e7eb;
}

.timeline-item b {
  width: 28px;
  height: 28px;
  border-radius: 999px;
  background: #eef2ff;
  color: #3730a3;
  display: grid;
  place-items: center;
}

.timeline-item p {
  margin: 3px 0 0;
  color: #334155;
  line-height: 1.45;
}

.ai-card {
  margin-top: 18px;
  padding: 18px;
  border-radius: 20px;
  background: #eef2ff;
  border: 1px solid #c7d2fe;
  line-height: 1.6;
}

.explain {
  max-width: 1180px;
  margin: 0 auto 70px;
  padding: 0 24px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.explain h2 {
  font-size: 34px;
  margin-bottom: 8px;
}

.explain p {
  line-height: 1.7;
  color: #475569;
}

.cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}

.cards div {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 12px 34px rgba(15, 23, 42, 0.08);
}

.cards strong,
.cards span {
  display: block;
}

.cards span {
  color: #64748b;
  margin-top: 4px;
}

@media (max-width: 900px) {
  .hero,
  .workspace,
  .explain,
  .metrics {
    grid-template-columns: 1fr;
  }

  .hero {
    padding: 32px 24px 90px;
  }

  h1 {
    font-size: 44px;
  }

  .grid,
  .sliders,
  .cards {
    grid-template-columns: 1fr;
  }
}
'''

Path("frontend/src/App.jsx").write_text(app, encoding="utf-8")
Path("frontend/src/App.css").write_text(css, encoding="utf-8")

print("✅ AI Copilot frontend applied.")
