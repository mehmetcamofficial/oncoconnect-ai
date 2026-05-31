from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")
app.with_name("App.SAFE_BACKUP_BEFORE_ONLY_HERO_REPAIR.jsx").write_text(s, encoding="utf-8")

start = s.find('<section className="old-portal-hero">')
end = s.find('<section id="what-is-it"', start)

if start == -1 or end == -1:
    raise SystemExit("❌ Hero sınırı bulunamadı. App.jsx içinde old-portal-hero veya what-is-it yok.")

hero = r'''<section className="old-portal-hero">
        <div className="old-hero-content">
          <div className="old-hero-left">
            <p className="eyebrow">ONCOCONNECT AI PUBLIC PORTAL</p>
            <h1>Safe cancer support, research awareness and AI guidance</h1>
            <p className="old-hero-subtitle">
              A two-layer platform for patients, caregivers, clinicians, researchers and NGOs:
              first trusted information, then AI Copilot and Splunk-powered operational monitoring.
            </p>

            <div className="old-hero-actions">
              <button type="button" onClick={() => setPage("copilot")}>Launch AI Copilot</button>
              <button type="button" onClick={() => setPage("map")}>Open Knowledge Graph</button>
              <button type="button" onClick={() => setPage("kids")}>Onco Kids</button>
            </div>

            <div className="old-hero-note">
              This platform does not provide diagnosis or treatment advice. It supports doctor-visit
              preparation, trusted source navigation and support coordination.
            </div>
          </div>

          <div className="old-hero-card child-hope-hero-card">
            <div className="child-hope-overlay">
              <span>Safe companion</span>
              <h2>Calm, clear and hopeful guidance</h2>
              <p>
                Guidance with warmth, not fear — helping children, families and care teams feel supported.
              </p>
            </div>
          </div>
        </div>
      </section>

      '''

s = s[:start] + hero + s[end:]
app.write_text(s, encoding="utf-8")

patch = r'''

/* HERO STABLE REPAIR - keep all other features */
.old-portal-hero {
  min-height: 860px !important;
  padding: 110px 5vw 80px !important;
}

.old-portal-hero > .old-hero-content {
  width: 100% !important;
  max-width: 1680px !important;
  margin: 0 auto !important;
  display: grid !important;
  grid-template-columns: minmax(620px, 1.05fr) minmax(520px, .85fr) !important;
  gap: 70px !important;
  align-items: center !important;
}

.old-hero-left {
  min-width: 0 !important;
}

.old-hero-left h1 {
  max-width: 900px !important;
  font-size: clamp(58px, 6vw, 104px) !important;
  line-height: .96 !important;
  letter-spacing: -0.06em !important;
}

.old-hero-subtitle {
  max-width: 900px !important;
  font-size: 22px !important;
  line-height: 1.45 !important;
}

.child-hope-hero-card {
  position: relative !important;
  min-height: 560px !important;
  border-radius: 40px !important;
  overflow: hidden !important;
  background:
    linear-gradient(180deg, rgba(15,23,42,0.02), rgba(15,23,42,0.56)),
    url("/assets/hope-child-sunrise.png") center / cover no-repeat !important;
  border: 1px solid rgba(255,255,255,0.34) !important;
  box-shadow: 0 34px 100px rgba(15,23,42,0.28) !important;
}

.child-hope-hero-card::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 76% 18%, rgba(255,220,140,.52), transparent 36%),
    linear-gradient(180deg, transparent 40%, rgba(15,23,42,.64) 100%);
  pointer-events: none;
}

.child-hope-overlay {
  position: absolute !important;
  left: 28px !important;
  right: 28px !important;
  bottom: 28px !important;
  padding: 24px !important;
  border-radius: 28px !important;
  background: rgba(15,23,42,0.50) !important;
  border: 1px solid rgba(255,255,255,0.28) !important;
  backdrop-filter: blur(14px) !important;
  color: white !important;
}

.child-hope-overlay span {
  color: #a5f3fc !important;
  font-size: 12px !important;
  font-weight: 950 !important;
  letter-spacing: .16em !important;
  text-transform: uppercase !important;
}

.child-hope-overlay h2 {
  margin: 10px 0 !important;
  color: white !important;
  font-size: 34px !important;
  line-height: 1.05 !important;
}

.child-hope-overlay p {
  margin: 0 !important;
  color: rgba(255,255,255,.9) !important;
  font-size: 17px !important;
  line-height: 1.5 !important;
  font-weight: 700 !important;
}

.safe-companion-pill,
.hero-orb,
.hope-companion-card,
.hope-companion-image,
.hope-companion-copy {
  display: none !important;
}

@media (max-width: 1100px) {
  .old-portal-hero > .old-hero-content {
    grid-template-columns: 1fr !important;
  }

  .child-hope-hero-card {
    min-height: 460px !important;
  }
}
'''

text = css.read_text(encoding="utf-8")
if "HERO STABLE REPAIR - keep all other features" not in text:
    css.write_text(text + patch, encoding="utf-8")

print("✅ Sadece hero tamir edildi. Diğer eklenen bölümlere dokunulmadı.")
