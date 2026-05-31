from pathlib import Path
import re

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) selectedMapItem state yoksa ekle
if "const [selectedMapItem, setSelectedMapItem]" not in app:
    app = app.replace(
        'const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");',
        '''const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");
  const [selectedMapItem, setSelectedMapItem] = useState(null);'''
    )

# 2) Harita pinlerini kesin tıklanabilir yap
# className="map-pin" olan buttonlara onClick ve selected class ekle
app = app.replace(
    'className="map-pin"',
    'className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}'
)

# Eğer onClick yoksa style öncesine ekle
app = app.replace(
    '''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    style={{''',
    '''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    onClick={() => setSelectedMapItem(item)}
                    style={{'''
)

# Bazı dosyalarda boşluk farklı olabilir
app = app.replace(
    '''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    onClick={() => setSelectedMapItem(item)}
                    onClick={() => setSelectedMapItem(item)}''',
    '''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    onClick={() => setSelectedMapItem(item)}'''
)

# 3) Harita içine floating detail card ekle
# Map pin container içinde mapData.map bittikten sonra detail kartını koyacağız.
if "map-floating-detail-v25" not in app:
    target = '''                {mapData.map((item, index) => (
                  <button'''
    
    if target not in app:
        print("⚠️ mapData.map target not found. Trying alternative target.")
    else:
        # Sadece map container'a selectedMapItem detayını mapData map bloğundan sonra eklemek için
        # En güvenli yöntem: map caption varsa onun önüne ekle.
        caption_target = '''                <div className="map-caption">'''
        floating_detail = r'''                {selectedMapItem && (
                  <div className="map-floating-detail-v25">
                    <button className="close-map-detail" onClick={() => setSelectedMapItem(null)}>×</button>
                    <small>{lang === "tr" ? "Seçili bölge" : "Selected area"}</small>
                    <h3>{selectedMapItem.name}</h3>

                    <div className="floating-detail-grid">
                      <div>
                        <span>{lang === "tr" ? "Vaka göstergesi" : "Incidence indicator"}</span>
                        <strong>{selectedMapItem.value?.toLocaleString?.() || "-"}</strong>
                      </div>
                      <div>
                        <span>{lang === "tr" ? "Ölüm göstergesi" : "Mortality indicator"}</span>
                        <strong>{selectedMapItem.mortality?.toLocaleString?.() || "-"}</strong>
                      </div>
                      <div>
                        <span>{lang === "tr" ? "Sağkalım / prevalans" : "Survival / prevalence"}</span>
                        <strong>{selectedMapItem.survival?.toLocaleString?.() || "-"}</strong>
                      </div>
                      <div>
                        <span>{lang === "tr" ? "Yıl ayarlı değişim" : "Year-adjusted change"}</span>
                        <strong>+{selectedMapItem.growth || 0}%</strong>
                      </div>
                    </div>

                    {selectedMapItem.breakdown?.length > 0 && (
                      <div className="floating-breakdown">
                        <b>{lang === "tr" ? "Kanser türü kırılımı" : "Cancer type breakdown"}</b>
                        {selectedMapItem.breakdown.slice(0, 4).map((b) => (
                          <p key={b.name}>
                            <span>{b.name}</span>
                            <strong>{b.incidence?.toLocaleString?.() || b.incidence}</strong>
                          </p>
                        ))}
                      </div>
                    )}

                    <div className="floating-source">
                      {selectedMapItem.sourceMode === "official" ? "Official GLOBOCAN layer" : "CSV data layer"}
                    </div>
                  </div>
                )}

'''
        if caption_target in app:
            app = app.replace(caption_target, floating_detail + caption_target, 1)
        else:
            print("⚠️ map-caption not found. Floating detail not inserted.")

# 4) Top list satırlarına tıklama ekle
app = app.replace(
    '<div className="rank-row" key={item.name}>',
    '<button className="rank-row clickable-rank" key={item.name} onClick={() => setSelectedMapItem(item)}>'
)

# Sadece ilk uygun rank kapanışını div -> button yapmaya çalış
app = app.replace(
    '''                  </div>
                ))}
              </div>''',
    '''                  </button>
                ))}
              </div>''',
    1
)

# 5) Eğer mapData objelerinde detail alanları yoksa en azından default değerler ekle
# CSV map return objesinde mortality/survival/breakdown yoksa kırılmasın diye fallback zaten JSX'te var.

# CSS
css += r'''

/* Step 25: force clickable map detail popup and remove empty visual space */

/* Pin click stability */
.image-pin-map,
.turkiye-pin-map,
.europe-bubble-map {
  position: relative !important;
}

.map-pin {
  cursor: pointer !important;
  pointer-events: auto !important;
}

.map-pin.selected {
  background: #fbbf24 !important;
  transform: translate(-50%, -50%) scale(1.95) !important;
  z-index: 90 !important;
  box-shadow:
    0 0 0 12px rgba(251,191,36,0.20),
    0 0 46px rgba(251,191,36,0.95) !important;
}

.map-pin:hover {
  transform: translate(-50%, -50%) scale(1.65) !important;
}

/* Detail card appears directly on the map */
.map-floating-detail-v25 {
  position: absolute;
  right: 24px;
  top: 24px;
  width: min(360px, calc(100% - 48px));
  z-index: 120;
  border-radius: 26px;
  padding: 20px;
  background: rgba(255,255,255,0.94);
  border: 1px solid rgba(255,255,255,0.88);
  box-shadow: 0 26px 80px rgba(0,0,0,0.28);
  backdrop-filter: blur(18px);
  color: #0f172a;
  animation: detailPop .25s ease both;
}

@keyframes detailPop {
  from {
    opacity: 0;
    transform: translateY(-8px) scale(.97);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.close-map-detail {
  position: absolute;
  right: 14px;
  top: 12px;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 999px;
  background: #0f172a;
  color: white;
  font-size: 22px;
  cursor: pointer;
  line-height: 1;
}

.map-floating-detail-v25 small {
  display: block;
  color: #64748b;
  font-weight: 950;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.map-floating-detail-v25 h3 {
  margin: 6px 36px 14px 0;
  font-size: 30px;
  color: #0f172a;
  line-height: 1;
}

.floating-detail-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}

.floating-detail-grid div {
  border-radius: 16px;
  padding: 12px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
}

.floating-detail-grid span,
.floating-detail-grid strong {
  display: block;
}

.floating-detail-grid span {
  color: #64748b;
  font-size: 12px;
  font-weight: 850;
}

.floating-detail-grid strong {
  margin-top: 4px;
  color: #0f172a;
  font-size: 21px;
}

.floating-breakdown {
  margin-top: 14px;
  display: grid;
  gap: 7px;
}

.floating-breakdown > b {
  color: #0f172a;
}

.floating-breakdown p {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px;
  margin: 0;
  border-radius: 12px;
  background: #eff6ff;
  padding: 8px 10px;
}

.floating-breakdown span {
  color: #334155;
  font-weight: 850;
}

.floating-breakdown strong {
  color: #1d4ed8;
}

.floating-source {
  display: inline-flex;
  margin-top: 12px;
  border-radius: 999px;
  padding: 8px 11px;
  background: #eef2ff;
  color: #3730a3;
  font-weight: 950;
  font-size: 13px;
}

/* Rank list clickable */
.clickable-rank {
  width: 100%;
  border: none;
  text-align: left;
  cursor: pointer;
}

.clickable-rank:hover {
  background: #eef2ff;
}

/* Remove giant empty spaces around map */
.premium-map-dashboard,
.map-dashboard {
  align-items: start !important;
}

.map-visual-card,
.premium-map-card {
  min-height: auto !important;
  padding-bottom: 18px !important;
}

.turkiye-pin-map,
.europe-bubble-map,
.image-pin-map {
  min-height: 520px !important;
}

.map-rank-card {
  min-height: auto !important;
}

/* OncoKids: reduce empty hero area and add more game-like right side */
.kids-game-page {
  background-position: center top !important;
}

.kids-game-nav {
  position: sticky !important;
  top: 10px !important;
  max-width: 1180px !important;
  padding: 10px 20px !important;
}

.kids-game-nav .ghost-btn {
  background: rgba(255,255,255,0.86) !important;
  color: #7c2d12 !important;
  border: 1px solid rgba(251,146,60,0.30) !important;
  border-radius: 999px !important;
  padding: 10px 16px !important;
  font-weight: 950 !important;
  text-decoration: none !important;
  box-shadow: 0 12px 32px rgba(15,23,42,0.10) !important;
}

.kids-game-nav .ghost-btn::before {
  content: "🏠 ";
}

.kids-game-hero {
  min-height: auto !important;
  padding: 18px 24px 16px !important;
  align-items: center !important;
}

.kids-hero-overlay {
  max-width: 540px !important;
  padding: 26px !important;
}

.kids-hero-overlay h1 {
  font-size: clamp(42px, 5vw, 64px) !important;
  margin-bottom: 12px !important;
}

.kids-hero-overlay p {
  font-size: 18px !important;
  line-height: 1.55 !important;
}

.character-stage {
  min-height: 340px !important;
  display: block !important;
}

.hope-journey {
  margin-top: 0 !important;
  padding-top: 0 !important;
}

.hope-journey h2 {
  margin-top: 0 !important;
}

/* If character stage is missing/transparent, make it visible with content */
.character-stage::after {
  content: "🎈 Complete quests, collect badges, and help Lumi move forward.";
  position: absolute;
  left: 24px;
  right: 24px;
  bottom: 22px;
  padding: 14px 16px;
  border-radius: 20px;
  background: rgba(255,255,255,0.78);
  color: #7c2d12;
  font-weight: 950;
  text-align: center;
  box-shadow: 0 12px 32px rgba(15,23,42,0.10);
}

@media (max-width: 900px) {
  .map-floating-detail-v25 {
    left: 16px;
    right: 16px;
    top: 16px;
    width: auto;
  }

  .floating-detail-grid {
    grid-template-columns: 1fr;
  }

  .turkiye-pin-map,
  .europe-bubble-map,
  .image-pin-map {
    min-height: 430px !important;
  }

  .kids-game-hero {
    grid-template-columns: 1fr !important;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Step 25 applied: map pin detail card forced, rank rows clickable, empty spaces reduced.")
