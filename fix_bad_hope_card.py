from pathlib import Path
import re

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# Yanlış eklenen hope-hero-card classlarını kaldır
s = s.replace(" hope-hero-card", "").replace("hope-hero-card ", "").replace("hope-hero-card", "")
app.write_text(s, encoding="utf-8")

patch = r'''

/* RESET broken hope card experiment */
.hope-hero-card,
.hope-hero-card::before,
.hope-hero-card::after {
  all: unset !important;
}

/* Soft image layer for the existing calm guidance card */
.hero-safe-card,
.safe-guidance-card,
.guidance-card {
  position: relative;
}

/* Disable accidental huge glass/pillar effect */
.hope-hero-card::before,
.hope-hero-card::after {
  display: none !important;
}

'''

text = css.read_text(encoding="utf-8")
if "RESET broken hope card experiment" not in text:
    css.write_text(text + patch, encoding="utf-8")

print("✅ Kötü hope-card denemesi temizlendi.")
