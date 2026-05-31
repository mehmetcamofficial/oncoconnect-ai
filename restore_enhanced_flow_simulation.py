from pathlib import Path
import re

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")

component = r'''
  const EnhancedFlowSimulation = () => {
    const [scenario, setScenario] = useState("critical");
    const [activeStep, setActiveStep] = useState(0);
    const [isRunning, setIsRunning] = useState(true);
    const [eventCount, setEventCount] = useState(128);

    const scenarios = {
      stable: {
        label: "Stable patient",
        score: 18,
        status: "Stable",
        symptoms: "Fatigue 3 · Pain 2 · Mood 3",
        recommendation: "Continue tracking symptoms and prepare questions for the next visit."
      },
      review: {
        label: "Needs review",
        score: 46,
        status: "Needs review",
        symptoms: "Fatigue 6 · Pain 5 · Mood 6",
        recommendation: "Monitor symptoms closely and share the structured note with the care team."
      },
      critical: {
        label: "High support priority",
        score: 82,
        status: "Critical",
        symptoms: "Fatigue 9 · Pain 8 · Mood 7",
        recommendation: "Contact care team if symptoms are new, worsening or hard to tolerate."
      }
    };

    const current = scenarios[scenario];

    const steps = [
      {
        title: "Patient input",
        subtitle: "Role, symptoms and support need entered",
        detail: current.symptoms,
        icon: "01"
      },
      {
        title: "AI Copilot reasoning",
        subtitle: "Symptom burden is converted into a support signal",
        detail: `Support score ${current.score}/100 · ${current.status}`,
        icon: "02"
      },
      {
        title: "Doctor-ready note",
        subtitle: "Questions and next actions are generated",
        detail: current.recommendation,
        icon: "03"
      },
      {
        title: "Splunk event stream",
        subtitle: "Operational support event is prepared",
        detail: `source=oncoconnect_ai score=${current.score} status=${current.status}`,
        icon: "04"
      }
    ];

    useEffect(() => {
      if (!isRunning) return;

      const timer = setInterval(() => {
        setActiveStep((prev) => (prev + 1) % steps.length);
        setEventCount((prev) => prev + 1);
      }, 1800);

      return () => clearInterval(timer);
    }, [isRunning, scenario]);

    const resetSimulation = () => {
      setActiveStep(0);
      setEventCount(128);
      setIsRunning(true);
    };

    return (
      <section className="enhanced-flow-sim">
        <div className="enhanced-flow-head">
          <div>
            <p>LIVE FLOW SIMULATION</p>
            <h2>From symptom note to coordinated support action</h2>
            <span>
              Watch how OncoConnect AI transforms patient input into AI guidance,
              doctor-ready questions and a Splunk-ready operational event.
            </span>
          </div>

          <div className={`enhanced-risk-badge ${scenario}`}>
            <small>Risk signal</small>
            <strong>{current.score}</strong>
            <b>{current.status}</b>
          </div>
        </div>

        <div className="enhanced-flow-controls">
          {Object.entries(scenarios).map(([key, item]) => (
            <button
              key={key}
              className={scenario === key ? "active" : ""}
              onClick={() => {
                setScenario(key);
                setActiveStep(0);
                setEventCount((prev) => prev + 4);
              }}
            >
              <span>{item.label}</span>
              <b>{item.score}</b>
            </button>
          ))}

          <button className="control-dark" onClick={() => setIsRunning((v) => !v)}>
            {isRunning ? "Pause simulation" : "Run simulation"}
          </button>

          <button className="control-light" onClick={resetSimulation}>
            Reset
          </button>
        </div>

        <div className="enhanced-flow-canvas">
          <div className="flow-grid-bg"></div>

          <div className="flow-stream-line">
            <i></i>
            <i></i>
            <i></i>
          </div>

          <div className="flow-step-row">
            {steps.map((step, index) => (
              <article
                key={step.title}
                className={`flow-step-card ${activeStep === index ? "active" : ""} ${activeStep > index ? "done" : ""}`}
                onClick={() => setActiveStep(index)}
              >
                <div className="flow-step-icon">{step.icon}</div>
                <small>{step.subtitle}</small>
                <h3>{step.title}</h3>
                <p>{step.detail}</p>
              </article>
            ))}
          </div>

          <div className="flow-output-panel">
            <div className="flow-output-main">
              <span>AI Copilot current action</span>
              <h3>{steps[activeStep].title}</h3>
              <p>{steps[activeStep].detail}</p>
            </div>

            <div className="flow-event-panel">
              <span>Splunk event preview</span>
              <code>{`{
  "source": "oncoconnect_ai",
  "scenario": "${scenario}",
  "step": "${steps[activeStep].title}",
  "risk_score": ${current.score},
  "status": "${current.status}",
  "event_count": ${eventCount}
}`}</code>
            </div>

            <div className="flow-mini-metrics">
              <div>
                <small>Events</small>
                <strong>{eventCount}</strong>
              </div>
              <div>
                <small>Latency</small>
                <strong>{activeStep === 1 ? "0.8s" : "1.2s"}</strong>
              </div>
              <div>
                <small>Mode</small>
                <strong>{isRunning ? "Live" : "Paused"}</strong>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  };


'''

# Component yoksa LandingPage öncesine ekle
if "const EnhancedFlowSimulation" not in s:
    idx = s.find("  const LandingPage")
    if idx == -1:
        raise SystemExit("❌ LandingPage bulunamadı.")
    s = s[:idx] + component + s[idx:]

# Eski LIVE FLOW SIMULATION section'ı varsa EnhancedFlowSimulation ile değiştir
if "<EnhancedFlowSimulation />" not in s:
    live_idx = s.find("LIVE FLOW SIMULATION")
    if live_idx != -1:
        sec_start = s.rfind("<section", 0, live_idx)
        sec_end = s.find("</section>", live_idx)
        if sec_start != -1 and sec_end != -1:
            sec_end += len("</section>")
            s = s[:sec_start] + "<EnhancedFlowSimulation />" + s[sec_end:]
        else:
            # fallback: LandingDataDashboard öncesine ekle
            s = s.replace("<LandingDataDashboard />", "<EnhancedFlowSimulation />\n        <LandingDataDashboard />", 1)
    else:
        s = s.replace("<LandingDataDashboard />", "<EnhancedFlowSimulation />\n        <LandingDataDashboard />", 1)

APP.write_text(s, encoding="utf-8")

css_patch = r'''

/* Enhanced live flow simulation */

.enhanced-flow-sim {
  padding: 80px 5vw;
  background:
    radial-gradient(circle at 12% 8%, rgba(34,211,238,0.14), transparent 30%),
    radial-gradient(circle at 88% 18%, rgba(124,58,237,0.10), transparent 34%),
    #f5f8fc;
}

.enhanced-flow-head {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 220px;
  gap: 28px;
  align-items: end;
  margin-bottom: 26px;
}

.enhanced-flow-head p {
  margin: 0 0 12px;
  color: #155eef;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.24em;
}

.enhanced-flow-head h2 {
  margin: 0;
  max-width: 1050px;
  color: #101828;
  font-size: clamp(42px, 5vw, 76px);
  line-height: 1;
  letter-spacing: -0.06em;
}

.enhanced-flow-head span {
  display: block;
  max-width: 940px;
  margin-top: 18px;
  color: #475467;
  font-size: 20px;
  line-height: 1.65;
  font-weight: 750;
}

.enhanced-risk-badge {
  padding: 22px;
  border-radius: 28px;
  color: white;
  background: linear-gradient(135deg, #155eef, #14b8a6);
  box-shadow: 0 24px 70px rgba(15,23,42,0.16);
}

.enhanced-risk-badge.review {
  background: linear-gradient(135deg, #f59e0b, #ea580c);
}

.enhanced-risk-badge.critical {
  background: linear-gradient(135deg, #dc2626, #991b1b);
}

.enhanced-risk-badge small {
  display: block;
  color: rgba(255,255,255,0.78);
  font-weight: 950;
  letter-spacing: 0.14em;
}

.enhanced-risk-badge strong {
  display: block;
  margin: 12px 0 2px;
  font-size: 58px;
  line-height: 1;
}

.enhanced-risk-badge b {
  font-size: 18px;
}

.enhanced-flow-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 22px;
}

.enhanced-flow-controls button {
  border: 0;
  border-radius: 999px;
  padding: 13px 17px;
  background: white;
  color: #101828;
  font-weight: 950;
  cursor: pointer;
  box-shadow: 0 16px 42px rgba(15,23,42,0.08);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}

.enhanced-flow-controls button:hover {
  transform: translateY(-2px);
  box-shadow: 0 22px 54px rgba(15,23,42,0.13);
}

.enhanced-flow-controls button.active {
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
}

.enhanced-flow-controls button span,
.enhanced-flow-controls button b {
  display: inline-block;
}

.enhanced-flow-controls button b {
  margin-left: 9px;
}

.enhanced-flow-controls .control-dark {
  background: #101828;
  color: white;
}

.enhanced-flow-controls .control-light {
  background: #eef4ff;
  color: #155eef;
}

.enhanced-flow-canvas {
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

.flow-grid-bg {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.055) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.055) 1px, transparent 1px);
  background-size: 42px 42px;
  opacity: 0.6;
  animation: flowGridMove 16s linear infinite;
}

@keyframes flowGridMove {
  from { transform: translate3d(0,0,0); }
  to { transform: translate3d(42px,42px,0); }
}

.flow-stream-line {
  position: absolute;
  left: 8%;
  right: 8%;
  top: 180px;
  height: 4px;
  border-radius: 999px;
  background: rgba(125,211,252,0.18);
  overflow: hidden;
  z-index: 1;
}

.flow-stream-line i {
  position: absolute;
  top: 0;
  width: 18%;
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, transparent, #22d3ee, transparent);
  animation: flowPacket 2.2s linear infinite;
}

.flow-stream-line i:nth-child(2) { animation-delay: 0.7s; }
.flow-stream-line i:nth-child(3) { animation-delay: 1.4s; }

@keyframes flowPacket {
  from { left: -20%; opacity: 0.2; }
  45% { opacity: 1; }
  to { left: 110%; opacity: 0.2; }
}

.flow-step-row {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.flow-step-card {
  min-height: 210px;
  padding: 22px;
  border-radius: 28px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.13);
  color: white;
  backdrop-filter: blur(18px);
  cursor: pointer;
  transition: transform 0.22s ease, border-color 0.22s ease, background 0.22s ease;
}

.flow-step-card:hover,
.flow-step-card.active {
  transform: translateY(-5px);
  border-color: rgba(34,211,238,0.58);
  background: rgba(255,255,255,0.14);
  box-shadow: 0 24px 70px rgba(34,211,238,0.16);
}

.flow-step-card.done {
  border-color: rgba(20,184,166,0.42);
}

.flow-step-icon {
  width: 48px;
  height: 48px;
  display: grid;
  place-items: center;
  margin-bottom: 18px;
  border-radius: 999px;
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
  font-weight: 950;
  box-shadow: 0 0 28px rgba(34,211,238,0.26);
}

.flow-step-card small {
  display: block;
  color: #a5f3fc;
  font-weight: 850;
  line-height: 1.45;
}

.flow-step-card h3 {
  margin: 10px 0 8px;
  color: white;
  font-size: 23px;
  letter-spacing: -0.03em;
}

.flow-step-card p {
  margin: 0;
  color: rgba(226,232,240,0.78);
  line-height: 1.5;
  font-weight: 700;
}

.flow-output-panel {
  position: relative;
  z-index: 2;
  margin-top: 26px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 420px;
  gap: 18px;
}

.flow-output-main,
.flow-event-panel,
.flow-mini-metrics {
  padding: 24px;
  border-radius: 28px;
  background: rgba(255,255,255,0.09);
  border: 1px solid rgba(255,255,255,0.12);
  color: white;
  backdrop-filter: blur(18px);
}

.flow-output-main span,
.flow-event-panel span {
  display: block;
  color: #a5f3fc;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.16em;
}

.flow-output-main h3 {
  margin: 10px 0;
  color: white;
  font-size: 32px;
  letter-spacing: -0.04em;
}

.flow-output-main p {
  color: rgba(226,232,240,0.82);
  font-size: 18px;
  line-height: 1.6;
  font-weight: 750;
}

.flow-event-panel code {
  display: block;
  margin-top: 12px;
  white-space: pre-wrap;
  color: #dffcff;
  font-size: 13px;
  line-height: 1.45;
}

.flow-mini-metrics {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  padding: 18px;
}

.flow-mini-metrics div {
  padding: 16px;
  border-radius: 20px;
  background: rgba(255,255,255,0.08);
}

.flow-mini-metrics small {
  display: block;
  color: rgba(226,232,240,0.72);
  font-weight: 850;
}

.flow-mini-metrics strong {
  display: block;
  margin-top: 5px;
  color: #a5f3fc;
  font-size: 28px;
}

@media (max-width: 1100px) {
  .enhanced-flow-head,
  .flow-output-panel,
  .flow-step-row {
    grid-template-columns: 1fr;
  }

  .flow-stream-line {
    display: none;
  }

  .flow-mini-metrics {
    grid-template-columns: 1fr;
  }
}

'''

css = CSS.read_text(encoding="utf-8")
if "Enhanced live flow simulation" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Enhanced live flow simulation restored.")
