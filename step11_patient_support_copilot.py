from pathlib import Path

app = r'''
import { useMemo, useState } from "react";
import "./App.css";

const API_URL = "http://localhost:5050";

const patientPresets = {
  P999: {
    patientId: "P999",
    label: "Critical symptom escalation",
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

const roles = {
  patient: {
    title: "I am a patient",
    description: "I want to understand my symptoms and prepare for my doctor visit."
  },
  caregiver: {
    title: "I am a caregiver",
    description: "I want to understand whether my loved one may need extra support."
  },
  support: {
    title: "I am a support organization",
    description: "I want to prioritize high-risk patients for outreach."
  }
};

const goals = {
  symptoms: "Understand today’s symptoms",
  doctor: "Prepare questions for doctor visit",
  support: "Check whether extra support is needed"
};

function App() {
  const [role, setRole] = useState("patient");
  const [goal, setGoal] = useState("doctor");
  const [form, setForm] = useState(patientPresets.P999);
  const [result, setResult] = useState(null);
  const [aiSummary, setAiSummary] = useState(null);
  const [splunkStatus, setSplunkStatus] = useState("No event sent yet.");
  const [loading, setLoading] = useState(false);

  const riskScore = useMemo(() => {
    return Number(form.fatigue) + Number(form.nausea) + Number(form.pain) + (10 - Number(form.mood));
  }, [form]);

  const riskLevel = useMemo(() => {
    if (riskScore >= 25) return "Critical";
    if (riskScore >= 20) return "High";
    if (riskScore >= 12) return "Medium";
    return "Low";
  }, [riskScore]);

  const riskClass = riskLevel.toLowerCase();

  const update = (key, value) => {
    setForm({ ...form, [key]: value });
    setResult(null);
    setAiSummary(null);
    setSplunkStatus("Changes not sent yet.");
  };

  const selectPatient = (patientId) => {
    setForm(patientPresets[patientId]);
    setResult(null);
    setAiSummary(null);
    setSplunkStatus("Scenario loaded. Send check-in to Splunk when ready.");
  };

  const buildDoctorQuestions = () => {
    const questions = [];

    if (form.fatigue >= 7) {
      questions.push("My fatigue is high. Is this expected at this stage of treatment?");
    }

    if (form.nausea >= 7) {
      questions.push("My nausea has increased. What should I monitor or report before the next appointment?");
    }

    if (form.pain >= 7) {
      questions.push("My pain level is elevated. When should I contact the care team urgently?");
    }

    if (form.mood <= 3) {
      questions.push("My mood score is low. What support options are available for emotional wellbeing?");
    }

    if (questions.length === 0) {
      questions.push("Are my current symptoms consistent with my treatment stage?");
      questions.push("What signs should I monitor before my next appointment?");
    }

    questions.push("Which symptoms should trigger immediate contact with the care team?");

    return questions;
  };

  const buildUserExplanation = () => {
    if (riskLevel === "Critical") {
      return "Your symptom burden appears significantly elevated based on the values entered. This should be prioritized for care team review or support outreach.";
    }

    if (riskLevel === "High") {
      return "Your symptoms suggest a high support need. It may be useful to contact your care team or support organization for follow-up.";
    }

    if (riskLevel === "Medium") {
      return "Your symptoms show a moderate support need. Continue tracking changes and prepare key questions for your next appointment.";
    }

    return "Your symptoms appear lower risk based on this support model. Continue routine tracking and raise any changes with your care team.";
  };

  const buildRecommendedAction = () => {
    if (role === "support") {
      if (riskLevel === "Critical" || riskLevel === "High") {
        return "Prioritize this patient in the outreach queue and review recent symptom escalation.";
      }
      return "Keep this patient in routine monitoring.";
    }

    if (role === "caregiver") {
      if (riskLevel === "Critical" || riskLevel === "High") {
        return "Encourage the patient to contact their care team or support organization and help document symptoms.";
      }
      return "Continue observing symptoms and help the patient prepare questions for the next visit.";
    }

    if (riskLevel === "Critical" || riskLevel === "High") {
      return "Consider contacting your care team or patient support organization for follow-up.";
    }

    return "Continue routine symptom tracking and bring this summary to your next doctor visit.";
  };

  const guidance = {
    explanation: buildUserExplanation(),
    questions: buildDoctorQuestions(),
    action: buildRecommendedAction()
  };

  const sendCheckin = async () => {
    setLoading(true);
    setSplunkStatus("Sending symptom check-in to Splunk HEC...");

    try {
      const res = await fetch(`${API_URL}/checkin`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      const data = await res.json();
      setResult(data);

      if (data.success) {
        setSplunkStatus(`Success: symptom event sent to Splunk as oncoconnect:symptom. Risk score: ${data.risk_score}.`);
      } else {
        setSplunkStatus("Check-in failed.");
      }
    } catch (error) {
      setSplunkStatus("Backend connection failed. Start backend with: node server.js");
    }

    setLoading(false);
  };

  const generateAISummary = async () => {
    setLoading(true);
    setSplunkStatus("Generating AI support summary and sending it to Splunk...");

    try {
      const res = await fetch(`${API_URL}/ai-summary`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      const data = await res.json();
      setAiSummary(data.summary);

      if (data.success) {
        setSplunkStatus("Success: AI summary event sent to Splunk as oncoconnect:ai_summary.");
      } else {
        setSplunkStatus("AI summary failed.");
      }
    } catch (error) {
      setSplunkStatus("AI endpoint failed. Check backend server.");
    }

    setLoading(false);
  };

  return (
    <div className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">SPLUNK AI HACKATHON PROJECT</p>
          <h1>OncoConnect AI Copilot</h1>
          <p className="subtitle">
            A patient support copilot that helps cancer patients, caregivers,
            and support teams turn symptom updates into care-ready guidance and
            Splunk-powered operational intelligence.
          </p>

          <div className="hero-points">
            <span>Patient guidance</span>
            <span>Doctor visit preparation</span>
            <span>Risk prioritization</span>
            <span>Splunk monitoring</span>
          </div>
        </div>

        <div className="hero-card">
          <h3>What value does it provide?</h3>
          <p>
            A user can select their situation, enter symptoms, receive a clear
            explanation, get doctor-visit questions, and send the event to
            Splunk so support teams can monitor high-risk cases.
          </p>
        </div>
      </section>

      <section className="metrics">
        <div>
          <strong>15K+</strong>
          <span>Operational events in Splunk</span>
        </div>
        <div>
          <strong>10K</strong>
          <span>Chemotherapy records</span>
        </div>
        <div>
          <strong>5.2K</strong>
          <span>Monitoring follow-ups</span>
        </div>
        <div>
          <strong>Live</strong>
          <span>HEC event streaming</span>
        </div>
      </section>

      <main className="workspace">
        <section className="panel">
          <div className="step-header">
            <div className="step-number">1</div>
            <div>
              <h2>Who are you?</h2>
              <p>Select the user perspective for the guidance.</p>
            </div>
          </div>

          <div className="role-grid">
            {Object.entries(roles).map(([key, item]) => (
              <button
                key={key}
                className={`role-card ${role === key ? "active" : ""}`}
                onClick={() => setRole(key)}
              >
                <strong>{item.title}</strong>
                <span>{item.description}</span>
              </button>
            ))}
          </div>

          <div className="step-header compact">
            <div className="step-number">2</div>
            <div>
              <h2>What do you need help with?</h2>
              <p>The output adapts to your selected goal.</p>
            </div>
          </div>

          <div className="goal-grid">
            {Object.entries(goals).map(([key, label]) => (
              <button
                key={key}
                className={`goal-card ${goal === key ? "active" : ""}`}
                onClick={() => setGoal(key)}
              >
                {label}
              </button>
            ))}
          </div>

          <div className="step-header compact">
            <div className="step-number">3</div>
            <div>
              <h2>Select patient scenario</h2>
              <p>These are demo scenarios. The population-scale datasets are analyzed in Splunk dashboards.</p>
            </div>
          </div>

          <select
            className="wide-select"
            value={form.patientId}
            onChange={(e) => selectPatient(e.target.value)}
          >
            {Object.values(patientPresets).map((p) => (
              <option key={p.patientId} value={p.patientId}>
                {p.patientId} — {p.label} / {p.cancerType} / {p.city}
              </option>
            ))}
          </select>

          <div className="info-grid">
            <select value={form.cancerType} onChange={(e) => update("cancerType", e.target.value)}>
              <option>Breast Cancer</option>
              <option>Lung Cancer</option>
              <option>Colon Cancer</option>
              <option>Lymphoma</option>
              <option>Leukemia</option>
            </select>

            <select value={form.treatmentStage} onChange={(e) => update("treatmentStage", e.target.value)}>
              <option>Chemotherapy</option>
              <option>Radiotherapy</option>
              <option>Immunotherapy</option>
              <option>Follow-up</option>
              <option>Post-surgery follow-up</option>
            </select>

            <select value={form.city} onChange={(e) => update("city", e.target.value)}>
              <option>Istanbul</option>
              <option>Izmir</option>
              <option>Ankara</option>
              <option>Bursa</option>
            </select>

            <div className={`risk-pill ${riskClass}`}>
              <small>Predicted support risk</small>
              <strong>{riskScore}</strong>
              <span>{riskLevel}</span>
            </div>
          </div>

          <div className="step-header compact">
            <div className="step-number">4</div>
            <div>
              <h2>Enter symptoms</h2>
              <p>Risk model: fatigue + nausea + pain + (10 - mood)</p>
            </div>
          </div>

          <div className="sliders">
            {[
              ["fatigue", "Fatigue"],
              ["nausea", "Nausea"],
              ["pain", "Pain"],
              ["mood", "Mood"]
            ].map(([key, label]) => (
              <div className="slider-row" key={key}>
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
            placeholder="Describe what changed today..."
          />

          <div className="actions">
            <button onClick={sendCheckin} disabled={loading}>
              Send check-in to Splunk
            </button>
            <button className="secondary" onClick={generateAISummary} disabled={loading}>
              Generate AI care guidance
            </button>
          </div>
        </section>

        <section className="panel output-panel">
          <div className="copilot-header">
            <div>
              <p className="eyebrow dark">AI COPILOT RESULT</p>
              <h2>{roles[role].title}</h2>
              <p>{goals[goal]}</p>
            </div>
            <div className={`risk-score ${riskClass}`}>
              <strong>{riskScore}</strong>
              <span>{riskLevel}</span>
            </div>
          </div>

          <div className="answer-card">
            <h3>What this means</h3>
            <p>{guidance.explanation}</p>
          </div>

          <div className="answer-card">
            <h3>Questions to ask your doctor</h3>
            <ol>
              {guidance.questions.map((q, i) => (
                <li key={i}>{q}</li>
              ))}
            </ol>
          </div>

          <div className="answer-card highlight">
            <h3>Suggested next step</h3>
            <p>{guidance.action}</p>
          </div>

          {aiSummary && (
            <div className="answer-card ai">
              <h3>AI Summary Event</h3>
              <p>{aiSummary.ai_summary}</p>
              <strong>Recommended action</strong>
              <p>{aiSummary.recommended_action}</p>
            </div>
          )}

          <div className="splunk-status">
            <strong>Splunk pipeline status</strong>
            <p>{splunkStatus}</p>
          </div>

          <small className="safety">
            Safety note: This tool does not provide diagnosis, treatment, or
            medication advice. It supports symptom tracking, doctor-visit
            preparation, and care coordination.
          </small>
        </section>
      </main>

      <section className="explain">
        <div>
          <h2>Where the 15K+ records are used</h2>
          <p>
            The frontend creates live check-in and AI summary events. Splunk
            dashboards analyze both these live events and the imported historical
            chemotherapy and monitoring datasets.
          </p>
        </div>

        <div className="cards">
          <div>
            <strong>Frontend</strong>
            <span>Patient support experience</span>
          </div>
          <div>
            <strong>Backend</strong>
            <span>Risk score + AI summary event</span>
          </div>
          <div>
            <strong>Splunk</strong>
            <span>Monitoring, prioritization, dashboards</span>
          </div>
          <div>
            <strong>Support team</strong>
            <span>High-risk outreach queue</span>
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
  min-height: 46vh;
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  align-items: center;
  gap: 34px;
  padding: 40px 56px 105px;
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

.eyebrow.dark {
  color: #64748b;
}

h1 {
  font-size: 56px;
  margin: 10px 0;
  line-height: 1;
}

.subtitle {
  font-size: 18px;
  line-height: 1.55;
  max-width: 900px;
  color: rgba(255,255,255,0.92);
}

.hero-points {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 24px;
}

.hero-points span {
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
  margin: -72px auto 24px;
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
  grid-template-columns: 1.1fr 0.9fr;
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

.step-header {
  display: grid;
  grid-template-columns: 38px 1fr;
  gap: 12px;
  align-items: start;
  margin-bottom: 14px;
}

.step-header.compact {
  margin-top: 24px;
}

.step-number {
  width: 34px;
  height: 34px;
  border-radius: 999px;
  background: #1d4ed8;
  color: white;
  display: grid;
  place-items: center;
  font-weight: 950;
}

.step-header h2 {
  margin: 0;
  font-size: 22px;
}

.step-header p {
  margin: 4px 0 0;
  color: #64748b;
}

.role-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.role-card,
.goal-card {
  text-align: left;
  border: 1px solid #cbd5e1;
  border-radius: 16px;
  background: white;
  color: #111827;
  padding: 14px;
  cursor: pointer;
}

.role-card strong,
.role-card span {
  display: block;
}

.role-card span {
  margin-top: 6px;
  color: #64748b;
  font-size: 13px;
  line-height: 1.35;
}

.role-card.active,
.goal-card.active {
  border-color: #1d4ed8;
  background: #eef2ff;
  box-shadow: 0 0 0 2px rgba(29,78,216,0.12);
}

.goal-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.goal-card {
  font-weight: 850;
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
  margin-bottom: 12px;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.risk-pill {
  border-radius: 16px;
  padding: 12px 14px;
  color: white;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
}

.risk-pill small {
  opacity: 0.9;
}

.risk-pill strong {
  font-size: 32px;
}

.risk-pill span {
  grid-column: 1 / 3;
  font-weight: 900;
}

.critical {
  background: #dc2626;
}

.high {
  background: #ea580c;
}

.medium {
  background: #ca8a04;
}

.low {
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
  min-height: 94px;
  margin-top: 18px;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 16px;
}

button {
  font-family: inherit;
}

.actions button {
  border: none;
  background: #1d4ed8;
  color: white;
  padding: 14px 17px;
  border-radius: 14px;
  font-weight: 950;
  cursor: pointer;
}

.actions button.secondary {
  background: #7c3aed;
}

button:disabled {
  opacity: 0.55;
}

.output-panel {
  align-self: start;
}

.copilot-header {
  display: grid;
  grid-template-columns: 1fr 120px;
  gap: 16px;
  align-items: start;
  margin-bottom: 16px;
}

.copilot-header h2 {
  margin: 4px 0;
}

.copilot-header p {
  color: #64748b;
  margin: 0;
}

.risk-score {
  color: white;
  border-radius: 20px;
  padding: 16px;
  text-align: center;
}

.risk-score strong,
.risk-score span {
  display: block;
}

.risk-score strong {
  font-size: 42px;
}

.risk-score span {
  font-weight: 950;
}

.answer-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 16px;
  margin-top: 12px;
}

.answer-card h3 {
  margin: 0 0 8px;
}

.answer-card p,
.answer-card li {
  line-height: 1.55;
  color: #334155;
}

.answer-card.highlight {
  background: #ecfdf5;
  border-color: #bbf7d0;
}

.answer-card.ai {
  background: #eef2ff;
  border-color: #c7d2fe;
}

.splunk-status {
  margin-top: 12px;
  background: #111827;
  color: white;
  border-radius: 18px;
  padding: 16px;
}

.splunk-status p {
  margin-bottom: 0;
  color: #d1d5db;
}

.safety {
  display: block;
  margin-top: 12px;
  color: #64748b;
  line-height: 1.5;
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
  .metrics,
  .role-grid,
  .goal-grid {
    grid-template-columns: 1fr;
  }

  .hero {
    padding: 32px 24px 90px;
  }

  h1 {
    font-size: 44px;
  }

  .info-grid,
  .sliders,
  .cards {
    grid-template-columns: 1fr;
  }
}
'''

Path("frontend/src/App.jsx").write_text(app, encoding="utf-8")
Path("frontend/src/App.css").write_text(css, encoding="utf-8")

print("✅ Patient Support Copilot UX applied.")
