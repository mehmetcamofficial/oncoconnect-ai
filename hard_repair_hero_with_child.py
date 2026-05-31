from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

backup = app.with_name("App.BEFORE_CHILD_HERO_HARD_REPAIR.jsx")
backup.write_text(s, encoding="utf-8")

start = s.find('<section className="old-portal-hero">')
end = s.find('<section id="what-is-it"', start)

if start == -1:
    raise SystemExit("❌ old-portal-hero bulunamadı.")
if end == -1:
    raise SystemExit("❌ what-is-it section bulunamadı.")

new_hero = r'''<section className="old-portal-hero">
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
              <button type="button" onClick={() => setPage("graph")}>Open Knowledge Graph</button>
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
                Guidance with warmth, not fear — helping children, families and care teams
                feel supported before the next step.
              </p>
            </div>
          </div>
        </div>
      </section>

      '''

s = s[:start] + new_hero + s[end:]

app.write_text(s, encoding="utf-8")

patch = r'''

/* FINAL CLEAN CHILD HERO CARD */
.old-hero-content {
  display: grid !important;
  grid-template-columns: minmax(0, 1.05fr) minmax(430px, .86fr) !important;
  gap: 56px !important;
  align-items: center !important;
}

.child-hope-hero-card {
  position: relative !important;
  min-height: 560px !important;
  border-radius: 40px !important;
  overflow: hidden !important;
  background:
    linear-gradient(180deg, rgba(15,23,42,0.00), rgba(15,23,42,0.50)),
    url("/assets/hope-child-sunrise.png") center / cover no-repeat !important;
  border: 1px solid rgba(255,255,255,0.34) !important;
  box-shadow: 0 34px 100px rgba(15,23,42,0.28) !important;
}

.child-hope-hero-card::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 78% 16%, rgba(255,220,140,.55), transparent 36%),
    linear-gradient(180deg, rgba(15,23,42,0.02) 0%, rgba(15,23,42,0.60) 100%);
  pointer-events: none;
}

.child-hope-overlay {
  position: absolute !important;
  left: 28px !important;
  right: 28px !important;
  bottom: 28px !important;
  padding: 24px !important;
  border-radius: 28px !important;
  background: rgba(15,23,42,0.46) !important;
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
  margin: 10px 0 10px !important;
  color: white !important;
  font-size: 34px !important;
  line-height: 1.05 !important;
}

.child-hope-overlay p {
  margin: 0 !important;
  color: rgba(255,255,255,.88) !important;
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

@media (max-width: 1000px) {
  .old-hero-content {
    grid-template-columns: 1fr !important;
  }

  .child-hope-hero-card {
    min-height: 460px !important;
  }
}

'''

text = css.read_text(encoding="utf-8")
if "FINAL CLEAN CHILD HERO CARD" not in text:
    css.write_text(text + patch, encoding="utf-8")

print("✅ Hero repaired and child image card inserted.")
print(f"Backup saved: {backup}")
