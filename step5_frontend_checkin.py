from pathlib import Path

Path("frontend/src/App.jsx").write_text("""
import { useState } from "react";
import "./App.css";

function App() {
  const [form, setForm] = useState({
    patientId: "P001",
    cancerType: "Breast Cancer",
    treatmentStage: "Chemotherapy",
    city: "Izmir",
    fatigue: 8,
    nausea: 7,
    pain: 3,
    mood: 2,
    note: "Kemoterapi sonrası halsizlik ve bulantı arttı."
  });

  const [message, setMessage] = useState("");
  const [riskScore, setRiskScore] = useState(null);

  const update = (key, value) => {
    setForm({ ...form, [key]: value });
  };

  const submit = async () => {
    setMessage("Splunk'a gönderiliyor...");
    setRiskScore(null);

    try {
      const res = await fetch("http://localhost:5050/checkin", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(form)
      });

      const data = await res.json();

      if (data.success) {
        setRiskScore(data.risk_score);
        setMessage("Kayıt başarıyla Splunk'a gönderildi.");
      } else {
        setMessage("Gönderim başarısız oldu.");
      }
    } catch (error) {
      setMessage("Backend bağlantısı yok. Backend açık mı kontrol edin.");
    }
  };

  return (
    <div className="page">
      <section className="hero">
        <div className="hero-content">
          <p className="eyebrow">ONCOCONNECT AI</p>

          <h1>
            Kanser Hastaları ve Hasta Yakınları İçin
            <br />
            Akıllı Destek Platformu
          </h1>

          <p className="subtitle">
            Hasta semptom verilerini Splunk ile izleyin, risk skorlarını
            analiz edin ve doktor görüşmelerine hazırlık sağlayın.
          </p>

          <div className="status-pills">
            <span>React Frontend</span>
            <span>Node Backend</span>
            <span>Splunk HEC</span>
            <span>Risk Analytics</span>
          </div>
        </div>
      </section>

      <section className="form-section">
        <div className="form-card">
          <div className="section-label">Patient Check-In</div>
          <h2>Günlük Semptom Girişi</h2>
          <p className="muted">
            Bu formdan girilen veri backend üzerinden Splunk HEC'e gönderilir.
          </p>

          <div className="two-col">
            <input
              placeholder="Hasta ID"
              value={form.patientId}
              onChange={(e) => update("patientId", e.target.value)}
            />

            <input
              placeholder="Şehir"
              value={form.city}
              onChange={(e) => update("city", e.target.value)}
            />

            <input
              placeholder="Kanser Türü"
              value={form.cancerType}
              onChange={(e) => update("cancerType", e.target.value)}
            />

            <input
              placeholder="Tedavi Aşaması"
              value={form.treatmentStage}
              onChange={(e) => update("treatmentStage", e.target.value)}
            />
          </div>

          <div className="slider-grid">
            <div>
              <label>Halsizlik: {form.fatigue}</label>
              <input
                type="range"
                min="0"
                max="10"
                value={form.fatigue}
                onChange={(e) => update("fatigue", e.target.value)}
              />
            </div>

            <div>
              <label>Bulantı: {form.nausea}</label>
              <input
                type="range"
                min="0"
                max="10"
                value={form.nausea}
                onChange={(e) => update("nausea", e.target.value)}
              />
            </div>

            <div>
              <label>Ağrı: {form.pain}</label>
              <input
                type="range"
                min="0"
                max="10"
                value={form.pain}
                onChange={(e) => update("pain", e.target.value)}
              />
            </div>

            <div>
              <label>Moral: {form.mood}</label>
              <input
                type="range"
                min="0"
                max="10"
                value={form.mood}
                onChange={(e) => update("mood", e.target.value)}
              />
            </div>
          </div>

          <textarea
            placeholder="Bugün nasıl hissediyorsunuz?"
            value={form.note}
            onChange={(e) => update("note", e.target.value)}
          />

          <button onClick={submit}>Splunk'a Gönder</button>

          <div className="result-box">
            <p>{message}</p>
            {riskScore !== null && (
              <h3>Risk Skoru: {riskScore}</h3>
            )}
          </div>
        </div>

        <div className="form-card side-card">
          <div className="section-label">AI Safety Layer</div>
          <h2>Güvenli Kullanım Notu</h2>
          <p>
            OncoConnect AI tıbbi tanı, tedavi veya ilaç önerisi sunmaz. Bu
            platform yalnızca semptom takibi, destek koordinasyonu, doktor
            görüşmesine hazırlık ve operasyonel izleme amacıyla tasarlanmıştır.
          </p>

          <div className="mini-panel">
            <strong>Splunk sourcetype</strong>
            <span>oncoconnect:symptom</span>
          </div>

          <div className="mini-panel">
            <strong>Risk formülü</strong>
            <span>fatigue + nausea + pain + (10 - mood)</span>
          </div>
        </div>
      </section>
    </div>
  );
}

export default App;
""", encoding="utf-8")

Path("frontend/src/App.css").write_text("""
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  background: #f5f7fb;
  color: #0f172a;
}

.page {
  min-height: 100vh;
}

.hero {
  min-height: 88vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0f172a, #1e3a8a, #7c3aed);
  color: white;
}

.hero-content {
  max-width: 1050px;
  text-align: center;
  padding: 40px;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 4px;
  opacity: 0.8;
  font-weight: 700;
}

h1 {
  font-size: 56px;
  line-height: 1.1;
  margin: 16px 0 24px;
  color: white;
}

.subtitle {
  max-width: 900px;
  margin: 0 auto;
  font-size: 22px;
  line-height: 1.7;
  color: rgba(255,255,255,0.9);
}

.status-pills {
  margin-top: 34px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
}

.status-pills span {
  padding: 10px 14px;
  border-radius: 999px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.2);
}

.form-section {
  display: grid;
  grid-template-columns: 1.7fr 1fr;
  gap: 24px;
  padding: 34px;
  max-width: 1250px;
  margin: -80px auto 60px;
  position: relative;
  z-index: 2;
}

.form-card {
  background: white;
  border-radius: 24px;
  padding: 28px;
  box-shadow: 0 24px 70px rgba(15, 23, 42, 0.16);
}

.section-label {
  color: #7c3aed;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 800;
  font-size: 13px;
}

.form-card h2 {
  margin: 8px 0 10px;
  font-size: 28px;
}

.muted {
  color: #64748b;
}

.two-col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
  margin-top: 20px;
}

input,
textarea {
  width: 100%;
  border: 1px solid #cbd5e1;
  border-radius: 14px;
  padding: 13px;
  font-size: 15px;
}

.slider-grid {
  margin-top: 24px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

label {
  font-weight: 700;
  display: block;
  margin-bottom: 8px;
}

textarea {
  min-height: 110px;
  margin-top: 22px;
}

button {
  margin-top: 18px;
  background: #1e3a8a;
  color: white;
  border: none;
  border-radius: 14px;
  padding: 14px 22px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background: #172554;
}

.result-box {
  margin-top: 18px;
  background: #f8fafc;
  border-radius: 16px;
  padding: 16px;
}

.result-box h3 {
  margin: 8px 0 0;
  color: #7c3aed;
}

.side-card {
  height: fit-content;
}

.side-card p {
  line-height: 1.7;
  color: #334155;
}

.mini-panel {
  margin-top: 18px;
  background: #f8fafc;
  border-radius: 16px;
  padding: 16px;
}

.mini-panel strong,
.mini-panel span {
  display: block;
}

.mini-panel span {
  color: #475569;
  margin-top: 6px;
}

@media (max-width: 900px) {
  h1 {
    font-size: 38px;
  }

  .form-section {
    grid-template-columns: 1fr;
    margin-top: -40px;
    padding: 18px;
  }

  .two-col,
  .slider-grid {
    grid-template-columns: 1fr;
  }
}
""", encoding="utf-8")

print("✅ Frontend connected to /checkin endpoint.")
