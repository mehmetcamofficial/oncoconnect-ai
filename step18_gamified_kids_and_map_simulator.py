from pathlib import Path
import re

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) App-level map simulator states
app = app.replace(
'''  const [prevention, setPrevention] = useState({
    tobaccoFree: 60,
    alcoholReduction: 45,
    movement: 40,
    screeningAwareness: 55
  });''',
'''  const [prevention, setPrevention] = useState({
    tobaccoFree: 60,
    alcoholReduction: 45,
    movement: 40,
    screeningAwareness: 55
  });

  const [mapMode, setMapMode] = useState("turkiye");
  const [mapYear, setMapYear] = useState(2024);
  const [mapGender, setMapGender] = useState("total");'''
)

# 2) Add map data after preventionLevel block
app = app.replace(
'''  const updatePrevention = (key, value) => {
    setPrevention({ ...prevention, [key]: Number(value) });
  };

  const riskScore = useMemo(() => {''',
'''  const updatePrevention = (key, value) => {
    setPrevention({ ...prevention, [key]: Number(value) });
  };

  const turkeyCities = [
    "Adana","Adıyaman","Afyonkarahisar","Ağrı","Amasya","Ankara","Antalya","Artvin","Aydın","Balıkesir","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Edirne","Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Isparta","Mersin","Istanbul","Izmir","Kars","Kastamonu","Kayseri","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya","Malatya","Manisa","Kahramanmaraş","Mardin","Muğla","Muş","Nevşehir","Niğde","Ordu","Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Şanlıurfa","Uşak","Van","Yozgat","Zonguldak","Aksaray","Bayburt","Karaman","Kırıkkale","Batman","Şırnak","Bartın","Ardahan","Iğdır","Yalova","Karabük","Kilis","Osmaniye","Düzce"
  ];

  const europeCountries = [
    "Türkiye","Germany","France","Italy","Spain","Poland","Netherlands","Belgium","Greece","Portugal","Sweden","Austria","Romania","Bulgaria","Denmark","Ireland","Czechia","Hungary"
  ];

  const mapData = useMemo(() => {
    const yearFactor = 1 + (mapYear - 2020) * 0.045;
    const genderFactor = mapGender === "female" ? 0.92 : mapGender === "male" ? 1.08 : 1;

    if (mapMode === "turkiye") {
      return turkeyCities.map((city, index) => {
        const metroBoost =
          ["Istanbul","Ankara","Izmir","Bursa","Antalya","Adana","Konya","Gaziantep","Kocaeli"].includes(city)
            ? 2.2
            : 1;

        const base = 320 + ((index * 137) % 950);
        const value = Math.round(base * metroBoost * yearFactor * genderFactor);

        return {
          name: city,
          value,
          growth: Math.round(((yearFactor - 1) * 100) + ((index % 7) * 1.4)),
          intensity: Math.min(100, Math.round(value / 45))
        };
      });
    }

    return europeCountries.map((country, index) => {
      const boost =
        ["Türkiye","Germany","France","Italy","Spain"].includes(country)
          ? 2.4
          : 1.2;

      const base = 8200 + ((index * 3921) % 18000);
      const value = Math.round(base * boost * yearFactor * genderFactor);

      return {
        name: country,
        value,
        growth: Math.round(((yearFactor - 1) * 100) + ((index % 5) * 2.2)),
        intensity: Math.min(100, Math.round(value / 780))
      };
    });
  }, [mapMode, mapYear, mapGender]);

  const totalMapCases = useMemo(() => {
    return mapData.reduce((sum, item) => sum + item.value, 0);
  }, [mapData]);

  const topMapItems = useMemo(() => {
    return [...mapData].sort((a, b) => b.value - a.value).slice(0, 6);
  }, [mapData]);

  const riskScore = useMemo(() => {'''
)

# 3) Insert interactive map after Cancer Burden section before Prevention Simulator
map_section = r'''
        <section className="cancer-map-simulator">
          <div className="section-intro">
            <p className="eyebrow dark">{lang === "tr" ? "İNTERAKTİF KANSER HARİTASI" : "INTERACTIVE CANCER MAP"}</p>
            <h2>
              {lang === "tr"
                ? "Türkiye ve Avrupa için animasyonlu kanser yükü simülasyonu"
                : "Animated cancer burden simulation for Türkiye and Europe"}
            </h2>
            <p>
              {lang === "tr"
                ? "Bu görselleştirme resmi kayıt verisi değildir. Demo amaçlı simülasyon verisiyle, gerçek veri bağlandığında platformun nasıl çalışacağını gösterir."
                : "This visualization is not official registry data. It uses demo simulation data to show how the platform would work when connected to real data sources."}
            </p>
          </div>

          <div className="map-controls">
            <button className={mapMode === "turkiye" ? "active" : ""} onClick={() => setMapMode("turkiye")}>
              Türkiye — 81 {lang === "tr" ? "İl" : "Cities"}
            </button>
            <button className={mapMode === "europe" ? "active" : ""} onClick={() => setMapMode("europe")}>
              Europe
            </button>

            <select value={mapGender} onChange={(e) => setMapGender(e.target.value)}>
              <option value="total">{lang === "tr" ? "Toplam" : "Total"}</option>
              <option value="female">{lang === "tr" ? "Kadın" : "Female"}</option>
              <option value="male">{lang === "tr" ? "Erkek" : "Male"}</option>
            </select>

            <div className="year-slider">
              <strong>{mapYear}</strong>
              <input type="range" min="2020" max="2026" value={mapYear} onChange={(e) => setMapYear(Number(e.target.value))} />
            </div>
          </div>

          <div className="map-dashboard">
            <div className="map-visual-card">
              <div className="map-summary">
                <div>
                  <small>{lang === "tr" ? "Simüle edilen toplam vaka" : "Simulated total cases"}</small>
                  <strong>{totalMapCases.toLocaleString()}</strong>
                </div>
                <div>
                  <small>{lang === "tr" ? "Görünüm" : "View"}</small>
                  <strong>{mapMode === "turkiye" ? "Türkiye" : "Europe"}</strong>
                </div>
                <div>
                  <small>{lang === "tr" ? "Filtre" : "Filter"}</small>
                  <strong>{mapGender === "total" ? (lang === "tr" ? "Toplam" : "Total") : mapGender === "female" ? (lang === "tr" ? "Kadın" : "Female") : (lang === "tr" ? "Erkek" : "Male")}</strong>
                </div>
              </div>

              <div className={mapMode === "turkiye" ? "turkiye-pin-map" : "europe-bubble-map"}>
                {mapData.map((item, index) => (
                  <button
                    key={item.name}
                    className="map-pin"
                    style={{
                      "--size": `${Math.max(12, Math.min(34, item.intensity / 2.8))}px`,
                      "--delay": `${(index % 12) * 0.08}s`
                    }}
                    title={`${item.name}: ${item.value.toLocaleString()}`}
                  >
                    <span>{item.name}</span>
                    <b>{item.value.toLocaleString()}</b>
                  </button>
                ))}
              </div>
            </div>

            <div className="map-rank-card">
              <h3>{lang === "tr" ? "En yüksek simüle edilen alanlar" : "Highest simulated areas"}</h3>
              <div className="rank-list">
                {topMapItems.map((item, index) => (
                  <div className="rank-row" key={item.name}>
                    <span>{index + 1}</span>
                    <div>
                      <strong>{item.name}</strong>
                      <small>{lang === "tr" ? "Yıllık artış simülasyonu" : "Simulated yearly growth"}: +{item.growth}%</small>
                    </div>
                    <b>{item.value.toLocaleString()}</b>
                  </div>
                ))}
              </div>

              <div className="map-warning">
                {lang === "tr"
                  ? "Gerçek kullanım için Sağlık Bakanlığı, kanser kayıt merkezi, GLOBOCAN veya ulusal/AB açık veri kaynakları bağlanmalıdır."
                  : "For real-world use, this should be connected to Ministry of Health, cancer registry, GLOBOCAN or national/EU open data sources."}
              </div>
            </div>
          </div>
        </section>

'''

marker = '        <section className="prevention-simulator-section">'
if marker not in app:
    print("⚠️ prevention-simulator-section marker not found. Map section not inserted.")
else:
    if "cancer-map-simulator" not in app:
        app = app.replace(marker, map_section + marker)

# 4) Replace OncoKidsPage with much more gamified page
new_kids = r'''
  const OncoKidsPage = () => {
    const [hopePoints, setHopePoints] = useState(120);
    const [activeQuest, setActiveQuest] = useState("learn");
    const [feeling, setFeeling] = useState(lang === "tr" ? "Umutlu" : "Hopeful");
    const [characterX, setCharacterX] = useState(42);
    const [quizAnswer, setQuizAnswer] = useState(null);
    const [badges, setBadges] = useState(["🌈"]);

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
        safety: "Bu alan tıbbi karar vermez. Çocukların duygularını konuşmasına ve ailelerin doktora daha hazır gitmesine yardımcı olur.",
        quizGood: "Harika! Soru sormak cesur bir davranıştır.",
        quizTry: "Tekrar deneyebilirsin. Burada hata yapmak sorun değil."
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
        safety: "This space does not make medical decisions. It helps children talk about feelings and helps families prepare for doctor conversations.",
        quizGood: "Great! Asking questions is brave.",
        quizTry: "Try again. Making mistakes is okay here."
      }
    }[lang];

    const addPoints = (amount, quest, badge = null) => {
      setHopePoints((p) => p + amount);
      setActiveQuest(quest);
      setCharacterX((x) => Math.min(82, x + 8));
      if (badge && !badges.includes(badge)) setBadges([...badges, badge]);
    };

    const resetAdventure = () => {
      setHopePoints(120);
      setActiveQuest("learn");
      setCharacterX(42);
      setQuizAnswer(null);
      setBadges(["🌈"]);
    };

    const feelings = lang === "tr"
      ? ["Korkmuş", "Meraklı", "Üzgün", "Umutlu", "Yorgun", "Cesur"]
      : ["Scared", "Curious", "Sad", "Hopeful", "Tired", "Brave"];

    return (
      <div className="kids-game-page advanced-kids">
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

        <section className="kids-game-hero advanced">
          <div className="kids-hero-overlay">
            <p className="eyebrow dark">ONCO KIDS</p>
            <h1>{kidText.title}</h1>
            <p>{kidText.subtitle}</p>

            <div className="kids-hero-actions">
              <button className="kids-main-btn" onClick={() => addPoints(25, "learn", "📘")}>{kidText.start}</button>
              <button className="kids-reset-btn" onClick={resetAdventure}>
                {lang === "tr" ? "Yeniden Başlat" : "Restart"}
              </button>
            </div>

            <div className="badge-row">
              {badges.map((badge) => <span key={badge}>{badge}</span>)}
            </div>

            <div className="lumi-card">
              <div className="lumi-avatar moving">🌟</div>
              <div>
                <strong>{kidText.helper}</strong>
                <span>{kidText.helperText}</span>
              </div>
            </div>
          </div>

          <div className="character-stage">
            <div className="cloud c1"></div>
            <div className="cloud c2"></div>
            <div className="rainbow-arc"></div>
            <div className="character-path">
              <div className="path-line"></div>
              <div className="kid-character" style={{ left: `${characterX}%` }}>
                <div className="kid-face">😊</div>
                <div className="kid-body"></div>
              </div>
            </div>
            <div className="stage-label">
              {lang === "tr" ? "Lumi ile umut yolculuğu" : "Hope journey with Lumi"}
            </div>
          </div>
        </section>

        <section className="hope-journey advanced">
          <h2>{kidText.journey}</h2>

          <div className="journey-path">
            {[
              ["learn", "🌈", lang === "tr" ? "Öğren" : "Learn", "📘"],
              ["ask", "🧸", lang === "tr" ? "Sor" : "Ask", "🧸"],
              ["feel", "💛", lang === "tr" ? "Hislerini Seç" : "Choose Feeling", "💛"],
              ["breathe", "☁️", lang === "tr" ? "Nefes Al" : "Breathe", "☁️"],
              ["hero", "🏆", lang === "tr" ? "Cesur Kahraman" : "Brave Hero", "🏆"]
            ].map(([key, icon, label, badge], index) => (
              <button
                key={key}
                className={`journey-step ${activeQuest === key ? "active" : ""}`}
                onClick={() => addPoints(10 + index * 5, key, badge)}
              >
                <span>{icon}</span>
                <strong>{label}</strong>
              </button>
            ))}
          </div>
        </section>

        <section className="kids-game-grid advanced">
          <div className="kids-game-card story-card">
            <h3>{lang === "tr" ? "Hikâye Görevi" : "Story Quest"}</h3>
            <p>
              {lang === "tr"
                ? "Elif hastane ziyaretinden önce biraz meraklı ve biraz endişeli. Ona hangi soruları sorabileceğini birlikte hazırlayalım."
                : "Elif feels curious and a little worried before a hospital visit. Let’s help her prepare gentle questions."}
            </p>
            <div className="choice-grid">
              <button onClick={() => addPoints(18, "ask", "❓")}>{lang === "tr" ? "Doktora soru hazırla" : "Prepare a doctor question"}</button>
              <button onClick={() => addPoints(18, "feel", "💬")}>{lang === "tr" ? "Duygusunu söylemesine yardım et" : "Help her name a feeling"}</button>
            </div>
          </div>

          <div className="kids-game-card quiz-card">
            <h3>{lang === "tr" ? "Mini Quiz" : "Mini Quiz"}</h3>
            <p>{lang === "tr" ? "Hastaneye gitmeden önce soru sormak iyi midir?" : "Is it okay to ask questions before going to the hospital?"}</p>

            <div className="choice-grid">
              <button onClick={() => { setQuizAnswer("good"); addPoints(30, "hero", "🏆"); }}>
                {lang === "tr" ? "Evet, soru sormak iyidir" : "Yes, questions are good"}
              </button>
              <button onClick={() => { setQuizAnswer("try"); addPoints(5, "learn"); }}>
                {lang === "tr" ? "Hayır, hiç sormamalıyız" : "No, we should not ask"}
              </button>
            </div>

            {quizAnswer && (
              <div className={`quiz-result ${quizAnswer}`}>
                {quizAnswer === "good" ? kidText.quizGood : kidText.quizTry}
              </div>
            )}
          </div>

          <div className="kids-game-card knowledge-card">
            <h3>{lang === "tr" ? "Bilgi Baloncukları" : "Knowledge Bubbles"}</h3>
            <div className="bubble-map">
              {[
                lang === "tr" ? "Doktorlar yardım eder" : "Doctors help",
                lang === "tr" ? "İlaçlar planlıdır" : "Medicines have plans",
                lang === "tr" ? "Aile yanında" : "Family is near",
                lang === "tr" ? "Soru sormak iyidir" : "Questions are good",
                lang === "tr" ? "Dinlenmek önemlidir" : "Rest matters",
                lang === "tr" ? "Duygular konuşulabilir" : "Feelings can be shared"
              ].map((item) => (
                <button key={item} onClick={() => addPoints(12, "learn", "✨")}>{item}</button>
              ))}
            </div>
          </div>

          <div className="kids-game-card feeling-card">
            <h3>{lang === "tr" ? "Duygu Bahçesi" : "Emotion Garden"}</h3>
            <div className="feeling-grid game">
              {feelings.map((item) => (
                <button
                  key={item}
                  className={feeling === item ? "selected" : ""}
                  onClick={() => {
                    setFeeling(item);
                    addPoints(8, "feel", "💛");
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

          <div className="kids-game-card breathing-card wide">
            <h3>{lang === "tr" ? "Sakin Nefes Oyunu" : "Calm Breathing Game"}</h3>
            <div className="breathing-game-row">
              <div className="breathing-circle">inhale<br />exhale</div>
              <div>
                <p>
                  {lang === "tr"
                    ? "Yavaşça nefes al, gökyüzüne bak ve içinden üç güzel şey düşün."
                    : "Breathe slowly, look at the sky and think of three kind things."}
                </p>
                <button onClick={() => addPoints(20, "breathe", "☁️")}>
                  {lang === "tr" ? "Nefes görevini tamamladım" : "I completed the breathing quest"}
                </button>
              </div>
            </div>
          </div>

          <div className="kids-game-card reward-card">
            <h3>{lang === "tr" ? "Rozetlerim" : "My Badges"}</h3>
            <div className="reward-badges">
              {badges.map((badge) => <span key={badge}>{badge}</span>)}
            </div>
            <p>{lang === "tr" ? "Her görev küçük bir cesaret adımıdır." : "Each quest is a small step of courage."}</p>
          </div>
        </section>

        <section className="kids-safety-note">
          {kidText.safety}
        </section>
      </div>
    );
  };

'''

start = app.find("const OncoKidsPage")
end = app.find("const KnowledgeGraph")

if start == -1 or end == -1 or end <= start:
    raise RuntimeError("OncoKidsPage or KnowledgeGraph not found in App.jsx")

app = app[:start] + new_kids.lstrip() + "\n  " + app[end:]

app_path.write_text(app, encoding="utf-8")

css += r'''

/* Step 18: deeper OncoKids game + interactive cancer map simulator */

.cancer-map-simulator {
  max-width: 1180px;
  margin: 68px auto;
  padding: 0 24px;
}

.map-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  margin: 18px 0;
}

.map-controls button,
.map-controls select {
  border: 1px solid #cbd5e1;
  background: white;
  color: #0f172a;
  border-radius: 999px;
  padding: 12px 16px;
  font-weight: 900;
  cursor: pointer;
}

.map-controls button.active {
  background: #1d4ed8;
  color: white;
  border-color: #1d4ed8;
}

.year-slider {
  display: flex;
  align-items: center;
  gap: 12px;
  background: white;
  border: 1px solid #cbd5e1;
  border-radius: 999px;
  padding: 10px 16px;
}

.year-slider strong {
  color: #1d4ed8;
}

.year-slider input {
  width: 170px;
  accent-color: #1d4ed8;
}

.map-dashboard {
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 22px;
  align-items: stretch;
}

.map-visual-card,
.map-rank-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 30px;
  padding: 24px;
  box-shadow: 0 24px 80px rgba(15,23,42,0.12);
}

.map-summary {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 18px;
}

.map-summary div {
  border-radius: 20px;
  background: #f8fafc;
  padding: 16px;
  border: 1px solid #e2e8f0;
}

.map-summary small,
.map-summary strong {
  display: block;
}

.map-summary small {
  color: #64748b;
  font-weight: 800;
}

.map-summary strong {
  margin-top: 4px;
  color: #0f172a;
  font-size: 22px;
}

.turkiye-pin-map,
.europe-bubble-map {
  min-height: 520px;
  position: relative;
  border-radius: 28px;
  overflow: hidden;
  background:
    radial-gradient(circle at 20% 20%, rgba(59,130,246,0.24), transparent 28%),
    radial-gradient(circle at 80% 70%, rgba(20,184,166,0.20), transparent 30%),
    linear-gradient(135deg, #0f172a, #1e3a8a);
}

.turkiye-pin-map {
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  gap: 8px;
  padding: 26px;
  align-content: center;
}

.europe-bubble-map {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 14px;
  padding: 34px;
  align-content: center;
}

.map-pin {
  position: relative;
  min-height: 48px;
  border: none;
  border-radius: 999px;
  color: white;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.20);
  backdrop-filter: blur(10px);
  cursor: pointer;
  animation: pinPulse 3s ease-in-out infinite;
  animation-delay: var(--delay);
  overflow: hidden;
}

.map-pin::before {
  content: "";
  width: var(--size);
  height: var(--size);
  border-radius: 999px;
  background: #38bdf8;
  box-shadow: 0 0 24px rgba(56,189,248,0.65);
  position: absolute;
  left: 8px;
  top: 50%;
  transform: translateY(-50%);
}

.map-pin span,
.map-pin b {
  display: block;
  padding-left: 28px;
  text-align: left;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.map-pin span {
  font-size: 11px;
  font-weight: 900;
}

.map-pin b {
  font-size: 10px;
  opacity: .8;
}

.europe-bubble-map .map-pin {
  min-height: 86px;
  border-radius: 24px;
}

.europe-bubble-map .map-pin::before {
  left: 50%;
  top: 20px;
  transform: translateX(-50%);
}

.europe-bubble-map .map-pin span,
.europe-bubble-map .map-pin b {
  padding-left: 0;
  text-align: center;
  margin-top: 30px;
}

@keyframes pinPulse {
  0%, 100% { transform: scale(1); background: rgba(255,255,255,0.12); }
  50% { transform: scale(1.035); background: rgba(255,255,255,0.18); }
}

.map-rank-card h3 {
  margin-top: 0;
  color: #0f172a;
  font-size: 24px;
}

.rank-list {
  display: grid;
  gap: 12px;
}

.rank-row {
  display: grid;
  grid-template-columns: 34px 1fr auto;
  gap: 12px;
  align-items: center;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 12px;
}

.rank-row > span {
  width: 34px;
  height: 34px;
  border-radius: 999px;
  background: #dbeafe;
  color: #1d4ed8;
  display: grid;
  place-items: center;
  font-weight: 950;
}

.rank-row strong,
.rank-row small {
  display: block;
}

.rank-row small {
  color: #64748b;
}

.rank-row b {
  color: #0f172a;
}

.map-warning {
  margin-top: 16px;
  border-radius: 18px;
  background: #fff7ed;
  border: 1px solid #fed7aa;
  color: #9a3412;
  padding: 14px;
  line-height: 1.5;
  font-weight: 750;
}

/* Deeper OncoKids game */

.advanced-kids .kids-game-hero {
  grid-template-columns: 0.95fr 1.05fr;
  gap: 26px;
}

.kids-hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.kids-reset-btn {
  border: none;
  border-radius: 999px;
  padding: 14px 20px;
  background: white;
  color: #c2410c;
  font-weight: 950;
  cursor: pointer;
  border: 1px solid #fed7aa;
}

.badge-row,
.reward-badges {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 16px;
}

.badge-row span,
.reward-badges span {
  width: 44px;
  height: 44px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: white;
  border: 1px solid #fed7aa;
  font-size: 22px;
  box-shadow: 0 10px 24px rgba(15,23,42,0.10);
  animation: badgePop .45s ease both;
}

@keyframes badgePop {
  from { transform: scale(.5); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.character-stage {
  position: relative;
  min-height: 440px;
  border-radius: 38px;
  background:
    radial-gradient(circle at 50% 20%, rgba(255,255,255,0.74), transparent 28%),
    linear-gradient(180deg, rgba(186,230,253,0.80), rgba(220,252,231,0.82));
  border: 1px solid rgba(255,255,255,0.9);
  box-shadow: 0 28px 90px rgba(15,23,42,0.14);
  overflow: hidden;
}

.cloud {
  position: absolute;
  width: 130px;
  height: 50px;
  background: rgba(255,255,255,0.82);
  border-radius: 999px;
  filter: blur(.2px);
  animation: cloudMove 9s ease-in-out infinite;
}

.cloud::before,
.cloud::after {
  content: "";
  position: absolute;
  border-radius: 999px;
  background: inherit;
}

.cloud::before {
  width: 58px;
  height: 58px;
  left: 20px;
  top: -24px;
}

.cloud::after {
  width: 78px;
  height: 78px;
  right: 20px;
  top: -38px;
}

.c1 {
  left: 12%;
  top: 18%;
}

.c2 {
  right: 12%;
  top: 30%;
  animation-delay: 1.2s;
}

@keyframes cloudMove {
  0%, 100% { transform: translateX(0); }
  50% { transform: translateX(18px); }
}

.rainbow-arc {
  position: absolute;
  width: 360px;
  height: 180px;
  left: 50%;
  top: 26%;
  transform: translateX(-50%);
  border-radius: 360px 360px 0 0;
  border-top: 18px solid rgba(251,146,60,0.7);
  box-shadow:
    0 -18px 0 rgba(244,114,182,0.45),
    0 -36px 0 rgba(96,165,250,0.45),
    0 -54px 0 rgba(45,212,191,0.45);
  opacity: .75;
}

.character-path {
  position: absolute;
  left: 8%;
  right: 8%;
  bottom: 82px;
  height: 120px;
}

.path-line {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 28px;
  height: 14px;
  border-radius: 999px;
  background: rgba(34,197,94,0.35);
}

.kid-character {
  position: absolute;
  bottom: 34px;
  transform: translateX(-50%);
  transition: left .7s cubic-bezier(.2,.8,.2,1);
  animation: characterBounce 1.8s ease-in-out infinite;
}

.kid-face {
  width: 68px;
  height: 68px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: #fff7ed;
  border: 3px solid #fed7aa;
  font-size: 34px;
  box-shadow: 0 12px 28px rgba(15,23,42,0.16);
}

.kid-body {
  width: 50px;
  height: 58px;
  margin: -4px auto 0;
  border-radius: 20px 20px 24px 24px;
  background: linear-gradient(135deg, #60a5fa, #a78bfa);
}

@keyframes characterBounce {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(-8px); }
}

.stage-label {
  position: absolute;
  left: 24px;
  bottom: 24px;
  right: 24px;
  padding: 14px;
  border-radius: 20px;
  background: rgba(255,255,255,0.72);
  color: #7c2d12;
  font-weight: 950;
  text-align: center;
}

.kids-game-grid.advanced {
  grid-template-columns: repeat(3, 1fr);
}

.kids-game-card.wide {
  grid-column: span 2;
}

.choice-grid {
  display: grid;
  gap: 10px;
  margin-top: 14px;
}

.choice-grid button {
  text-align: left;
}

.quiz-result {
  margin-top: 14px;
  border-radius: 18px;
  padding: 14px;
  font-weight: 900;
}

.quiz-result.good {
  background: #dcfce7;
  color: #166534;
}

.quiz-result.try {
  background: #ffedd5;
  color: #9a3412;
}

.breathing-game-row {
  display: grid;
  grid-template-columns: 180px 1fr;
  gap: 18px;
  align-items: center;
}

.reward-card {
  background: rgba(255,255,255,0.86);
}

@media (max-width: 1100px) {
  .map-dashboard,
  .advanced-kids .kids-game-hero,
  .kids-game-grid.advanced {
    grid-template-columns: 1fr;
  }

  .kids-game-card.wide {
    grid-column: span 1;
  }

  .map-summary {
    grid-template-columns: 1fr;
  }

  .turkiye-pin-map {
    grid-template-columns: repeat(5, 1fr);
  }

  .europe-bubble-map {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 700px) {
  .turkiye-pin-map {
    grid-template-columns: repeat(3, 1fr);
    padding: 16px;
  }

  .europe-bubble-map {
    grid-template-columns: repeat(2, 1fr);
    padding: 16px;
  }

  .breathing-game-row {
    grid-template-columns: 1fr;
  }

  .character-stage {
    min-height: 360px;
  }
}
'''

css_path.write_text(css, encoding="utf-8")

print("✅ Step 18 applied: deeper OncoKids gamification and interactive cancer map simulator.")
