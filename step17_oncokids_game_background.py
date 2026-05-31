from pathlib import Path
import re
import shutil

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")
assets = Path("frontend/src/assets")

# Görselleri otomatik bul ve standart isim ver
pngs = list(assets.glob("ChatGPT Image*.png"))

sea = None
kids = None

for p in pngs:
    name = p.name
    if "04_24_36" in name:
        sea = p
    if "04_33_48" in name:
        kids = p

if sea:
    shutil.copyfile(sea, assets / "onco-sea-hero.png")
    print("✅ Landing background copied:", sea.name)
else:
    print("⚠️ Sea image not found.")

if kids:
    shutil.copyfile(kids, assets / "oncokids-bg.png")
    print("✅ OncoKids background copied:", kids.name)
else:
    print("⚠️ OncoKids image not found.")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

new_kids = r'''
  const OncoKidsPage = () => {
    const [hopePoints, setHopePoints] = useState(120);
    const [activeQuest, setActiveQuest] = useState("learn");
    const [feeling, setFeeling] = useState(lang === "tr" ? "Umutlu" : "Hopeful");

    const addPoints = (amount, quest) => {
      setHopePoints((p) => p + amount);
      setActiveQuest(quest);
    };

    const kidText = {
      tr: {
        home: "← Ana Sayfa",
        title: "Onco Kids",
        subtitle: "Çocuklar ve aileler için yumuşak, umut veren ve oyunlaştırılmış öğrenme alanı.",
        start: "Macaraya Başla",
        points: "Umut Puanı",
        journey: "Umut Yolculuğu",
        helper: "Lumi diyor ki",
        helperText: "Küçük sorular büyük güçlere dönüşür. Hazırsan birlikte öğrenelim.",
        learn: "Öğren",
        ask: "Sor",
        feel: "Hislerini Seç",
        breathe: "Nefes Al",
        hero: "Cesur Kahraman",
        question: "Bugün nasıl hissediyorsun?",
        safety: "Bu alan tıbbi karar vermez. Çocukların duygularını konuşmasına ve ailelerin doktora daha hazır gitmesine yardımcı olur."
      },
      en: {
        home: "← Home",
        title: "Onco Kids",
        subtitle: "A gentle, hopeful and gamified learning space for children and families.",
        start: "Start Adventure",
        points: "Hope Points",
        journey: "Hope Journey",
        helper: "Lumi says",
        helperText: "Small questions can become big strengths. Let’s learn together.",
        learn: "Learn",
        ask: "Ask",
        feel: "Choose Feeling",
        breathe: "Breathe",
        hero: "Brave Hero",
        question: "How do you feel today?",
        safety: "This space does not make medical decisions. It helps children talk about feelings and helps families prepare for doctor conversations."
      }
    }[lang];

    const feelings = lang === "tr"
      ? ["Korkmuş", "Meraklı", "Üzgün", "Umutlu", "Yorgun", "Cesur"]
      : ["Scared", "Curious", "Sad", "Hopeful", "Tired", "Brave"];

    return (
      <div className="kids-game-page">
        <header className="kids-game-nav">
          <button className="ghost-btn" onClick={() => setPage("landing")}>{kidText.home}</button>

          <div className="kids-points">
            ⭐ {kidText.points}: <strong>{hopePoints}</strong>
          </div>

          <div className="language-control kids-lang">
            <label>{t.langLabel}</label>
            <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">English</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>
        </header>

        <section className="kids-game-hero">
          <div className="kids-hero-overlay">
            <p className="eyebrow dark">ONCO KIDS</p>
            <h1>{kidText.title}</h1>
            <p>{kidText.subtitle}</p>

            <button className="kids-main-btn" onClick={() => addPoints(25, "learn")}>
              {kidText.start}
            </button>

            <div className="lumi-card">
              <div className="lumi-avatar">🌟</div>
              <div>
                <strong>{kidText.helper}</strong>
                <span>{kidText.helperText}</span>
              </div>
            </div>
          </div>
        </section>

        <section className="hope-journey">
          <h2>{kidText.journey}</h2>

          <div className="journey-path">
            {[
              ["learn", "🌈", kidText.learn],
              ["ask", "🧸", kidText.ask],
              ["feel", "💛", kidText.feel],
              ["breathe", "☁️", kidText.breathe],
              ["hero", "🏆", kidText.hero]
            ].map(([key, icon, label], index) => (
              <button
                key={key}
                className={`journey-step ${activeQuest === key ? "active" : ""}`}
                onClick={() => addPoints(10 + index * 5, key)}
              >
                <span>{icon}</span>
                <strong>{label}</strong>
              </button>
            ))}
          </div>
        </section>

        <section className="kids-game-grid">
          <div className="kids-game-card story-card">
            <h3>{lang === "tr" ? "Mini Hikâye" : "Mini Story"}</h3>
            <p>
              {lang === "tr"
                ? "Elif hastane ziyaretinden önce biraz meraklı ve biraz endişeli. Ona hangi soruları sorabileceğini birlikte hazırlayalım."
                : "Elif feels a little curious and a little worried before a hospital visit. Let’s help her prepare gentle questions."}
            </p>
            <button onClick={() => addPoints(30, "ask")}>
              {lang === "tr" ? "Elif’e yardım et" : "Help Elif"}
            </button>
          </div>

          <div className="kids-game-card knowledge-card">
            <h3>{lang === "tr" ? "Çocuklar için Bilgi Baloncukları" : "Knowledge Bubbles"}</h3>
            <div className="bubble-map">
              {[
                lang === "tr" ? "Doktorlar yardım eder" : "Doctors help",
                lang === "tr" ? "İlaçlar planlıdır" : "Medicines have plans",
                lang === "tr" ? "Aile yanında" : "Family is near",
                lang === "tr" ? "Soru sormak iyidir" : "Questions are good"
              ].map((item) => (
                <button key={item} onClick={() => addPoints(12, "learn")}>{item}</button>
              ))}
            </div>
          </div>

          <div className="kids-game-card feeling-card">
            <h3>{kidText.question}</h3>
            <div className="feeling-grid game">
              {feelings.map((item) => (
                <button
                  key={item}
                  className={feeling === item ? "selected" : ""}
                  onClick={() => {
                    setFeeling(item);
                    addPoints(8, "feel");
                  }}
                >
                  {item}
                </button>
              ))}
            </div>
            <p className="feeling-result">
              {lang === "tr"
                ? `${feeling} hissetmek normal. Bunu güvendiğin bir yetişkinle paylaşabilirsin.`
                : `Feeling ${feeling.toLowerCase()} is okay. You can share it with a trusted adult.`}
            </p>
          </div>

          <div className="kids-game-card breathing-card">
            <h3>{lang === "tr" ? "Sakin Nefes Egzersizi" : "Calm Breathing"}</h3>
            <div className="breathing-circle">inhale<br />exhale</div>
            <p>
              {lang === "tr"
                ? "Yavaşça nefes al, gökyüzüne bak ve içinden üç güzel şey düşün."
                : "Breathe slowly, look at the sky and think of three kind things."}
            </p>
            <button onClick={() => addPoints(20, "breathe")}>
              {lang === "tr" ? "Tamamladım" : "Completed"}
            </button>
          </div>
        </section>

        <section className="kids-safety-note">
          {kidText.safety}
        </section>
      </div>
    );
  };

'''

# OncoKidsPage component değiştir
start = app.find("const OncoKidsPage")
end = app.find("const KnowledgeGraph")

if start == -1 or end == -1 or end <= start:
    raise RuntimeError("OncoKidsPage or KnowledgeGraph not found in App.jsx")

app = app[:start] + new_kids.lstrip() + "\n  " + app[end:]
app_path.write_text(app, encoding="utf-8")

css += r'''

/* Step 17: Gamified Onco Kids + real image backgrounds */

.calm-sea-hero {
  background:
    linear-gradient(90deg, rgba(4, 16, 38, 0.66), rgba(4, 16, 38, 0.30), rgba(4, 16, 38, 0.08)),
    linear-gradient(180deg, rgba(4, 16, 38, 0.22), rgba(248,251,255,0.08)),
    url("./assets/onco-sea-hero.png") center / cover no-repeat !important;
}

.kids-game-page {
  min-height: 100vh;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.64), rgba(239,246,255,0.88)),
    url("./assets/oncokids-bg.png") center top / cover fixed no-repeat;
  color: #0f172a;
}

.kids-game-nav {
  position: sticky;
  top: 16px;
  z-index: 30;
  max-width: 1180px;
  margin: 0 auto;
  padding: 16px 24px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 16px;
  align-items: center;
}

.kids-points {
  justify-self: center;
  padding: 12px 18px;
  border-radius: 999px;
  background: rgba(255,255,255,0.78);
  border: 1px solid rgba(255,255,255,0.8);
  backdrop-filter: blur(16px);
  color: #7c2d12;
  font-weight: 900;
  box-shadow: 0 14px 40px rgba(15,23,42,0.12);
}

.kids-game-hero {
  max-width: 1180px;
  margin: 0 auto;
  min-height: 620px;
  display: flex;
  align-items: center;
  padding: 24px;
}

.kids-hero-overlay {
  max-width: 610px;
  padding: 34px;
  border-radius: 36px;
  background: rgba(255,255,255,0.72);
  border: 1px solid rgba(255,255,255,0.9);
  backdrop-filter: blur(18px);
  box-shadow: 0 28px 90px rgba(15,23,42,0.16);
}

.kids-hero-overlay h1 {
  font-size: clamp(48px, 6vw, 82px);
  margin: 8px 0;
  line-height: 0.94;
  letter-spacing: -0.06em;
  color: #7c2d12;
}

.kids-hero-overlay p {
  font-size: 20px;
  color: #7c2d12;
  line-height: 1.65;
}

.kids-main-btn,
.kids-game-card button {
  border: none;
  border-radius: 999px;
  padding: 14px 20px;
  background: linear-gradient(135deg, #fb923c, #f97316);
  color: white;
  font-weight: 950;
  cursor: pointer;
  box-shadow: 0 14px 34px rgba(249,115,22,0.25);
}

.lumi-card {
  margin-top: 20px;
  display: grid;
  grid-template-columns: 56px 1fr;
  gap: 14px;
  align-items: center;
  padding: 16px;
  border-radius: 24px;
  background: #fff7ed;
  border: 1px solid #fed7aa;
}

.lumi-avatar {
  width: 56px;
  height: 56px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: #fef3c7;
  font-size: 28px;
  animation: floatNode 4s ease-in-out infinite;
}

.lumi-card strong,
.lumi-card span {
  display: block;
}

.lumi-card span {
  margin-top: 4px;
  color: #7c2d12;
  line-height: 1.45;
}

.hope-journey {
  max-width: 1180px;
  margin: 0 auto 28px;
  padding: 0 24px;
}

.hope-journey h2 {
  font-size: 36px;
  color: #7c2d12;
}

.journey-path {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
}

.journey-step {
  min-height: 130px;
  border: 1px solid rgba(255,255,255,0.9);
  border-radius: 28px;
  background: rgba(255,255,255,0.72);
  backdrop-filter: blur(14px);
  box-shadow: 0 20px 60px rgba(15,23,42,0.10);
  cursor: pointer;
  transition: transform .2s ease, box-shadow .2s ease;
}

.journey-step:hover,
.journey-step.active {
  transform: translateY(-6px);
  box-shadow: 0 28px 80px rgba(15,23,42,0.16);
  outline: 3px solid rgba(251,146,60,0.28);
}

.journey-step span,
.journey-step strong {
  display: block;
}

.journey-step span {
  font-size: 34px;
  margin-bottom: 8px;
}

.journey-step strong {
  color: #7c2d12;
  font-size: 17px;
}

.kids-game-grid {
  max-width: 1180px;
  margin: 0 auto;
  padding: 24px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.kids-game-card {
  min-height: 300px;
  border-radius: 32px;
  padding: 26px;
  background: rgba(255,255,255,0.78);
  border: 1px solid rgba(255,255,255,0.9);
  backdrop-filter: blur(18px);
  box-shadow: 0 24px 70px rgba(15,23,42,0.12);
}

.kids-game-card h3 {
  margin-top: 0;
  font-size: 26px;
  color: #7c2d12;
}

.kids-game-card p {
  color: #7c2d12;
  line-height: 1.65;
}

.bubble-map {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.bubble-map button {
  background: #ccfbf1;
  color: #0f766e;
  box-shadow: none;
}

.feeling-grid.game {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 11px;
}

.feeling-grid.game button {
  background: #ffedd5;
  color: #9a3412;
  box-shadow: none;
}

.feeling-grid.game button.selected {
  background: #fb923c;
  color: white;
}

.feeling-result {
  margin-top: 14px;
  padding: 14px;
  border-radius: 18px;
  background: #fff7ed;
}

.breathing-card {
  position: relative;
  overflow: hidden;
}

.breathing-circle {
  width: 160px;
  height: 160px;
  border-radius: 999px;
  margin: 12px auto 20px;
  display: grid;
  place-items: center;
  text-align: center;
  background: radial-gradient(circle, #ffffff, #bae6fd 52%, #38bdf8);
  color: #075985;
  font-weight: 950;
  box-shadow: 0 0 60px rgba(56,189,248,0.34);
  animation: breathe 5s ease-in-out infinite;
}

.kids-safety-note {
  max-width: 1180px;
  margin: 16px auto 70px;
  padding: 22px 24px;
  border-radius: 26px;
  background: rgba(255,255,255,0.78);
  border: 1px solid rgba(255,255,255,0.9);
  color: #7c2d12;
  line-height: 1.6;
  font-weight: 800;
  backdrop-filter: blur(16px);
}

@media (max-width: 900px) {
  .kids-game-nav,
  .journey-path,
  .kids-game-grid {
    grid-template-columns: 1fr;
  }

  .kids-points {
    justify-self: stretch;
    text-align: center;
  }

  .kids-game-hero {
    min-height: 540px;
  }

  .feeling-grid.game {
    grid-template-columns: repeat(2, 1fr);
  }
}
'''

css_path.write_text(css, encoding="utf-8")

print("✅ OncoKids gamified page and both backgrounds connected.")
