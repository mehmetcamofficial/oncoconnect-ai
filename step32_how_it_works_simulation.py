from pathlib import Path

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

title = "A safe path from information to action"

if "how-live-sim-v32" not in app:
    idx = app.find(title)
    if idx == -1:
        raise RuntimeError("How It Works title bulunamadı.")

    section_start = app.rfind("<section", 0, idx)
    if section_start == -1:
        raise RuntimeError("How It Works section başlangıcı bulunamadı.")

    # matching section close bul
    i = section_start
    depth = 0
    section_end = None

    while i < len(app):
        if app.startswith("<section", i):
            depth += 1
            i += 8
        elif app.startswith("</section>", i):
            depth -= 1
            i += len("</section>")
            if depth == 0:
                section_end = i - len("</section>")
                break
        else:
            i += 1

    if section_end is None:
        raise RuntimeError("How It Works section kapanışı bulunamadı.")

    sim = r'''
          <div className="how-live-sim-v32">
            <div className="sim-header-v32">
              <div>
                <small>LIVE FLOW SIMULATION</small>
                <h3>From symptom note to support action</h3>
              </div>
              <span className="sim-status-v32">AI Copilot running</span>
            </div>

            <div className="sim-flow-v32">
              <div className="sim-step-v32 active">
                <span>1</span>
                <strong>Role</strong>
                <p>Patient / caregiver</p>
              </div>

              <i></i>

              <div className="sim-step-v32">
                <span>2</span>
                <strong>Symptoms</strong>
                <p>Fatigue 10 · Pain 9</p>
              </div>

              <i></i>

              <div className="sim-step-v32 ai">
                <span>3</span>
                <strong>AI explains</strong>
                <p>Risk meaning + questions</p>
              </div>

              <i></i>

              <div className="sim-step-v32 splunk">
                <span>4</span>
                <strong>Splunk</strong>
                <p>Event monitored</p>
              </div>
            </div>

            <div className="sim-output-v32">
              <div>
                <small>Risk signal</small>
                <strong>37</strong>
                <span>Critical</span>
              </div>
              <p>
                “Prepare for a care-team conversation: list current symptoms,
                ask when to seek urgent support, and share this structured note.”
              </p>
            </div>

            <details className="sim-details-v32">
              <summary>What happens when the user clicks Generate AI Summary?</summary>
              <p>
                The platform turns symptom values into an operational risk signal,
                creates a plain-language explanation, and streams the event to Splunk
                for support-team monitoring.
              </p>
            </details>
          </div>
'''

    app = app[:section_end] + sim + app[section_end:]
    print("✅ How It Works simulation inserted.")
else:
    print("ℹ️ Simulation already exists.")

css += r'''

/* Step 32: How It Works interactive simulation */

.how-live-sim-v32 {
  margin: 34px auto 0;
  max-width: 1180px;
  padding: 24px;
  border-radius: 34px;
  background: rgba(255,255,255,0.92);
  border: 1px solid #dbeafe;
  box-shadow: 0 28px 90px rgba(37,99,235,0.14);
}

.sim-header-v32 {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  align-items: center;
  margin-bottom: 20px;
}

.sim-header-v32 small {
  color: #64748b;
  font-weight: 950;
  letter-spacing: .14em;
}

.sim-header-v32 h3 {
  margin: 4px 0 0;
  font-size: 30px;
  color: #0f172a;
}

.sim-status-v32 {
  border-radius: 999px;
  padding: 10px 14px;
  background: #ecfeff;
  color: #0f766e;
  font-weight: 950;
  box-shadow: 0 10px 26px rgba(15,118,110,.12);
}

.sim-flow-v32 {
  display: grid;
  grid-template-columns: 1fr 64px 1fr 64px 1fr 64px 1fr;
  align-items: center;
  gap: 10px;
}

.sim-step-v32 {
  min-height: 145px;
  padding: 20px;
  border-radius: 26px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  transition: transform .25s ease, box-shadow .25s ease;
}

.sim-step-v32:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 60px rgba(15,23,42,.12);
}

.sim-step-v32 span {
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: #2563eb;
  color: white;
  font-weight: 950;
  margin-bottom: 14px;
}

.sim-step-v32 strong {
  display: block;
  font-size: 20px;
  color: #0f172a;
}

.sim-step-v32 p {
  margin: 8px 0 0;
  color: #475569;
  font-weight: 750;
}

.sim-step-v32.ai span {
  background: #7c3aed;
}

.sim-step-v32.splunk span {
  background: #16a34a;
}

.sim-flow-v32 i {
  height: 6px;
  border-radius: 999px;
  background: linear-gradient(90deg, #2563eb, #14b8a6);
  position: relative;
  overflow: hidden;
}

.sim-flow-v32 i::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, white, transparent);
  animation: simMoveV32 2s linear infinite;
}

.sim-output-v32 {
  margin-top: 20px;
  display: grid;
  grid-template-columns: 180px 1fr;
  gap: 18px;
  align-items: stretch;
}

.sim-output-v32 div {
  border-radius: 26px;
  padding: 18px;
  background: #0f172a;
  color: white;
}

.sim-output-v32 small,
.sim-output-v32 strong,
.sim-output-v32 span {
  display: block;
}

.sim-output-v32 strong {
  font-size: 54px;
  line-height: 1;
  margin: 6px 0;
}

.sim-output-v32 span {
  color: #fecaca;
  font-weight: 950;
}

.sim-output-v32 p {
  margin: 0;
  border-radius: 26px;
  padding: 22px;
  background: #eff6ff;
  color: #1e3a8a;
  font-weight: 850;
  line-height: 1.55;
}

.sim-details-v32 {
  margin-top: 16px;
  border-radius: 22px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 16px 18px;
  color: #334155;
}

.sim-details-v32 summary {
  cursor: pointer;
  font-weight: 950;
  color: #0f172a;
}

@keyframes simMoveV32 {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}

@media (max-width: 900px) {
  .sim-flow-v32 {
    grid-template-columns: 1fr;
  }

  .sim-flow-v32 i {
    width: 6px;
    height: 34px;
    justify-self: center;
  }

  .sim-output-v32 {
    grid-template-columns: 1fr;
  }

  .sim-header-v32 {
    display: block;
  }

  .sim-status-v32 {
    display: inline-flex;
    margin-top: 12px;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Step 32 applied.")
