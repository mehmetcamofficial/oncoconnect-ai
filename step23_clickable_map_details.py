from pathlib import Path
import re

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) selected map item state ekle
app = app.replace(
'''  const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");''',
'''  const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");
  const [selectedMapItem, setSelectedMapItem] = useState(null);'''
)

# 2) parseCSV daha güvenli hale getir
old_parse = r'''  const parseCSV = (text) => {
    const lines = text.trim().split(/\r?\n/);
    const headers = lines[0].split(",").map((h) => h.trim());

    return lines.slice(1).map((line) => {
      const values = line.split(",");
      const row = {};
      headers.forEach((h, i) => {
        row[h] = values[i]?.trim() ?? "";
      });
      return row;
    });
  };'''

new_parse = r'''  const parseCSV = (text) => {
    const lines = text.trim().split(/\r?\n/);
    const headers = lines[0].split(",").map((h) => h.trim());

    return lines.slice(1).filter(Boolean).map((line) => {
      const values = [];
      let current = "";
      let inQuotes = false;

      for (let i = 0; i < line.length; i++) {
        const char = line[i];

        if (char === '"') {
          inQuotes = !inQuotes;
        } else if (char === "," && !inQuotes) {
          values.push(current);
          current = "";
        } else {
          current += char;
        }
      }

      values.push(current);

      const row = {};
      headers.forEach((h, i) => {
        row[h] = values[i]?.trim() ?? "";
      });
      return row;
    });
  };'''

app = app.replace(old_parse, new_parse)

# 3) official arrays sonrası official map rows ekle
insert_after = '''  const officialEuropeSources = [
    { name: "ECIS", label: "European Cancer Information System", scope: "Europe", type: "Incidence, mortality, prevalence, survival" },
    { name: "GLOBOCAN", label: "Global Cancer Observatory", scope: "185 countries", type: "2022 incidence, mortality, prevalence estimates" },
    { name: "HSGM", label: "Türkiye Kanser İstatistikleri", scope: "Türkiye", type: "Official national cancer statistics reports" }
  ];'''

official_map_rows = r'''
  const officialMapRows = useMemo(() => {
    return officialTurkeyCancerData.flatMap((item) => {
      const site = item.site;
      const siteTR = item.siteTR;

      return [
        {
          Bolge: "Turkiye",
          Ulke_Sehir: "Türkiye",
          Cinsiyet: "Total",
          Kanser_Turu: site,
          Kanser_Turu_TR: siteTR,
          Yas_Grubu: "All",
          Yillik_Vaka_Hizi_100Bin: item.newCases,
          Yillik_Olum_Hizi_100Bin: item.deaths,
          Bes_Yillik_Sagkalim_Yuzdesi: item.prevalence5y,
          Veri_Tipi: "GLOBOCAN 2022 official country estimate",
          Kaynak: "GLOBOCAN 2022 Türkiye Fact Sheet"
        }
      ];
    });
  }, []);
'''

if official_map_rows not in app:
    app = app.replace(insert_after, insert_after + "\n\n" + official_map_rows)

# 4) mapData içindeki sourceRows tanımını official merge ile değiştir
old_source = r'''    const sourceRows = cancerRows.filter((row) => {
      const regionOk = mapMode === "turkiye"
        ? row.Bolge === "Turkiye"
        : row.Bolge === "Avrupa";

      const genderOk = mapGender === "total"
        ? true
        : row.Cinsiyet === genderMap[mapGender];

      const cancerOk = selectedCancerType === "all"
        ? true
        : row.Kanser_Turu === selectedCancerType;

      const ageOk = selectedAgeGroup === "all"
        ? true
        : row.Yas_Grubu === selectedAgeGroup;

      return regionOk && genderOk && cancerOk && ageOk;
    });'''

new_source = r'''    const mergedRows = [...cancerRows, ...officialMapRows];

    const sourceRows = mergedRows.filter((row) => {
      const regionOk = mapMode === "turkiye"
        ? row.Bolge === "Turkiye"
        : row.Bolge === "Avrupa";

      const genderOk = mapGender === "total"
        ? true
        : row.Cinsiyet === genderMap[mapGender];

      const cancerOk = selectedCancerType === "all"
        ? true
        : row.Kanser_Turu === selectedCancerType;

      const ageOk = selectedAgeGroup === "all"
        ? true
        : row.Yas_Grubu === selectedAgeGroup || row.Yas_Grubu === "All";

      return regionOk && genderOk && cancerOk && ageOk;
    });'''

app = app.replace(old_source, new_source)

# 5) grouped detail alanları ekle
old_group_init = r'''          grouped[name] = {
            name,
            value: 0,
            mortality: 0,
            survival: 0,
            rows: 0
          };'''

new_group_init = r'''          grouped[name] = {
            name,
            value: 0,
            mortality: 0,
            survival: 0,
            rows: 0,
            cancerBreakdown: {},
            sourceTypes: new Set(),
            rawRows: []
          };'''

app = app.replace(old_group_init, new_group_init)

old_group_add = r'''        grouped[name].value += vaka * yearFactor;
        grouped[name].mortality += olum * yearFactor;
        grouped[name].survival += sagkalim;
        grouped[name].rows += 1;'''

new_group_add = r'''        grouped[name].value += vaka * yearFactor;
        grouped[name].mortality += olum * yearFactor;
        grouped[name].survival += sagkalim;
        grouped[name].rows += 1;
        grouped[name].rawRows.push(row);

        const cancerName = row.Kanser_Turu || "Unknown";
        if (!grouped[name].cancerBreakdown[cancerName]) {
          grouped[name].cancerBreakdown[cancerName] = {
            incidence: 0,
            mortality: 0,
            count: 0
          };
        }

        grouped[name].cancerBreakdown[cancerName].incidence += vaka;
        grouped[name].cancerBreakdown[cancerName].mortality += olum;
        grouped[name].cancerBreakdown[cancerName].count += 1;

        if (row.Veri_Tipi) grouped[name].sourceTypes.add(row.Veri_Tipi);
        if (row.data_type) grouped[name].sourceTypes.add(row.data_type);'''

app = app.replace(old_group_add, new_group_add)

old_return_obj = r'''        return {
          name: item.name,
          value: Math.round(item.value),
          growth: Math.round((yearFactor - 1) * 100),
          mortality: Math.round(item.mortality),
          survival: Math.round(avgSurvival),
          intensity: Math.min(100, Math.max(12, Math.round(item.value / 12)))
        };'''

new_return_obj = r'''        const breakdown = Object.entries(item.cancerBreakdown)
          .map(([name, data]) => ({
            name,
            incidence: Math.round(data.incidence / Math.max(1, data.count)),
            mortality: Math.round(data.mortality / Math.max(1, data.count))
          }))
          .sort((a, b) => b.incidence - a.incidence)
          .slice(0, 5);

        return {
          name: item.name,
          value: Math.round(item.value),
          growth: Math.round((yearFactor - 1) * 100),
          mortality: Math.round(item.mortality),
          survival: Math.round(avgSurvival),
          intensity: Math.min(100, Math.max(12, Math.round(item.value / 12))),
          breakdown,
          rowCount: item.rows,
          sourceTypes: Array.from(item.sourceTypes),
          sourceMode: item.rawRows.some((r) => String(r.Veri_Tipi || "").includes("GLOBOCAN"))
            ? "official"
            : "csv"
        };'''

app = app.replace(old_return_obj, new_return_obj)

# 6) dependency list officialMapRows ekle
app = app.replace(
'''} , [mapMode, mapYear, mapGender, cancerRows, selectedCancerType, selectedAgeGroup]);''',
'''} , [mapMode, mapYear, mapGender, cancerRows, officialMapRows, selectedCancerType, selectedAgeGroup]);'''
)

app = app.replace(
'''}, [mapMode, mapYear, mapGender, cancerRows, selectedCancerType, selectedAgeGroup]);''',
'''}, [mapMode, mapYear, mapGender, cancerRows, officialMapRows, selectedCancerType, selectedAgeGroup]);'''
)

# 7) pin buttonlarına onClick ekle
old_pin = r'''                  <button
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
                  </button>'''

new_pin = r'''                  <button
                    key={item.name}
                    className={`map-pin ${selectedMapItem?.name === item.name ? "selected" : ""}`}
                    onClick={() => setSelectedMapItem(item)}
                    style={{
                      "--size": `${Math.max(12, Math.min(34, item.intensity / 2.8))}px`,
                      "--delay": `${(index % 12) * 0.08}s`
                    }}
                    title={`${item.name}: ${item.value.toLocaleString()}`}
                  >
                    <span>{item.name}</span>
                    <b>{item.value.toLocaleString()}</b>
                  </button>'''

app = app.replace(old_pin, new_pin)

# 8) detail panel'i map-dashboard içine ekle: rank card öncesi değil, rank card içeriği başına selected info ekle
old_rank_start = r'''            <div className="map-rank-card">
              <h3>{lang === "tr" ? "En yüksek simüle edilen alanlar" : "Highest simulated areas"}</h3>'''

new_rank_start = r'''            <div className="map-rank-card">
              <h3>{selectedMapItem ? selectedMapItem.name : (lang === "tr" ? "En yüksek alanlar" : "Highest areas")}</h3>

              {selectedMapItem && (
                <div className="selected-map-detail">
                  <div className="detail-kpis">
                    <div>
                      <small>{lang === "tr" ? "Vaka göstergesi" : "Incidence indicator"}</small>
                      <strong>{selectedMapItem.value.toLocaleString()}</strong>
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

                  <div className="detail-source-pill">
                    {selectedMapItem.sourceMode === "official"
                      ? (lang === "tr" ? "Official GLOBOCAN layer" : "Official GLOBOCAN layer")
                      : (lang === "tr" ? "CSV data layer" : "CSV data layer")}
                  </div>

                  {selectedMapItem.breakdown?.length > 0 && (
                    <div className="breakdown-list">
                      <strong>{lang === "tr" ? "Kanser türü kırılımı" : "Cancer type breakdown"}</strong>
                      {selectedMapItem.breakdown.map((b) => (
                        <div key={b.name} className="breakdown-row">
                          <span>{b.name}</span>
                          <b>{b.incidence.toLocaleString()}</b>
                        </div>
                      ))}
                    </div>
                  )}

                  <button className="clear-selection" onClick={() => setSelectedMapItem(null)}>
                    {lang === "tr" ? "Seçimi temizle" : "Clear selection"}
                  </button>
                </div>
              )}

              {!selectedMapItem && (
                <p className="map-click-hint">
                  {lang === "tr"
                    ? "Detayları görmek için harita üzerindeki bir pine tıklayın."
                    : "Click a pin on the map to see detailed statistics."}
                </p>
              )}'''

app = app.replace(old_rank_start, new_rank_start)

# 9) “simulated” kelimelerini daha doğru hale getir
app = app.replace("Simulated total cases", "Visualization total")
app = app.replace("Simüle edilen toplam vaka", "Görselleştirme toplamı")
app = app.replace("Highest simulated areas", "Highest areas")
app = app.replace("En yüksek simüle edilen alanlar", "En yüksek alanlar")
app = app.replace("Simulated yearly growth", "Year-adjusted change")
app = app.replace("Yıllık artış simülasyonu", "Yıl ayarlı değişim")

app_path.write_text(app, encoding="utf-8")

# CSS ekle
css += r'''

/* Step 23: clickable map pin detail panel */

.map-pin.selected {
  background: #fbbf24 !important;
  transform: translate(-50%, -50%) scale(1.95) !important;
  z-index: 60 !important;
  box-shadow:
    0 0 0 12px rgba(251,191,36,0.20),
    0 0 44px rgba(251,191,36,0.90) !important;
}

.map-click-hint {
  color: #64748b;
  line-height: 1.5;
  margin-top: -4px;
  margin-bottom: 16px;
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
  grid-template-columns: 1fr;
  gap: 10px;
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
  margin-top: 3px;
  font-size: 23px;
  color: #0f172a;
}

.detail-source-pill {
  margin-top: 12px;
  display: inline-flex;
  border-radius: 999px;
  padding: 8px 11px;
  background: #eef2ff;
  color: #3730a3;
  font-weight: 950;
  font-size: 13px;
}

.breakdown-list {
  margin-top: 14px;
  display: grid;
  gap: 8px;
}

.breakdown-list > strong {
  color: #0f172a;
  margin-bottom: 2px;
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
  font-weight: 800;
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

.rank-list {
  margin-top: 10px;
}
'''

css_path.write_text(css, encoding="utf-8")

print("✅ Step 23 applied: CSV + official data merged, map pins are clickable, detail panel added.")
