from pathlib import Path

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")

# Metric/region değişince merged chart yeniden mount olsun
s = s.replace(
    '<div className="landing-merged-intelligence">',
    '<div className="landing-merged-intelligence" key={`${landingMetric}-${landingRegion}`}>',
    1
)

# Her merged row'a gecikme zaten varsa dokunma; yoksa ekle
s = s.replace(
    '''className={`merged-data-row ${row.sourceType}`}
                  key={`${row.sourceType}-${row.label}-${index}`}
                  style={{ animationDelay: `${index * 0.055}s` }}''',
    '''className={`merged-data-row ${row.sourceType}`}
                  key={`${landingMetric}-${landingRegion}-${row.sourceType}-${row.label}-${index}`}
                  style={{
                    animationDelay: `${index * 0.075}s`,
                    "--row-delay": `${index * 0.075}s`
                  }}''',
    1
)

APP.write_text(s, encoding="utf-8")

css_patch = r'''

/* FINAL classy animated merged data bars */

.landing-merged-intelligence {
  display: grid !important;
  gap: 16px !important;
}

.merged-data-row {
  opacity: 0 !important;
  transform: translateY(18px) scale(0.985) !important;
  animation: mergedRowReveal 0.58s cubic-bezier(.2,.85,.2,1) forwards !important;
  animation-delay: var(--row-delay, 0s) !important;
  transition:
    transform 0.22s ease,
    box-shadow 0.22s ease,
    border-color 0.22s ease,
    background 0.22s ease !important;
}

@keyframes mergedRowReveal {
  0% {
    opacity: 0;
    transform: translateY(18px) scale(0.985);
    filter: blur(3px);
  }
  60% {
    opacity: 1;
    transform: translateY(-2px) scale(1.006);
    filter: blur(0);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
}

.merged-data-row:hover {
  transform: translateY(-3px) scale(1.004) !important;
  border-color: rgba(20,184,166,0.35) !important;
  box-shadow:
    0 22px 52px rgba(15,23,42,0.10),
    0 0 0 1px rgba(20,184,166,0.08) !important;
}

.merged-data-bar {
  height: 18px !important;
  background:
    linear-gradient(90deg, rgba(226,232,240,0.95), rgba(241,245,249,0.95)) !important;
  box-shadow: inset 0 1px 2px rgba(15,23,42,0.06);
}

.merged-data-bar i {
  transform-origin: left center !important;
  animation:
    mergedBarFill 1.05s cubic-bezier(.16,.9,.24,1) both,
    mergedBarGlow 2.6s ease-in-out infinite !important;
  animation-delay:
    calc(var(--row-delay, 0s) + 0.18s),
    calc(var(--row-delay, 0s) + 1.1s) !important;
  box-shadow:
    0 0 18px rgba(20,184,166,0.25),
    inset 0 1px 0 rgba(255,255,255,0.35);
}

@keyframes mergedBarFill {
  from {
    transform: scaleX(0);
    filter: brightness(1.35) saturate(1.25);
  }
  to {
    transform: scaleX(1);
    filter: brightness(1) saturate(1);
  }
}

@keyframes mergedBarGlow {
  0%, 100% {
    box-shadow:
      0 0 12px rgba(20,184,166,0.18),
      inset 0 1px 0 rgba(255,255,255,0.28);
  }
  50% {
    box-shadow:
      0 0 26px rgba(34,211,238,0.34),
      inset 0 1px 0 rgba(255,255,255,0.42);
  }
}

.merged-data-bar i b {
  width: 42% !important;
  background:
    linear-gradient(90deg, transparent, rgba(255,255,255,0.82), transparent) !important;
  animation: mergedShineRun 1.9s linear infinite !important;
  animation-delay: calc(var(--row-delay, 0s) + 0.75s) !important;
}

@keyframes mergedShineRun {
  from {
    transform: translateX(-130%);
  }
  to {
    transform: translateX(330%);
  }
}

.merged-data-row > strong {
  animation: mergedValuePop 0.5s ease forwards !important;
  animation-delay: calc(var(--row-delay, 0s) + 0.48s) !important;
  opacity: 0;
}

@keyframes mergedValuePop {
  from {
    opacity: 0;
    transform: translateX(10px) scale(0.92);
  }
  to {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
}

.merged-data-main span {
  animation: mergedBadgePulse 2.8s ease-in-out infinite;
  animation-delay: var(--row-delay, 0s);
}

@keyframes mergedBadgePulse {
  0%, 100% {
    box-shadow: 0 0 0 rgba(20,184,166,0);
  }
  50% {
    box-shadow: 0 0 22px rgba(20,184,166,0.16);
  }
}

/* subtle moving background only inside the chart */
.landing-live-chart {
  position: relative !important;
  overflow: hidden !important;
}

.landing-live-chart::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(120deg, transparent 0%, rgba(34,211,238,0.08) 38%, transparent 68%);
  transform: translateX(-100%);
  animation: mergedChartScan 7s linear infinite;
  pointer-events: none;
}

@keyframes mergedChartScan {
  from { transform: translateX(-110%); }
  to { transform: translateX(110%); }
}

.landing-live-chart > * {
  position: relative;
  z-index: 2;
}

'''

css = CSS.read_text(encoding="utf-8")
if "FINAL classy animated merged data bars" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Merged data bars now animate with delayed fill, shine and hover effects.")
