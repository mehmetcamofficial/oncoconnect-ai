from pathlib import Path

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")

lp_start = s.find("  const LandingPage")
if lp_start == -1:
    raise SystemExit("❌ LandingPage bulunamadı.")

next_const = s.find("\n  const ", lp_start + 10)
if next_const == -1:
    raise SystemExit("❌ LandingPage bitişi bulunamadı.")

landing = s[lp_start:next_const]

# Eski statik flow section'ı bul
needle = "From symptom note to support action"
hit = landing.find(needle)

if hit == -1:
    # Alternatif eski başlık
    hit = landing.find("LIVE FLOW SIMULATION")

if hit == -1:
    print("⚠️ Eski flow alanı bulunamadı. LandingDataDashboard önüne inline simulation eklenecek.")
    insert_marker = "<LandingDataDashboard />"
    if insert_marker not in landing:
        raise SystemExit("❌ LandingDataDashboard marker da bulunamadı.")
    replace_start = landing.find(insert_marker)
    replace_end = replace_start
else:
    replace_start = landing.rfind("<section", 0, hit)
    replace_end = landing.find("</section>", hit)

    if replace_start == -1 or replace_end == -1:
        raise SystemExit("❌ Eski flow section sınırları bulunamadı.")

    replace_end += len("</section>")

inline_sim = r'''
        <section className="inline-live-simulation">
          <div className="inline-sim-head">
            <div>
              <p>LIVE FLOW SIMULATION</p>
              <h2>AI support flow running in real time</h2>
              <span>
                A dynamic patient-support simulation showing symptom input, AI reasoning,
                doctor-ready guidance and Splunk-ready operational monitoring.
              </span>
            </div>

            <div className="inline-risk-chip">
              <small>Live risk signal</small>
              <strong>82</strong>
              <b>Critical</b>
            </div>
          </div>

          <div className="inline-sim-controls">
            <button className="active">Critical scenario</button>
            <button>Needs review</button>
            <button>Stable</button>
            <button className="dark">Auto-running</button>
          </div>

          <div className="inline-sim-canvas">
            <div className="inline-sim-grid"></div>
            <div className="inline-sim-stream">
              <i></i>
              <i></i>
              <i></i>
              <i></i>
            </div>

            <div className="inline-sim-steps">
              <article className="active">
                <b>01</b>
                <h3>Patient input</h3>
                <p>Fatigue 9 · Pain 8 · Mood 7</p>
                <span>Role and symptoms entered</span>
              </article>

              <article>
                <b>02</b>
                <h3>AI Copilot reasoning</h3>
                <p>Support priority calculated</p>
                <span>Risk score converted into action</span>
              </article>

              <article>
                <b>03</b>
                <h3>Doctor-ready note</h3>
                <p>Questions and next steps generated</p>
                <span>Care-team communication prepared</span>
              </article>

              <article>
                <b>04</b>
                <h3>Splunk event</h3>
                <p>Monitoring event streamed</p>
                <span>Operational signal created</span>
              </article>
            </div>

            <div className="inline-sim-output">
              <div>
                <span>AI current recommendation</span>
                <h3>Prepare for care-team conversation</h3>
                <p>
                  List current symptoms, ask when to seek urgent support,
                  and share this structured note with a clinician or caregiver.
                </p>
              </div>

              <pre>{`{
  source: "oncoconnect_ai",
  scenario: "critical",
  risk_score: 82,
  status: "Critical",
  action: "support_outreach"
}`}</pre>
            </div>
          </div>
        </section>
'''

if hit == -1:
    landing = landing[:replace_start] + inline_sim + "\n        " + landing[replace_start:]
else:
    landing = landing[:replace_start] + inline_sim + landing[replace_end:]

s = s[:lp_start] + landing + s[next_const:]
APP.write_text(s, encoding="utf-8")

css_patch = r'''

/* HARD INLINE LIVE SIMULATION */

.inline-live-simulation {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  padding: 84px 5vw !important;
  background:
    radial-gradient(circle at 10% 10%, rgba(34,211,238,0.16), transparent 28%),
    radial-gradient(circle at 90% 20%, rgba(124,58,237,0.12), transparent 32%),
    #f5f8fc !important;
  position: relative !important;
  z-index: 30 !important;
}

.inline-sim-head {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 220px;
  gap: 28px;
  align-items: end;
  margin-bottom: 24px;
}

.inline-sim-head p {
  margin: 0 0 12px;
  color: #155eef;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.24em;
}

.inline-sim-head h2 {
  margin: 0;
  max-width: 1100px;
  color: #101828;
  font-size: clamp(44px, 5vw, 78px);
  line-height: 1;
  letter-spacing: -0.06em;
}

.inline-sim-head span {
  display: block;
  max-width: 950px;
  margin-top: 18px;
  color: #475467;
  font-size: 20px;
  line-height: 1.65;
  font-weight: 750;
}

.inline-risk-chip {
  padding: 22px;
  border-radius: 28px;
  color: white;
  background: linear-gradient(135deg, #dc2626, #991b1b);
  box-shadow: 0 24px 70px rgba(220,38,38,0.18);
}

.inline-risk-chip small {
  display: block;
  color: rgba(255,255,255,0.78);
  font-weight: 950;
  letter-spacing: 0.12em;
}

.inline-risk-chip strong {
  display: block;
  margin: 12px 0 2px;
  font-size: 58px;
  line-height: 1;
}

.inline-sim-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 22px;
}

.inline-sim-controls button {
  border: 0;
  border-radius: 999px;
  padding: 14px 18px;
  background: white;
  color: #101828;
  font-weight: 950;
  cursor: pointer;
  box-shadow: 0 16px 42px rgba(15,23,42,0.08);
}

.inline-sim-controls button.active {
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
}

.inline-sim-controls button.dark {
  background: #101828;
  color: white;
}

.inline-sim-canvas {
  position: relative;
  overflow: hidden;
  border-radius: 36px;
  padding: 34px;
  background:
    radial-gradient(circle at 15% 20%, rgba(34,211,238,0.18), transparent 28%),
    linear-gradient(135deg, #0f172a 0%, #172554 58%, #0f172a 100%);
  border: 1px solid rgba(125,211,252,0.22);
  box-shadow: 0 30px 90px rgba(15,23,42,0.18);
}

.inline-sim-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.055) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.055) 1px, transparent 1px);
  background-size: 42px 42px;
  opacity: 0.55;
  animation: inlineGridMove 16s linear infinite;
}

@keyframes inlineGridMove {
  from { transform: translate3d(0,0,0); }
  to { transform: translate3d(42px,42px,0); }
}

.inline-sim-stream {
  position: absolute;
  left: 8%;
  right: 8%;
  top: 170px;
  height: 5px;
  border-radius: 999px;
  background: rgba(125,211,252,0.18);
  overflow: hidden;
  z-index: 1;
}

.inline-sim-stream i {
  position: absolute;
  top: 0;
  width: 20%;
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, transparent, #22d3ee, transparent);
  animation: inlinePacket 2.2s linear infinite;
}

.inline-sim-stream i:nth-child(2) { animation-delay: .55s; }
.inline-sim-stream i:nth-child(3) { animation-delay: 1.1s; }
.inline-sim-stream i:nth-child(4) { animation-delay: 1.65s; }

@keyframes inlinePacket {
  from { left: -20%; opacity: 0.2; }
  45% { opacity: 1; }
  to { left: 110%; opacity: 0.2; }
}

.inline-sim-steps {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.inline-sim-steps article {
  min-height: 210px;
  padding: 22px;
  border-radius: 28px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.13);
  color: white;
  backdrop-filter: blur(18px);
  animation: inlineStepPulse 5.6s ease-in-out infinite;
}

.inline-sim-steps article:nth-child(2) { animation-delay: 1.4s; }
.inline-sim-steps article:nth-child(3) { animation-delay: 2.8s; }
.inline-sim-steps article:nth-child(4) { animation-delay: 4.2s; }

@keyframes inlineStepPulse {
  0%, 100% {
    transform: translateY(0);
    border-color: rgba(255,255,255,0.13);
    box-shadow: none;
  }
  18% {
    transform: translateY(-6px);
    border-color: rgba(34,211,238,0.58);
    box-shadow: 0 24px 70px rgba(34,211,238,0.16);
  }
}

.inline-sim-steps b {
  width: 48px;
  height: 48px;
  display: grid;
  place-items: center;
  margin-bottom: 18px;
  border-radius: 999px;
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
}

.inline-sim-steps h3 {
  margin: 10px 0 8px;
  color: white;
  font-size: 23px;
}

.inline-sim-steps p {
  margin: 0 0 8px;
  color: rgba(226,232,240,0.9);
  font-weight: 800;
}

.inline-sim-steps span {
  color: #a5f3fc;
  font-weight: 750;
}

.inline-sim-output {
  position: relative;
  z-index: 2;
  margin-top: 26px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 420px;
  gap: 18px;
}

.inline-sim-output > div,
.inline-sim-output pre {
  padding: 24px;
  border-radius: 28px;
  background: rgba(255,255,255,0.09);
  border: 1px solid rgba(255,255,255,0.12);
  color: white;
  backdrop-filter: blur(18px);
}

.inline-sim-output span {
  display: block;
  color: #a5f3fc;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.16em;
}

.inline-sim-output h3 {
  margin: 10px 0;
  color: white;
  font-size: 32px;
}

.inline-sim-output p {
  color: rgba(226,232,240,0.82);
  font-size: 18px;
  line-height: 1.6;
}

.inline-sim-output pre {
  margin: 0;
  white-space: pre-wrap;
  color: #dffcff;
  font-size: 14px;
  line-height: 1.5;
}

@media (max-width: 1100px) {
  .inline-sim-head,
  .inline-sim-steps,
  .inline-sim-output {
    grid-template-columns: 1fr;
  }

  .inline-sim-stream {
    display: none;
  }
}

'''

css_text = CSS.read_text(encoding="utf-8")
if "HARD INLINE LIVE SIMULATION" not in css_text:
    CSS.write_text(css_text + css_patch, encoding="utf-8")

print("✅ Old/static flow section replaced inline with visible animated simulation.")
