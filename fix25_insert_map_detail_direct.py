from pathlib import Path
import re

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# selectedMapItem state yoksa ekle
if "const [selectedMapItem, setSelectedMapItem]" not in app:
    app = app.replace(
        'const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");',
        '''const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");
  const [selectedMapItem, setSelectedMapItem] = useState(null);'''
    )

# Pinlere selected class + onClick ekle
app = app.replace(
    'className="map-pin"',
    'className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}'
)

app = app.replace(
    '''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    style={{''',
    '''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    onClick={() => setSelectedMapItem(item)}
                    style={{'''
)

# Duplicate onClick temizle
app = app.replace(
    '''onClick={() => setSelectedMapItem(item)}
                    onClick={() => setSelectedMapItem(item)}''',
    '''onClick={() => setSelectedMapItem(item)}'''
)

detail = r'''
                {selectedMapItem && (
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

# mapData.map bittikten hemen sonra detay kartını ekle
if "map-floating-detail-v25" not in app:
    pattern = r'''(\{mapData\.map\(\(item, index\) => \([\s\S]*?</button>\s*\)\)\})'''
    app, count = re.subn(pattern, r"\1\n" + detail, app, count=1)

    if count != 1:
        raise RuntimeError("mapData.map block bulunamadı. App.jsx içindeki harita JSX'i değişmiş olabilir.")
    print("✅ Floating detail inserted.")
else:
    print("ℹ️ Floating detail already exists.")

css += r'''

/* Force map detail popup */
.turkiye-pin-map,
.europe-bubble-map,
.image-pin-map {
  position: relative !important;
}

.map-pin {
  cursor: pointer !important;
  pointer-events: auto !important;
}

.map-pin.selected {
  background: #fbbf24 !important;
  transform: translate(-50%, -50%) scale(1.9) !important;
  z-index: 90 !important;
}

.map-floating-detail-v25 {
  position: absolute;
  right: 24px;
  top: 24px;
  width: min(360px, calc(100% - 48px));
  z-index: 200;
  border-radius: 26px;
  padding: 20px;
  background: rgba(255,255,255,0.96);
  border: 1px solid rgba(255,255,255,0.9);
  box-shadow: 0 26px 80px rgba(0,0,0,0.28);
  backdrop-filter: blur(18px);
  color: #0f172a;
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
  font-size: 21px;
}

.floating-breakdown {
  margin-top: 14px;
  display: grid;
  gap: 7px;
}

.floating-breakdown p {
  display: grid;
  grid-template-columns: 1fr auto;
  margin: 0;
  border-radius: 12px;
  background: #eff6ff;
  padding: 8px 10px;
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

/* OncoKids boşluk azaltma */
.kids-game-hero {
  min-height: auto !important;
  padding-bottom: 12px !important;
}

.kids-game-grid.advanced {
  margin-top: -20px !important;
}

.kids-game-card {
  min-height: 220px !important;
}

.reward-card,
.kids-game-card.reward-card {
  min-height: 220px !important;
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Fix applied.")
