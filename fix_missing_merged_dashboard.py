from pathlib import Path
import re

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")
css = CSS.read_text(encoding="utf-8")

# 1) Eğer key yanlış şekilde div'e iki kez eklenmişse düzelt
s = s.replace(
    '<div className="landing-merged-intelligence" key={`${landingMetric}-${landingRegion}`}>',
    '<div className="landing-merged-intelligence" key={`${landingMetric}-${landingRegion}-${mergedCancerRows.length}`}>'
)

# 2) merged block var mı kontrol et
if "landing-merged-intelligence" not in s:
    raise SystemExit("❌ landing-merged-intelligence JSX bloğu bulunamadı. Önceki patch eksik uygulanmış.")

# 3) merged rows değişkeni var mı kontrol et
if "const mergedCancerRows" not in s:
    raise SystemExit("❌ const mergedCancerRows bulunamadı. Veri merge bloğu eksik.")

APP.write_text(s, encoding="utf-8")

css_patch = r'''

/* EMERGENCY RESTORE: merged dashboard visibility */

.landing-live-chart {
  min-height: auto !important;
  height: auto !important;
  overflow: visible !important;
  padding: 30px !important;
}

.landing-live-chart::before,
.landing-live-chart::after {
  pointer-events: none !important;
}

.landing-merged-intelligence {
  display: grid !important;
  visibility: visible !important;
  opacity: 1 !important;
  gap: 16px !important;
  min-height: 200px !important;
  margin-top: 18px !important;
  position: relative !important;
  z-index: 20 !important;
}

.merged-data-row {
  display: grid !important;
  visibility: visible !important;
  opacity: 1 !important;
  grid-template-columns: minmax(280px, 0.9fr) minmax(300px, 1fr) 180px !important;
  gap: 18px !important;
  align-items: center !important;
  min-height: 92px !important;
  padding: 18px 20px !important;
  border-radius: 26px !important;
  background: rgba(255,255,255,0.96) !important;
  border: 1px solid #dbeafe !important;
  box-shadow: 0 14px 36px rgba(15,23,42,0.07) !important;
  position: relative !important;
  z-index: 21 !important;
  transform: none !important;
  filter: none !important;
  animation: mergedRowVisible 0.45s ease both !important;
}

@keyframes mergedRowVisible {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.merged-data-main {
  display: block !important;
}

.merged-data-main span {
  display: inline-flex !important;
  margin-bottom: 8px !important;
  padding: 6px 10px !important;
  border-radius: 999px !important;
  background: #e0f2fe !important;
  color: #075985 !important;
  font-size: 11px !important;
  font-weight: 950 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
}

.merged-data-main h4 {
  display: block !important;
  margin: 0 0 5px !important;
  color: #101828 !important;
  font-size: 22px !important;
  line-height: 1.15 !important;
}

.merged-data-main p {
  display: block !important;
  margin: 0 !important;
  color: #64748b !important;
  font-size: 14px !important;
  font-weight: 750 !important;
}

.merged-data-bar {
  display: block !important;
  height: 18px !important;
  border-radius: 999px !important;
  background: #e2e8f0 !important;
  overflow: hidden !important;
}

.merged-data-bar i {
  display: block !important;
  height: 100% !important;
  border-radius: 999px !important;
  background: linear-gradient(90deg, #155eef, #14b8a6, #a5f3fc) !important;
  transform-origin: left center !important;
  animation: mergedEmergencyFill 0.9s cubic-bezier(.2,.8,.2,1) both !important;
  position: relative !important;
}

@keyframes mergedEmergencyFill {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}

.merged-data-bar i b {
  display: block !important;
  position: absolute !important;
  inset: 0 !important;
  width: 40% !important;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.7), transparent) !important;
  animation: mergedEmergencyShine 1.8s linear infinite !important;
}

@keyframes mergedEmergencyShine {
  from { transform: translateX(-120%); }
  to { transform: translateX(300%); }
}

.merged-data-row > strong {
  display: block !important;
  justify-self: end !important;
  color: #101828 !important;
  font-size: 22px !important;
  font-weight: 950 !important;
  opacity: 1 !important;
  visibility: visible !important;
  transform: none !important;
  animation: none !important;
}

/* Eski gizleme kuralları sadece eski class'lara uygulansın */
.landing-live-row,
.landing-official-source-strip,
.landing-official-bars,
.landing-demo-bars-head {
  display: none !important;
}

/* Research Pulse tekrar aşağıda görünsün */
.landing-research-feed,
.landing-research-feed-after {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  position: relative !important;
  z-index: 10 !important;
  margin-top: 26px !important;
}

@media (max-width: 900px) {
  .merged-data-row {
    grid-template-columns: 1fr !important;
  }

  .merged-data-row > strong {
    justify-self: start !important;
  }
}

'''

if "EMERGENCY RESTORE: merged dashboard visibility" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Merged dashboard visibility restored.")
