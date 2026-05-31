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
    const [cancerType, setCancerType] = useState("all");
    const [treatmentStage, setTreatmentStage] = useState("chemotherapy");
    const [mainConcern, setMainConcern] = useState("fatigue");
    const [city, setCity] = useState("İstanbul");
    const [ageGroup, setAgeGroup] = useState("All");
    const [fatigue, setFatigue] = useState(6);
    const [pain, setPain] = useState(4);
    const [nausea, setNausea] = useState(3);
    const [mood, setMood] = useState(5);
    const [activeInsight, setActiveInsight] = useState("ai");
    const [eventSent, setEventSent] = useState(false);
    const [mapRows, setMapRows] = useState([]);

    useEffect(() => {
      async function loadPublicRows() {
        try {
          const res = await fetch(`${API}/public/map-data`);
          const data = await res.json();

          const rows =
            Array.isArray(data) ? data :
            Array.isArray(data.rows) ? data.rows :
            Array.isArray(data.data) ? data.data :
            Array.isArray(data.records) ? data.records :
            [];

          setMapRows(rows);
        } catch {
          setMapRows([]);
        }
      }

      loadPublicRows();
    }, []);

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
      all: "All cancer types",
      breast: "Breast cancer",
      lung: "Lung cancer",
      colorectal: "Colorectal cancer",
      prostate: "Prostate cancer",
      leukemia: "Leukemia / blood cancer",
      other: "Other / not sure"
    };

    const cancerMatch = {
      all: "",
      breast: "Meme",
      lung: "Akciğer",
      colorectal: "Kolorektal",
      prostate: "Prostat",
      leukemia: "Lösemi",
      other: ""
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

    const cityOptions = Array.from(
      new Set(
        mapRows
          .map((row) => row.Ulke_Sehir || row.city || row.country)
          .filter(Boolean)
      )
    ).slice(0, 120);

    const ageOptions = [
      "All",
      ...Array.from(
        new Set(
          mapRows
            .map((row) => row.Yas_Grubu)
            .filter(Boolean)
        )
      )
    ].slice(0, 40);

    const filteredRows = mapRows.filter((row) => {
      const rowCity = row.Ulke_Sehir || row.city || row.country || "";
      const rowAge = row.Yas_Grubu || "";
      const rowCancer = row.Kanser_Turu || "";
      const cancerNeedle = cancerMatch[cancerType];

      const cityOk = !city || rowCity === city;
      const ageOk = ageGroup === "All" || rowAge === ageGroup;
      const cancerOk = !cancerNeedle || rowCancer.toLowerCase().includes(cancerNeedle.toLowerCase());

      return cityOk && ageOk && cancerOk;
    });

    const avg = (key) => {
      const nums = filteredRows
        .map((row) => safeNumber(row[key], NaN))
        .filter((n) => Number.isFinite(n));

      if (!nums.length) return null;
      return nums.reduce((a, b) => a + b, 0) / nums.length;
    };

    const incidenceAvg = avg("Yillik_Vaka_Hizi_100Bin");
    const mortalityAvg = avg("Yillik_Olum_Hizi_100Bin");
    const survivalAvg = avg("Bes_Yillik_Sagkalim_Yuzdesi");

    const symptomScore = Math.round(fatigue * 2.2 + pain * 2.4 + nausea * 1.8 + mood * 2.1);
    const dataSignal =
      incidenceAvg && mortalityAvg
        ? Math.min(30, Math.round((incidenceAvg + mortalityAvg) / 7))
        : 8;

    const supportScore = Math.min(100, symptomScore + dataSignal);

    const supportLevel =
      supportScore >= 72 ? "High support priority" :
      supportScore >= 45 ? "Needs attention" :
      "Stable today";

    const supportClass =
      supportScore >= 72 ? "high" :
      supportScore >= 45 ? "medium" :
      "low";

    const doctorQuestions = [
      "Which of my symptoms are expected, and which ones should I report immediately?",
      "At what point should I call the clinic or seek urgent support?",
      "Could fatigue, pain or nausea be related to my treatment?",
      "What should I track daily before my next visit?",
      "Is there anything my caregiver should watch for at home?"
    ];

    const actionSteps =
      supportScore >= 72
        ? [
            "Do not ignore today’s symptoms.",
            "Contact your care team or clinic if symptoms are new, worsening or hard to tolerate.",
            "Share the structured note below with a doctor, nurse or caregiver.",
            "Ask clearly: “When should I seek urgent support?”"
          ]
        : supportScore >= 45
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

    const aiRecommendation =
      supportScore >= 72
        ? "Your answers suggest that extra support may be needed today. This does not mean a diagnosis or emergency by itself, but it is strong enough to contact a care team, especially if symptoms are new, worsening, or difficult to tolerate."
        : supportScore >= 45
        ? "Your answers suggest that you should monitor symptoms closely and prepare clear questions for your doctor. A caregiver or support team can help you track changes."
        : "Your answers look relatively stable today. Keep tracking symptoms and use the doctor-visit note to communicate clearly at your next appointment.";

    const patientSummary = `ONCOCONNECT AI — Doctor Visit Note

Role: ${roleLabels[role]}
Goal: ${goalLabels[goal]}
Location / data context: ${city || "Not selected"}
Age group: ${ageGroup}
Cancer context: ${cancerLabels[cancerType]}
Treatment stage: ${stageLabels[treatmentStage]}
Main concern: ${concernLabels[mainConcern]}

Symptoms today:
- Fatigue / weakness: ${fatigue}/10
- Pain: ${pain}/10
- Nausea / appetite problem: ${nausea}/10
- Fear, worry or low mood: ${mood}/10

Data signal:
- Matching public data rows: ${filteredRows.length}
- Average annual incidence: ${incidenceAvg ? incidenceAvg.toFixed(2) : "not available"}
- Average annual mortality: ${mortalityAvg ? mortalityAvg.toFixed(2) : "not available"}
- Five-year survival: ${survivalAvg ? survivalAvg.toFixed(1) + "%" : "not available"}

Support priority:
${supportScore}/100 — ${supportLevel}

AI recommendation:
${aiRecommendation}`;

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
      setActiveInsight("splunk");
      setTimeout(() => setEventSent(false), 2600);
    };

    return (
      <div className="patient-copilot-page">
        <nav className="patient-copilot-nav">
          <button onClick={() => setPage("landing")}>← Home</button>
          <button onClick={() => setPage("map")}>Türkiye / Europe Map</button>
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
              Choose your situation, select your city and age group, enter symptoms,
              then generate an AI recommendation, risk explanation, doctor note and Splunk support event.
            </p>

            <div className="patient-hero-actions">
              <button onClick={() => setActiveInsight("ai")} className={activeInsight === "ai" ? "active" : ""}>
                AI Recommendation
              </button>
              <button onClick={() => setActiveInsight("risk")} className={activeInsight === "risk" ? "active" : ""}>
                Risk Assessment
              </button>
              <button onClick={() => setActiveInsight("note")} className={activeInsight === "note" ? "active" : ""}>
                Doctor Note
              </button>
              <button onClick={sendEvent} className={activeInsight === "splunk" ? "active" : ""}>
                Send Splunk Event
              </button>
            </div>
          </div>

          <div className="patient-hero-card">
            <span>How to use this page</span>
            <ol>
              <li>Choose who you are.</li>
              <li>Select what you want to learn.</li>
              <li>Pick city, age group and cancer context.</li>
              <li>Move symptom sliders.</li>
              <li>Click AI Recommendation or Risk Assessment.</li>
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
                  <h2>What do you want to learn today?</h2>
                  <p>Choose one simple goal.</p>
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
                  <h2>Select data context</h2>
                  <p>City, age group and cancer type are read from the public dataset when available.</p>
                </div>
              </div>

              <div className="patient-dropdown-grid">
                <label>
                  <span>City / country</span>
                  <select value={city} onChange={(e) => setCity(e.target.value)}>
                    <option value="">All locations</option>
                    {(cityOptions.length ? cityOptions : ["İstanbul", "Ankara", "İzmir", "Türkiye"]).map((item) => (
                      <option key={item} value={item}>{item}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Age group</span>
                  <select value={ageGroup} onChange={(e) => setAgeGroup(e.target.value)}>
                    {ageOptions.map((item) => (
                      <option key={item} value={item}>{item}</option>
                    ))}
                  </select>
                </label>

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

              <div className="patient-primary-actions">
                <button onClick={() => setActiveInsight("ai")}>Generate AI recommendation</button>
                <button onClick={() => setActiveInsight("risk")}>Run risk assessment</button>
                <button onClick={() => setActiveInsight("note")}>Create doctor note</button>
                <button onClick={sendEvent}>Send to Splunk</button>
              </div>
            </div>
          </div>

          <aside className="patient-output-panel">
            <div className={`patient-score-card ${supportClass}`}>
              <span>Support priority</span>
              <strong>{supportScore}</strong>
              <b>{supportLevel}</b>
              <p>
                This is not a diagnosis. It is a support-priority signal combining your symptom inputs
                with the selected public data context.
              </p>
            </div>

            <div className="patient-data-card">
              <span>Dataset signal</span>
              <h2>{city || "All locations"} · {ageGroup}</h2>
              <div className="patient-data-grid">
                <div>
                  <small>Rows</small>
                  <strong>{filteredRows.length}</strong>
                </div>
                <div>
                  <small>Incidence</small>
                  <strong>{incidenceAvg ? incidenceAvg.toFixed(1) : "-"}</strong>
                </div>
                <div>
                  <small>Mortality</small>
                  <strong>{mortalityAvg ? mortalityAvg.toFixed(1) : "-"}</strong>
                </div>
                <div>
                  <small>5-year survival</small>
                  <strong>{survivalAvg ? `${survivalAvg.toFixed(0)}%` : "-"}</strong>
                </div>
              </div>
            </div>

            <div className="patient-insight-tabs">
              <button className={activeInsight === "ai" ? "active" : ""} onClick={() => setActiveInsight("ai")}>AI</button>
              <button className={activeInsight === "risk" ? "active" : ""} onClick={() => setActiveInsight("risk")}>Risk</button>
              <button className={activeInsight === "actions" ? "active" : ""} onClick={() => setActiveInsight("actions")}>Actions</button>
              <button className={activeInsight === "note" ? "active" : ""} onClick={() => setActiveInsight("note")}>Note</button>
              <button className={activeInsight === "splunk" ? "active" : ""} onClick={() => setActiveInsight("splunk")}>Splunk</button>
            </div>

            {activeInsight === "ai" && (
              <div className="patient-result-card">
                <span>AI recommendation</span>
                <h2>What should I understand?</h2>
                <p>{aiRecommendation}</p>
              </div>
            )}

            {activeInsight === "risk" && (
              <div className="patient-result-card">
                <span>Risk assessment</span>
                <h2>Why this priority?</h2>
                <p>
                  The score combines today’s symptom strength with the selected data context.
                  Higher symptom values and higher public incidence/mortality signal increase the support priority.
                </p>
                <ul>
                  <li>Symptom signal: {symptomScore}/70</li>
                  <li>Dataset signal: {dataSignal}/30</li>
                  <li>Total support priority: {supportScore}/100</li>
                </ul>
              </div>
            )}

            {activeInsight === "actions" && (
              <div className="patient-result-card">
                <span>Next steps</span>
                <h2>What should I do now?</h2>
                <ul>
                  {actionSteps.map((step) => <li key={step}>{step}</li>)}
                </ul>
              </div>
            )}

            {activeInsight === "note" && (
              <div className="patient-note-card">
                <span>Doctor visit note</span>
                <pre>{patientSummary}</pre>

                <div className="patient-note-actions">
                  <button onClick={copySummary}>Copy note</button>
                  <button onClick={() => setActiveInsight("actions")}>Show next steps</button>
                </div>
              </div>
            )}

            {activeInsight === "splunk" && (
              <div className="patient-note-card">
                <span>Splunk event preview</span>
                <pre>{`{
  "source": "oncoconnect_ai_copilot",
  "role": "${role}",
  "goal": "${goal}",
  "city": "${city}",
  "age_group": "${ageGroup}",
  "cancer_type": "${cancerType}",
  "support_score": ${supportScore},
  "support_level": "${supportLevel}",
  "incidence": "${incidenceAvg ? incidenceAvg.toFixed(2) : "NA"}",
  "mortality": "${mortalityAvg ? mortalityAvg.toFixed(2) : "NA"}",
  "survival": "${survivalAvg ? survivalAvg.toFixed(1) : "NA"}"
}`}</pre>

                <div className="patient-note-actions">
                  <button onClick={sendEvent}>Send support event</button>
                  <button onClick={() => setActiveInsight("note")}>Create doctor note</button>
                </div>

                {eventSent && (
                  <div className="patient-event-success">
                    Splunk support event prepared successfully.
                  </div>
                )}
              </div>
            )}

            <div className="patient-result-card">
              <span>Doctor visit preparation</span>
              <h2>Questions to ask</h2>
              <ul>
                {doctorQuestions.map((question) => <li key={question}>{question}</li>)}
              </ul>
            </div>
          </aside>
        </section>
      </div>
    );
  };


  const MapPage = () => {
    const [rows, setRows] = useState([]);
    const [view, setView] = useState("turkiye");
    const [metric, setMetric] = useState("incidence");
    const [year, setYear] = useState(2024);
    const [selectedArea, setSelectedArea] = useState(null);
    const [cancerFilter, setCancerFilter] = useState("All");
    const [ageFilter, setAgeFilter] = useState("All");
    const [status, setStatus] = useState("Loading public cancer indicators...");

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
          setStatus(`${extracted.length} public rows loaded from published datasets`);
        } catch (err) {
          setStatus("Public endpoint could not be loaded. Showing simulation fallback.");
          setRows([]);
        }
      }

      loadMap();
    }, []);

    const fallbackRows = [
      { Bolge: "Türkiye", Ulke_Sehir: "İstanbul", Kanser_Turu: "Meme", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 48.2, Yillik_Olum_Hizi_100Bin: 13.4, Bes_Yillik_Sagkalim_Yuzdesi: 82 },
      { Bolge: "Türkiye", Ulke_Sehir: "Ankara", Kanser_Turu: "Akciğer", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 44.8, Yillik_Olum_Hizi_100Bin: 21.1, Bes_Yillik_Sagkalim_Yuzdesi: 37 },
      { Bolge: "Türkiye", Ulke_Sehir: "İzmir", Kanser_Turu: "Kolorektal", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 39.6, Yillik_Olum_Hizi_100Bin: 14.8, Bes_Yillik_Sagkalim_Yuzdesi: 64 },
      { Bolge: "Türkiye", Ulke_Sehir: "Antalya", Kanser_Turu: "Prostat", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 36.5, Yillik_Olum_Hizi_100Bin: 9.2, Bes_Yillik_Sagkalim_Yuzdesi: 89 },
      { Bolge: "Türkiye", Ulke_Sehir: "Trabzon", Kanser_Turu: "Mide", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 31.3, Yillik_Olum_Hizi_100Bin: 15.1, Bes_Yillik_Sagkalim_Yuzdesi: 45 },
      { Bolge: "Europe", Ulke_Sehir: "Germany", Kanser_Turu: "Breast", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 61.4, Yillik_Olum_Hizi_100Bin: 15.7, Bes_Yillik_Sagkalim_Yuzdesi: 86 },
      { Bolge: "Europe", Ulke_Sehir: "France", Kanser_Turu: "Lung", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 52.1, Yillik_Olum_Hizi_100Bin: 24.2, Bes_Yillik_Sagkalim_Yuzdesi: 39 },
      { Bolge: "Europe", Ulke_Sehir: "Italy", Kanser_Turu: "Colorectal", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 47.8, Yillik_Olum_Hizi_100Bin: 16.4, Bes_Yillik_Sagkalim_Yuzdesi: 67 },
      { Bolge: "Europe", Ulke_Sehir: "Spain", Kanser_Turu: "Prostate", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 45.7, Yillik_Olum_Hizi_100Bin: 10.8, Bes_Yillik_Sagkalim_Yuzdesi: 90 },
      { Bolge: "Europe", Ulke_Sehir: "Poland", Kanser_Turu: "All", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 43.2, Yillik_Olum_Hizi_100Bin: 20.4, Bes_Yillik_Sagkalim_Yuzdesi: 58 }
    ];

    const sourceRows = rows.length ? rows : fallbackRows;

    const cancerOptions = [
      "All",
      ...Array.from(new Set(sourceRows.map((row) => row.Kanser_Turu).filter(Boolean)))
    ].slice(0, 40);

    const ageOptions = [
      "All",
      ...Array.from(new Set(sourceRows.map((row) => row.Yas_Grubu).filter(Boolean)))
    ].slice(0, 40);

    const metricConfig = {
      incidence: {
        label: "New cases",
        short: "Vaka",
        field: "Yillik_Vaka_Hizi_100Bin",
        suffix: " / 100K",
        explanation: "Annual case-rate signal. Higher values indicate higher observed burden in the selected dataset."
      },
      mortality: {
        label: "Deaths",
        short: "Ölüm",
        field: "Yillik_Olum_Hizi_100Bin",
        suffix: " / 100K",
        explanation: "Annual mortality-rate signal. It helps identify where care coordination and early support matter most."
      },
      survival: {
        label: "5-year survival",
        short: "Sağkalım",
        field: "Bes_Yillik_Sagkalim_Yuzdesi",
        suffix: "%",
        explanation: "Five-year survival percentage when available. Higher values indicate better survival outcomes."
      }
    };

    const viewRows = sourceRows.filter((row) => {
      const region = String(row.Bolge || "").toLowerCase();
      const place = String(row.Ulke_Sehir || "").toLowerCase();

      const isTurkey =
        region.includes("türkiye") ||
        region.includes("turkiye") ||
        place.includes("istanbul") ||
        place.includes("ankara") ||
        place.includes("izmir") ||
        place.includes("antalya") ||
        place.includes("trabzon") ||
        place.includes("bursa");

      const viewOk = view === "turkiye" ? isTurkey : !isTurkey;
      const cancerOk = cancerFilter === "All" || row.Kanser_Turu === cancerFilter;
      const ageOk = ageFilter === "All" || row.Yas_Grubu === ageFilter;

      return viewOk && cancerOk && ageOk;
    });

    const groupedAreas = useMemo(() => {
      const map = new Map();

      viewRows.forEach((row) => {
        const name = row.Ulke_Sehir || "Unknown";
        const item = map.get(name) || {
          name,
          rows: 0,
          incidence: [],
          mortality: [],
          survival: [],
          cancerTypes: new Set()
        };

        item.rows += 1;
        item.incidence.push(safeNumber(row.Yillik_Vaka_Hizi_100Bin, NaN));
        item.mortality.push(safeNumber(row.Yillik_Olum_Hizi_100Bin, NaN));
        item.survival.push(safeNumber(row.Bes_Yillik_Sagkalim_Yuzdesi, NaN));
        if (row.Kanser_Turu) item.cancerTypes.add(row.Kanser_Turu);

        map.set(name, item);
      });

      const avg = (values) => {
        const clean = values.filter((n) => Number.isFinite(n));
        if (!clean.length) return null;
        return clean.reduce((a, b) => a + b, 0) / clean.length;
      };

      return Array.from(map.values()).map((item) => {
        const incidence = avg(item.incidence);
        const mortality = avg(item.mortality);
        const survival = avg(item.survival);

        const simulationMultiplier = 1 + ((year - 2024) * 0.018);

        return {
          ...item,
          incidence: incidence == null ? null : incidence * simulationMultiplier,
          mortality: mortality == null ? null : mortality * simulationMultiplier,
          survival: survival == null ? null : Math.max(5, Math.min(98, survival - ((year - 2024) * 0.25))),
          cancerTypes: Array.from(item.cancerTypes)
        };
      });
    }, [viewRows, year]);

    const currentMetric = metricConfig[metric];

    const rankedAreas = [...groupedAreas].sort((a, b) => {
      const av = a[metric] ?? -Infinity;
      const bv = b[metric] ?? -Infinity;
      return metric === "survival" ? av - bv : bv - av;
    });

    const selected = selectedArea
      ? groupedAreas.find((area) => area.name === selectedArea) || rankedAreas[0]
      : rankedAreas[0];

    const totalSignal = groupedAreas.reduce((sum, area) => sum + (area[metric] || 0), 0);

    const displayValue = (area, key = metric) => {
      const value = area?.[key];
      if (value == null || !Number.isFinite(value)) return "-";
      return key === "survival" ? `${value.toFixed(0)}%` : value.toFixed(1);
    };

    const pinPositionsTurkey = [
      [18, 52], [34, 49], [28, 62], [45, 42], [53, 54], [66, 48], [75, 55], [82, 41],
      [58, 35], [22, 66], [37, 59], [70, 62], [49, 66], [30, 40], [86, 58], [60, 44]
    ];

    const pinPositionsEurope = [
      [48, 43], [37, 55], [51, 62], [30, 70], [59, 34], [44, 32], [67, 52], [55, 72],
      [25, 45], [72, 38], [40, 78], [63, 66], [34, 30], [77, 60], [46, 68], [57, 48]
    ];

    const pinPositions = view === "turkiye" ? pinPositionsTurkey : pinPositionsEurope;

    return (
      <div className="futuristic-map-page">
        <nav className="future-map-nav">
          <button onClick={() => setPage("landing")}>← Home</button>
          <button onClick={() => setPage("copilot")}>AI Copilot</button>
          <button onClick={() => setPage("admin")}>Admin Console</button>

          <div className="future-map-status">
            <span></span>
            {status}
          </div>
        </nav>

        <section className="future-map-hero">
          <div>
            <p className="future-kicker">INTERACTIVE CANCER BURDEN MAP</p>
            <h1>Türkiye–Europe cancer data simulation</h1>
            <p>
              Select Türkiye or Europe, switch between new cases, deaths and survival,
              then click map points to inspect the selected area. Values are powered by the public dataset when available.
            </p>
          </div>

          <div className="future-map-command">
            <span>Live simulation year</span>
            <strong>{year}</strong>
            <input
              type="range"
              min="2024"
              max="2030"
              value={year}
              onChange={(e) => setYear(Number(e.target.value))}
            />
          </div>
        </section>

        <section className="future-map-controls">
          <div className="future-segment">
            <button className={view === "turkiye" ? "active" : ""} onClick={() => { setView("turkiye"); setSelectedArea(null); }}>
              Türkiye — 81 cities
            </button>
            <button className={view === "europe" ? "active" : ""} onClick={() => { setView("europe"); setSelectedArea(null); }}>
              Europe
            </button>
          </div>

          <div className="future-metric-tabs">
            {Object.entries(metricConfig).map(([key, item]) => (
              <button
                key={key}
                className={metric === key ? "active" : ""}
                onClick={() => setMetric(key)}
              >
                <small>{item.short}</small>
                <strong>{item.label}</strong>
              </button>
            ))}
          </div>

          <div className="future-filter-row">
            <label>
              <span>Cancer type</span>
              <select value={cancerFilter} onChange={(e) => setCancerFilter(e.target.value)}>
                {cancerOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </label>

            <label>
              <span>Age group</span>
              <select value={ageFilter} onChange={(e) => setAgeFilter(e.target.value)}>
                {ageOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </label>
          </div>
        </section>

        <section className="future-map-dashboard">
          <div className="future-map-visual-card">
            <div className="future-map-summary">
              <div>
                <span>View</span>
                <strong>{view === "turkiye" ? "Türkiye" : "Europe"}</strong>
              </div>
              <div>
                <span>Metric</span>
                <strong>{currentMetric.label}</strong>
              </div>
              <div>
                <span>Areas</span>
                <strong>{groupedAreas.length}</strong>
              </div>
              <div>
                <span>Total signal</span>
                <strong>{totalSignal ? totalSignal.toFixed(1) : "-"}</strong>
              </div>
            </div>

            <div className={`future-map-canvas ${view}`}>
              <div className="future-map-grid"></div>
              <div className="future-map-glow"></div>
              <div className="future-map-shape">
                <span>{view === "turkiye" ? "TÜRKİYE" : "EUROPE"}</span>
              </div>

              {rankedAreas.slice(0, 16).map((area, index) => {
                const [left, top] = pinPositions[index % pinPositions.length];
                const value = area[metric] || 0;
                const scale = Math.max(0.8, Math.min(1.85, value / (metric === "survival" ? 55 : 28)));

                return (
                  <button
                    key={area.name}
                    className={`future-map-pin ${selected?.name === area.name ? "selected" : ""}`}
                    style={{ left: `${left}%`, top: `${top}%`, "--pin-scale": scale }}
                    onClick={() => setSelectedArea(area.name)}
                    title={area.name}
                  >
                    <i></i>
                    <span>{area.name}</span>
                    <b>{displayValue(area)}</b>
                  </button>
                );
              })}
            </div>

            <div className="future-map-legend">
              <span><i className="low"></i> lower signal</span>
              <span><i className="mid"></i> medium signal</span>
              <span><i className="high"></i> higher signal</span>
            </div>
          </div>

          <aside className="future-map-side-panel">
            <div className="future-selected-card">
              <span>Selected area</span>
              <h2>{selected?.name || "No area selected"}</h2>
              <p>{currentMetric.explanation}</p>

              <div className="future-selected-metrics">
                <button className={metric === "incidence" ? "active" : ""} onClick={() => setMetric("incidence")}>
                  <small>Annual cases</small>
                  <strong>{displayValue(selected, "incidence")}</strong>
                </button>
                <button className={metric === "mortality" ? "active" : ""} onClick={() => setMetric("mortality")}>
                  <small>Annual deaths</small>
                  <strong>{displayValue(selected, "mortality")}</strong>
                </button>
                <button className={metric === "survival" ? "active" : ""} onClick={() => setMetric("survival")}>
                  <small>5-year survival</small>
                  <strong>{displayValue(selected, "survival")}</strong>
                </button>
              </div>
            </div>

            <div className="future-rank-card">
              <span>Highest areas</span>
              <h3>{currentMetric.label}</h3>

              <div className="future-rank-list">
                {rankedAreas.slice(0, 7).map((area, index) => (
                  <button
                    key={area.name}
                    className={selected?.name === area.name ? "active" : ""}
                    onClick={() => setSelectedArea(area.name)}
                  >
                    <b>{index + 1}</b>
                    <span>
                      <strong>{area.name}</strong>
                      <small>{area.rows} rows · {area.cancerTypes.slice(0, 2).join(", ") || "mixed"}</small>
                    </span>
                    <em>{displayValue(area)}</em>
                  </button>
                ))}
              </div>
            </div>

            <div className="future-ai-note">
              <span>AI interpretation</span>
              <p>
                {metric === "survival"
                  ? "Lower survival areas should be interpreted carefully and used for support planning, not individual prognosis."
                  : "Higher burden areas can guide awareness, screening, research prioritization and care coordination."}
              </p>
              <button onClick={() => setPage("copilot")}>Use in AI Copilot</button>
            </div>
          </aside>
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
