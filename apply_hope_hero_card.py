from pathlib import Path
import re

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# Hero sağ kartını metne göre bulup class ekle
targets = [
    "Calm, clear and safe guidance",
    "Safe companion",
    "Guidance with warmth, not fear"
]

idx = -1
for t in targets:
    idx = s.find(t)
    if idx != -1:
        break

if idx == -1:
    raise SystemExit("❌ Kart metni bulunamadı.")

# Yakındaki ilk className'i hope-hero-card yap
start = max(0, idx - 1200)
window = s[start:idx]
matches = list(re.finditer(r'className="([^"]*)"', window))

if not matches:
    raise SystemExit("❌ Yakında className bulunamadı.")

m = matches[-1]
old = m.group(1)

if "hope-hero-card" not in old:
    new = old + " hope-hero-card"
    s = s[:start + m.start(1)] + new + s[start + m.end(1):]

app.write_text(s, encoding="utf-8")

patch = r'''

/* Hope sunrise hero card */

.hope-hero-card {
  position: relative !important;
  overflow: hidden !important;
  min-height: 520px !important;
  border-radius: 38px !important;
  isolation: isolate !important;
  background:
    linear-gradient(90deg, rgba(15,23,42,0.08) 0%, rgba(15,23,42,0.36) 52%, rgba(15,23,42,0.68) 100%),
    url("/assets/hope-child-sunrise.png") left center / cover no-repeat !important;
  box-shadow: 0 32px 90px rgba(15,23,42,0.22) !important;
}

.hope-hero-card::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  background:
    radial-gradient(circle at 72% 18%, rgba(255,215,140,0.62), rgba(255,190,90,0.22) 34%, transparent 62%),
    linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.08) 42%, rgba(255,255,255,0.18) 100%);
  animation: hopeSunrisePulse 9s ease-in-out infinite;
  pointer-events: none;
}

.hope-hero-card::after {
  content: "";
  position: absolute;
  top: 46px;
  right: 46px;
  bottom: 46px;
  width: min(48%, 560px);
  z-index: 2;
  border-radius: 34px;
  background: rgba(255,255,255,0.16);
  border: 1px solid rgba(255,255,255,0.35);
  backdrop-filter: blur(18px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.22), 0 24px 70px rgba(15,23,42,0.16);
  pointer-events: none;
}

.hope-hero-card > * {
  position: relative !important;
  z-index: 3 !important;
  margin-left: auto !important;
  max-width: min(46%, 520px) !important;
}

@keyframes hopeSunrisePulse {
  0%, 100% { opacity: .68; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.08); }
}

@media (max-width: 900px) {
  .hope-hero-card {
    background-position: center !important;
  }

  .hope-hero-card::after {
    inset: auto 20px 20px 20px;
    width: auto;
    height: 48%;
  }

  .hope-hero-card > * {
    max-width: none !important;
    margin-left: 0 !important;
  }
}

'''

text = css.read_text(encoding="utf-8")
if "Hope sunrise hero card" not in text:
    css.write_text(text + patch, encoding="utf-8")

print("✅ Hope sunrise card applied.")
