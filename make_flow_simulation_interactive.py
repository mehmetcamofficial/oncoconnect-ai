from pathlib import Path

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")

component = r'''
  const InteractiveFlowSimulation = () => {
    const scenarios = {
      critical: {
        label: "Critical scenario",
        score: 82,
        status: "Critical",
        symptoms: "Fatigue 9 · Pain 8 · Mood 7",
        action: "Support outreach recommended",
        color: "critical"
      },
      review: {
        label: "Needs review",
        score: 46,
        status: "Needs review",
        symptoms: "Fatigue 6 · Pain 5 · Mood 6",
        action: "Monitor symptoms and prepare doctor questions",
        color: "review"
      },
      stable: {
        label: "Stable",
        score: 18,
        status: "Stable",
        symptoms: "Fatigue 3 · Pain 2 · Mood 3",
        action: "Continue tracking symptoms",
        color: "stable"
      }
    };

    const [scenario, setScenario] = useState("critical");
    const [running, setRunning] = useState(true);
    const [step, setStep] = useState(0);
    const [events, setEvents] = useState(128);

    const current = scenarios[scenario];

    const steps = [
      {
        title: "Patient input",
        subtitle: "Role and symptoms entered",
        detail: current.symptoms
      },
      {
        title: "AI Copilot reasoning",
        subtitle: "Support signal calculated",
        detail: `Risk score ${current.score}/100 · ${current.status}`
      },
      {
        title: "Doctor-ready note",
        subtitle: "Questions and next steps generated",
        detail: current.action
      },
      {
        title: "Splunk event",
        subtitle: "Monitoring event streamed",
        detail: `source=oncoconnect_ai status=${current.status}`
      }
    ];

    useEffect(() => {
      if (!running) return;

      const timer = setInterval(() => {
        setStep((prev) => (prev + 1) % steps.length);
        setEvents((prev) => prev + 1);
      }, 1600);

      return () => clearInterval(timer);
    }, [running, scenario]);

    const changeScenario = (key) => {
      setScenario(key);
      setStep(0);
      setEvents((prev) => prev + 3);
      setRunning(true);
    };

    return (
      <section className="inline-live-simulation interactive-flow-live">
        <div className="inline-sim-head">
          <div>
            <p>LIVE FLOW SIMULATION</p>
            <h2>AI support flow running in real time</h2>
            <span>
              Select a scenario and watch how symptom input becomes AI guidance,
              doctor-ready action and Splunk-ready monitoring.
            </span>
          </div>

          <div className={`inline-risk-chip ${current.color}`}>
            <small>Live risk signal</small>
            <strong>{current.score}</strong>
            <b>{current.status}</b>
          </div>
        </div>

        <div className="inline-sim-controls">
          {Object.entries(scenarios).map(([key, item]) => (
            <button
              key={key}
              type="button"
              className={scenario === key ? "active" : ""}
              onClick={() => changeScenario(key)}
            >
              {item.label}
            </button>
          ))}

          <button
            type="button"
            className={`dark ${running ? "active-running" : ""}`}
            onClick={() => setRunning((value) => !value)}
          >
            {running ? "Pause simulation" : "Auto-running"}
          </button>
        </div>

        <div className="inline-sim-canvas">
          <div className="inline-sim-grid"></div>

          <div className={`inline-sim-stream ${running ? "running" : "paused"}`}>
            <i></i>
            <i></i>
            <i></i>
            <i></i>
          </div>

          <div className="inline-sim-steps">
            {steps.map((item, index) => (
              <article
                key={item.title}
                className={step === index ? "active" : step > index ? "done" : ""}
                onClick={() => setStep(index)}
              >
                <b>{String(index + 1).padStart(2, "0")}</b>
                <h3>{item.title}</h3>
                <p>{item.detail}</p>
                <span>{item.subtitle}</span>
              </article>
            ))}
          </div>

          <div className="inline-sim-output">
            <div>
              <span>AI current recommendation</span>
              <h3>{steps[step].title}</h3>
              <p>{steps[step].detail}</p>
            </div>

            <pre>{`{
  source: "oncoconnect_ai",
  scenario: "${scenario}",
  step: "${steps[step].title}",
  risk_score: ${current.score},
  status: "${current.status}",
  event_count: ${events}
}`}</pre>
          </div>
        </div>
      </section>
    );
  };


'''

# Component'i ekle
if "const InteractiveFlowSimulation" not in s:
    idx = s.find("  const LandingPage")
    if idx == -1:
        raise SystemExit("❌ LandingPage bulunamadı.")
    s = s[:idx] + component + s[idx:]

# Statik inline section'ı component çağrısı ile değiştir
section_start = s.find('<section className="inline-live-simulation">')
if section_start == -1:
    section_start = s.find('<section className="inline-live-simulation interactive-flow-live">')

if section_start != -1:
    section_end = s.find("</section>", section_start)
    if section_end == -1:
        raise SystemExit("❌ inline-live-simulation kapanışı bulunamadı.")
    section_end += len("</section>")
    s = s[:section_start] + "<InteractiveFlowSimulation />" + s[section_end:]
elif "<InteractiveFlowSimulation />" not in s:
    if "<LandingDataDashboard />" in s:
        s = s.replace("<LandingDataDashboard />", "<InteractiveFlowSimulation />\n        <LandingDataDashboard />", 1)
    else:
        raise SystemExit("❌ Simülasyonu yerleştirecek marker bulunamadı.")

APP.write_text(s, encoding="utf-8")

css_patch = r'''

/* Interactive flow simulation behavior */

.interactive-flow-live .inline-sim-controls button {
  pointer-events: auto !important;
  cursor: pointer !important;
}

.interactive-flow-live .inline-sim-controls button.active {
  background: linear-gradient(135deg, #155eef, #14b8a6) !important;
  color: white !important;
  box-shadow: 0 18px 46px rgba(21,94,239,0.26) !important;
}

.interactive-flow-live .inline-sim-controls button.active-running {
  background: linear-gradient(135deg, #101828, #334155) !important;
  color: white !important;
}

.inline-risk-chip.stable {
  background: linear-gradient(135deg, #059669, #14b8a6) !important;
}

.inline-risk-chip.review {
  background: linear-gradient(135deg, #f59e0b, #ea580c) !important;
}

.inline-risk-chip.critical {
  background: linear-gradient(135deg, #dc2626, #991b1b) !important;
}

.interactive-flow-live .inline-sim-steps article {
  cursor: pointer !important;
}

.interactive-flow-live .inline-sim-steps article.active {
  transform: translateY(-7px) !important;
  border-color: rgba(34,211,238,0.7) !important;
  background: rgba(255,255,255,0.16) !important;
  box-shadow: 0 26px 80px rgba(34,211,238,0.18) !important;
}

.interactive-flow-live .inline-sim-steps article.done {
  border-color: rgba(20,184,166,0.45) !important;
}

.inline-sim-stream.paused i {
  animation-play-state: paused !important;
  opacity: 0.35 !important;
}

'''

css = CSS.read_text(encoding="utf-8")
if "Interactive flow simulation behavior" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Flow simulation buttons are now interactive.")
