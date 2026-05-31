from pathlib import Path

css_path = Path("frontend/src/App.css")
css = css_path.read_text(encoding="utf-8")

css += r'''

/* Step 26: premium stable map pins */

.turkiye-pin-map,
.europe-bubble-map,
.image-pin-map {
  min-height: 560px !important;
}

/* Pinleri küçült, sabitle, daha az göz yorsun */
.turkiye-pin-map .map-pin,
.europe-bubble-map .map-pin,
.image-pin-map .map-pin {
  width: 18px !important;
  height: 18px !important;
  min-width: 18px !important;
  min-height: 18px !important;
  border: 2px solid rgba(255,255,255,0.95) !important;
  background: #38bdf8 !important;
  box-shadow:
    0 0 0 5px rgba(56,189,248,0.13),
    0 0 18px rgba(56,189,248,0.55) !important;
  animation: subtlePinPulse 5.5s ease-in-out infinite !important;
}

/* Büyük veri noktaları sadece biraz büyüsün */
.turkiye-pin-map .map-pin:nth-child(6),
.turkiye-pin-map .map-pin:nth-child(34),
.turkiye-pin-map .map-pin:nth-child(35),
.turkiye-pin-map .map-pin:nth-child(16),
.turkiye-pin-map .map-pin:nth-child(7) {
  width: 25px !important;
  height: 25px !important;
}

/* Hover ve selected daha kontrollü */
.turkiye-pin-map .map-pin:hover,
.europe-bubble-map .map-pin:hover,
.image-pin-map .map-pin:hover {
  transform: translate(-50%, -50%) scale(1.35) !important;
  background: #fbbf24 !important;
  z-index: 80 !important;
}

.turkiye-pin-map .map-pin.selected,
.europe-bubble-map .map-pin.selected,
.image-pin-map .map-pin.selected {
  width: 32px !important;
  height: 32px !important;
  background: #fbbf24 !important;
  transform: translate(-50%, -50%) scale(1) !important;
  z-index: 90 !important;
  box-shadow:
    0 0 0 10px rgba(251,191,36,0.18),
    0 0 34px rgba(251,191,36,0.78) !important;
}

/* Etiketler sadece hover/selected olduğunda görünsün */
.turkiye-pin-map .map-pin span,
.turkiye-pin-map .map-pin b,
.europe-bubble-map .map-pin span,
.europe-bubble-map .map-pin b,
.image-pin-map .map-pin span,
.image-pin-map .map-pin b {
  opacity: 0 !important;
}

.turkiye-pin-map .map-pin:hover span,
.turkiye-pin-map .map-pin:hover b,
.turkiye-pin-map .map-pin.selected span,
.turkiye-pin-map .map-pin.selected b,
.europe-bubble-map .map-pin:hover span,
.europe-bubble-map .map-pin:hover b,
.europe-bubble-map .map-pin.selected span,
.europe-bubble-map .map-pin.selected b,
.image-pin-map .map-pin:hover span,
.image-pin-map .map-pin:hover b,
.image-pin-map .map-pin.selected span,
.image-pin-map .map-pin.selected b {
  opacity: 1 !important;
}

/* Daha sakin animasyon */
@keyframes subtlePinPulse {
  0%, 100% {
    opacity: .82;
    box-shadow:
      0 0 0 4px rgba(56,189,248,0.10),
      0 0 16px rgba(56,189,248,0.45);
  }
  50% {
    opacity: 1;
    box-shadow:
      0 0 0 7px rgba(56,189,248,0.16),
      0 0 24px rgba(56,189,248,0.62);
  }
}

/* Bilgi kartını biraz daha kompakt ve okunabilir yap */
.map-floating-detail-v25 {
  width: min(330px, calc(100% - 48px)) !important;
  padding: 18px !important;
  border-radius: 24px !important;
}

.map-floating-detail-v25 h3 {
  font-size: 26px !important;
}

.floating-detail-grid {
  grid-template-columns: 1fr 1fr !important;
  gap: 8px !important;
}

.floating-detail-grid div {
  padding: 10px !important;
}

.floating-detail-grid strong {
  font-size: 18px !important;
}

.floating-breakdown p {
  padding: 7px 9px !important;
}

/* Harita açıklaması kartın altında kalmasın */
.map-caption {
  max-width: 60%;
  font-size: 15px !important;
}

@media (max-width: 900px) {
  .turkiye-pin-map .map-pin,
  .europe-bubble-map .map-pin,
  .image-pin-map .map-pin {
    width: 13px !important;
    height: 13px !important;
    min-width: 13px !important;
    min-height: 13px !important;
  }

  .map-floating-detail-v25 {
    width: auto !important;
    left: 16px !important;
    right: 16px !important;
  }
}
'''

css_path.write_text(css, encoding="utf-8")
print("✅ Step 26 applied: map pins refined, motion reduced, detail card compact.")
