from pathlib import Path
import re

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# Hope companion JSX bloğunu kaldır
s = re.sub(
    r'\n\s*<div className="hope-companion-card">[\s\S]*?</div>\s*</div>\s*</div>',
    '\n',
    s,
    count=1
)

# Daha güvenli ikinci temizleme
s = re.sub(
    r'\n\s*<div className="hope-companion-card">[\s\S]*?</div>\s*',
    '\n',
    s,
    count=1
)

app.write_text(s, encoding="utf-8")

patch = r'''

/* REMOVE broken hope companion card */
.hope-companion-card,
.hope-companion-image,
.hope-companion-copy {
  display: none !important;
}

'''

text = css.read_text(encoding="utf-8")
if "REMOVE broken hope companion card" not in text:
    css.write_text(text + patch, encoding="utf-8")

print("✅ Hope companion card removed.")
