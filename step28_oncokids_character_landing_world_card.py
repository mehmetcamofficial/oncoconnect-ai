from pathlib import Path

css_path = Path("frontend/src/App.css")
css = css_path.read_text(encoding="utf-8")

css += r'''

/* Step 28: OncoKids animated companion + landing world card visual */

/* OncoKids sağ tarafı güçlü karakter alanı */
.character-stage {
  display: block !important;
  position: relative !important;
  min-height: 520px !important;
  border-radius: 42px !important;
  overflow: hidden !important;
  background:
    radial-gradient(circle at 50% 22%, rgba(255,255,255,0.95), transparent 24%),
    linear-gradient(180deg, rgba(186,230,253,0.78), rgba(254,243,199,0.74)) !important;
  border: 1px solid rgba(255,255,255,0.92) !important;
  box-shadow: 0 28px 90px rgba(15,23,42,0.14) !important;
}

/* Eski pseudo yazıları baskıla */
.character-stage::after {
  content: "Hi, I am Lumi. Let’s collect hope points together." !important;
  left: 38px !important;
  right: 38px !important;
  bottom: 32px !important;
  padding: 18px 22px !important;
  border-radius: 26px !important;
  background: rgba(255,255,255,0.86) !important;
  color: #7c2d12 !important;
  font-weight: 950 !important;
  font-size: 18px !important;
  text-align: center !important;
}

/* Büyük çizgi karakter */
.character-stage::before {
  content: "😊" !important;
  position: absolute !important;
  left: 50% !important;
  top: 43% !important;
  transform: translate(-50%, -50%) !important;
  width: 190px !important;
  height: 190px !important;
  display: grid !important;
  place-items: center !important;
  border-radius: 999px !important;
  background:
    radial-gradient(circle at 32% 28%, #ffffff, #fff7ed 46%, #fed7aa 100%) !important;
  border: 5px solid rgba(251,146,60,0.34) !important;
  box-shadow:
    0 24px 70px rgba(15,23,42,0.16),
    0 0 0 24px rgba(255,255,255,0.36) !important;
  font-size: 98px !important;
  animation: lumiFloat 4.5s ease-in-out infinite !important;
  z-index: 5 !important;
}

/* Karakter gövdesi */
.character-stage .kid-character,
.character-stage .character-path,
.character-stage .rainbow-arc,
.character-stage .cloud {
  display: none !important;
}

.character-stage .stage-label {
  display: none !important;
}

/* Çevresel oyun objeleri */
.character-stage {
  isolation: isolate;
}

.character-stage .lumi-sparkle {
  position: absolute;
}

/* CSS-only decorative stars */
.character-stage > div:not(.stage-label):not(.character-path):not(.cloud):not(.rainbow-arc) {
  z-index: 1;
}

.kids-game-hero.advanced {
  grid-template-columns: 0.82fr 1.18fr !important;
  gap: 28px !important;
}

/* Karakter alanına hareketli baloncuklar */
.advanced-kids .character-stage {
  background-image:
    radial-gradient(circle at 22% 28%, rgba(251,191,36,0.55) 0 8px, transparent 9px),
    radial-gradient(circle at 78% 30%, rgba(96,165,250,0.55) 0 10px, transparent 11px),
    radial-gradient(circle at 25% 72%, rgba(244,114,182,0.42) 0 13px, transparent 14px),
    radial-gradient(circle at 76% 72%, rgba(45,212,191,0.40) 0 15px, transparent 16px),
    radial-gradient(circle at 50% 22%, rgba(255,255,255,0.95), transparent 24%),
    linear-gradient(180deg, rgba(186,230,253,0.78), rgba(254,243,199,0.74)) !important;
  background-size: auto, auto, auto, auto, auto, auto !important;
}

@keyframes lumiFloat {
  0%, 100% {
    transform: translate(-50%, -50%) translateY(0) rotate(-1deg);
  }
  50% {
    transform: translate(-50%, -50%) translateY(-16px) rotate(2deg);
  }
}

/* Hero kartı biraz küçült, sağ karakter daha görünür olsun */
.kids-hero-overlay {
  max-width: 520px !important;
  padding: 28px !important;
}

.kids-hero-overlay h1 {
  font-size: clamp(44px, 5vw, 70px) !important;
}

.lumi-card {
  margin-top: 18px !important;
}

/* My Badges boş kartı küçült */
.reward-card,
.kids-game-card.reward-card {
  min-height: 190px !important;
  max-width: 520px !important;
}

.kids-game-grid.advanced {
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  align-items: stretch !important;
}

/* Landing page sağ üstteki dünya/ekosistem kartını daha anlamlı göster */
.hero-flow-card,
.demo-flow-card,
.live-demo-flow,
.flow-card {
  position: relative;
  overflow: hidden;
}

.hero-flow-card::before,
.demo-flow-card::before,
.live-demo-flow::before,
.flow-card::before {
  content: "🌍";
  position: absolute;
  right: 28px;
  top: 22px;
  width: 92px;
  height: 92px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: rgba(255,255,255,0.18);
  border: 1px solid rgba(255,255,255,0.32);
  font-size: 52px;
  box-shadow: 0 18px 50px rgba(15,23,42,0.18);
  animation: worldFloat 6s ease-in-out infinite;
}

.hero-flow-card::after,
.demo-flow-card::after,
.live-demo-flow::after,
.flow-card::after {
  content: "Patient • NGO • Clinician • Research • AI";
  position: absolute;
  right: 28px;
  bottom: 22px;
  max-width: 260px;
  padding: 10px 14px;
  border-radius: 999px;
  background: rgba(255,255,255,0.16);
  color: rgba(255,255,255,0.92);
  font-weight: 850;
  font-size: 13px;
  letter-spacing: 0.02em;
}

@keyframes worldFloat {
  0%, 100% {
    transform: translateY(0) rotate(-3deg);
  }
  50% {
    transform: translateY(-10px) rotate(3deg);
  }
}

/* Eğer sağ kart class farklıysa landing içindeki mor kartlara genel dokunuş */
.landing-page .glass-card:nth-of-type(1)::before {
  content: "🌍";
}

/* Mobil */
@media (max-width: 1000px) {
  .kids-game-hero.advanced {
    grid-template-columns: 1fr !important;
  }

  .character-stage {
    min-height: 360px !important;
  }

  .character-stage::before {
    width: 135px !important;
    height: 135px !important;
    font-size: 72px !important;
  }

  .character-stage::after {
    font-size: 15px !important;
  }
}
'''

css_path.write_text(css, encoding="utf-8")
print("✅ Step 28 applied: animated OncoKids companion and landing world card visual added.")
