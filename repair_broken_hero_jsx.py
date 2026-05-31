from pathlib import Path

app = Path("frontend/src/App.jsx")
s = app.read_text(encoding="utf-8")

backup = app.with_name("App.BEFORE_HERO_REPAIR.jsx")
backup.write_text(s, encoding="utf-8")

start = s.find('<section className="old-portal-hero">')
if start == -1:
    raise SystemExit("❌ old-portal-hero bulunamadı.")

# Hero section'dan sonraki ilk section'a kadar olan bozuk bölümü değiştir
next_section = s.find('\n      <section', start + 10)
if next_section == -1:
    raise SystemExit("❌ Sonraki section bulunamadı.")

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
              <button onClick={() => setPage("copilot")}>Launch AI Copilot</button>
              <button onClick={() => setPage("map")}>Open Knowledge Graph</button>
              <button onClick={() => setPage("kids")}>Onco Kids</button>
            </div>

            <div className="old-hero-note">
              This platform does not provide diagnosis or treatment advice. It supports doctor-visit
              preparation, trusted source navigation and support coordination.
            </div>
          </div>

          <div className="old-hero-card">
            <div className="hero-orb"></div>
            <h2>Calm, clear and safe guidance</h2>
            <p>
              The goal is not to create fear; it is to prepare better questions,
              surface support needs and give care teams more structured information.
            </p>

            <div className="safe-companion-pill">
              <span>😊</span>
              <div>
                <strong>Safe companion</strong>
                <small>Guidance with warmth, not fear.</small>
              </div>
            </div>
          </div>
        </div>
      </section>'''

s = s[:start] + new_hero + s[next_section:]

# Kötü hope companion kalıntıları varsa gizle/temizle
s = s.replace("hope-companion-card", "hope-companion-card-removed")
s = s.replace("hope-hero-card", "")

app.write_text(s, encoding="utf-8")
print("✅ Broken hero JSX repaired.")
print(f"Backup: {backup}")
