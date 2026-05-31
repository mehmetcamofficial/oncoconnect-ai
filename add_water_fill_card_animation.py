from pathlib import Path
import re

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")

anchors = [
    "~20M",
    "~9.7M",
    "Türkiye context",
    "EU Cancer Mission"
]

# İlgili kartların className alanına water-fill-card ekle
for anchor in anchors:
    idx = s.find(anchor)
    if idx == -1:
        print(f"⚠️ Anchor bulunamadı: {anchor}")
        continue

    window_start = max(0, idx - 1000)
    window = s[window_start:idx]

    matches = list(re.finditer(r'className="([^"]+)"', window))
    if not matches:
        print(f"⚠️ className bulunamadı: {anchor}")
        continue

    last = matches[-1]
    old_class = last.group(1)

    if "water-fill-card" in old_class:
        continue

    new_class = old_class + " water-fill-card"
    abs_start = window_start + last.start(1)
    abs_end = window_start + last.end(1)

    s = s[:abs_start] + new_class + s[abs_end:]
    print(f"✅ water-fill-card added near: {anchor}")

APP.write_text(s, encoding="utf-8")

css_patch = r'''

/* Water fill animation for cancer burden cards */

.water-fill-card {
  position: relative !important;
  overflow: hidden !important;
  isolation: isolate !important;
}

.water-fill-card > * {
  position: relative;
  z-index: 3;
}

.water-fill-card::before {
  content: "";
  position: absolute;
  left: -18%;
  right: -18%;
  bottom: -42%;
  height: 62%;
  z-index: 1;
  background:
    radial-gradient(circle at 25% 18%, rgba(255,255,255,0.28), transparent 22%),
    linear-gradient(135deg, rgba(125,211,252,0.42), rgba(20,184,166,0.28));
  border-radius: 42% 48% 35% 46%;
  animation:
    waterRise 7.5s ease-in-out infinite,
    waterSway 4.8s ease-in-out infinite;
  opacity: 0.78;
  pointer-events: none;
}

.water-fill-card::after {
  content: "";
  position: absolute;
  left: -35%;
  right: -35%;
  bottom: 18%;
  height: 90px;
  z-index: 2;
  background:
    radial-gradient(ellipse at center, rgba(255,255,255,0.26), rgba(255,255,255,0.06) 38%, transparent 70%);
  border-radius: 50%;
  animation: waterWave 3.8s ease-in-out infinite;
  opacity: 0.62;
  pointer-events: none;
  mix-blend-mode: screen;
}

@keyframes waterRise {
  0%, 100% {
    bottom: -46%;
    height: 58%;
  }

  45% {
    bottom: -31%;
    height: 72%;
  }

  70% {
    bottom: -37%;
    height: 66%;
  }
}

@keyframes waterSway {
  0%, 100% {
    transform: translateX(-2%) rotate(-1deg);
  }

  35% {
    transform: translateX(4%) rotate(1.4deg);
  }

  65% {
    transform: translateX(-5%) rotate(-1.2deg);
  }
}

@keyframes waterWave {
  0%, 100% {
    transform: translateX(-8%) translateY(0) scaleX(1.05);
  }

  35% {
    transform: translateX(10%) translateY(-8px) scaleX(1.14);
  }

  70% {
    transform: translateX(-3%) translateY(5px) scaleX(0.96);
  }
}

/* farklı kartlarda dalga zamanlaması farklı olsun */
.water-fill-card:nth-child(2)::before,
.water-fill-card:nth-child(2)::after {
  animation-delay: .45s;
}

.water-fill-card:nth-child(3)::before,
.water-fill-card:nth-child(3)::after {
  animation-delay: .9s;
}

.water-fill-card:nth-child(4)::before,
.water-fill-card:nth-child(4)::after {
  animation-delay: 1.25s;
}

/* hover'da su biraz daha canlı aksın */
.water-fill-card:hover::before {
  animation-duration: 4.6s, 2.8s;
  opacity: 0.92;
}

.water-fill-card:hover::after {
  animation-duration: 2.2s;
  opacity: 0.8;
}

'''

css = CSS.read_text(encoding="utf-8")
if "Water fill animation for cancer burden cards" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Water fill animation added to burden/stat cards.")
