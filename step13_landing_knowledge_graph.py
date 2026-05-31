from pathlib import Path

path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) useState içine page state ekle
app = app.replace(
'''  const [role, setRole] = useState("patient");''',
'''  const [page, setPage] = useState("landing");
  const [role, setRole] = useState("patient");'''
)

# 2) return başlangıcına landing + graph wrapper ekle
app = app.replace(
'''  return (
    <div className="page">''',
'''  const LandingPage = () => (
    <div className="landing-page">
      <section className="landing-hero">
        <div className="language-control landing-lang">
          <label>{t.langLabel}</label>
          <select value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">English</option>
            <option value="tr">Türkçe</option>
          </select>
        </div>

        <div className="landing-content">
          <p className="eyebrow">SPLUNK AI HACKATHON PROJECT</p>
          <h1>{lang === "tr" ? "Kanser Yolculuğunda AI Destekli Rehberlik" : "AI-Powered Support for the Cancer Care Journey"}</h1>
          <p className="landing-subtitle">
            {lang === "tr"
              ? "OncoConnect AI; hastalar, hasta yakınları, doktorlar, araştırmacılar ve STK’lar için semptom değerlendirme, doktor görüşmesine hazırlık, risk önceliklendirme ve Splunk destekli operasyonel izleme sunar."
              : "OncoConnect AI helps patients, caregivers, clinicians, researchers and NGOs turn symptom updates into care-ready guidance, risk prioritization and Splunk-powered operational intelligence."}
          </p>

          <div className="landing-actions">
            <button onClick={() => setPage("copilot")}>
              {lang === "tr" ? "AI Copilot’u Başlat" : "Launch AI Copilot"}
            </button>
            <button className="secondary" onClick={() => setPage("graph")}>
              {lang === "tr" ? "Ekosistemi Keşfet" : "Explore Knowledge Graph"}
            </button>
          </div>

          <div className="trust-row">
            <span>{lang === "tr" ? "Hasta rehberliği" : "Patient guidance"}</span>
            <span>{lang === "tr" ? "Doktor görüşmesi hazırlığı" : "Doctor visit preparation"}</span>
            <span>{lang === "tr" ? "STK destek koordinasyonu" : "NGO support coordination"}</span>
            <span>{lang === "tr" ? "Splunk izleme" : "Splunk monitoring"}</span>
          </div>
        </div>

        <div className="landing-orbit">
          <div className="orbit-center">OncoConnect<br />AI</div>
          <div className="orbit-node n1">{lang === "tr" ? "Hasta" : "Patient"}</div>
          <div className="orbit-node n2">{lang === "tr" ? "Doktor" : "Doctor"}</div>
          <div className="orbit-node n3">Splunk</div>
          <div className="orbit-node n4">AI</div>
          <div className="orbit-node n5">{lang === "tr" ? "STK" : "NGO"}</div>
          <div className="orbit-line l1"></div>
          <div className="orbit-line l2"></div>
          <div className="orbit-line l3"></div>
        </div>
      </section>

      <section className="why-section">
        <div className="why-card main">
          <h2>{lang === "tr" ? "Neden var?" : "Why it exists"}</h2>
          <p>
            {lang === "tr"
              ? "Kanser hastaları ve hasta yakınları çoğu zaman semptomların ne anlama geldiğini, doktora ne soracağını ve ne zaman ek desteğe ihtiyaç duyulacağını anlamakta zorlanır."
              : "Cancer patients and caregivers often struggle to understand what symptoms mean, what to ask clinicians, and when extra support may be needed."}
          </p>
        </div>

        <div className="why-card">
          <h3>{lang === "tr" ? "Nasıl çalışır?" : "How it works"}</h3>
          <ol>
            <li>{lang === "tr" ? "Kullanıcı rolünü ve ihtiyacını seçer" : "User selects role and support need"}</li>
            <li>{lang === "tr" ? "Semptomlarını girer" : "Symptoms are entered"}</li>
            <li>{lang === "tr" ? "AI Copilot açıklama ve doktor soruları üretir" : "AI Copilot generates explanation and doctor questions"}</li>
            <li>{lang === "tr" ? "Risk olayı Splunk’a aktarılır" : "Risk event streams into Splunk"}</li>
            <li>{lang === "tr" ? "Destek ekipleri yüksek riskli vakaları izler" : "Support teams monitor high-risk cases"}</li>
          </ol>
        </div>

        <div className="why-card">
          <h3>{lang === "tr" ? "Kimler için?" : "Who benefits?"}</h3>
          <div className="mini-tags">
            <span>{lang === "tr" ? "Hastalar" : "Patients"}</span>
            <span>{lang === "tr" ? "Hasta yakınları" : "Caregivers"}</span>
            <span>{lang === "tr" ? "Doktorlar" : "Clinicians"}</span>
            <span>{lang === "tr" ? "Araştırmacılar" : "Researchers"}</span>
            <span>{lang === "tr" ? "STK’lar" : "NGOs"}</span>
            <span>{lang === "tr" ? "Destek ekipleri" : "Support teams"}</span>
          </div>
        </div>
      </section>

      <section className="alignment-section">
        <div>
          <p className="eyebrow dark">POLICY ALIGNMENT</p>
          <h2>{lang === "tr" ? "Avrupa Birliği ve Türkiye kanser bakım öncelikleriyle uyumlu" : "Aligned with European and Türkiye cancer care priorities"}</h2>
          <p>
            {lang === "tr"
              ? "Platform; erken farkındalık, hasta yaşam kalitesi, bakım koordinasyonu, veri temelli izleme ve destek hizmetlerinin güçlendirilmesi hedefleriyle uyumlu bir dijital sağlık yaklaşımı sunar."
              : "The platform supports a digital health approach aligned with awareness, quality of life, care coordination, data-driven monitoring and stronger support services."}
          </p>
        </div>

        <div className="alignment-grid">
          <div>
            <strong>European Union</strong>
            <span>{lang === "tr" ? "Önleme, erken teşhis, tanı & tedavi, yaşam kalitesi" : "Prevention, early detection, diagnosis & treatment, quality of life"}</span>
          </div>
          <div>
            <strong>Türkiye</strong>
            <span>{lang === "tr" ? "Farkındalık, tarama, erken tanı, hasta destek hizmetleri" : "Awareness, screening, early diagnosis, patient support services"}</span>
          </div>
        </div>
      </section>
    </div>
  );

  const KnowledgeGraph = () => (
    <div className="graph-page">
      <div className="graph-topbar">
        <button className="ghost-btn" onClick={() => setPage("landing")}>
          {lang === "tr" ? "← Geri" : "← Back"}
        </button>
        <button onClick={() => setPage("copilot")}>
          {lang === "tr" ? "AI Copilot’a Geç" : "Open AI Copilot"}
        </button>
      </div>

      <section className="graph-hero">
        <p className="eyebrow">KNOWLEDGE GRAPH</p>
        <h1>{lang === "tr" ? "Kanser Destek Ekosistemi" : "Cancer Support Ecosystem"}</h1>
        <p>
          {lang === "tr"
            ? "OncoConnect AI; hasta deneyimi, klinik görüşme hazırlığı, araştırma verisi, STK koordinasyonu ve Splunk operasyonel izlemeyi tek bir akışta birleştirir."
            : "OncoConnect AI connects patient experience, clinical preparation, research data, NGO coordination and Splunk operational monitoring in one flow."}
        </p>
      </section>

      <section className="knowledge-graph">
        <div className="kg-center">OncoConnect<br />AI</div>

        {[
          [lang === "tr" ? "Hastalar" : "Patients", "submit symptoms", "kg1"],
          [lang === "tr" ? "Hasta Yakınları" : "Caregivers", "support context", "kg2"],
          [lang === "tr" ? "Doktorlar" : "Clinicians", "care questions", "kg3"],
          [lang === "tr" ? "Araştırmacılar" : "Researchers", "pattern analysis", "kg4"],
          [lang === "tr" ? "STK’lar" : "NGOs", "outreach queue", "kg5"],
          ["Splunk", "HEC + dashboards", "kg6"],
          ["AI Copilot", "guidance engine", "kg7"],
          [lang === "tr" ? "Veri Setleri" : "Datasets", "15K+ records", "kg8"]
        ].map(([name, sub, cls]) => (
          <div key={name} className={`kg-node ${cls}`}>
            <strong>{name}</strong>
            <span>{sub}</span>
          </div>
        ))}

        <div className="kg-line a"></div>
        <div className="kg-line b"></div>
        <div className="kg-line c"></div>
        <div className="kg-line d"></div>
        <div className="kg-line e"></div>
        <div className="kg-line f"></div>
      </section>

      <section className="stakeholder-section">
        <h2>{lang === "tr" ? "Paydaşlar için değer" : "Value by stakeholder"}</h2>

        <div className="stakeholder-grid">
          <div>
            <strong>{lang === "tr" ? "Hastalar" : "Patients"}</strong>
            <p>{lang === "tr" ? "Semptomlarını anlamlandırır, doktor görüşmesine daha hazırlıklı gider." : "Understand symptoms and prepare more clearly for doctor visits."}</p>
          </div>
          <div>
            <strong>{lang === "tr" ? "Hasta yakınları" : "Caregivers"}</strong>
            <p>{lang === "tr" ? "Yakınlarının destek ihtiyacını daha erken fark edebilir." : "Identify when a loved one may need extra support."}</p>
          </div>
          <div>
            <strong>{lang === "tr" ? "Doktorlar" : "Clinicians"}</strong>
            <p>{lang === "tr" ? "Hasta görüşmesine daha yapılandırılmış semptom özetiyle başlanabilir." : "Start visits with a more structured symptom summary."}</p>
          </div>
          <div>
            <strong>{lang === "tr" ? "Araştırmacılar" : "Researchers"}</strong>
            <p>{lang === "tr" ? "Semptom, tedavi ve risk örüntülerini izleyebilir." : "Monitor symptom, treatment and risk patterns."}</p>
          </div>
          <div>
            <strong>{lang === "tr" ? "STK’lar" : "NGOs"}</strong>
            <p>{lang === "tr" ? "Yüksek riskli vakaları önceliklendirerek destek koordinasyonu yapabilir." : "Prioritize high-risk cases for outreach and support coordination."}</p>
          </div>
          <div>
            <strong>Splunk</strong>
            <p>{lang === "tr" ? "Canlı olayları, risk sinyallerini ve AI özetlerini izler." : "Monitors live events, risk signals and AI-generated summaries."}</p>
          </div>
        </div>
      </section>
    </div>
  );

  if (page === "landing") return <LandingPage />;
  if (page === "graph") return <KnowledgeGraph />;

  return (
    <div className="page">'''
)

# 3) Copilot hero içine geri butonu ekle
app = app.replace(
'''      <section className="hero">
        <div className="language-control">''',
'''      <section className="hero">
        <div className="copilot-nav">
          <button className="ghost-btn" onClick={() => setPage("landing")}>
            {lang === "tr" ? "← Karşılama" : "← Welcome"}
          </button>
          <button className="ghost-btn" onClick={() => setPage("graph")}>
            {lang === "tr" ? "Knowledge Graph" : "Knowledge Graph"}
          </button>
        </div>

        <div className="language-control">'''
)

path.write_text(app, encoding="utf-8")

# CSS append
css += r'''

/* Step 13 Landing + Knowledge Graph */

.landing-page,
.graph-page {
  min-height: 100vh;
  background:
    radial-gradient(circle at top left, rgba(124, 58, 237, 0.18), transparent 28%),
    radial-gradient(circle at bottom right, rgba(20, 184, 166, 0.16), transparent 28%),
    #f4f7fb;
}

.landing-hero {
  position: relative;
  min-height: 78vh;
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 42px;
  align-items: center;
  padding: 70px 64px 100px;
  color: white;
  overflow: hidden;
  background:
    linear-gradient(rgba(6, 24, 47, 0.88), rgba(30, 58, 138, 0.78)),
    radial-gradient(circle at center, rgba(168, 85, 247, 0.4), transparent 45%),
    linear-gradient(135deg, #06182f, #1e3a8a 48%, #6d28d9);
}

.landing-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px);
  background-size: 44px 44px;
  mask-image: linear-gradient(to bottom, black, transparent 90%);
}

.landing-content,
.landing-orbit,
.landing-hero .hero-card {
  position: relative;
  z-index: 2;
}

.landing-content h1 {
  font-size: 64px;
  max-width: 880px;
}

.landing-subtitle {
  font-size: 21px;
  line-height: 1.65;
  color: rgba(255,255,255,0.92);
  max-width: 860px;
}

.landing-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  margin-top: 28px;
}

.landing-actions button,
.graph-topbar button {
  border: none;
  background: white;
  color: #1d4ed8;
  padding: 14px 20px;
  border-radius: 999px;
  font-weight: 950;
  cursor: pointer;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.18);
}

.landing-actions button.secondary {
  background: rgba(255,255,255,0.13);
  color: white;
  border: 1px solid rgba(255,255,255,0.26);
}

.trust-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 26px;
}

.trust-row span {
  padding: 9px 13px;
  border-radius: 999px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.2);
  font-weight: 800;
}

.landing-lang {
  z-index: 5;
}

.landing-orbit {
  min-height: 470px;
  border-radius: 36px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.16);
  backdrop-filter: blur(18px);
  box-shadow: inset 0 0 80px rgba(255,255,255,0.05);
}

.orbit-center {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  width: 170px;
  height: 170px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  text-align: center;
  background: linear-gradient(135deg, #fff, #dbeafe);
  color: #1e3a8a;
  font-weight: 950;
  font-size: 24px;
  box-shadow: 0 0 60px rgba(255,255,255,0.45);
}

.orbit-node {
  position: absolute;
  padding: 11px 16px;
  border-radius: 999px;
  background: rgba(255,255,255,0.14);
  border: 1px solid rgba(255,255,255,0.24);
  font-weight: 900;
  animation: floatNode 5s ease-in-out infinite;
}

.n1 { left: 8%; top: 18%; }
.n2 { right: 10%; top: 18%; animation-delay: .5s; }
.n3 { right: 8%; bottom: 20%; animation-delay: 1s; }
.n4 { left: 12%; bottom: 16%; animation-delay: 1.5s; }
.n5 { left: 50%; top: 8%; transform: translateX(-50%); animation-delay: 2s; }

.orbit-line {
  position: absolute;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
  transform-origin: center;
  opacity: 0.6;
}

.l1 { width: 70%; left: 15%; top: 50%; }
.l2 { width: 65%; left: 17%; top: 50%; transform: rotate(55deg); }
.l3 { width: 65%; left: 17%; top: 50%; transform: rotate(-55deg); }

@keyframes floatNode {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

.why-section,
.alignment-section,
.stakeholder-section {
  max-width: 1180px;
  margin: 30px auto;
  padding: 0 24px;
}

.why-section {
  display: grid;
  grid-template-columns: 1.2fr 1fr 1fr;
  gap: 18px;
  margin-top: -54px;
  position: relative;
  z-index: 3;
}

.why-card,
.alignment-section,
.stakeholder-grid > div {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 26px;
  padding: 24px;
  box-shadow: 0 24px 70px rgba(15, 23, 42, 0.12);
}

.why-card h2,
.alignment-section h2,
.graph-hero h1,
.stakeholder-section h2 {
  margin-top: 0;
}

.why-card p,
.why-card li,
.alignment-section p,
.stakeholder-grid p {
  color: #475569;
  line-height: 1.65;
}

.mini-tags {
  display: flex;
  gap: 9px;
  flex-wrap: wrap;
}

.mini-tags span {
  background: #eef2ff;
  color: #3730a3;
  font-weight: 850;
  padding: 8px 11px;
  border-radius: 999px;
}

.alignment-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.alignment-grid {
  display: grid;
  gap: 14px;
}

.alignment-grid div {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 18px;
}

.alignment-grid strong,
.alignment-grid span {
  display: block;
}

.alignment-grid span {
  margin-top: 6px;
  color: #475569;
}

.graph-topbar {
  max-width: 1180px;
  margin: 0 auto;
  padding: 24px;
  display: flex;
  justify-content: space-between;
}

.ghost-btn {
  background: rgba(255,255,255,0.2) !important;
  color: #1e3a8a !important;
  border: 1px solid rgba(30, 58, 138, 0.18) !important;
  box-shadow: none !important;
}

.copilot-nav {
  position: absolute;
  left: 56px;
  top: 20px;
  display: flex;
  gap: 10px;
  z-index: 5;
}

.copilot-nav .ghost-btn {
  color: white !important;
  border-color: rgba(255,255,255,0.25) !important;
}

.graph-hero {
  max-width: 1180px;
  margin: 0 auto;
  padding: 28px 24px 10px;
  text-align: center;
}

.graph-hero h1 {
  font-size: 56px;
  color: #0f172a;
}

.graph-hero p {
  max-width: 820px;
  margin: 0 auto;
  color: #475569;
  line-height: 1.7;
}

.knowledge-graph {
  position: relative;
  max-width: 1040px;
  height: 620px;
  margin: 30px auto;
  border-radius: 36px;
  overflow: hidden;
  background:
    radial-gradient(circle at center, rgba(124,58,237,0.18), transparent 28%),
    linear-gradient(135deg, #0f172a, #1e3a8a);
  box-shadow: 0 30px 90px rgba(15, 23, 42, 0.22);
}

.kg-center {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  width: 180px;
  height: 180px;
  border-radius: 999px;
  background: white;
  color: #1e3a8a;
  display: grid;
  place-items: center;
  text-align: center;
  font-weight: 950;
  font-size: 26px;
  z-index: 2;
  box-shadow: 0 0 70px rgba(255,255,255,0.45);
}

.kg-node {
  position: absolute;
  width: 170px;
  padding: 16px;
  border-radius: 20px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.22);
  color: white;
  backdrop-filter: blur(14px);
  animation: floatNode 5.5s ease-in-out infinite;
}

.kg-node strong,
.kg-node span {
  display: block;
}

.kg-node span {
  margin-top: 5px;
  opacity: 0.78;
  font-size: 13px;
}

.kg1 { left: 8%; top: 12%; }
.kg2 { right: 8%; top: 12%; animation-delay: .3s; }
.kg3 { left: 7%; bottom: 16%; animation-delay: .7s; }
.kg4 { right: 7%; bottom: 16%; animation-delay: 1s; }
.kg5 { left: 41%; top: 6%; animation-delay: 1.4s; }
.kg6 { left: 42%; bottom: 6%; animation-delay: 1.8s; }
.kg7 { left: 5%; top: 45%; animation-delay: 2.2s; }
.kg8 { right: 5%; top: 45%; animation-delay: 2.6s; }

.kg-line {
  position: absolute;
  left: 18%;
  top: 50%;
  width: 64%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.42), transparent);
}

.kg-line.b { transform: rotate(35deg); }
.kg-line.c { transform: rotate(-35deg); }
.kg-line.d { transform: rotate(70deg); }
.kg-line.e { transform: rotate(-70deg); }
.kg-line.f { transform: rotate(90deg); }

.stakeholder-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

@media (max-width: 900px) {
  .landing-hero,
  .why-section,
  .alignment-section,
  .stakeholder-grid {
    grid-template-columns: 1fr;
  }

  .landing-content h1,
  .graph-hero h1 {
    font-size: 42px;
  }

  .landing-hero {
    padding: 80px 24px 100px;
  }

  .landing-orbit,
  .knowledge-graph {
    height: 520px;
  }

  .copilot-nav {
    position: static;
    padding: 16px 24px 0;
  }
}
'''

css_path.write_text(css, encoding="utf-8")

print("✅ Landing page and Knowledge Graph added.")
