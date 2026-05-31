from pathlib import Path

path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) Prevention simulator state ekle
app = app.replace(
'''  const [copied, setCopied] = useState(false);''',
'''  const [copied, setCopied] = useState(false);
  const [prevention, setPrevention] = useState({
    tobaccoFree: 60,
    alcoholReduction: 45,
    movement: 40,
    screeningAwareness: 55
  });'''
)

# 2) Risk awareness hesaplamalarını App içinde ekle
app = app.replace(
'''  const riskScore = useMemo(() => {''',
'''  const preventionScore = useMemo(() => {
    const score =
      prevention.tobaccoFree * 0.34 +
      prevention.alcoholReduction * 0.18 +
      prevention.movement * 0.24 +
      prevention.screeningAwareness * 0.24;

    return Math.round(score);
  }, [prevention]);

  const preventionLevel = useMemo(() => {
    if (preventionScore >= 80) return lang === "tr" ? "Güçlü farkındalık" : "Strong awareness";
    if (preventionScore >= 60) return lang === "tr" ? "İyi başlangıç" : "Good progress";
    if (preventionScore >= 40) return lang === "tr" ? "Geliştirilebilir" : "Needs improvement";
    return lang === "tr" ? "Destek gerekli" : "Support needed";
  }, [preventionScore, lang]);

  const updatePrevention = (key, value) => {
    setPrevention({ ...prevention, [key]: Number(value) });
  };

  const riskScore = useMemo(() => {'''
)

# 3) Statistics section sonrası Prevention Simulator ekle
insert_after = '''      </section>

      <section id="research-feed" className="research-feed-section">'''

prevention_section = r'''      </section>

      <section className="prevention-simulator-section">
        <div className="simulator-copy">
          <p className="eyebrow dark">{lang === "tr" ? "ÖNLEME FARKINDALIĞI SİMÜLATÖRÜ" : "PREVENTION AWARENESS SIMULATOR"}</p>
          <h2>
            {lang === "tr"
              ? "Küçük davranış değişiklikleri, büyük farkındalık yaratabilir"
              : "Small behavior changes can create meaningful awareness"}
          </h2>
          <p>
            {lang === "tr"
              ? "Bu araç kişisel kanser riskinizi hesaplamaz. Tütün, alkol, hareket ve tarama farkındalığı gibi değiştirilebilir faktörlerin önemini görselleştiren eğitim amaçlı bir simülasyondur."
              : "This tool does not calculate your personal cancer risk. It is an educational simulation that visualizes the importance of modifiable factors such as tobacco, alcohol, movement and screening awareness."}
          </p>

          <div className="evidence-note">
            {lang === "tr"
              ? "WHO’ya göre kanser vakalarının yaklaşık %30–50’si önlenebilir. Bu nedenle erken farkındalık, sağlıklı yaşam davranışları ve tarama programları kritik öneme sahiptir."
              : "WHO states that around 30–50% of cancer cases are preventable. This makes awareness, healthy behaviors and screening programs critical."}
          </div>
        </div>

        <div className="simulator-card">
          <div className="simulator-score">
            <div className="score-ring" style={{ "--score": `${preventionScore}%` }}>
              <span>{preventionScore}</span>
            </div>
            <div>
              <strong>{preventionLevel}</strong>
              <p>
                {lang === "tr"
                  ? "Bu skor kişisel tıbbi risk değildir; eğitim ve farkındalık göstergesidir."
                  : "This score is not a personal medical risk; it is an education and awareness indicator."}
              </p>
            </div>
          </div>

          <div className="simulator-sliders">
            {[
              [
                "tobaccoFree",
                lang === "tr" ? "Tütünsüz yaşam farkındalığı" : "Tobacco-free awareness",
                lang === "tr" ? "Tütün kullanmamak kanserden korunmada en güçlü adımlardan biridir." : "Avoiding tobacco is one of the strongest steps for cancer prevention."
              ],
              [
                "alcoholReduction",
                lang === "tr" ? "Alkol azaltma farkındalığı" : "Alcohol reduction awareness",
                lang === "tr" ? "Alkol tüketimini azaltmak bazı kanser türleri için risk azaltma stratejilerinde yer alır." : "Reducing alcohol is part of cancer risk reduction strategies for several cancer types."
              ],
              [
                "movement",
                lang === "tr" ? "Fiziksel aktivite" : "Physical activity",
                lang === "tr" ? "Düzenli hareket, sağlıklı kilo ve genel iyilik hali için destekleyicidir." : "Regular movement supports healthy weight and overall wellbeing."
              ],
              [
                "screeningAwareness",
                lang === "tr" ? "Tarama ve erken farkındalık" : "Screening and early awareness",
                lang === "tr" ? "Yaşa ve risk durumuna uygun taramalar için doktorla görüşmek önemlidir." : "Discussing age- and risk-appropriate screening with clinicians is important."
              ]
            ].map(([key, label, desc]) => (
              <div className="prevention-slider" key={key}>
                <div className="slider-meta">
                  <strong>{label}</strong>
                  <span>{prevention[key]}%</span>
                </div>
                <input
                  type="range"
                  min="0"
                  max="100"
                  value={prevention[key]}
                  onChange={(e) => updatePrevention(key, e.target.value)}
                />
                <small>{desc}</small>
              </div>
            ))}
          </div>
        </div>

        <div className="simulator-visual">
          <div className="floating-stat s1">
            <strong>30–50%</strong>
            <span>{lang === "tr" ? "önlenebilir vaka potansiyeli" : "preventable case potential"}</span>
          </div>
          <div className="floating-stat s2">
            <strong>{lang === "tr" ? "Tarama" : "Screening"}</strong>
            <span>{lang === "tr" ? "erken farkındalık" : "early awareness"}</span>
          </div>
          <div className="floating-stat s3">
            <strong>{lang === "tr" ? "Destek" : "Support"}</strong>
            <span>{lang === "tr" ? "bakım koordinasyonu" : "care coordination"}</span>
          </div>
          <div className="visual-orb"></div>
        </div>
      </section>

      <section id="research-feed" className="research-feed-section">'''

app = app.replace(insert_after, prevention_section)

# 4) CSS güçlendirme
css += r'''

/* Step 15: Premium layout fixes + Prevention Simulator */

.portal-hero {
  min-height: 760px !important;
  grid-template-columns: minmax(0, 1fr) minmax(420px, 0.82fr) !important;
  align-items: center !important;
  padding: 96px 64px 120px !important;
}

.portal-copy {
  grid-column: 1 !important;
  max-width: 900px !important;
}

.portal-copy h1 {
  font-size: clamp(48px, 5.2vw, 78px) !important;
  max-width: 920px !important;
  letter-spacing: -0.04em;
}

.portal-subtitle {
  max-width: 780px !important;
}

.calm-visual {
  grid-column: 2 !important;
  display: block !important;
  min-height: 540px !important;
}

.language-control.landing-lang {
  position: absolute !important;
  right: 64px !important;
  left: auto !important;
  top: 28px !important;
  z-index: 8 !important;
}

.need-section {
  margin-top: -72px !important;
}

.need-grid {
  align-items: stretch;
}

.need-card {
  min-height: 190px;
}

.statistics-section {
  margin-top: 64px;
}

.stat-world-grid {
  align-items: stretch;
}

.stat-panel {
  min-height: 285px;
}

.research-feed-section {
  margin-top: 72px;
}

.portal-page {
  background:
    radial-gradient(circle at 10% 10%, rgba(147, 197, 253, 0.20), transparent 28%),
    radial-gradient(circle at 90% 30%, rgba(196, 181, 253, 0.22), transparent 28%),
    radial-gradient(circle at 60% 90%, rgba(153, 246, 228, 0.18), transparent 30%),
    #f8fbff !important;
}

/* Premium background texture */
.portal-page::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background:
    radial-gradient(circle at 20% 20%, rgba(255,255,255,0.72), transparent 18%),
    linear-gradient(120deg, rgba(255,255,255,0.25), transparent);
  opacity: 0.6;
}

.portal-page > section {
  position: relative;
  z-index: 1;
}

/* Prevention simulator */

.prevention-simulator-section {
  max-width: 1180px;
  margin: 64px auto;
  padding: 34px;
  display: grid;
  grid-template-columns: 0.85fr 1.05fr 0.75fr;
  gap: 24px;
  align-items: center;
  border-radius: 36px;
  background:
    radial-gradient(circle at top left, rgba(45, 212, 191, 0.22), transparent 34%),
    radial-gradient(circle at bottom right, rgba(167, 139, 250, 0.26), transparent 34%),
    linear-gradient(135deg, rgba(255,255,255,0.95), rgba(239,246,255,0.95));
  border: 1px solid #dbeafe;
  box-shadow: 0 28px 90px rgba(15, 23, 42, 0.13);
  overflow: hidden;
  position: relative;
}

.prevention-simulator-section::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(30,58,138,0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(30,58,138,0.05) 1px, transparent 1px);
  background-size: 36px 36px;
  mask-image: linear-gradient(to bottom, black, transparent 92%);
}

.simulator-copy,
.simulator-card,
.simulator-visual {
  position: relative;
  z-index: 2;
}

.simulator-copy h2 {
  font-size: 36px;
  line-height: 1.06;
  margin: 8px 0;
  color: #0f172a;
  letter-spacing: -0.03em;
}

.simulator-copy p {
  color: #475569;
  line-height: 1.65;
}

.evidence-note {
  margin-top: 18px;
  padding: 16px;
  border-radius: 20px;
  background: #ecfeff;
  border: 1px solid #a5f3fc;
  color: #155e75;
  line-height: 1.55;
  font-weight: 750;
}

.simulator-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 30px;
  padding: 24px;
  box-shadow: 0 24px 70px rgba(15, 23, 42, 0.12);
}

.simulator-score {
  display: grid;
  grid-template-columns: 132px 1fr;
  gap: 18px;
  align-items: center;
  margin-bottom: 22px;
}

.score-ring {
  width: 132px;
  height: 132px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background:
    conic-gradient(#14b8a6 var(--score), #e2e8f0 0);
  position: relative;
  animation: ringPulse 3.5s ease-in-out infinite;
}

.score-ring::after {
  content: "";
  position: absolute;
  inset: 12px;
  border-radius: 999px;
  background: white;
}

.score-ring span {
  position: relative;
  z-index: 1;
  font-size: 42px;
  font-weight: 950;
  color: #0f766e;
}

.simulator-score strong {
  font-size: 24px;
  color: #0f172a;
}

.simulator-score p {
  color: #64748b;
  line-height: 1.5;
}

@keyframes ringPulse {
  0%, 100% { transform: scale(1); filter: drop-shadow(0 0 0 rgba(20,184,166,0)); }
  50% { transform: scale(1.035); filter: drop-shadow(0 0 24px rgba(20,184,166,0.28)); }
}

.simulator-sliders {
  display: grid;
  gap: 18px;
}

.prevention-slider {
  padding: 15px;
  border-radius: 20px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
}

.slider-meta {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  align-items: center;
  margin-bottom: 8px;
}

.slider-meta strong {
  color: #0f172a;
}

.slider-meta span {
  color: #1d4ed8;
  font-weight: 950;
}

.prevention-slider input[type="range"] {
  accent-color: #14b8a6;
}

.prevention-slider small {
  display: block;
  color: #64748b;
  line-height: 1.45;
  margin-top: 8px;
}

.simulator-visual {
  min-height: 420px;
  border-radius: 30px;
  background:
    radial-gradient(circle at center, rgba(20,184,166,0.22), transparent 30%),
    linear-gradient(135deg, #0f172a, #1e3a8a);
  overflow: hidden;
  box-shadow: inset 0 0 70px rgba(255,255,255,0.08);
}

.visual-orb {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 170px;
  height: 170px;
  transform: translate(-50%, -50%);
  border-radius: 999px;
  background:
    radial-gradient(circle at 35% 30%, #ffffff, #93c5fd 38%, #14b8a6 75%);
  box-shadow: 0 0 70px rgba(147,197,253,0.55);
  animation: orbFloat 5s ease-in-out infinite;
}

@keyframes orbFloat {
  0%, 100% { transform: translate(-50%, -50%) translateY(0); }
  50% { transform: translate(-50%, -50%) translateY(-12px); }
}

.floating-stat {
  position: absolute;
  width: 150px;
  padding: 14px;
  border-radius: 20px;
  color: white;
  background: rgba(255,255,255,0.13);
  border: 1px solid rgba(255,255,255,0.20);
  backdrop-filter: blur(14px);
  z-index: 2;
  animation: floatNode 5s ease-in-out infinite;
}

.floating-stat strong,
.floating-stat span {
  display: block;
}

.floating-stat strong {
  font-size: 22px;
}

.floating-stat span {
  margin-top: 4px;
  opacity: 0.82;
  line-height: 1.35;
}

.floating-stat.s1 {
  left: 24px;
  top: 34px;
}

.floating-stat.s2 {
  right: 22px;
  top: 130px;
  animation-delay: .8s;
}

.floating-stat.s3 {
  left: 44px;
  bottom: 40px;
  animation-delay: 1.4s;
}

/* Fix section title overflow */
.section-intro h2 {
  max-width: 980px;
  line-height: 1.08;
  letter-spacing: -0.035em;
}

.feed-intro {
  align-items: start !important;
}

/* Better large cards spacing */
.need-section,
.statistics-section,
.research-feed-section,
.kids-section,
.source-section,
.platform-entry-section {
  scroll-margin-top: 40px;
}

/* Responsive fixes */
@media (max-width: 1100px) {
  .portal-hero {
    grid-template-columns: 1fr !important;
    min-height: auto !important;
  }

  .calm-visual {
    grid-column: 1 !important;
    min-height: 430px !important;
  }

  .prevention-simulator-section {
    grid-template-columns: 1fr;
  }

  .simulator-visual {
    min-height: 330px;
  }
}

@media (max-width: 700px) {
  .portal-hero {
    padding: 92px 24px 96px !important;
  }

  .language-control.landing-lang {
    right: 24px !important;
    top: 22px !important;
  }

  .portal-copy h1 {
    font-size: 40px !important;
  }

  .portal-subtitle {
    font-size: 17px !important;
  }

  .prevention-simulator-section {
    padding: 22px;
    border-radius: 26px;
  }

  .simulator-score {
    grid-template-columns: 1fr;
  }

  .score-ring {
    margin: 0 auto;
  }
}
'''

path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Premium layout fixes and prevention awareness simulator added.")
