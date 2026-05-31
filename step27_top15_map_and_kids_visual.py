from pathlib import Path

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# State ekle
if "const [showAllMapPins, setShowAllMapPins]" not in app:
    app = app.replace(
        'const [selectedMapItem, setSelectedMapItem] = useState(null);',
        '''const [selectedMapItem, setSelectedMapItem] = useState(null);
  const [showAllMapPins, setShowAllMapPins] = useState(false);'''
    )

# Pin render edilen mapData.map kısmını filtreli hale getir
app = app.replace(
    '{mapData.map((item, index) => (',
    '''{[...mapData]
                    .sort((a, b) => b.value - a.value)
                    .slice(0, showAllMapPins ? mapData.length : 15)
                    .map((item, index) => ('''
)

# Harita içine Show all / Top 15 butonu ekle
if "show-all-map-toggle-v27" not in app:
    target = '''{selectedMapItem && (
                  <div className="map-floating-detail-v25">'''
    insert = r'''<button
                  className="show-all-map-toggle-v27"
                  onClick={() => {
                    setShowAllMapPins(!showAllMapPins);
                    setSelectedMapItem(null);
                  }}
                >
                  {showAllMapPins
                    ? (lang === "tr" ? "Sadece Top 15 göster" : "Show Top 15 only")
                    : (lang === "tr" ? "Tüm pinleri göster" : "Show all provinces")}
                </button>

                '''
    app = app.replace(target, insert + target)

# OncoKids sağ tarafı doldurmak için karakter paneli CSS ile güçlendir
css += r'''

/* Step 27: Top 15 map pins + cleaner map + OncoKids visual panel */

.show-all-map-toggle-v27 {
  position: absolute;
  left: 24px;
  top: 24px;
  z-index: 150;
  border: none;
  border-radius: 999px;
  padding: 12px 16px;
  background: rgba(255,255,255,0.92);
  color: #0f172a;
  font-weight: 950;
  cursor: pointer;
  box-shadow: 0 16px 44px rgba(0,0,0,0.20);
  backdrop-filter: blur(14px);
}

.show-all-map-toggle-v27:hover {
  transform: translateY(-1px);
  background: white;
}

/* Top 15 modunda pinler daha temiz görünsün */
.turkiye-pin-map .map-pin,
.europe-bubble-map .map-pin,
.image-pin-map .map-pin {
  width: 20px !important;
  height: 20px !important;
  min-width: 20px !important;
  min-height: 20px !important;
}

.turkiye-pin-map .map-pin.selected,
.europe-bubble-map .map-pin.selected,
.image-pin-map .map-pin.selected {
  width: 34px !important;
  height: 34px !important;
}

/* Harita görseli daha tam otursun */
.turkiye-pin-map,
.europe-bubble-map {
  background-size: contain !important;
  background-repeat: no-repeat !important;
  background-position: center center !important;
  background-color: #06182f !important;
  min-height: 620px !important;
}

/* OncoKids sağ alanı boş kalmasın: büyük oyun paneli */
.character-stage {
  min-height: 420px !important;
  background:
    radial-gradient(circle at 50% 22%, rgba(255,255,255,0.82), transparent 24%),
    linear-gradient(180deg, rgba(186,230,253,0.82), rgba(220,252,231,0.88)) !important;
}

.character-stage::before {
  content: "😊";
  position: absolute;
  left: 50%;
  top: 38%;
  transform: translate(-50%, -50%);
  width: 150px;
  height: 150px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: rgba(255,255,255,0.82);
  border: 4px solid rgba(251,146,60,0.38);
  box-shadow: 0 28px 80px rgba(15,23,42,0.18);
  font-size: 78px;
  animation: kidSmileFloat 4s ease-in-out infinite;
}

.character-stage::after {
  content: "Lumi helps children collect hope points, name feelings and prepare gentle questions.";
  position: absolute;
  left: 28px;
  right: 28px;
  bottom: 28px;
  padding: 18px 20px;
  border-radius: 24px;
  background: rgba(255,255,255,0.84);
  color: #7c2d12;
  font-weight: 950;
  text-align: center;
  line-height: 1.45;
  box-shadow: 0 18px 46px rgba(15,23,42,0.12);
}

@keyframes kidSmileFloat {
  0%, 100% { transform: translate(-50%, -50%) translateY(0); }
  50% { transform: translate(-50%, -50%) translateY(-12px); }
}

/* OncoKids alt boşlukları azalt */
.kids-game-grid.advanced {
  margin-top: -12px !important;
}

.reward-card,
.kids-game-card.reward-card {
  min-height: 180px !important;
}

@media (max-width: 900px) {
  .turkiye-pin-map,
  .europe-bubble-map {
    min-height: 460px !important;
  }

  .show-all-map-toggle-v27 {
    left: 16px;
    top: 16px;
  }

  .character-stage::before {
    width: 110px;
    height: 110px;
    font-size: 56px;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Step 27 applied: map defaults to Top 15 pins, show-all toggle added, OncoKids visual panel improved.")
