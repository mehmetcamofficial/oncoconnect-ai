from pathlib import Path
import re

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) selectedMapItem state yoksa ekle
if "selectedMapItem" not in app:
    app = app.replace(
        'const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");',
        '''const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");
  const [selectedMapItem, setSelectedMapItem] = useState(null);'''
    )

# 2) map pin buttonlarını tıklanabilir yap
# Eski map-pin className satırını bulup selected class ve onClick ekler.
app = app.replace(
'''className="map-pin"
                    style={{''',
'''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    onClick={() => setSelectedMapItem(item)}
                    style={{'''
)

# Eğer className zaten template değilse ama tek satır farklıysa alternatif patch
app = app.replace(
'''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    style={{''',
'''className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    onClick={() => setSelectedMapItem(item)}
                    style={{'''
)

# 3) Sağ panelde detay görünmesi için rank panel başlığını genişlet
# Eğer daha önce eklenmediyse map-rank-card içine seçili detay paneli ekler.
if "selected-map-detail-panel-v24" not in app:
    app = app.replace(
'''<div className="map-rank-card">
              <h3>{lang === "tr" ? "En yüksek alanlar" : "Highest areas"}</h3>''',
'''<div className="map-rank-card selected-map-detail-panel-v24">
              {selectedMapItem ? (
                <>
                  <h3>{selectedMapItem.name}</h3>

                  <div className="selected-map-detail">
                    <div className="detail-kpis">
                      <div>
                        <small>{lang === "tr" ? "Vaka göstergesi" : "Incidence indicator"}</small>
                        <strong>{selectedMapItem.value?.toLocaleString?.() || "-"}</strong>
                      </div>
                      <div>
                        <small>{lang === "tr" ? "Ölüm göstergesi" : "Mortality indicator"}</small>
                        <strong>{selectedMapItem.mortality?.toLocaleString?.() || "-"}</strong>
                      </div>
                      <div>
                        <small>{lang === "tr" ? "Sağkalım / prevalans" : "Survival / prevalence"}</small>
                        <strong>{selectedMapItem.survival?.toLocaleString?.() || "-"}</strong>
                      </div>
                      <div>
                        <small>{lang === "tr" ? "Yıl ayarlı değişim" : "Year-adjusted change"}</small>
                        <strong>+{selectedMapItem.growth || 0}%</strong>
                      </div>
                    </div>

                    <div className="detail-source-pill">
                      {selectedMapItem.sourceMode === "official"
                        ? "Official GLOBOCAN layer"
                        : "CSV data layer"}
                    </div>

                    {selectedMapItem.breakdown?.length > 0 && (
                      <div className="breakdown-list">
                        <strong>{lang === "tr" ? "Kanser türü kırılımı" : "Cancer type breakdown"}</strong>
                        {selectedMapItem.breakdown.map((b) => (
                          <div key={b.name} className="breakdown-row">
                            <span>{b.name}</span>
                            <b>{b.incidence?.toLocaleString?.() || b.incidence}</b>
                          </div>
                        ))}
                      </div>
                    )}

                    <button className="clear-selection" onClick={() => setSelectedMapItem(null)}>
                      {lang === "tr" ? "Seçimi temizle" : "Clear selection"}
                    </button>
                  </div>
                </>
              ) : (
                <>
                  <h3>{lang === "tr" ? "Harita detayı" : "Map details"}</h3>
                  <p className="map-click-hint">
                    {lang === "tr"
                      ? "Detayları görmek için Türkiye veya Avrupa haritasındaki bir pine tıklayın."
                      : "Click a pin on the Türkiye or Europe map to see details."}
                  </p>
                </>
              )}'''
    )

# 4) Eğer başlık hâlâ "Highest simulated areas" ise onu da yakala
if "selected-map-detail-panel-v24" not in app:
    app = app.replace(
'''<div className="map-rank-card">
              <h3>{lang === "tr" ? "En yüksek simüle edilen alanlar" : "Highest simulated areas"}</h3>''',
'''<div className="map-rank-card selected-map-detail-panel-v24">
              {selectedMapItem ? (
                <>
                  <h3>{selectedMapItem.name}</h3>

                  <div className="selected-map-detail">
                    <div className="detail-kpis">
                      <div>
                        <small>{lang === "tr" ? "Vaka göstergesi" : "Incidence indicator"}</small>
                        <strong>{selectedMapItem.value?.toLocaleString?.() || "-"}</strong>
                      </div>
                      <div>
                        <small>{lang === "tr" ? "Ölüm göstergesi" : "Mortality indicator"}</small>
                        <strong>{selectedMapItem.mortality?.toLocaleString?.() || "-"}</strong>
                      </div>
                      <div>
                        <small>{lang === "tr" ? "Sağkalım / prevalans" : "Survival / prevalence"}</small>
                        <strong>{selectedMapItem.survival?.toLocaleString?.() || "-"}</strong>
                      </div>
                    </div>

                    <button className="clear-selection" onClick={() => setSelectedMapItem(null)}>
                      {lang === "tr" ? "Seçimi temizle" : "Clear selection"}
                    </button>
                  </div>
                </>
              ) : (
                <>
                  <h3>{lang === "tr" ? "Harita detayı" : "Map details"}</h3>
                  <p className="map-click-hint">
                    {lang === "tr"
                      ? "Detayları görmek için haritadaki bir pine tıklayın."
                      : "Click a map pin to see details."}
                  </p>
                </>
              )}'''
    )

# 5) Rank satırlarını da tıklanabilir yap
app = app.replace(
'''<div className="rank-row" key={item.name}>''',
'''<button className="rank-row clickable-rank" key={item.name} onClick={() => setSelectedMapItem(item)}>'''
)

app = app.replace(
'''</div>
                ))}
              </div>''',
'''</button>
                ))}
              </div>''',
1
)

# 6) OncoKids home butonunu daha güzel yapmak için CSS ekle
css += r'''

/* Fix 24: clickable map detail panel + stable pins + better OncoKids nav */

.map-pin {
  cursor: pointer !important;
}

.map-pin.selected {
  background: #fbbf24 !important;
  transform: translate(-50%, -50%) scale(1.9) !important;
  z-index: 80 !important;
  box-shadow:
    0 0 0 12px rgba(251,191,36,0.22),
    0 0 44px rgba(251,191,36,0.9) !important;
}

.map-pin:hover {
  transform: translate(-50%, -50%) scale(1.65) !important;
}

.selected-map-detail {
  border-radius: 24px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 16px;
  margin-bottom: 18px;
}

.detail-kpis {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.detail-kpis div {
  border-radius: 16px;
  background: white;
  border: 1px solid #e2e8f0;
  padding: 12px;
}

.detail-kpis small,
.detail-kpis strong {
  display: block;
}

.detail-kpis small {
  color: #64748b;
  font-weight: 850;
}

.detail-kpis strong {
  margin-top: 4px;
  font-size: 24px;
  color: #0f172a;
}

.detail-source-pill {
  display: inline-flex;
  margin-top: 14px;
  border-radius: 999px;
  padding: 8px 12px;
  background: #eef2ff;
  color: #3730a3;
  font-weight: 950;
}

.breakdown-list {
  display: grid;
  gap: 8px;
  margin-top: 14px;
}

.breakdown-list > strong {
  color: #0f172a;
}

.breakdown-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  border-radius: 14px;
  background: white;
  border: 1px solid #e2e8f0;
  padding: 10px 12px;
}

.breakdown-row span {
  color: #334155;
  font-weight: 850;
}

.breakdown-row b {
  color: #1d4ed8;
}

.clear-selection {
  margin-top: 14px;
  border: none;
  background: #0f172a;
  color: white;
  border-radius: 999px;
  padding: 10px 14px;
  font-weight: 950;
  cursor: pointer;
}

.map-click-hint {
  color: #475569;
  line-height: 1.55;
  margin-bottom: 16px;
}

.clickable-rank {
  width: 100%;
  border: none;
  text-align: left;
  cursor: pointer;
}

.clickable-rank:hover {
  background: #eef2ff;
}

.kids-game-nav {
  top: 12px !important;
  padding: 10px 20px !important;
}

.kids-game-nav .ghost-btn {
  background: rgba(255,255,255,0.82) !important;
  color: #7c2d12 !important;
  border: 1px solid rgba(251,146,60,0.28) !important;
  border-radius: 999px !important;
  padding: 10px 16px !important;
  font-weight: 950 !important;
  box-shadow: 0 12px 32px rgba(15,23,42,0.10) !important;
}

.kids-game-nav .ghost-btn:hover {
  background: #fff7ed !important;
  transform: translateY(-1px);
}

.kids-game-hero {
  min-height: 520px !important;
  padding-top: 8px !important;
}

.kids-hero-overlay {
  max-width: 560px !important;
  padding: 28px !important;
}

.kids-hero-overlay h1 {
  font-size: clamp(44px, 5vw, 68px) !important;
}

.character-stage {
  min-height: 360px !important;
}

.hope-journey {
  margin-top: -16px !important;
}

@media (max-width: 700px) {
  .detail-kpis {
    grid-template-columns: 1fr;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Fix 24 applied: map pins clickable, detail panel added, OncoKids Home button improved.")
