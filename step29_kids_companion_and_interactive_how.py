from pathlib import Path

css_path = Path("frontend/src/App.css")
css = css_path.read_text(encoding="utf-8")

css += r'''

/* Step 29: interactive How It Works + OncoKids real cartoon companion */

/* HOW IT WORKS kartlarını daha interaktif/simülasyon hissi */
.how-it-works,
.how-section,
.steps-section {
  position: relative;
}

.how-it-works .step-card,
.how-section .step-card,
.steps-section .step-card {
  position: relative;
  overflow: hidden;
  transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}

.how-it-works .step-card:hover,
.how-section .step-card:hover,
.steps-section .step-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 28px 80px rgba(37,99,235,0.18);
  border-color: rgba(37,99,235,0.35);
}

.how-it-works .step-card::after,
.how-section .step-card::after,
.steps-section .step-card::after {
  content: "";
  position: absolute;
  left: -40%;
  top: 0;
  width: 40%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(59,130,246,0.14), transparent);
  transform: skewX(-18deg);
  animation: cardScan 5s ease-in-out infinite;
}

@keyframes cardScan {
  0%, 65% { left: -45%; }
  100% { left: 120%; }
}

/* How it works kartları arasına akış çizgisi hissi */
.how-it-works .step-card:not(:last-child)::before,
.how-section .step-card:not(:last-child)::before,
.steps-section .step-card:not(:last-child)::before {
  content: "→";
  position: absolute;
  right: -24px;
  top: 50%;
  transform: translateY(-50%);
  color: #2563eb;
  font-size: 28px;
  font-weight: 950;
  z-index: 5;
}

/* Calm clear safe guidance kartı içine çocuk/companion görsel hissi */
.guidance-card,
.safety-card,
.calm-card,
.info-safe-card {
  position: relative;
  overflow: hidden;
}

.guidance-card::before,
.safety-card::before,
.calm-card::before,
.info-safe-card::before {
  content: "😊";
  position: absolute;
  right: 54px;
  top: 54px;
  width: 150px;
  height: 150px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: radial-gradient(circle at 35% 30%, #ffffff, #dbeafe 45%, #99f6e4);
  border: 4px solid rgba(255,255,255,0.75);
  box-shadow: 0 24px 70px rgba(15,23,42,0.18);
  font-size: 76px;
  animation: companionFloat 4.5s ease-in-out infinite;
}

.guidance-card::after,
.safety-card::after,
.calm-card::after,
.info-safe-card::after {
  content: "Safe guidance, not fear";
  position: absolute;
  right: 44px;
  top: 218px;
  padding: 10px 14px;
  border-radius: 999px;
  background: rgba(255,255,255,0.72);
  color: #0f172a;
  font-weight: 900;
  box-shadow: 0 12px 34px rgba(15,23,42,0.12);
}

/* Eğer class isimleri farklıysa büyük glass kartlarda da uygula */
.landing-page .glass-card:has(h2)::before {
  content: "😊";
}

/* ONCOKIDS: sağ tarafı tam cartoon companion alanı yap */
.kids-game-hero.advanced {
  grid-template-columns: 0.78fr 1.22fr !important;
  gap: 32px !important;
  align-items: stretch !important;
}

.character-stage {
  display: block !important;
  position: relative !important;
  min-height: 560px !important;
  border-radius: 46px !important;
  overflow: hidden !important;
  background:
    radial-gradient(circle at 50% 16%, rgba(255,255,255,0.95), transparent 20%),
    radial-gradient(circle at 25% 30%, rgba(251,191,36,0.28), transparent 15%),
    radial-gradient(circle at 80% 36%, rgba(96,165,250,0.28), transparent 14%),
    linear-gradient(180deg, rgba(186,230,253,0.86), rgba(254,243,199,0.78)) !important;
  border: 1px solid rgba(255,255,255,0.94) !important;
  box-shadow: 0 28px 90px rgba(15,23,42,0.14) !important;
}

/* Eski stage içeriğini gizle */
.character-stage .kid-character,
.character-stage .character-path,
.character-stage .rainbow-arc,
.character-stage .cloud,
.character-stage .stage-label {
  display: none !important;
}

/* Companion head */
.character-stage::before {
  content: "😊" !important;
  position: absolute !important;
  left: 50% !important;
  top: 38% !important;
  transform: translate(-50%, -50%) !important;
  width: 210px !important;
  height: 210px !important;
  display: grid !important;
  place-items: center !important;
  border-radius: 999px !important;
  background:
    radial-gradient(circle at 32% 26%, #ffffff, #fff7ed 48%, #fed7aa 100%) !important;
  border: 6px solid rgba(251,146,60,0.34) !important;
  box-shadow:
    0 26px 76px rgba(15,23,42,0.18),
    0 0 0 28px rgba(255,255,255,0.38) !important;
  font-size: 108px !important;
  animation: companionFloat 4.2s ease-in-out infinite !important;
  z-index: 5 !important;
}

/* Companion message */
.character-stage::after {
  content: "Hi, I am Lumi. Pick a quest, collect badges, and practice brave questions." !important;
  position: absolute !important;
  left: 38px !important;
  right: 38px !important;
  bottom: 34px !important;
  padding: 20px 24px !important;
  border-radius: 28px !important;
  background: rgba(255,255,255,0.88) !important;
  color: #7c2d12 !important;
  font-weight: 950 !important;
  font-size: 19px !important;
  line-height: 1.45 !important;
  text-align: center !important;
  box-shadow: 0 18px 46px rgba(15,23,42,0.13) !important;
  z-index: 6 !important;
}

@keyframes companionFloat {
  0%, 100% {
    transform: translate(-50%, -50%) translateY(0) rotate(-1deg);
  }
  50% {
    transform: translate(-50%, -50%) translateY(-16px) rotate(2deg);
  }
}

/* Dekoratif oyun objeleri */
.character-stage {
  background-image:
    radial-gradient(circle at 18% 22%, rgba(251,191,36,.75) 0 9px, transparent 10px),
    radial-gradient(circle at 80% 24%, rgba(96,165,250,.72) 0 11px, transparent 12px),
    radial-gradient(circle at 22% 74%, rgba(244,114,182,.54) 0 14px, transparent 15px),
    radial-gradient(circle at 78% 72%, rgba(45,212,191,.54) 0 15px, transparent 16px),
    radial-gradient(circle at 50% 16%, rgba(255,255,255,0.95), transparent 20%),
    linear-gradient(180deg, rgba(186,230,253,0.86), rgba(254,243,199,0.78)) !important;
}

/* Boşluğu azalt */
.kids-game-hero {
  padding-bottom: 10px !important;
}

.kids-game-grid.advanced {
  margin-top: -24px !important;
}

.reward-card,
.kids-game-card.reward-card {
  min-height: 170px !important;
}

/* Mobil */
@media (max-width: 1000px) {
  .kids-game-hero.advanced {
    grid-template-columns: 1fr !important;
  }

  .character-stage {
    min-height: 380px !important;
  }

  .character-stage::before {
    width: 145px !important;
    height: 145px !important;
    font-size: 76px !important;
  }

  .character-stage::after {
    font-size: 15px !important;
  }

  .how-it-works .step-card:not(:last-child)::before,
  .how-section .step-card:not(:last-child)::before,
  .steps-section .step-card:not(:last-child)::before {
    display: none;
  }
}
'''

css_path.write_text(css, encoding="utf-8")
print("✅ Step 29 applied: interactive How It Works, calm card companion, OncoKids animated Lumi companion.")
