from pathlib import Path

app = r'''
import { useState } from "react";
import "./App.css";

const API_URL = "http://localhost:5050";

function App() {
  const [form, setForm] = useState({
    patientId: "P999",
    cancerType: "Breast Cancer",
    treatmentStage: "Chemotherapy",
    city: "Istanbul",
    fatigue: 10,
    nausea: 9,
    pain: 9,
    mood: 1,
    note: "Critical symptom escalation detected during demo."
  });

  const [result, setResult] = useState(null);
  const [aiSummary, setAiSummary] = useState(null);
  const [loading, setLoading] = useState(false);

  const update = (key, value) => {
    setForm({ ...form, [key]: value });
  };

  const submitCheckin = async () => {
    setLoading(true);
    setResult(null);

    try {
      const res = await fetch(`${API_URL}/checkin`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      const data = await res.json();
      setResult(data);
    } catch (e) {
      setResult({ success: false, message: "Backend connection failed." });
    }

    setLoading(false);
  };

  const generateAISummary = async () => {
    setLoading(true);
    setAiSummary(null);

    try {
      const res = await fetch(`${API_URL}/ai-summary`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      const data = await res.json();
      setAiSummary(data.summary);
    } catch (e) {
      setAiSummary({ ai_summary: "AI summary endpoint failed." });
    }

    setLoading(false);
  };

  const riskLabel = (score) => {
    if (score >= 25) return "Critical";
    if (score >= 20) return "High";
    if (score >= 12) return "Medium";
    return "Low";
  };

  return (
    <div className="page">
      <section className="hero">
        <div className="hero-left">
          <p className="eyebrow">SPLUNK AI HACKATHON PROJECT</p>
          <h1>OncoConnect AI</h1>
          <p className="subtitle">
            Real-time oncology symptom monitoring, AI risk assessment, and
            Splunk-powered operational intelligence for patients, caregivers,
            and support organizations.
          </p>

          <div className="pipeline">
            <span>React Patient App</span>
            <b>→</b>
            <span>Node Risk API</span>
            <b>→</b>
            <span>AI Summary Agent</span>
            <b>→</b>
            <span>Splunk HEC</span>
            <b>→</b>
            <span>Command Center</span>
          </div>

          <div className="stats">
            <div>
              <strong>15K+</strong>
              <small>Splunk Events</small>
            </div>
            <div>
              <strong>10K</strong>
              <small>Chemotherapy Cases</small>
            </div>
            <div>
              <strong>5.2K</strong>
              <small>Monitoring Events</small>
            </div>
          </div>
        </div>

        <div className="hero-card">
          <h3>Live Demo Flow</h3>
          <ol>
            <li>Submit patient symptom check-in</li>
            <li>Backend calculates operational risk score</li>
            <li>AI agent generates patient summary</li>
            <li>Events stream into Splunk dashboards</li>
          </ol>
        </div>
      </section>

      <section className="workspace">
        <div className="panel form-panel">
          <div className="section-title">
            <span>Patient Check-In</span>
            <small>Live data sent to Splunk HEC</small>
          </div>

          <div className="grid">
            <input value={form.patientId} onChange={(e) => update("patientId", e.target.value)} placeholder="Patient ID" />
            <input value={form.city} onChange={(e) => update("city", e.target.value)} placeholder="City" />
            <input value={form.cancerType} onChange={(e) => update("cancerType", e.target.value)} placeholder="Cancer Type" />
            <input value={form.treatmentStage} onChange={(e) => update("treatmentStage", e.target.value)} placeholder="Treatment Stage" />
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
              Send Check-In to Splunk
            </button>
            <button className="secondary" onClick={generateAISummary} disabled={loading}>
              Generate AI Summary
            </button>
          </div>
        </div>

        <div className="panel output-panel">
          <div className="section-title">
            <span>Risk Intelligence</span>
            <small>Operational support signal, not medical advice</small>
          </div>

          {result?.success ? (
            <div className="risk-card">
              <p>Risk Score</p>
              <h2>{result.risk_score}</h2>
              <span className={`badge ${riskLabel(result.risk_score).toLowerCase()}`}>
                {riskLabel(result.risk_score)}
              </span>
              <small>Event sent to Splunk as oncoconnect:symptom</small>
            </div>
          ) : (
            <div className="empty">
              Submit a patient check-in to generate a risk score.
            </div>
          )}

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
          <h2>Why Splunk?</h2>
          <p>
            OncoConnect AI treats patient-reported symptoms as operational
            events. Splunk ingests these events in real time, enables risk
            analytics, highlights critical cases, and powers a command center
            for care coordination.
          </p>
        </div>

        <div className="cards">
          <div>Real-time HEC ingestion</div>
          <div>Risk score calculation</div>
          <div>AI summary events</div>
          <div>Dashboard monitoring</div>
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
  background: #f5f7fb;
  color: #111827;
}

.page {
  min-height: 100vh;
}

.hero {
  min-height: 88vh;
  display: grid;
  grid-template-columns: 1.4fr 0.8fr;
  align-items: center;
  gap: 36px;
  padding: 64px;
  color: white;
  background:
    radial-gradient(circle at top right, rgba(168, 85, 247, 0.55), transparent 35%),
    linear-gradient(135deg, #06182f, #1e3a8a 50%, #6d28d9);
}

.eyebrow {
  letter-spacing: 3px;
  font-size: 13px;
  font-weight: 800;
  opacity: 0.8;
}

h1 {
  font-size: 76px;
  margin: 14px 0;
  line-height: 0.95;
}

.subtitle {
  font-size: 22px;
  line-height: 1.6;
  max-width: 880px;
  color: rgba(255,255,255,0.9);
}

.pipeline {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-top: 30px;
}

.pipeline span {
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.25);
  padding: 10px 14px;
  border-radius: 999px;
  font-weight: 700;
}

.stats {
  display: flex;
  gap: 16px;
  margin-top: 34px;
}

.stats div,
.hero-card,
.panel {
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.18);
  backdrop-filter: blur(16px);
  border-radius: 24px;
}

.stats div {
  padding: 18px 22px;
}

.stats strong {
  display: block;
  font-size: 30px;
}

.stats small {
  opacity: 0.85;
}

.hero-card {
  padding: 28px;
}

.hero-card h3 {
  font-size: 28px;
  margin-top: 0;
}

.hero-card li {
  margin: 14px 0;
  line-height: 1.5;
}

.workspace {
  display: grid;
  grid-template-columns: 1.3fr 0.8fr;
  gap: 24px;
  max-width: 1260px;
  margin: -90px auto 40px;
  padding: 0 24px;
  position: relative;
  z-index: 2;
}

.panel {
  background: white;
  color: #111827;
  box-shadow: 0 30px 80px rgba(15, 23, 42, 0.16);
  border: 1px solid #e5e7eb;
  padding: 28px;
}

.section-title {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 20px;
}

.section-title span {
  font-weight: 900;
  font-size: 22px;
}

.section-title small {
  color: #64748b;
}

.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}

input,
textarea {
  width: 100%;
  border: 1px solid #cbd5e1;
  border-radius: 14px;
  padding: 13px;
  font-size: 15px;
}

.sliders {
  margin-top: 22px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.slider-row label {
  display: block;
  font-weight: 800;
  margin-bottom: 8px;
}

textarea {
  min-height: 110px;
  margin-top: 20px;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 18px;
}

button {
  border: none;
  background: #1d4ed8;
  color: white;
  padding: 14px 18px;
  border-radius: 14px;
  font-weight: 900;
  cursor: pointer;
}

button.secondary {
  background: #7c3aed;
}

button:disabled {
  opacity: 0.6;
}

.risk-card {
  border-radius: 22px;
  padding: 24px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
}

.risk-card p {
  color: #64748b;
  margin: 0;
}

.risk-card h2 {
  font-size: 82px;
  margin: 6px 0;
}

.badge {
  display: inline-block;
  padding: 8px 14px;
  border-radius: 999px;
  color: white;
  font-weight: 900;
}

.badge.critical {
  background: #dc2626;
}

.badge.high {
  background: #ea580c;
}

.badge.medium {
  background: #ca8a04;
}

.badge.low {
  background: #16a34a;
}

.ai-card {
  margin-top: 18px;
  padding: 20px;
  border-radius: 20px;
  background: #eef2ff;
  border: 1px solid #c7d2fe;
  line-height: 1.6;
}

.empty {
  color: #64748b;
  padding: 24px;
  border-radius: 20px;
  background: #f8fafc;
}

.explain {
  max-width: 1260px;
  margin: 0 auto 70px;
  padding: 24px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
}

.explain h2 {
  font-size: 38px;
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
  padding: 22px;
  font-weight: 900;
  box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
}

@media (max-width: 900px) {
  .hero,
  .workspace,
  .explain {
    grid-template-columns: 1fr;
  }

  .hero {
    padding: 34px;
  }

  h1 {
    font-size: 48px;
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

print("✅ Frontend polished for OncoConnect AI demo.")
