from pathlib import Path

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) Official data state
app = app.replace(
'''  const [mapGender, setMapGender] = useState("total");''',
'''  const [mapGender, setMapGender] = useState("total");
  const [officialCancerMetric, setOfficialCancerMetric] = useState("incidence");'''
)

# 2) Add official data arrays before mapData
app = app.replace(
'''  const mapData = useMemo(() => {''',
'''  const officialTurkeyCancerData = [
    { site: "All cancers", siteTR: "Tüm kanserler", newCases: 240013, deaths: 129672, prevalence5y: 679335 },
    { site: "Lung", siteTR: "Akciğer", newCases: 41032, deaths: 38505, prevalence5y: 54335 },
    { site: "Breast", siteTR: "Meme", newCases: 25249, deaths: 7360, prevalence5y: 100765 },
    { site: "Colorectum", siteTR: "Kolorektal", newCases: 21718, deaths: 11698, prevalence5y: 66896 },
    { site: "Prostate", siteTR: "Prostat", newCases: 17274, deaths: 5428, prevalence5y: 65052 },
    { site: "Thyroid", siteTR: "Tiroid", newCases: 15376, deaths: 867, prevalence5y: 57970 },
    { site: "Bladder", siteTR: "Mesane", newCases: 13125, deaths: 3905, prevalence5y: 42648 },
    { site: "Stomach", siteTR: "Mide", newCases: 12773, deaths: 10457, prevalence5y: 19275 },
    { site: "Pancreas", siteTR: "Pankreas", newCases: 8636, deaths: 8415, prevalence5y: 8325 },
    { site: "Corpus uteri", siteTR: "Rahim gövdesi", newCases: 7847, deaths: 1524, prevalence5y: 30453 },
    { site: "NHL", siteTR: "Non-Hodgkin Lenfoma", newCases: 6801, deaths: 3050, prevalence5y: 23186 },
    { site: "Brain CNS", siteTR: "Beyin / MSS", newCases: 6511, deaths: 6016, prevalence5y: 24831 },
    { site: "Leukaemia", siteTR: "Lösemi", newCases: 6344, deaths: 5034, prevalence5y: 20778 }
  ];

  const officialEuropeSources = [
    { name: "ECIS", label: "European Cancer Information System", scope: "Europe", type: "Incidence, mortality, prevalence, survival" },
    { name: "GLOBOCAN", label: "Global Cancer Observatory", scope: "185 countries", type: "2022 incidence, mortality, prevalence estimates" },
    { name: "HSGM", label: "Türkiye Kanser İstatistikleri", scope: "Türkiye", type: "Official national cancer statistics reports" }
  ];

  const officialMetricLabel = officialCancerMetric === "incidence"
    ? (lang === "tr" ? "Yeni vaka" : "New cases")
    : officialCancerMetric === "mortality"
      ? (lang === "tr" ? "Ölüm" : "Deaths")
      : (lang === "tr" ? "5 yıllık prevalans" : "5-year prevalence");

  const officialMetricValue = (item) => {
    if (officialCancerMetric === "incidence") return item.newCases;
    if (officialCancerMetric === "mortality") return item.deaths;
    return item.prevalence5y;
  };

  const sortedOfficialTurkeyData = useMemo(() => {
    return [...officialTurkeyCancerData]
      .filter((item) => item.site !== "All cancers")
      .sort((a, b) => officialMetricValue(b) - officialMetricValue(a));
  }, [officialCancerMetric]);

  const mapData = useMemo(() => {'''
)

# 3) Insert official data section before map simulator
official_section = r'''
        <section className="official-data-section">
          <div className="section-intro">
            <p className="eyebrow dark">{lang === "tr" ? "RESMÎ VERİ KATMANI" : "OFFICIAL DATA LAYER"}</p>
            <h2>
              {lang === "tr"
                ? "Türkiye için GLOBOCAN 2022 verisi bağlandı"
                : "GLOBOCAN 2022 data connected for Türkiye"}
            </h2>
            <p>
              {lang === "tr"
                ? "Bu bölüm gerçek kaynaklı ülke geneli veriyi gösterir. 81 il haritası ise resmî il bazlı açık veri bulunana kadar demo dağılım simülasyonu olarak kalır."
                : "This section shows source-backed national data. The 81-city map remains a demo distribution until official province-level open data is available."}
            </p>
          </div>

          <div className="official-source-badges">
            <div>
              <strong>GLOBOCAN 2022</strong>
              <span>{lang === "tr" ? "Türkiye toplam yeni vaka, ölüm ve 5 yıllık prevalans" : "Türkiye total new cases, deaths and 5-year prevalence"}</span>
            </div>
            <div>
              <strong>ECIS</strong>
              <span>{lang === "tr" ? "Avrupa ülkeleri için kanser yükü göstergeleri" : "Cancer burden indicators for European countries"}</span>
            </div>
            <div>
              <strong>HSGM</strong>
              <span>{lang === "tr" ? "Türkiye Kanser İstatistikleri yıllık raporları" : "Türkiye official annual cancer statistics reports"}</span>
            </div>
          </div>

          <div className="official-kpi-grid">
            <div>
              <small>{lang === "tr" ? "Türkiye, 2022" : "Türkiye, 2022"}</small>
              <strong>240,013</strong>
              <span>{lang === "tr" ? "tüm kanserler yeni vaka" : "all cancers new cases"}</span>
            </div>
            <div>
              <small>{lang === "tr" ? "Türkiye, 2022" : "Türkiye, 2022"}</small>
              <strong>129,672</strong>
              <span>{lang === "tr" ? "tüm kanserler ölüm" : "all cancers deaths"}</span>
            </div>
            <div>
              <small>{lang === "tr" ? "Türkiye, 2022" : "Türkiye, 2022"}</small>
              <strong>679,335</strong>
              <span>{lang === "tr" ? "5 yıllık prevalans" : "5-year prevalence"}</span>
            </div>
          </div>

          <div className="official-data-controls">
            <button className={officialCancerMetric === "incidence" ? "active" : ""} onClick={() => setOfficialCancerMetric("incidence")}>
              {lang === "tr" ? "Yeni vaka" : "New cases"}
            </button>
            <button className={officialCancerMetric === "mortality" ? "active" : ""} onClick={() => setOfficialCancerMetric("mortality")}>
              {lang === "tr" ? "Ölüm" : "Deaths"}
            </button>
            <button className={officialCancerMetric === "prevalence" ? "active" : ""} onClick={() => setOfficialCancerMetric("prevalence")}>
              {lang === "tr" ? "5 yıllık prevalans" : "5-year prevalence"}
            </button>
          </div>

          <div className="official-chart-layout">
            <div className="official-bars">
              {sortedOfficialTurkeyData.slice(0, 10).map((item, index) => {
                const value = officialMetricValue(item);
                const maxValue = officialMetricValue(sortedOfficialTurkeyData[0]);
                const width = Math.max(8, Math.round((value / maxValue) * 100));

                return (
                  <div className="official-bar-row" key={item.site}>
                    <div className="official-bar-label">
                      <strong>{lang === "tr" ? item.siteTR : item.site}</strong>
                      <span>{value.toLocaleString()} — {officialMetricLabel}</span>
                    </div>
                    <div className="official-bar-track">
                      <i style={{ width: `${width}%`, animationDelay: `${index * 0.08}s` }}></i>
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="official-context-card">
              <h3>{lang === "tr" ? "81 il verisi hakkında önemli not" : "Important note on 81-city data"}</h3>
              <p>
                {lang === "tr"
                  ? "GLOBOCAN Türkiye tahminlerinde İzmir, Antalya, Samsun, Bursa, Erzurum, Eskişehir, Edirne, Trabzon ve Ankara kanser kayıtları gibi alt-ulusal kaynaklar kullanılmıştır. Ancak açık erişimde 81 ilin tamamı için güncel resmî hasta/vaka sayısı bulunmadığı için harita yerel dağılımı simüle eder."
                  : "GLOBOCAN Türkiye estimates use subnational sources such as Izmir, Antalya, Samsun, Bursa, Erzurum, Eskişehir, Edirne, Trabzon and Ankara cancer registries. However, because public official case counts for all 81 cities are not available, the local map remains a distribution simulation."}
              </p>

              <div className="registry-city-tags">
                {["Izmir","Antalya","Samsun","Bursa","Erzurum","Eskişehir","Edirne","Trabzon","Ankara"].map((city) => (
                  <span key={city}>{city}</span>
                ))}
              </div>
            </div>
          </div>
        </section>

'''

marker = '<section className="cancer-map-simulator">'
if marker in app and "official-data-section" not in app:
    app = app.replace(marker, official_section + marker)
else:
    print("⚠️ cancer-map-simulator marker not found or official section already exists.")

# 4) Make map warning stricter and source-backed
app = app.replace(
'''This visualization is not official registry data. It uses demo simulation data to show how the platform would work when connected to real data sources.''',
'''Country-level indicators are connected to official sources. City-level distribution is a demo layer until official province-level open data is available.''')

app = app.replace(
'''Bu görselleştirme resmi kayıt verisi değildir. Demo amaçlı simülasyon verisiyle, gerçek veri bağlandığında platformun nasıl çalışacağını gösterir.''',
'''Ülke geneli göstergeler resmî kaynaklara bağlandı. İl bazlı dağılım ise resmî açık veri sağlanana kadar demo katmanıdır.''')

css += r'''

/* Step 19: Official source-backed cancer data layer */

.official-data-section {
  max-width: 1180px;
  margin: 68px auto;
  padding: 0 24px;
}

.official-source-badges {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  margin: 20px 0;
}

.official-source-badges div {
  border-radius: 24px;
  background: white;
  border: 1px solid #dbeafe;
  padding: 20px;
  box-shadow: 0 18px 60px rgba(15,23,42,0.08);
}

.official-source-badges strong,
.official-source-badges span {
  display: block;
}

.official-source-badges strong {
  color: #1d4ed8;
  font-size: 20px;
}

.official-source-badges span {
  color: #475569;
  margin-top: 6px;
  line-height: 1.45;
}

.official-kpi-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  margin: 20px 0;
}

.official-kpi-grid div {
  position: relative;
  overflow: hidden;
  border-radius: 28px;
  padding: 24px;
  color: white;
  background: linear-gradient(135deg, #0f172a, #1d4ed8);
  box-shadow: 0 24px 80px rgba(15,23,42,0.16);
}

.official-kpi-grid div:nth-child(2) {
  background: linear-gradient(135deg, #7c2d12, #ea580c);
}

.official-kpi-grid div:nth-child(3) {
  background: linear-gradient(135deg, #0f766e, #14b8a6);
}

.official-kpi-grid small,
.official-kpi-grid strong,
.official-kpi-grid span {
  display: block;
  position: relative;
  z-index: 1;
}

.official-kpi-grid strong {
  font-size: clamp(34px, 4vw, 54px);
  line-height: 1;
  margin: 10px 0 4px;
  letter-spacing: -0.05em;
}

.official-kpi-grid span {
  color: rgba(255,255,255,0.86);
  font-weight: 850;
}

.official-data-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin: 22px 0;
}

.official-data-controls button {
  border: 1px solid #cbd5e1;
  background: white;
  color: #0f172a;
  border-radius: 999px;
  padding: 12px 16px;
  font-weight: 950;
  cursor: pointer;
}

.official-data-controls button.active {
  background: #1d4ed8;
  color: white;
  border-color: #1d4ed8;
}

.official-chart-layout {
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 22px;
}

.official-bars,
.official-context-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 30px;
  padding: 24px;
  box-shadow: 0 24px 80px rgba(15,23,42,0.10);
}

.official-bars {
  display: grid;
  gap: 15px;
}

.official-bar-label {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  margin-bottom: 7px;
}

.official-bar-label strong {
  color: #0f172a;
}

.official-bar-label span {
  color: #64748b;
  font-weight: 850;
  text-align: right;
}

.official-bar-track {
  position: relative;
  height: 13px;
  background: #e2e8f0;
  border-radius: 999px;
  overflow: hidden;
}

.official-bar-track i {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, #1d4ed8, #14b8a6);
  animation: officialBarGrow 1.2s ease both;
}

@keyframes officialBarGrow {
  from { width: 0; }
}

.official-context-card h3 {
  margin-top: 0;
  color: #0f172a;
  font-size: 24px;
}

.official-context-card p {
  color: #475569;
  line-height: 1.65;
}

.registry-city-tags {
  display: flex;
  gap: 9px;
  flex-wrap: wrap;
  margin-top: 18px;
}

.registry-city-tags span {
  border-radius: 999px;
  padding: 8px 11px;
  background: #eef2ff;
  color: #3730a3;
  font-weight: 900;
}

@media (max-width: 900px) {
  .official-source-badges,
  .official-kpi-grid,
  .official-chart-layout {
    grid-template-columns: 1fr;
  }

  .official-bar-label {
    display: block;
  }

  .official-bar-label span {
    display: block;
    text-align: left;
    margin-top: 4px;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Official source-backed cancer data layer added.")
