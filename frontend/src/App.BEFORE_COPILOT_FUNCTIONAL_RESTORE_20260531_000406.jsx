import React, { useEffect, useMemo, useState } from "react";
import "./App.css";

const API = "http://localhost:5050";

function safeNumber(value, fallback = 0) {
  const cleaned = String(value ?? "").replace(",", ".").trim();
  const n = Number(cleaned);
  return Number.isFinite(n) ? n : fallback;
}

function App() {
  const [page, setPage] = useState("landing");
  const [lang, setLang] = useState("en");

  const t = {
    langLabel: lang === "tr" ? "Dil" : "Language",
    home: lang === "tr" ? "Ana Sayfa" : "Home",
    admin: lang === "tr" ? "Admin Panel" : "Admin Panel",
    map: lang === "tr" ? "Harita" : "Map",
    kids: "Onco Kids",
  };

  const LandingPage = () => (
    <div className="old-home-page">
      <nav className="old-home-nav">
        <div className="old-home-brand">OncoConnect AI</div>

        <div className="old-home-links">
          <button onClick={() => setPage("landing")}>Home</button>
          <a href="#what-is-it">What is it?</a>
          <a href="#how-it-works">How it works</a>
          <a href="#cancer-burden">Cancer Burden</a>
          <a href="#research">Research</a>
          <button type="button" onClick={() => setPage("copilot")}>AI Copilot</button>
          <button type="button" onClick={() => setPage("kids")}>Onco Kids</button>
          <button onClick={() => setPage("admin")}>Admin</button>
          <button onClick={() => setPage("showcase")}>Platform</button>
        </div>

        <div className="old-home-lang">
          <label>{t.langLabel}</label>
          <select value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">English</option>
            <option value="tr">Türkçe</option>
          </select>
        </div>
      </nav>

      <section className="old-portal-hero">
        <div className="old-portal-copy">
          <p className="old-eyebrow">ONCOCONNECT AI PUBLIC PORTAL</p>

          <h1>
            Safe cancer support, research awareness and AI guidance
          </h1>

          <p>
            A two-layer platform for patients, caregivers, clinicians, researchers and NGOs:
            first trusted information, then AI Copilot and Splunk-powered operational monitoring.
          </p>

          <div className="old-hero-actions">
            <button type="button" onClick={() => setPage("copilot")}>Launch AI Copilot</button>
            <button onClick={() => setPage("map")}>Open Knowledge Graph</button>
            <button onClick={() => setPage("kids")}>Onco Kids</button>
          </div>

          <div className="old-disclaimer">
            This platform does not provide diagnosis or treatment advice. It supports doctor-visit
            preparation, trusted source navigation and support coordination.
          </div>
        </div>

        <div className="old-hero-card">
          <div className="old-orb"></div>
          <h3>Calm, clear and safe guidance</h3>
          <p>
            The goal is not to create fear; it is to prepare better questions, surface support
            needs and give care teams more structured information.
          </p>

          <div className="old-companion-pill">
            <span>😊</span>
            <div>
              <strong>Safe companion</strong>
              <small>Guidance with warmth, not fear.</small>
            </div>
          </div>
        </div>
      </section>

      <section id="what-is-it" className="old-section">
        <div className="old-section-head">
          <h2>Patient support portal + AI Copilot + operational monitoring</h2>
          <p>
            OncoConnect AI helps cancer patients and caregivers make symptoms easier to understand,
            prepare for doctor visits and help support teams identify high-risk cases when needed.
          </p>
        </div>

        <div className="old-grid old-grid-3">
          <div className="old-info-card">
            <h3>I want to understand my symptoms</h3>
            <p>AI Copilot explains symptom burden, creates a risk signal and prepares doctor questions.</p>
          </div>
          <div className="old-info-card">
            <h3>I want to prepare for a doctor visit</h3>
            <p>Turns symptoms into a structured conversation note.</p>
          </div>
          <div className="old-info-card">
            <h3>I want simple information for my child</h3>
            <p>Onco Kids provides gentler, hopeful explanations for children and families.</p>
          </div>
          <div className="old-info-card">
            <h3>I want to follow new cancer research</h3>
            <p>A safe source-aware feed for trials, immunotherapy, early detection and patient support.</p>
          </div>
          <div className="old-info-card">
            <h3>I am an NGO or support team</h3>
            <p>Prioritizes high-risk cases through Splunk dashboards and AI summaries.</p>
          </div>
          <div className="old-info-card">
            <h3>I want to see the ecosystem</h3>
            <p>Shows the flow between patients, clinicians, researchers, NGOs, datasets and Splunk.</p>
          </div>
        </div>
      </section>

      <section id="how-it-works" className="old-section old-blue-section">
        <div className="old-section-head">
          <h2>A safe path from information to action</h2>
        </div>

        <div className="old-step-grid">
          {[
            ["1", "User selects role", "Patient, caregiver, support team or researcher perspective."],
            ["2", "Symptoms or needs are entered", "Fatigue, nausea, pain, mood and short notes."],
            ["3", "AI Copilot explains", "Risk level, meaning, doctor questions and next step."],
            ["4", "Event streams to Splunk", "Support teams monitor high-risk cases in dashboards."]
          ].map(([num, title, desc]) => (
            <div className="old-step-card" key={num}>
              <b>{num}</b>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>
          ))}
        </div>

        <div className="old-live-flow">
          <div className="old-flow-title">
            <span>LIVE FLOW SIMULATION</span>
            <h2>From symptom note to support action</h2>
            <strong>AI Copilot running</strong>
          </div>

          <div className="old-flow-row">
            <div>
              <b>1</b>
              <h3>Role</h3>
              <p>Patient / caregiver</p>
            </div>
            <i></i>
            <div>
              <b>2</b>
              <h3>Symptoms</h3>
              <p>Fatigue 10 · Pain 9</p>
            </div>
            <i></i>
            <div>
              <b>3</b>
              <h3>AI explains</h3>
              <p>Risk meaning + questions</p>
            </div>
            <i></i>
            <div>
              <b>4</b>
              <h3>Splunk</h3>
              <p>Event monitored</p>
            </div>
          </div>

          <div className="old-risk-row">
            <div className="old-risk-score">
              <span>Risk signal</span>
              <strong>37</strong>
              <b>Critical</b>
            </div>
            <blockquote>
              “Prepare for a care-team conversation: list current symptoms, ask when to seek urgent
              support, and share this structured note.”
            </blockquote>
          </div>
        </div>
      </section>

      <section id="cancer-burden" className="old-section">
        <p className="old-eyebrow dark">CANCER BURDEN</p>
        <h2>Data is not for fear, it is for earlier support and coordination</h2>

        <div className="old-burden-grid">
          <div className="old-burden-card blue">
            <span>Worldwide, 2022</span>
            <strong>~20M</strong>
            <b>new cancer cases</b>
            <p>GLOBOCAN 2022 estimates around 20 million new cancer cases worldwide.</p>
          </div>

          <div className="old-burden-card blue">
            <span>Worldwide, 2022</span>
            <strong>~9.7M</strong>
            <b>cancer deaths</b>
            <p>This highlights the importance of support, awareness, screening and care coordination.</p>
          </div>

          <div className="old-burden-card teal">
            <span>Türkiye context</span>
            <strong>Türkiye</strong>
            <b>country-level cancer statistics</b>
            <p>Lung, breast and colorectal cancers are among key cancer burden areas for Türkiye.</p>
          </div>

          <div className="old-burden-card purple">
            <span>EU Cancer Mission</span>
            <strong>2030</strong>
            <b>quality of life and care goals</b>
            <p>The EU approach emphasizes prevention, cure, quality of life and family support.</p>
          </div>
        </div>
      </section>

      <section id="research" className="old-section old-research-section">
        <p className="old-eyebrow dark">RESEARCH DATA</p>
        <h2>GLOBOCAN 2022 data connected for Türkiye</h2>
        <p className="old-section-desc">
          This section shows source-backed national data. The 81-city map remains a demo distribution
          until official province-level open data is available.
        </p>

        <div className="old-source-grid">
          <div>
            <strong>GLOBOCAN 2022</strong>
            <p>Türkiye total new cases, deaths and 5-year prevalence</p>
          </div>
          <div>
            <strong>ECIS</strong>
            <p>Cancer burden indicators for European countries</p>
          </div>
          <div>
            <strong>HSGM</strong>
            <p>Türkiye official annual cancer statistics reports</p>
          </div>
        </div>

        <div className="old-turkiye-stats">
          <div>
            <span>Türkiye, 2022</span>
            <strong>240,013</strong>
            <b>all cancers new cases</b>
          </div>
          <div>
            <span>Türkiye, 2022</span>
            <strong>129,672</strong>
            <b>all cancers deaths</b>
          </div>
          <div>
            <span>Türkiye, 2022</span>
            <strong>679,335</strong>
            <b>5-year prevalence</b>
          </div>
        </div>

        <div className="old-research-actions">
          <button onClick={() => setPage("map")}>Open Interactive Cancer Map</button>
          <button onClick={() => setPage("admin")}>Open Admin Data Console</button>
        </div>
      </section>
    </div>
  );


  const CopilotPage = () => {
    const [role, setRole] = useState("patient");
    const [goal, setGoal] = useState("doctor");
    const [cancerType, setCancerType] = useState("breast");
    const [treatmentStage, setTreatmentStage] = useState("chemotherapy");
    const [mainConcern, setMainConcern] = useState("fatigue");
    const [fatigue, setFatigue] = useState(6);
    const [pain, setPain] = useState(4);
    const [nausea, setNausea] = useState(3);
    const [mood, setMood] = useState(5);
    const [copilotMode, setCopilotMode] = useState("simple");
    const [eventSent, setEventSent] = useState(false);

    const supportScore = Math.min(
      100,
      Math.round(fatigue * 2.2 + pain * 2.4 + nausea * 1.8 + mood * 2.1)
    );

    const supportLevel =
      supportScore >= 65 ? "High support priority" :
      supportScore >= 38 ? "Needs attention" :
      "Stable today";

    const supportClass =
      supportScore >= 65 ? "high" :
      supportScore >= 38 ? "medium" :
      "low";

    const roleLabels = {
      patient: "I am a patient",
      caregiver: "I am a family member / caregiver",
      support: "I am a support team"
    };

    const goalLabels = {
      symptoms: "Understand my symptoms",
      doctor: "Prepare for my doctor visit",
      urgent: "Know when to ask for urgent support",
      child: "Explain this gently to a child"
    };

    const cancerLabels = {
      breast: "Breast cancer",
      lung: "Lung cancer",
      colorectal: "Colorectal cancer",
      prostate: "Prostate cancer",
      leukemia: "Leukemia / blood cancer",
      other: "Other / not sure"
    };

    const stageLabels = {
      diagnosis: "Recently diagnosed",
      chemotherapy: "Receiving chemotherapy",
      radiotherapy: "Receiving radiotherapy",
      surgery: "Before / after surgery",
      followup: "Follow-up / remission",
      palliative: "Supportive / palliative care"
    };

    const concernLabels = {
      fatigue: "Fatigue / weakness",
      pain: "Pain",
      nausea: "Nausea / appetite",
      anxiety: "Fear / anxiety",
      sleep: "Sleep problems",
      questions: "I do not know what to ask"
    };

    const patientSummary = `Role: ${roleLabels[role]}
Goal: ${goalLabels[goal]}
Cancer context: ${cancerLabels[cancerType]}
Treatment stage: ${stageLabels[treatmentStage]}
Main concern: ${concernLabels[mainConcern]}
Fatigue: ${fatigue}/10
Pain: ${pain}/10
Nausea: ${nausea}/10
Mood distress: ${mood}/10
Support priority: ${supportScore}/100 — ${supportLevel}`;

    const doctorQuestions = [
      "Which of my symptoms are expected, and which ones should I report immediately?",
      "At what point should I call the clinic or seek urgent support?",
      "Could fatigue, pain or nausea be related to my treatment?",
      "What should I track daily before my next visit?",
      "Is there anything my caregiver should watch for at home?"
    ];

    const actionSteps =
      supportScore >= 65
        ? [
            "Do not ignore today’s symptoms.",
            "Contact your care team or clinic if symptoms are new, worsening or hard to tolerate.",
            "Share the structured note below with a doctor, nurse or caregiver.",
            "Ask clearly: “When should I seek urgent support?”"
          ]
        : supportScore >= 38
        ? [
            "Track your symptoms today and tomorrow.",
            "Prepare the doctor questions below before your visit.",
            "Tell a trusted caregiver how you are feeling.",
            "Ask your care team which symptoms should trigger a call."
          ]
        : [
            "Continue tracking symptoms calmly.",
            "Use the questions below for your next doctor visit.",
            "Share changes early if symptoms increase.",
            "Keep this note as a simple visit-preparation summary."
          ];

    const copySummary = async () => {
      try {
        await navigator.clipboard.writeText(patientSummary);
        alert("Doctor visit note copied.");
      } catch {
        alert(patientSummary);
      }
    };

    const sendEvent = () => {
      setEventSent(true);
      setTimeout(() => setEventSent(false), 2600);
    };

    return (
      <div className="patient-copilot-page">
        <nav className="patient-copilot-nav">
          <button onClick={() => setPage("landing")}>← Home</button>
          <button onClick={() => setPage("map")}>Cancer Map</button>
          <button onClick={() => setPage("kids")}>Onco Kids</button>

          <div className="patient-copilot-lang">
            <label>{t.langLabel}</label>
            <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">English</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>
        </nav>

        <section className="patient-copilot-hero">
          <div>
            <p className="patient-kicker">ONCOCONNECT AI COPILOT</p>
            <h1>Simple cancer support guidance, step by step</h1>
            <p>
              This tool does not diagnose or replace your doctor. It helps you understand what to track,
              prepare better questions, and create a clear note for your care team.
            </p>

            <div className="patient-hero-actions">
              <button onClick={() => setCopilotMode("simple")} className={copilotMode === "simple" ? "active" : ""}>
                Simple mode
              </button>
              <button onClick={() => setCopilotMode("doctor")} className={copilotMode === "doctor" ? "active" : ""}>
                Doctor visit mode
              </button>
              <button onClick={() => setCopilotMode("support")} className={copilotMode === "support" ? "active" : ""}>
                Support team mode
              </button>
            </div>
          </div>

          <div className="patient-hero-card">
            <span>How to use this page</span>
            <ol>
              <li>Choose who you are.</li>
              <li>Select what you need help with.</li>
              <li>Pick your cancer/treatment context.</li>
              <li>Move symptom sliders.</li>
              <li>Copy the doctor visit note.</li>
            </ol>
          </div>
        </section>

        <section className="patient-copilot-layout">
          <div className="patient-input-panel">
            <div className="patient-block">
              <div className="patient-block-title">
                <b>1</b>
                <div>
                  <h2>Who are you?</h2>
                  <p>Choose the perspective. The explanation changes based on this.</p>
                </div>
              </div>

              <div className="patient-choice-grid">
                {Object.entries(roleLabels).map(([key, label]) => (
                  <button
                    key={key}
                    className={role === key ? "selected" : ""}
                    onClick={() => setRole(key)}
                  >
                    {label}
                  </button>
                ))}
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>2</b>
                <div>
                  <h2>What do you want to do today?</h2>
                  <p>Start with the simplest goal.</p>
                </div>
              </div>

              <div className="patient-choice-grid two">
                {Object.entries(goalLabels).map(([key, label]) => (
                  <button
                    key={key}
                    className={goal === key ? "selected" : ""}
                    onClick={() => setGoal(key)}
                  >
                    {label}
                  </button>
                ))}
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>3</b>
                <div>
                  <h2>Your context</h2>
                  <p>This does not diagnose you. It only makes the note clearer.</p>
                </div>
              </div>

              <div className="patient-dropdown-grid">
                <label>
                  <span>Cancer type</span>
                  <select value={cancerType} onChange={(e) => setCancerType(e.target.value)}>
                    {Object.entries(cancerLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Treatment stage</span>
                  <select value={treatmentStage} onChange={(e) => setTreatmentStage(e.target.value)}>
                    {Object.entries(stageLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Main concern today</span>
                  <select value={mainConcern} onChange={(e) => setMainConcern(e.target.value)}>
                    {Object.entries(concernLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>4</b>
                <div>
                  <h2>How strong are your symptoms today?</h2>
                  <p>0 means none. 10 means very strong.</p>
                </div>
              </div>

              <div className="patient-slider-list">
                {[
                  ["Fatigue / weakness", fatigue, setFatigue],
                  ["Pain", pain, setPain],
                  ["Nausea / appetite problem", nausea, setNausea],
                  ["Fear, worry or low mood", mood, setMood]
                ].map(([label, value, setter]) => (
                  <label key={label}>
                    <div>
                      <span>{label}</span>
                      <strong>{value}/10</strong>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={value}
                      onChange={(e) => setter(Number(e.target.value))}
                    />
                  </label>
                ))}
              </div>
            </div>
          </div>

          <aside className="patient-output-panel">
            <div className={`patient-score-card ${supportClass}`}>
              <span>Support priority</span>
              <strong>{supportScore}</strong>
              <b>{supportLevel}</b>
              <p>
                This is not a medical risk score. It is a simple support-priority signal
                to help you prepare and communicate clearly.
              </p>
            </div>

            <div className="patient-result-card">
              <span>AI Copilot explains</span>
              <h2>What this means</h2>
              <p>
                Based on your answers, your main need today is:
                <strong> {goalLabels[goal].toLowerCase()}</strong>. Your selected context is
                <strong> {cancerLabels[cancerType].toLowerCase()}</strong> during
                <strong> {stageLabels[treatmentStage].toLowerCase()}</strong>.
              </p>
            </div>

            <div className="patient-result-card">
              <span>Next steps</span>
              <h2>What should I do now?</h2>
              <ul>
                {actionSteps.map((step) => <li key={step}>{step}</li>)}
              </ul>
            </div>

            <div className="patient-result-card">
              <span>Doctor visit preparation</span>
              <h2>Questions to ask</h2>
              <ul>
                {doctorQuestions.map((question) => <li key={question}>{question}</li>)}
              </ul>
            </div>

            <div className="patient-note-card">
              <span>Doctor visit note</span>
              <pre>{patientSummary}</pre>

              <div className="patient-note-actions">
                <button onClick={copySummary}>Copy note</button>
                <button onClick={sendEvent}>Send support event</button>
              </div>

              {eventSent && (
                <div className="patient-event-success">
                  Support event prepared for Splunk monitoring.
                </div>
              )}
            </div>
          </aside>
        </section>
      </div>
    );
  };


  const MapPage = () => {
    const [rows, setRows] = useState([]);
    const [status, setStatus] = useState("Loading map data...");

    useEffect(() => {
      async function loadMap() {
        try {
          const res = await fetch(`${API}/public/map-data`);
          const data = await res.json();

          const extracted =
            Array.isArray(data) ? data :
            Array.isArray(data.rows) ? data.rows :
            Array.isArray(data.data) ? data.data :
            Array.isArray(data.records) ? data.records :
            [];

          setRows(extracted);
          setStatus(`${extracted.length} public rows loaded`);
        } catch (err) {
          setStatus(err.message || "Map data could not be loaded");
        }
      }

      loadMap();
    }, []);

    const topAreas = useMemo(() => {
      const grouped = new Map();

      rows.forEach((row) => {
        const key = row.Ulke_Sehir || row.country || row.name || "Unknown";
        const incidence = safeNumber(row.Yillik_Vaka_Hizi_100Bin);

        if (!grouped.has(key)) {
          grouped.set(key, { name: key, total: 0, count: 0 });
        }

        const item = grouped.get(key);
        item.total += incidence;
        item.count += 1;
      });

      return [...grouped.values()]
        .map((item) => ({
          ...item,
          incidence: item.count ? item.total / item.count : 0
        }))
        .sort((a, b) => b.incidence - a.incidence)
        .slice(0, 12);
    }, [rows]);

    return (
      <div className="graph-page">
        <div className="graph-topbar">
          <button className="ghost-btn" onClick={() => setPage("landing")}>
            {lang === "tr" ? "← Ana Sayfa" : "← Home"}
          </button>
          <button onClick={() => setPage("admin")}>Admin</button>
        </div>

        <section className="graph-hero">
          <p className="eyebrow">PUBLIC CANCER MAP</p>
          <h1>{lang === "tr" ? "Yayınlanan Kanser Veri Haritası" : "Published Cancer Data Map"}</h1>
          <p>{status}</p>
        </section>

        <section className="stakeholder-section">
          <h2>{lang === "tr" ? "En yüksek alanlar" : "Highest areas"}</h2>

          <div className="stakeholder-grid">
            {topAreas.map((area, index) => (
              <div key={area.name}>
                <strong>{index + 1}. {area.name}</strong>
                <p>
                  {lang === "tr" ? "Ortalama yıllık vaka hızı" : "Average annual incidence rate"}:
                  {" "}
                  <b>{Number.isFinite(area.incidence) ? area.incidence.toFixed(1) : "-"}</b>
                </p>
              </div>
            ))}
          </div>
        </section>

        <section className="stakeholder-section">
          <h2>{lang === "tr" ? "Veri Önizleme" : "Data Preview"}</h2>
          <div className="stakeholder-grid">
            {rows.slice(0, 12).map((row, index) => (
              <div key={`${row.Ulke_Sehir}-${row.Kanser_Turu}-${index}`}>
                <strong>{row.Ulke_Sehir || "Unknown"} · {row.Kanser_Turu || "Cancer"}</strong>
                <p>
                  {lang === "tr" ? "Cinsiyet" : "Sex"}: {row.Cinsiyet || "-"}<br />
                  {lang === "tr" ? "Yaş" : "Age"}: {row.Yas_Grubu || "-"}<br />
                  {lang === "tr" ? "Vaka" : "Incidence"}: {row.Yillik_Vaka_Hizi_100Bin || "-"}<br />
                  {lang === "tr" ? "Ölüm" : "Mortality"}: {row.Yillik_Olum_Hizi_100Bin || "-"}
                </p>
              </div>
            ))}
          </div>
        </section>
      </div>
    );
  };

  const AdminPanel = () => {
    const [datasets, setDatasets] = useState([]);
    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("");
    const [loading, setLoading] = useState(false);
    const [tab, setTab] = useState("datasets");

    async function loadDatasets() {
      try {
        const res = await fetch(`${API}/admin/datasets`);
        const data = await res.json();
        setDatasets(Array.isArray(data) ? data : data.datasets || []);
      } catch (err) {
        setStatus(err.message || "Dataset load failed");
      }
    }

    useEffect(() => {
      loadDatasets();
    }, []);

    async function uploadDataset() {
      if (!file) {
        setStatus("Please select a CSV file first.");
        return;
      }

      setLoading(true);
      setStatus("Uploading dataset...");

      try {
        const form = new FormData();
        form.append("file", file);

        const res = await fetch(`${API}/admin/upload`, {
          method: "POST",
          body: form
        });

        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Upload failed");

        setStatus(`Uploaded: ${data.dataset?.name || file.name}`);
        setFile(null);
        await loadDatasets();
      } catch (err) {
        setStatus(err.message || "Upload failed");
      } finally {
        setLoading(false);
      }
    }

    async function updateDataset(id, patch) {
      setLoading(true);
      try {
        const res = await fetch(`${API}/admin/datasets/${id}`, {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(patch)
        });

        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Update failed");

        setStatus("Dataset updated.");
        await loadDatasets();
      } catch (err) {
        setStatus(err.message || "Update failed");
      } finally {
        setLoading(false);
      }
    }

    async function deleteDataset(id) {
      if (!confirm("Delete this dataset?")) return;

      setLoading(true);
      try {
        const res = await fetch(`${API}/admin/datasets/${id}`, {
          method: "DELETE"
        });

        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Delete failed");

        setStatus("Dataset deleted.");
        await loadDatasets();
      } catch (err) {
        setStatus(err.message || "Delete failed");
      } finally {
        setLoading(false);
      }
    }

    async function runAutoResearch() {
      setLoading(true);
      setStatus("Auto Research Agent is scanning trusted cancer data sources...");

      try {
        const res = await fetch(`${API}/admin/auto-research`, { method: "POST" });
        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Auto research failed");

        setStatus(data.message || "Auto research draft generated.");
        await loadDatasets();
        setTab("datasets");
      } catch (err) {
        setStatus(err.message || "Auto research failed");
      } finally {
        setLoading(false);
      }
    }

    async function runOfficialIngest() {
      setLoading(true);
      setStatus("Official Data Ingestion Agent is fetching, normalizing and validating indicators...");

      try {
        const res = await fetch(`${API}/admin/auto-ingest`, { method: "POST" });
        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Official ingestion failed");

        setStatus(
          `Official ingestion draft generated: ${data.dataset?.rowCount || 0} validated rows`
        );
        await loadDatasets();
        setTab("datasets");
      } catch (err) {
        setStatus(err.message || "Official ingestion failed");
      } finally {
        setLoading(false);
      }
    }

    const totalRows = datasets.reduce((sum, d) => sum + safeNumber(d.rowCount), 0);
    const publishedCount = datasets.filter((d) => d.published).length;

    return (
      <div className="admin-page-v35">
        <header className="admin-topbar-v35">
          <button onClick={() => setPage("landing")}>
            {lang === "tr" ? "← Ana Sayfa" : "← Home"}
          </button>
          <strong>OncoConnect Admin Console</strong>
          <button onClick={loadDatasets}>Refresh</button>
        </header>

        <section className="admin-hero-v35">
          <div>
            <p className="eyebrow">DATA OPERATIONS</p>
            <h1>Dataset Governance Console</h1>
            <p>
              Upload, validate, publish and monitor datasets powering the public cancer map.
            </p>
          </div>
        </section>

        <section className="admin-kpi-grid-v35">
          <div><strong>{datasets.length}</strong><span>Total datasets</span></div>
          <div><strong>{publishedCount}</strong><span>Published</span></div>
          <div><strong>{totalRows}</strong><span>Total rows</span></div>
        </section>

        <section className="admin-tabs-v38">
          {["datasets", "automation", "sources", "settings"].map((item) => (
            <button
              key={item}
              className={tab === item ? "active" : ""}
              onClick={() => setTab(item)}
            >
              {item}
            </button>
          ))}
        </section>

        {status && <section className="admin-status-v35">{status}</section>}

        {tab === "datasets" && (
          <section className="admin-card-v35">
            <h2>Datasets</h2>

            <div className="admin-upload-row-v35">
              <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files?.[0] || null)} />
              <button onClick={uploadDataset} disabled={loading}>Upload CSV</button>
            </div>

            <div className="admin-table-wrap-v35">
              <table>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Rows</th>
                    <th>Quality</th>
                    <th>Source</th>
                    <th>Published</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {datasets.map((d) => (
                    <tr key={d.id}>
                      <td>{d.name || d.originalName}</td>
                      <td>{d.rowCount || d.rows?.length || 0}</td>
                      <td>{d.qualityFlag || "-"}</td>
                      <td>{d.sourceName || "-"}</td>
                      <td>{d.published ? "Yes" : "No"}</td>
                      <td>
                        <button
                          onClick={() => updateDataset(d.id, { published: !d.published })}
                          disabled={loading}
                        >
                          {d.published ? "Unpublish" : "Publish"}
                        </button>
                        <button onClick={() => deleteDataset(d.id)} disabled={loading}>
                          Delete
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {tab === "automation" && (
          <section className="admin-card-v35">
            <h2>Automation</h2>
            <p>
              Research candidate sources, normalize official indicators and generate reviewable draft datasets.
            </p>

            <div className="admin-tab-actions-v39">
              <button onClick={runAutoResearch} disabled={loading}>
                Find Candidate Sources
              </button>
              <button onClick={runOfficialIngest} disabled={loading}>
                Fetch & Normalize Official Data
              </button>
              <button onClick={() => window.open(`${API}/public/map-data`, "_blank")}>
                Open Public JSON
              </button>
              <button onClick={() => window.open(`${API}/public/map-data.csv`, "_blank")}>
                Open Public CSV
              </button>
            </div>
          </section>
        )}

        {tab === "sources" && (
          <section className="admin-card-v35">
            <h2>Official Sources</h2>
            <p>ECIS, GCO / GLOBOCAN and future official registry connectors.</p>
            <div className="admin-tab-actions-v39">
              <button onClick={() => window.open(`${API}/admin/sources`, "_blank")}>
                View Source Registry
              </button>
              <button onClick={runOfficialIngest} disabled={loading}>
                Test Official Ingest
              </button>
            </div>
          </section>
        )}

        {tab === "settings" && (
          <section className="admin-card-v35">
            <h2>Settings</h2>
            <p>Recovery admin panel restored after App.jsx overwrite.</p>
            <div className="admin-tab-actions-v39">
              <button onClick={() => setPage("landing")}>Back Home</button>
              <button onClick={loadDatasets}>Reload Datasets</button>
            </div>
          </section>
        )}
      </div>
    );
  };

  const OncoKidsPage = () => {
    const [hopePoints, setHopePoints] = useState(120);
    const [activeQuest, setActiveQuest] = useState("learn");
    const [feeling, setFeeling] = useState(lang === "tr" ? "Umutlu" : "Hopeful");
    const [quizAnswer, setQuizAnswer] = useState(null);
    const [badges, setBadges] = useState(["🌈"]);
    const [checkedPrep, setCheckedPrep] = useState([]);

    const kidText = {
      tr: {
        home: "← Ana Sayfa",
        title: "Onco Kids",
        subtitle: "Çocuklar ve aileler için yumuşak, güven veren ve oyunlaştırılmış destek alanı.",
        start: "Macaraya Başla",
        restart: "Yeniden Başlat",
        points: "Umut Puanı",
        journey: "Umut Yolculuğu",
        helper: "Lumi diyor ki",
        helperText: "Küçük sorular büyük güçlere dönüşür. Hazırsan birlikte öğrenelim.",
        safety: "Bu alan tıbbi karar vermez. Çocukların duygularını konuşmasına ve ailelerin doktor görüşmesine hazırlanmasına yardımcı olur.",
        quizGood: "Harika! Soru sormak cesur bir davranıştır.",
        quizTry: "Tekrar deneyebilirsin. Burada hata yapmak sorun değil."
      },
      en: {
        home: "← Home",
        title: "Onco Kids",
        subtitle: "A gentle, safe and gamified support space for children and families.",
        start: "Start Adventure",
        restart: "Restart",
        points: "Hope Points",
        journey: "Hope Journey",
        helper: "Lumi says",
        helperText: "Small questions can become big strengths. Let’s learn together.",
        safety: "This space does not make medical decisions. It helps children talk about feelings and helps families prepare for doctor conversations.",
        quizGood: "Great! Asking questions is brave.",
        quizTry: "Try again. Making mistakes is okay here."
      }
    }[lang];

    const feelings = lang === "tr"
      ? ["Korkmuş", "Meraklı", "Üzgün", "Umutlu", "Yorgun", "Cesur"]
      : ["Scared", "Curious", "Sad", "Hopeful", "Tired", "Brave"];

    const addPoints = (amount, quest, badge = null) => {
      setHopePoints((p) => p + amount);
      setActiveQuest(quest);
      if (badge) {
        setBadges((current) => current.includes(badge) ? current : [...current, badge]);
      }
    };

    const resetAdventure = () => {
      setHopePoints(120);
      setActiveQuest("learn");
      setFeeling(lang === "tr" ? "Umutlu" : "Hopeful");
      setQuizAnswer(null);
      setBadges(["🌈"]);
      setCheckedPrep([]);
    };

    const togglePrep = (item) => {
      setCheckedPrep((current) =>
        current.includes(item)
          ? current.filter((entry) => entry !== item)
          : [...current, item]
      );

      if (!checkedPrep.includes(item)) {
        addPoints(6, "hero", "🎒");
      }
    };

    const journeySteps = [
      ["learn", "🌈", lang === "tr" ? "Öğren" : "Learn", "📘"],
      ["ask", "❓", lang === "tr" ? "Sor" : "Ask", "❓"],
      ["feel", "💛", lang === "tr" ? "Hislerini Seç" : "Choose Feeling", "💛"],
      ["breathe", "☁️", lang === "tr" ? "Nefes Al" : "Breathe", "☁️"],
      ["hero", "🏆", lang === "tr" ? "Cesur Kahraman" : "Brave Hero", "🏆"]
    ];

    return (
      <div className="kids-game-page advanced-kids">
        <header className="kids-game-nav">
          <button className="ghost-btn" onClick={() => setPage("landing")}>{kidText.home}</button>

          <div className="kids-points">
            ⭐ {kidText.points}: <strong>{hopePoints}</strong>
          </div>

          <div className="language-control kids-lang">
            <label>{t.langLabel}</label>
            <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">English</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>
        </header>

        <section className="kids-game-hero advanced">
          <div className="kids-hero-overlay">
            <p className="eyebrow dark">ONCO KIDS</p>
            <h1>{kidText.title}</h1>
            <p>{kidText.subtitle}</p>

            <div className="kids-hero-actions">
              <button className="kids-main-btn" onClick={() => addPoints(25, "learn", "📘")}>
                {kidText.start}
              </button>
              <button className="kids-reset-btn" onClick={resetAdventure}>
                {kidText.restart}
              </button>
            </div>

            <div className="badge-row">
              {badges.map((badge) => <span key={badge}>{badge}</span>)}
            </div>

            <div className="lumi-card">
              <div className="lumi-avatar moving">🌟</div>
              <div>
                <strong>{kidText.helper}</strong>
                <span>{kidText.helperText}</span>
              </div>
            </div>
          </div>

          <div className="character-stage lumi-companion-stage">
            <div className="lumi-sky-orb"></div>
            <div className="lumi-character">
              <div className="lumi-face">😊</div>
              <div className="lumi-body"></div>
              <div className="lumi-shadow"></div>
            </div>

            <div className="lumi-speech">
              <strong>{kidText.helper}</strong>
              <span>
                {lang === "tr"
                  ? "Bir görev seç, umut puanı topla ve cesur sorular hazırla."
                  : "Pick a quest, collect hope points and practice brave questions."}
              </span>
            </div>
          </div>
        </section>

        <section className="hope-journey advanced">
          <h2>{kidText.journey}</h2>

          <div className="journey-path">
            {journeySteps.map(([key, icon, label, badge], index) => (
              <button
                key={key}
                className={`journey-step ${activeQuest === key ? "active" : ""}`}
                onClick={() => addPoints(10 + index * 5, key, badge)}
              >
                <span>{icon}</span>
                <strong>{label}</strong>
              </button>
            ))}
          </div>
        </section>

        <section className="kids-game-grid advanced">
          <div className="kids-game-card story-card">
            <h3>{lang === "tr" ? "Hikâye Görevi" : "Story Quest"}</h3>
            <p>
              {lang === "tr"
                ? "Elif hastane ziyaretinden önce biraz meraklı ve biraz endişeli. Ona hangi soruları sorabileceğini birlikte hazırlayalım."
                : "Elif feels curious and a little worried before a hospital visit. Let’s help her prepare gentle questions."}
            </p>
            <div className="choice-grid">
              <button onClick={() => addPoints(18, "ask", "❓")}>
                {lang === "tr" ? "Doktora soru hazırla" : "Prepare a doctor question"}
              </button>
              <button onClick={() => addPoints(18, "feel", "💬")}>
                {lang === "tr" ? "Duygusunu söylemesine yardım et" : "Help her name a feeling"}
              </button>
            </div>
          </div>

          <div className="kids-game-card quiz-card">
            <h3>Mini Quiz</h3>
            <p>
              {lang === "tr"
                ? "Hastaneye gitmeden önce soru sormak iyi midir?"
                : "Is it okay to ask questions before going to the hospital?"}
            </p>

            <div className="choice-grid">
              <button onClick={() => { setQuizAnswer("good"); addPoints(30, "hero", "🏆"); }}>
                {lang === "tr" ? "Evet, soru sormak iyidir" : "Yes, questions are good"}
              </button>
              <button onClick={() => { setQuizAnswer("try"); addPoints(5, "learn"); }}>
                {lang === "tr" ? "Hayır, hiç sormamalıyız" : "No, we should not ask"}
              </button>
            </div>

            {quizAnswer && (
              <div className={`quiz-result ${quizAnswer}`}>
                {quizAnswer === "good" ? kidText.quizGood : kidText.quizTry}
              </div>
            )}
          </div>

          <div className="kids-game-card knowledge-card">
            <h3>{lang === "tr" ? "Bilgi Baloncukları" : "Knowledge Bubbles"}</h3>
            <div className="bubble-map">
              {[
                lang === "tr" ? "Doktorlar yardım eder" : "Doctors help",
                lang === "tr" ? "İlaçlar planlıdır" : "Medicines have plans",
                lang === "tr" ? "Aile yanında" : "Family is near",
                lang === "tr" ? "Soru sormak iyidir" : "Questions are good",
                lang === "tr" ? "Dinlenmek önemlidir" : "Rest matters",
                lang === "tr" ? "Duygular konuşulabilir" : "Feelings can be shared"
              ].map((item) => (
                <button key={item} onClick={() => addPoints(12, "learn", "✨")}>{item}</button>
              ))}
            </div>
          </div>

          <div className="kids-game-card feeling-card">
            <h3>{lang === "tr" ? "Duygu Bahçesi" : "Emotion Garden"}</h3>
            <div className="feeling-grid game">
              {feelings.map((item) => (
                <button
                  key={item}
                  className={feeling === item ? "selected" : ""}
                  onClick={() => {
                    setFeeling(item);
                    addPoints(8, "feel", "💛");
                  }}
                >
                  {item}
                </button>
              ))}
            </div>
            <p className="feeling-result">
              {lang === "tr"
                ? `${feeling} hissetmek normal. Bunu güvendiğin bir yetişkinle paylaşabilirsin.`
                : `Feeling ${feeling.toLowerCase()} is okay. You can share it with a trusted adult.`}
            </p>
          </div>

          <div className="kids-game-card breathing-card wide">
            <h3>{lang === "tr" ? "Sakin Nefes Oyunu" : "Calm Breathing Game"}</h3>
            <div className="breathing-game-row">
              <div className="breathing-circle">
                {lang === "tr" ? "nefes al" : "inhale"}<br />
                {lang === "tr" ? "yavaşça ver" : "exhale"}
              </div>
              <div>
                <p>
                  {lang === "tr"
                    ? "Yavaşça nefes al, gökyüzüne bak ve içinden üç güzel şey düşün."
                    : "Breathe slowly, look at the sky and think of three kind things."}
                </p>
                <button onClick={() => addPoints(20, "breathe", "☁️")}>
                  {lang === "tr" ? "Nefes görevini tamamladım" : "I completed the breathing quest"}
                </button>
              </div>
            </div>
          </div>

          <div className="kids-game-card reward-card">
            <h3>{lang === "tr" ? "Rozetlerim" : "My Badges"}</h3>
            <div className="reward-badges">
              {badges.map((badge) => <span key={badge}>{badge}</span>)}
            </div>
            <p>{lang === "tr" ? "Her görev küçük bir cesaret adımıdır." : "Each quest is a small step of courage."}</p>
          </div>

          <div className="kids-game-card prep-card wide">
            <h3>{lang === "tr" ? "Tedavi Günü Çantam" : "My Treatment Day Bag"}</h3>
            <p>
              {lang === "tr"
                ? "Hastane gününden önce küçük bir hazırlık listesi yapmak çocuğun kendini daha güvende hissetmesine yardımcı olabilir."
                : "A simple preparation list can help a child feel safer before a hospital day."}
            </p>

            <div className="kids-checklist">
              {[
                lang === "tr" ? "Sevdiğim küçük oyuncak" : "My favorite small toy",
                lang === "tr" ? "Doktora soracağım bir soru" : "One question for the doctor",
                lang === "tr" ? "Rahat kıyafet" : "Comfortable clothes",
                lang === "tr" ? "Su veya izin verilen atıştırmalık" : "Water or approved snack",
                lang === "tr" ? "Bana eşlik edecek kişi" : "The person coming with me"
              ].map((item) => (
                <button
                  key={item}
                  className={checkedPrep.includes(item) ? "checked" : ""}
                  onClick={() => togglePrep(item)}
                >
                  <span>{checkedPrep.includes(item) ? "✅" : "⬜"}</span>
                  {item}
                </button>
              ))}
            </div>
          </div>

          <div className="kids-game-card doctor-question-card">
            <h3>{lang === "tr" ? "Doktora Sorabileceğim Sorular" : "Questions I Can Ask"}</h3>
            <div className="question-chip-list">
              {[
                lang === "tr" ? "Bugün ne olacak?" : "What will happen today?",
                lang === "tr" ? "Acıyacak mı?" : "Will it hurt?",
                lang === "tr" ? "Ne zaman dinlenebilirim?" : "When can I rest?",
                lang === "tr" ? "Korkarsam kime söyleyebilirim?" : "Who can I tell if I feel scared?"
              ].map((item) => (
                <button key={item} onClick={() => addPoints(10, "ask", "❓")}>
                  {item}
                </button>
              ))}
            </div>
          </div>

          <div className="kids-game-card family-guide-card">
            <h3>{lang === "tr" ? "Aile İçin Mini Rehber" : "Mini Guide for Families"}</h3>
            <div className="family-guide-list">
              <div>
                <strong>{lang === "tr" ? "Basit anlat" : "Use simple words"}</strong>
                <p>{lang === "tr" ? "Kısa, sakin ve yaşına uygun cümleler kur." : "Use short, calm, age-appropriate sentences."}</p>
              </div>
              <div>
                <strong>{lang === "tr" ? "Duyguyu kabul et" : "Validate feelings"}</strong>
                <p>{lang === "tr" ? "Korku, merak veya yorgunluk normaldir." : "Fear, curiosity or tiredness can be normal."}</p>
              </div>
              <div>
                <strong>{lang === "tr" ? "Doktora hazır git" : "Prepare for the visit"}</strong>
                <p>{lang === "tr" ? "Çocuğun sorularını birlikte not alın." : "Write the child’s questions together."}</p>
              </div>
            </div>
          </div>
        </section>

        <section className="kids-safety-note">
          {kidText.safety}
        </section>
      </div>
    );
  };

  if (page === "landing") return <LandingPage />;
  if (page === "copilot") return <CopilotPage />;
  if (page === "map") return <MapPage />;
  if (page === "admin") return <AdminPanel />;
  if (page === "kids") return <OncoKidsPage />;

  return <LandingPage />;
}

export default App;
