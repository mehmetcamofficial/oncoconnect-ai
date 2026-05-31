from pathlib import Path

css_path = Path("frontend/src/App.css")
css = css_path.read_text(encoding="utf-8")

css += r'''

/* Step 21: cleaner Türkiye + Europe map visuals */

/* Top labels */
.map-summary div {
  min-height: 112px;
}

.map-summary strong {
  word-break: normal;
}

/* Better Türkiye silhouette */
.turkiye-pin-map {
  min-height: 600px !important;
  background:
    radial-gradient(circle at 18% 28%, rgba(56,189,248,0.24), transparent 25%),
    radial-gradient(circle at 78% 62%, rgba(20,184,166,0.18), transparent 34%),
    linear-gradient(135deg, #06182f 0%, #0f2d5c 45%, #1e3a8a 100%) !important;
}

.turkiye-pin-map::before {
  left: 5% !important;
  right: 5% !important;
  top: 28% !important;
  height: 40% !important;
  background:
    linear-gradient(135deg, rgba(255,255,255,0.20), rgba(255,255,255,0.08)) !important;
  clip-path: polygon(
    2% 57%, 8% 46%, 16% 43%, 25% 37%, 36% 31%,
    48% 28%, 59% 31%, 69% 36%, 78% 35%, 88% 41%,
    97% 50%, 92% 61%, 82% 63%, 70% 69%, 57% 69%,
    45% 73%, 33% 71%, 23% 67%, 13% 65%, 6% 61%
  ) !important;
  opacity: 0.88;
}

.turkiye-pin-map::after {
  content: "Türkiye map — demo province distribution layer" !important;
}

/* Türkiye pin positions tuned */
.turkiye-pin-map .map-pin {
  transform: translate(-50%, -50%);
}

.turkiye-pin-map .map-pin:hover {
  transform: translate(-50%, -50%) scale(1.9) !important;
}

/* Europe map: override card grid completely */
.europe-bubble-map {
  display: block !important;
  position: relative !important;
  min-height: 600px !important;
  padding: 0 !important;
  overflow: hidden !important;
  border-radius: 30px !important;
  background:
    radial-gradient(circle at 35% 28%, rgba(59,130,246,0.28), transparent 28%),
    radial-gradient(circle at 65% 58%, rgba(20,184,166,0.18), transparent 32%),
    linear-gradient(135deg, #06182f 0%, #0f2d5c 48%, #1e3a8a 100%) !important;
}

.europe-bubble-map::before {
  content: "";
  position: absolute;
  left: 14%;
  right: 10%;
  top: 16%;
  height: 58%;
  background:
    linear-gradient(135deg, rgba(255,255,255,0.18), rgba(255,255,255,0.07));
  border: 1px solid rgba(255,255,255,0.22);
  clip-path: polygon(
    20% 30%, 32% 15%, 48% 17%, 62% 22%, 72% 34%,
    68% 50%, 78% 58%, 70% 72%, 54% 75%, 42% 68%,
    32% 80%, 20% 70%, 25% 56%, 15% 48%
  );
  filter: drop-shadow(0 18px 40px rgba(0,0,0,0.24));
  opacity: 0.82;
}

.europe-bubble-map::after {
  content: "Europe cancer burden map — demo country distribution";
  position: absolute;
  left: 24px;
  bottom: 20px;
  color: rgba(255,255,255,0.78);
  font-weight: 850;
  letter-spacing: 0.02em;
}

.europe-bubble-map .map-pin {
  position: absolute !important;
  width: var(--size) !important;
  height: var(--size) !important;
  min-width: 18px !important;
  min-height: 18px !important;
  padding: 0 !important;
  border-radius: 999px !important;
  background: #38bdf8 !important;
  border: 2px solid rgba(255,255,255,0.9) !important;
  box-shadow:
    0 0 0 8px rgba(56,189,248,0.13),
    0 0 34px rgba(56,189,248,0.72) !important;
  animation: pinPulse 3.2s ease-in-out infinite !important;
  animation-delay: var(--delay) !important;
  z-index: 3;
  transform: translate(-50%, -50%);
}

.europe-bubble-map .map-pin::before {
  display: none !important;
}

.europe-bubble-map .map-pin span,
.europe-bubble-map .map-pin b {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  padding: 5px 8px !important;
  text-align: center !important;
  white-space: nowrap;
  background: rgba(15,23,42,0.92);
  color: white;
  border-radius: 12px;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s ease, transform .2s ease;
  margin-top: 0 !important;
}

.europe-bubble-map .map-pin span {
  bottom: calc(100% + 8px);
  font-size: 12px !important;
  font-weight: 950 !important;
}

.europe-bubble-map .map-pin b {
  top: calc(100% + 8px);
  font-size: 11px !important;
}

.europe-bubble-map .map-pin:hover {
  transform: translate(-50%, -50%) scale(1.75) !important;
  background: #fbbf24 !important;
  z-index: 30;
  box-shadow:
    0 0 0 10px rgba(251,191,36,0.16),
    0 0 38px rgba(251,191,36,0.8) !important;
}

.europe-bubble-map .map-pin:hover span,
.europe-bubble-map .map-pin:hover b {
  opacity: 1;
}

/* Europe approximate country coordinates */
.europe-bubble-map .map-pin:nth-child(1) { left: 68%; top: 68%; }  /* Türkiye */
.europe-bubble-map .map-pin:nth-child(2) { left: 48%; top: 42%; }  /* Germany */
.europe-bubble-map .map-pin:nth-child(3) { left: 39%; top: 52%; }  /* France */
.europe-bubble-map .map-pin:nth-child(4) { left: 50%; top: 63%; }  /* Italy */
.europe-bubble-map .map-pin:nth-child(5) { left: 31%; top: 68%; }  /* Spain */
.europe-bubble-map .map-pin:nth-child(6) { left: 58%; top: 38%; }  /* Poland */
.europe-bubble-map .map-pin:nth-child(7) { left: 44%; top: 39%; }  /* Netherlands */
.europe-bubble-map .map-pin:nth-child(8) { left: 42%; top: 44%; }  /* Belgium */
.europe-bubble-map .map-pin:nth-child(9) { left: 58%; top: 70%; }  /* Greece */
.europe-bubble-map .map-pin:nth-child(10) { left: 27%; top: 70%; } /* Portugal */
.europe-bubble-map .map-pin:nth-child(11) { left: 54%; top: 21%; } /* Sweden */
.europe-bubble-map .map-pin:nth-child(12) { left: 51%; top: 50%; } /* Austria */
.europe-bubble-map .map-pin:nth-child(13) { left: 63%; top: 54%; } /* Romania */
.europe-bubble-map .map-pin:nth-child(14) { left: 63%; top: 62%; } /* Bulgaria */
.europe-bubble-map .map-pin:nth-child(15) { left: 49%; top: 31%; } /* Denmark */
.europe-bubble-map .map-pin:nth-child(16) { left: 31%; top: 38%; } /* Ireland */
.europe-bubble-map .map-pin:nth-child(17) { left: 53%; top: 45%; } /* Czechia */
.europe-bubble-map .map-pin:nth-child(18) { left: 57%; top: 52%; } /* Hungary */

/* Better rank panel spacing */
.map-rank-card {
  align-self: stretch;
}

.rank-row {
  min-height: 72px;
}

.rank-row b {
  white-space: nowrap;
}

/* Responsive */
@media (max-width: 900px) {
  .turkiye-pin-map,
  .europe-bubble-map {
    min-height: 430px !important;
  }

  .europe-bubble-map::after,
  .turkiye-pin-map::after {
    font-size: 12px;
    right: 20px;
  }

  .europe-bubble-map .map-pin,
  .turkiye-pin-map .map-pin {
    width: 14px !important;
    height: 14px !important;
    min-width: 14px !important;
    min-height: 14px !important;
  }
}
'''

css_path.write_text(css, encoding="utf-8")
print("✅ Map visuals fixed: Türkiye and Europe now use animated map-style pins.")
