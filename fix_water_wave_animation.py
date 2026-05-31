from pathlib import Path

CSS = Path("frontend/src/App.css")

css_patch = r'''

/* FIX: more realistic water wave, less balloon/blob */

.water-fill-card {
  position: relative !important;
  overflow: hidden !important;
  isolation: isolate !important;
}

.water-fill-card > * {
  position: relative !important;
  z-index: 5 !important;
}

/* Ana su dolum alanı: artık balon değil, düz sıvı katmanı */
.water-fill-card::before {
  content: "";
  position: absolute;
  left: -8%;
  right: -8%;
  bottom: -18%;
  height: 46%;
  z-index: 1;
  border-radius: 0 !important;
  background:
    linear-gradient(
      180deg,
      rgba(186, 230, 253, 0.52) 0%,
      rgba(56, 189, 248, 0.38) 42%,
      rgba(20, 184, 166, 0.28) 100%
    ) !important;
  opacity: 0.72 !important;
  animation:
    realWaterLevel 7s ease-in-out infinite,
    realWaterDrift 5.5s ease-in-out infinite !important;
  pointer-events: none;
  transform: none;
}

/* Dalga yüzeyi: geniş, yatay, su gibi hareket eden layer */
.water-fill-card::after {
  content: "";
  position: absolute;
  left: -55%;
  width: 210%;
  bottom: 26%;
  height: 44px;
  z-index: 2;
  opacity: 0.78 !important;
  pointer-events: none;
  border-radius: 45% 55% 48% 52% / 65% 70% 30% 35% !important;
  background:
    radial-gradient(ellipse at 20% 55%, rgba(255,255,255,0.62) 0%, rgba(255,255,255,0.25) 22%, transparent 48%),
    radial-gradient(ellipse at 48% 45%, rgba(255,255,255,0.48) 0%, rgba(255,255,255,0.18) 26%, transparent 52%),
    radial-gradient(ellipse at 78% 58%, rgba(255,255,255,0.52) 0%, rgba(255,255,255,0.20) 24%, transparent 50%);
  mix-blend-mode: screen;
  animation:
    realWaveMove 4.2s ease-in-out infinite,
    realWaveFloat 6.8s ease-in-out infinite !important;
}

/* Eski blob etkisini kır */
.water-fill-card::before,
.water-fill-card::after {
  filter: none !important;
}

/* Su seviyesi bazen yükselsin/alçalsın */
@keyframes realWaterLevel {
  0%, 100% {
    bottom: -20%;
    height: 44%;
  }

  35% {
    bottom: -11%;
    height: 52%;
  }

  62% {
    bottom: -15%;
    height: 49%;
  }
}

/* Tüm su kütlesi hafif sağa sola aksın */
@keyframes realWaterDrift {
  0%, 100% {
    transform: translateX(-1.5%);
  }

  45% {
    transform: translateX(2.5%);
  }

  70% {
    transform: translateX(-3%);
  }
}

/* Dalga yüzeyi yatay aksın */
@keyframes realWaveMove {
  0%, 100% {
    transform: translateX(-7%) skewX(-2deg);
  }

  40% {
    transform: translateX(6%) skewX(2deg);
  }

  72% {
    transform: translateX(-2%) skewX(-1deg);
  }
}

/* Dalga yukarı/aşağı hafif salınsın */
@keyframes realWaveFloat {
  0%, 100% {
    bottom: 25%;
  }

  50% {
    bottom: 31%;
  }
}

/* Kart içinde ince su çizgisi / shimmer */
.water-fill-card .water-shimmer {
  display: none;
}

/* Renkli kartlarda yazı okunurluğu */
.water-fill-card {
  text-shadow: 0 1px 0 rgba(0,0,0,0.08);
}

/* Kartlar arasında dalga zaman farkı */
.water-fill-card:nth-child(1)::before,
.water-fill-card:nth-child(1)::after {
  animation-delay: 0s, 0s !important;
}

.water-fill-card:nth-child(2)::before,
.water-fill-card:nth-child(2)::after {
  animation-delay: .35s, .6s !important;
}

.water-fill-card:nth-child(3)::before,
.water-fill-card:nth-child(3)::after {
  animation-delay: .75s, 1s !important;
}

.water-fill-card:nth-child(4)::before,
.water-fill-card:nth-child(4)::after {
  animation-delay: 1.1s, 1.4s !important;
}

/* Hover'da dalga hızlansın ama bloblaşmasın */
.water-fill-card:hover::before {
  opacity: 0.82 !important;
  animation-duration: 5s, 3.8s !important;
}

.water-fill-card:hover::after {
  opacity: 0.95 !important;
  animation-duration: 2.7s, 4.2s !important;
}

'''

css = CSS.read_text(encoding="utf-8")
if "FIX: more realistic water wave" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Water animation changed from blob/bubble to wave-like liquid fill.")
