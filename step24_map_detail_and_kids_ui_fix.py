from pathlib import Path

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# Ensure selectedMapItem state exists
if "const [selectedMapItem, setSelectedMapItem]" not in app:
    app = app.replace(
        '''  const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");''',
        '''  const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");
  const [selectedMapItem, setSelectedMapItem] = useState(null);'''
    )

# Replace full cancer map simulator JSX with cleaner, clickable version
start_marker = '        <section className="cancer-map-simulator">'
end_marker = '        <section className="prevention-simulator-section">'

start = app.find(start_marker)
end = app.find(end_marker)

if start == -1 or end == -1 or end <= start:
    raise RuntimeError("Could not find cancer-map-simulator section or prevention-simulator-section marker.")

new_map_section = r'''        <section className="cancer-map-simulator premium-map-section">
          <div className="section-intro">
            <p className="eyebrow dark">{lang === "tr" ? "İNTERAKTİF KANSER HARİTASI" : "INTERACTIVE CANCER MAP"}</p>
            <h2>
              {lang === "tr"
                ? "Türkiye ve Avrupa için filtrelenebilir kanser veri haritası"
                : "Filterable cancer data map for Türkiye and Europe"}
            </h2>
            <p>
              {lang === "tr"
                ? "Harita, CSV veri katmanı ve mevcut resmî ülke geneli veri katmanını birlikte kullanır. İl/ülke pinlerine tıklayarak detayları görebilirsiniz."
                : "The map combines the CSV data layer with the current official country-level layer. Click pins to inspect details."}
            </p>
          </div>

          <div className="map-controls premium-controls">
            <button className={mapMode === "turkiye" ? "active" : ""} onClick={() => { setMapMode("turkiye"); setSelectedMapItem(null); }}>
              Türkiye
            </button>
            <button className={mapMode === "europe" ? "active" : ""} onClick={() => { setMapMode("europe"); setSelectedMapItem(null); }}>
              Europe
            </button>

            <select value={mapGender} onChange={(e) => { setMapGender(e.target.value); setSelectedMapItem(null); }}>
              <option value="total">{lang === "tr" ? "Toplam" : "Total"}</option>
              <option value="female">{lang === "tr" ? "Kadın" : "Female"}</option>
              <option value="male">{lang === "tr" ? "Erkek" : "Male"}</option>
            </select>

            <select value={selectedCancerType} onChange={(e) => { setSelectedCancerType(e.target.value); setSelectedMapItem(null); }}>
              <option value="all">{lang === "tr" ? "Tüm kanser türleri" : "All cancer types"}</option>
              {cancerTypeOptions.map((type) => (
                <option key={type} value={type}>{type}</option>
              ))}
            </select>

            <select value={selectedAgeGroup} onChange={(e) => { setSelectedAgeGroup(e.target.value); setSelectedMapItem(null); }}>
              <option value="all">{lang === "tr" ? "Tüm yaş grupları" : "All age groups"}</option>
              {ageGroupOptions.map((age) => (
                <option key={age} value={age}>{age}</option>
              ))}
            </select>

            <div className="year-slider">
              <strong>{mapYear}</strong>
              <input type="range" min="2020" max="2026" value={mapYear} onChange={(e) => { setMapYear(Number(e.target.value)); setSelectedMapItem(null); }} />
            </div>
          </div>

          <div className="map-dashboard premium-map-dashboard">
            <div className="map-visual-card premium-map-card">
              <div className="map-summary compact-summary">
                <div>
                  <small>{lang === "tr" ? "Görselleştirme toplamı" : "Visualization total"}</small>
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

              <div className={mapMode === "turkiye" ? "turkiye-pin-map image-pin-map" : "europe-bubble-map image-pin-map"}>
                {mapData.map((item, index) => (
                  <button
                    key={item.name}
                    type="button"
                    className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    onClick={() => setSelectedMapItem(item)}
                    style={{
                      "--size": `${Math.max(14, Math.min(36, item.intensity / 2.6))}px`,
                      "--delay": `${(index % 10) * 0.06}s`
                    }}
                    title={`${item.name}: ${item.value?.toLocaleString?.() || item.value}`}
                  >
                    <span>{item.name}</span>
                    <b>{item.value?.toLocaleString?.() || item.value}</b>
                  </button>
                ))}

                <div className="map-caption">
                  {mapMode === "turkiye"
                    ? (lang === "tr" ? "Türkiye haritası — CSV/veri katmanı pinleri" : "Türkiye map — CSV/data-layer pins")
                    : (lang === "tr" ? "Avrupa haritası — CSV/veri katmanı pinleri" : "Europe map — CSV/data-layer pins")}
                </div>
              </div>
            </div>

            <aside className="map-detail-panel">
              {selectedMapItem ? (
                <>
                  <div className="detail-header">
                    <small>{lang === "tr" ? "Seçili bölge" : "Selected area"}</small>
                    <h3>{selectedMapItem.name}</h3>
                  </div>

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
                </>
              ) : (
                <>
                  <div className="detail-header">
                    <small>{lang === "tr" ? "Harita detayı" : "Map details"}</small>
                    <h3>{lang === "tr" ? "Bir pine tıklayın" : "Click a pin"}</h3>
                  </div>

                  <p className="map-click-hint">
                    {lang === "tr"
                      ? "Ülke veya il pinine tıklayınca burada vaka göstergesi, ölüm göstergesi, sağkalım/prevalans ve kanser türü kırılımı görünecek."
                      : "Click a country or city pin to see incidence indicator, mortality indicator, survival/prevalence and cancer-type breakdown."}
                  </p>

                  <div className="rank-list">
                    {topMapItems.map((item, index) => (
                      <button className="rank-row clickable-rank" key={item.name} onClick={() => setSelectedMapItem(item)}>
                        <span>{index + 1}</span>
                        <div>
                          <strong>{item.name}</strong>
                          <small>{lang === "tr" ? "Yıl ayarlı değişim" : "Year-adjusted change"}: +{item.growth}%</small>
                        </div>
                        <b>{item.value.toLocaleString()}</b>
                      </button>
                    ))}
                  </div>
                </>
              )}

              <div className="map-warning">
                {lang === "tr"
                  ? "Not: CSV veri katmanı görselleştirme göstergesi olarak kullanılır. Resmî il bazlı hasta sayısı doğrulanmadan klinik/epidemiyolojik kesin sayı gibi sunulmamalıdır."
                  : "Note: The CSV data layer is used as a visualization indicator. It should not be presented as official clinical/epidemiological city-level counts unless verified."}
              </div>
            </aside>
          </div>
        </section>

'''

app = app[:start] + new_map_section + app[end:]

# Improve OncoKids hero text/card spacing if page exists
css += r'''

/* Step 24: premium clickable map + OncoKids spacing/navigation fixes */

.premium-map-section {
  max-width: 1240px;
}

.premium-controls {
  position: sticky;
  top: 88px;
  z-index: 12;
  padding: 12px;
  border-radius: 28px;
  background: rgba(255,255,255,0.82);
  border: 1px solid #e2e8f0;
  backdrop-filter: blur(16px);
  box-shadow: 0 18px 60px rgba(15,23,42,0.08);
}

.premium-controls select {
  min-width: 170px;
}

.premium-map-dashboard {
  grid-template-columns: minmax(0, 1.25fr) 420px !important;
  align-items: start;
}

.premium-map-card {
  overflow: hidden;
}

.compact-summary {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.compact-summary div {
  min-height: 96px;
}

.image-pin-map {
  border-radius: 30px;
  min-height: 620px !important;
  position: relative;
}

.image-pin-map .map-pin {
  transition: transform .18s ease, background .18s ease, box-shadow .18s ease;
}

.image-pin-map .map-pin:hover,
.image-pin-map .map-pin.selected {
  background: #fbbf24 !important;
}

.image-pin-map .map-pin.selected {
  transform: translate(-50%, -50%) scale(1.95) !important;
  z-index: 60 !important;
  box-shadow:
    0 0 0 12px rgba(251,191,36,0.20),
    0 0 44px rgba(251,191,36,0.90) !important;
}

.map-caption {
  position: absolute;
  left: 24px;
  bottom: 20px;
  right: 24px;
  color: rgba(255,255,255,0.86);
  font-weight: 950;
  letter-spacing: 0.01em;
  text-shadow: 0 2px 12px rgba(0,0,0,0.36);
}

.map-detail-panel {
  position: sticky;
  top: 164px;
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 30px;
  padding: 24px;
  box-shadow: 0 24px 80px rgba(15,23,42,0.12);
}

.detail-header small {
  display: block;
  color: #64748b;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.12em;
}

.detail-header h3 {
  margin: 6px 0 18px;
  font-size: 32px;
  color: #0f172a;
  line-height: 1;
}

.detail-kpis {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.detail-kpis div {
  border-radius: 18px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 14px;
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
  color: #0f172a;
  font-size: 25px;
}

.detail-source-pill {
  display: inline-flex;
  margin-top: 14px;
  border-radius: 999px;
  padding: 9px 12px;
  background: #eef2ff;
  color: #3730a3;
  font-weight: 950;
}

.breakdown-list {
  margin-top: 18px;
  display: grid;
  gap: 9px;
}

.breakdown-list > strong {
  color: #0f172a;
}

.breakdown-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  border-radius: 15px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 11px 12px;
}

.breakdown-row span {
  color: #334155;
  font-weight: 850;
}

.breakdown-row b {
  color: #1d4ed8;
}

.clear-selection {
  margin-top: 16px;
  border: none;
  background: #0f172a;
  color: white;
  border-radius: 999px;
  padding: 11px 15px;
  font-weight: 950;
  cursor: pointer;
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

.map-click-hint {
  color: #475569;
  line-height: 1.55;
  margin-bottom: 18px;
}

/* OncoKids fixes */
.kids-game-page {
  background-position: center center !important;
}

.kids-game-nav {
  top: 12px !important;
  padding: 10px 20px !important;
  grid-template-columns: auto 1fr auto !important;
}

.kids-game-nav .ghost-btn {
  background: rgba(255,255,255,0.78) !important;
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

.kids-points {
  padding: 10px 18px !important;
}

.kids-game-hero {
  min-height: 540px !important;
  padding-top: 8px !important;
  align-items: center !important;
}

.kids-hero-overlay {
  max-width: 560px !important;
  padding: 28px !important;
}

.kids-hero-overlay h1 {
  font-size: clamp(44px, 5vw, 68px) !important;
}

.kids-hero-overlay p {
  font-size: 18px !important;
}

.character-stage {
  min-height: 380px !important;
}

.hope-journey {
  margin-top: -12px !important;
}

.hope-journey h2 {
  margin-top: 0 !important;
}

@media (max-width: 1100px) {
  .premium-map-dashboard {
    grid-template-columns: 1fr !important;
  }

  .map-detail-panel {
    position: relative;
    top: auto;
  }

  .premium-controls {
    position: relative;
    top: auto;
  }
}

@media (max-width: 700px) {
  .detail-kpis,
  .compact-summary {
    grid-template-columns: 1fr;
  }

  .image-pin-map {
    min-height: 430px !important;
  }

  .kids-game-nav {
    grid-template-columns: 1fr !important;
  }

  .kids-points {
    justify-self: stretch;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Step 24 applied: clickable map detail panel forced, map UX improved, OncoKids spacing and Home button improved.")
