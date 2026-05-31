from pathlib import Path
import re

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# Sağ kart içeriğini temiz ve görselli hale getir
pattern = re.compile(
    r'<div className="old-hero-card">[\s\S]*?</div>\s*</div>\s*</div>',
    re.MULTILINE
)

new_card = r'''<div className="old-hero-card child-hope-hero-card">
            <div className="child-hope-overlay">
              <span>Safe companion</span>
              <h2>Calm, clear and hopeful guidance</h2>
              <p>
                Guidance with warmth, not fear — helping children, families and care teams
                feel supported before the next step.
              </p>
            </div>
          </div>
        </div>'''

if pattern.search(s):
    s = pattern.sub(new_card, s, count=1)
else:
    raise SystemExit("❌ old-hero-card bloğu bulunamadı.")

app.write_text(s, encoding="utf-8")

patch = r'''

/* FINAL: child image inside hero right card */
.old-hero-content {
  display: grid !important;
  grid-template-columns: minmax(0, 1.05fr) minmax(460px, .9fr) !important;
  gap: 56px !important;
  align-items: center !important;
}

.child-hope-hero-card {
  position: relative !important;
  min-height: 560px !important;
  border-radius: 40px !important;
  overflow: hidden !important;
  background:
    linear-gradient(180deg, rgba(15,23,42,0.06), rgba(15,23,42,0.42)),
    url("/assets/hope-child-sunrise.png") center / cover no-repeat !important;
  border: 1px solid rgba(255,255,255,0.32) !important;
  box-shadow: 0 34px 100px rgba(15,23,42,0.28) !important;
}

.child-hope-hero-card::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 72% 18%, rgba(255,220,140,.55), transparent 36%),
    linear-gradient(180deg, transparent 35%, rgba(15,23,42,.55) 100%);
  pointer-events: none;
}

.child-hope-overlay {
  position: absolute !important;
  left: 30px !important;
  right: 30px !important;
  bottom: 30px !important;
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
if "FINAL: child image inside hero right card" not in text:
    css.write_text(text + patch, encoding="utf-8")

print("✅ Çocuk görseli sağ hero karta yerleştirildi.")
