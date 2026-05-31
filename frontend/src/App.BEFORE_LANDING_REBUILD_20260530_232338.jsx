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
    <div className="portal-page">
      <nav className="portal-topnav">
        <div className="portal-brand">OncoConnect AI</div>

        <div className="portal-tabs">
          <button onClick={() => setPage("landing")}>{t.home}</button>
          <button onClick={() => setPage("map")}>{t.map}</button>
          <button onClick={() => setPage("kids")}>Onco Kids</button>
          <button onClick={() => setPage("admin")}>{t.admin}</button>
        </div>

        <div className="language-control nav-lang">
          <label>{t.langLabel}</label>
          <select value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">English</option>
            <option value="tr">Türkçe</option>
          </select>
        </div>
      </nav>

      <section className="calm-sea-hero">
        <div className="hero-glass-panel">
          <p className="eyebrow">ONCOCONNECT AI</p>
          <h1>
            {lang === "tr"
              ? "Kanser destek, veri ve çocuk dostu rehberlik platformu"
              : "Cancer support, data and child-friendly guidance platform"}
          </h1>
          <p>
            {lang === "tr"
              ? "Hasta, aile, araştırmacı ve kurumlar için veri odaklı kanser destek ekosistemi."
              : "A data-driven cancer support ecosystem for patients, families, researchers and organizations."}
          </p>

          <div className="hero-actions">
            <button onClick={() => setPage("map")}>
              {lang === "tr" ? "Kanser Veri Haritasını Aç" : "Open Cancer Data Map"}
            </button>
            <button onClick={() => setPage("kids")}>Open Onco Kids</button>
            <button onClick={() => setPage("admin")}>Admin Console</button>
          </div>
        </div>
      </section>

      <section className="improved-stats">
        <div className="stat-panel">
          <strong>Public Map</strong>
          <span>{lang === "tr" ? "Yayınlanan datasetlerden beslenir" : "Powered by published datasets"}</span>
        </div>
        <div className="stat-panel">
          <strong>Official Ingest</strong>
          <span>{lang === "tr" ? "Resmi kaynakları normalize eder" : "Normalizes official sources"}</span>
        </div>
        <div className="stat-panel">
          <strong>Onco Kids</strong>
          <span>{lang === "tr" ? "Çocuk ve aile odaklı destek" : "Child and family support"}</span>
        </div>
      </section>
    </div>
  );

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
  if (page === "map") return <MapPage />;
  if (page === "admin") return <AdminPanel />;
  if (page === "kids") return <OncoKidsPage />;

  return <LandingPage />;
}

export default App;
