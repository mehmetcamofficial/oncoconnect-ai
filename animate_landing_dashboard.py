from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# 1) Switchlerden sonra canlı sinyal şeridi ekle
old = '''        <div className="landing-live-grid">
          <div className="landing-live-chart">'''

new = '''        <div className="landing-live-signal">
          <span>Live data stream</span>
          <div>
            <i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i>
          </div>
          <b>{landingRegion === "turkiye" ? "Türkiye city layer" : "Europe country layer"} · {metricLabel[landingMetric]}</b>
        </div>

        <div className="landing-live-grid" key={`${landingRegion}-${landingMetric}`}>
          <div className="landing-live-chart">'''

if old in s:
    s = s.replace(old, new, 1)
else:
    print("⚠️ landing-live-grid marker bulunamadı; sadece CSS animasyonları eklenecek.")

# 2) Row animasyon gecikmesi ekle
old = '''                <div className="landing-live-row" key={row.area}>'''

new = '''                <div
                  className="landing-live-row"
                  key={row.area}
                  style={{ animationDelay: `${index * 0.055}s` }}
                >'''

if old in s:
    s = s.replace(old, new, 1)

# 3) Bar içine canlı ışık ekle
old = '''                  <i style={{ width: `${width}%` }}></i>'''

new = '''                  <i style={{ width: `${width}%` }}><span></span></i>'''

if old in s:
    s = s.replace(old, new, 1)

app.write_text(s, encoding="utf-8")

css_patch = r'''

/* LIVE ANIMATION UPGRADE FOR LANDING DATA DASHBOARD */

.landing-live-data {
  position: relative !important;
  overflow: hidden !important;
}

.landing-live-data::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(120deg, transparent 0%, rgba(34,211,238,0.10) 35%, transparent 70%);
  transform: translateX(-100%);
  animation: landingDataScan 5.5s linear infinite;
  pointer-events: none;
}

@keyframes landingDataScan {
  0% { transform: translateX(-110%); }
  100% { transform: translateX(110%); }
}

.landing-live-head,
.landing-live-switches,
.landing-live-signal,
.landing-live-grid {
  position: relative;
  z-index: 2;
}

.landing-live-switches button {
  transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease !important;
}

.landing-live-switches button:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 18px 44px rgba(21,94,239,0.20);
}

.landing-live-switches button.active {
  animation: activeMetricPulse 1.8s ease-in-out infinite;
}

@keyframes activeMetricPulse {
  0%, 100% {
    box-shadow: 0 14px 34px rgba(21,94,239,0.22);
  }
  50% {
    box-shadow: 0 22px 56px rgba(20,184,166,0.34);
  }
}

.landing-live-signal {
  margin-top: 22px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 16px;
  padding: 14px 18px;
  border-radius: 999px;
  background: rgba(15,23,42,0.92);
  border: 1px solid rgba(125,211,252,0.26);
  color: white;
  box-shadow: 0 22px 70px rgba(15,23,42,0.16);
  overflow: hidden;
}

.landing-live-signal > span {
  color: #a5f3fc;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.18em;
  white-space: nowrap;
}

.landing-live-signal > b {
  color: rgba(255,255,255,0.86);
  font-size: 13px;
  white-space: nowrap;
}

.landing-live-signal div {
  position: relative;
  height: 16px;
  overflow: hidden;
  border-radius: 999px;
  background: rgba(255,255,255,0.06);
}

.landing-live-signal div::before {
  content: "";
  position: absolute;
  left: -20%;
  top: 0;
  width: 20%;
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, transparent, rgba(34,211,238,0.9), transparent);
  animation: signalSweep 1.6s linear infinite;
}

@keyframes signalSweep {
  from { left: -20%; }
  to { left: 110%; }
}

.landing-live-signal i {
  position: absolute;
  top: 50%;
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: #22d3ee;
  box-shadow: 0 0 18px rgba(34,211,238,0.95);
  transform: translateY(-50%);
  animation: signalDot 2.8s linear infinite;
}

.landing-live-signal i:nth-child(1) { left: 8%; animation-delay: 0s; }
.landing-live-signal i:nth-child(2) { left: 18%; animation-delay: .2s; }
.landing-live-signal i:nth-child(3) { left: 31%; animation-delay: .45s; }
.landing-live-signal i:nth-child(4) { left: 44%; animation-delay: .7s; }
.landing-live-signal i:nth-child(5) { left: 58%; animation-delay: .95s; }
.landing-live-signal i:nth-child(6) { left: 70%; animation-delay: 1.2s; }
.landing-live-signal i:nth-child(7) { left: 83%; animation-delay: 1.45s; }
.landing-live-signal i:nth-child(8) { left: 94%; animation-delay: 1.7s; }

@keyframes signalDot {
  0%, 100% {
    opacity: 0.25;
    transform: translateY(-50%) scale(0.65);
  }
  50% {
    opacity: 1;
    transform: translateY(-50%) scale(1.25);
  }
}

.landing-live-chart {
  position: relative !important;
  overflow: hidden !important;
}

.landing-live-chart::after {
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 15% 20%, rgba(34,211,238,0.10), transparent 30%),
    radial-gradient(circle at 90% 70%, rgba(124,58,237,0.08), transparent 30%);
  pointer-events: none;
}

.landing-live-chart-title {
  position: relative;
  z-index: 2;
}

.landing-live-row {
  position: relative;
  z-index: 2;
  opacity: 0;
  animation: liveRowSlideIn 0.46s cubic-bezier(.2,.8,.2,1) forwards !important;
}

@keyframes liveRowSlideIn {
  from {
    opacity: 0;
    transform: translateX(-18px) scale(0.985);
  }
  to {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
}

.landing-live-row:hover {
  background: #eef4ff;
  border-radius: 18px;
  padding-left: 12px;
  padding-right: 12px;
  transition: all 0.18s ease;
}

.landing-live-row > b {
  animation: rankPulse 2.4s ease-in-out infinite;
}

@keyframes rankPulse {
  0%, 100% {
    box-shadow: 0 0 0 0 rgba(21,94,239,0.0);
  }
  50% {
    box-shadow: 0 0 0 8px rgba(21,94,239,0.08);
  }
}

.landing-live-row i {
  position: relative;
  overflow: hidden;
  transform-origin: left center;
  animation: barGrowLive 0.8s cubic-bezier(.2,.8,.2,1) both;
}

@keyframes barGrowLive {
  from {
    transform: scaleX(0);
    filter: brightness(1.4);
  }
  to {
    transform: scaleX(1);
    filter: brightness(1);
  }
}

.landing-live-row i span {
  position: absolute;
  inset: 0;
  width: 38%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.55), transparent);
  transform: translateX(-120%);
  animation: barLightRun 1.7s linear infinite;
}

@keyframes barLightRun {
  from { transform: translateX(-120%); }
  to { transform: translateX(280%); }
}

.landing-live-row em {
  animation: valuePop 0.55s ease both;
}

@keyframes valuePop {
  from {
    opacity: 0;
    transform: scale(0.85);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.landing-live-side {
  position: relative !important;
  overflow: hidden !important;
}

.landing-live-side::before {
  content: "";
  position: absolute;
  width: 220px;
  height: 220px;
  right: -80px;
  top: -80px;
  border-radius: 999px;
  background: radial-gradient(circle, rgba(34,211,238,0.18), transparent 70%);
  animation: sideGlowFloat 3.8s ease-in-out infinite;
}

@keyframes sideGlowFloat {
  0%, 100% { transform: scale(0.9); opacity: 0.55; }
  50% { transform: scale(1.12); opacity: 1; }
}

.landing-live-side > * {
  position: relative;
  z-index: 2;
}

.landing-live-side div strong {
  animation: numberGlow 2.2s ease-in-out infinite;
}

@keyframes numberGlow {
  0%, 100% {
    text-shadow: 0 0 0 rgba(21,94,239,0);
  }
  50% {
    text-shadow: 0 0 18px rgba(21,94,239,0.28);
  }
}

@media (max-width: 720px) {
  .landing-live-signal {
    grid-template-columns: 1fr;
    border-radius: 24px;
  }

  .landing-live-signal > b {
    white-space: normal;
  }
}

'''

css.write_text(css.read_text(encoding="utf-8") + css_patch, encoding="utf-8")
print("✅ Landing dashboard live animations upgraded.")
