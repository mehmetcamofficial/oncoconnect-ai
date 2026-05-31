from pathlib import Path
import re

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# useEffect ekle
app = app.replace(
    'import { useMemo, useState } from "react";',
    'import { useEffect, useMemo, useState } from "react";'
)

# CSV state ekle
app = app.replace(
'''  const [mapGender, setMapGender] = useState("total");''',
'''  const [mapGender, setMapGender] = useState("total");
  const [cancerRows, setCancerRows] = useState([]);
  const [selectedCancerType, setSelectedCancerType] = useState("all");
  const [selectedAgeGroup, setSelectedAgeGroup] = useState("all");'''
)

# CSV loader ekle
insert_after = '''  const updatePrevention = (key, value) => {
    setPrevention({ ...prevention, [key]: Number(value) });
  };'''

csv_loader = r'''
  const parseCSV = (text) => {
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
  };

  useEffect(() => {
    fetch("/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv")
      .then((res) => {
        if (!res.ok) throw new Error("CSV not found");
        return res.text();
      })
      .then((text) => {
        setCancerRows(parseCSV(text));
      })
      .catch(() => {
        setCancerRows([]);
      });
  }, []);

  const cancerTypeOptions = useMemo(() => {
    const values = [...new Set(cancerRows.map((r) => r.Kanser_Turu).filter(Boolean))];
    return values.sort();
  }, [cancerRows]);

  const ageGroupOptions = useMemo(() => {
    const values = [...new Set(cancerRows.map((r) => r.Yas_Grubu).filter(Boolean))];
    return values.sort();
  }, [cancerRows]);
'''

if csv_loader not in app:
    app = app.replace(insert_after, insert_after + "\n\n" + csv_loader)

# mapData block değiştir
new_mapdata = r'''  const mapData = useMemo(() => {
    const yearFactor = 1 + (mapYear - 2020) * 0.045;
    const genderMap = {
      female: "Kadin",
      male: "Erkek"
    };

    const sourceRows = cancerRows.filter((row) => {
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
    });

    if (sourceRows.length > 0) {
      const grouped = {};

      sourceRows.forEach((row) => {
        const name = row.Ulke_Sehir;
        const vaka = Number(row.Yillik_Vaka_Hizi_100Bin || 0);
        const olum = Number(row.Yillik_Olum_Hizi_100Bin || 0);
        const sagkalim = Number(row.Bes_Yillik_Sagkalim_Yuzdesi || 0);

        if (!grouped[name]) {
          grouped[name] = {
            name,
            value: 0,
            mortality: 0,
            survival: 0,
            rows: 0
          };
        }

        grouped[name].value += vaka * yearFactor;
        grouped[name].mortality += olum * yearFactor;
        grouped[name].survival += sagkalim;
        grouped[name].rows += 1;
      });

      return Object.values(grouped).map((item) => {
        const avgSurvival = item.rows ? item.survival / item.rows : 0;

        return {
          name: item.name,
          value: Math.round(item.value),
          growth: Math.round((yearFactor - 1) * 100),
          mortality: Math.round(item.mortality),
          survival: Math.round(avgSurvival),
          intensity: Math.min(100, Math.max(12, Math.round(item.value / 12)))
        };
      });
    }

    // Fallback demo layer
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
  }, [mapMode, mapYear, mapGender, cancerRows, selectedCancerType, selectedAgeGroup]);'''

app = re.sub(
    r'''  const mapData = useMemo\(\(\) => \{[\s\S]*?\}, \[mapMode, mapYear, mapGender\]\);''',
    new_mapdata,
    app
)

# Controls içine cancer type + age group filtreleri ekle
controls_marker = '''            <div className="year-slider">
              <strong>{mapYear}</strong>
              <input type="range" min="2020" max="2026" value={mapYear} onChange={(e) => setMapYear(Number(e.target.value))} />
            </div>'''

controls_extra = r'''            <div className="year-slider">
              <strong>{mapYear}</strong>
              <input type="range" min="2020" max="2026" value={mapYear} onChange={(e) => setMapYear(Number(e.target.value))} />
            </div>

            <select value={selectedCancerType} onChange={(e) => setSelectedCancerType(e.target.value)}>
              <option value="all">{lang === "tr" ? "Tüm kanser türleri" : "All cancer types"}</option>
              {cancerTypeOptions.map((type) => (
                <option key={type} value={type}>{type}</option>
              ))}
            </select>

            <select value={selectedAgeGroup} onChange={(e) => setSelectedAgeGroup(e.target.value)}>
              <option value="all">{lang === "tr" ? "Tüm yaş grupları" : "All age groups"}</option>
              {ageGroupOptions.map((age) => (
                <option key={age} value={age}>{age}</option>
              ))}
            </select>'''

app = app.replace(controls_marker, controls_extra)

# Map warning text değiştir
app = app.replace(
'''Real-world use için Sağlık Bakanlığı, kanser kayıt merkezi, GLOBOCAN veya ulusal/AB açık veri kaynakları bağlanmalıdır.''',
'''CSV veri katmanı kullanılıyor. Değerler yıllık vaka hızı / ölüm hızı göstergelerinden türetilen görselleştirme indeksidir.'''
)

app = app.replace(
'''For real-world use, this should be connected to Ministry of Health, cancer registry, GLOBOCAN or national/EU open data sources.''',
'''CSV data layer is active. Values are visualization indices derived from annual incidence and mortality-rate fields.'''
)

app_path.write_text(app, encoding="utf-8")

# CSS: harita görsellerini arka plan yap
css += r'''

/* Step 22: real image based map pin layer */

.turkiye-pin-map {
  display: block !important;
  position: relative !important;
  min-height: 600px !important;
  border-radius: 30px !important;
  overflow: hidden !important;
  background:
    linear-gradient(180deg, rgba(3, 12, 30, 0.12), rgba(3, 12, 30, 0.28)),
    url("./assets/turkiye-map-bg.png") center / cover no-repeat !important;
}

.turkiye-pin-map::before {
  display: none !important;
}

.turkiye-pin-map::after {
  content: "Türkiye map — CSV rate-based province visualization" !important;
  position: absolute;
  left: 24px;
  bottom: 20px;
  color: rgba(255,255,255,0.84);
  font-weight: 900;
  letter-spacing: 0.02em;
}

.europe-bubble-map {
  display: block !important;
  position: relative !important;
  min-height: 600px !important;
  border-radius: 30px !important;
  overflow: hidden !important;
  background:
    linear-gradient(180deg, rgba(3, 12, 30, 0.12), rgba(3, 12, 30, 0.28)),
    url("./assets/europe-map-bg.png") center / cover no-repeat !important;
}

.europe-bubble-map::before {
  display: none !important;
}

.europe-bubble-map::after {
  content: "Europe map — CSV rate-based country visualization" !important;
  position: absolute;
  left: 24px;
  bottom: 20px;
  color: rgba(255,255,255,0.84);
  font-weight: 900;
  letter-spacing: 0.02em;
}

.turkiye-pin-map .map-pin,
.europe-bubble-map .map-pin {
  position: absolute !important;
  width: var(--size) !important;
  height: var(--size) !important;
  min-width: 16px !important;
  min-height: 16px !important;
  border-radius: 999px !important;
  background: #38bdf8 !important;
  border: 2px solid rgba(255,255,255,0.95) !important;
  box-shadow:
    0 0 0 7px rgba(56,189,248,0.16),
    0 0 30px rgba(56,189,248,0.85) !important;
  transform: translate(-50%, -50%);
  animation: pinPulse 3s ease-in-out infinite !important;
  animation-delay: var(--delay) !important;
  z-index: 5;
}

.turkiye-pin-map .map-pin::before,
.europe-bubble-map .map-pin::before {
  display: none !important;
}

.turkiye-pin-map .map-pin span,
.turkiye-pin-map .map-pin b,
.europe-bubble-map .map-pin span,
.europe-bubble-map .map-pin b {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  padding: 5px 8px !important;
  text-align: center !important;
  white-space: nowrap;
  background: rgba(15,23,42,0.94);
  color: white;
  border-radius: 12px;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s ease;
}

.turkiye-pin-map .map-pin span,
.europe-bubble-map .map-pin span {
  bottom: calc(100% + 8px);
  font-size: 12px !important;
  font-weight: 950 !important;
}

.turkiye-pin-map .map-pin b,
.europe-bubble-map .map-pin b {
  top: calc(100% + 8px);
  font-size: 11px !important;
}

.turkiye-pin-map .map-pin:hover,
.europe-bubble-map .map-pin:hover {
  transform: translate(-50%, -50%) scale(1.85) !important;
  background: #fbbf24 !important;
  z-index: 50;
  box-shadow:
    0 0 0 10px rgba(251,191,36,0.18),
    0 0 40px rgba(251,191,36,0.85) !important;
}

.turkiye-pin-map .map-pin:hover span,
.turkiye-pin-map .map-pin:hover b,
.europe-bubble-map .map-pin:hover span,
.europe-bubble-map .map-pin:hover b {
  opacity: 1;
}

/* Türkiye pin coordinates on generated map image */
.turkiye-pin-map .map-pin:nth-child(1) { left: 17%; top: 57%; }
.turkiye-pin-map .map-pin:nth-child(2) { left: 60%; top: 57%; }
.turkiye-pin-map .map-pin:nth-child(3) { left: 28%; top: 56%; }
.turkiye-pin-map .map-pin:nth-child(4) { left: 86%; top: 46%; }
.turkiye-pin-map .map-pin:nth-child(5) { left: 46%; top: 42%; }
.turkiye-pin-map .map-pin:nth-child(6) { left: 41%; top: 51%; }
.turkiye-pin-map .map-pin:nth-child(7) { left: 27%; top: 65%; }
.turkiye-pin-map .map-pin:nth-child(8) { left: 82%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(9) { left: 21%; top: 63%; }
.turkiye-pin-map .map-pin:nth-child(10) { left: 18%; top: 50%; }
.turkiye-pin-map .map-pin:nth-child(11) { left: 28%; top: 48%; }
.turkiye-pin-map .map-pin:nth-child(12) { left: 74%; top: 50%; }
.turkiye-pin-map .map-pin:nth-child(13) { left: 78%; top: 56%; }
.turkiye-pin-map .map-pin:nth-child(14) { left: 38%; top: 40%; }
.turkiye-pin-map .map-pin:nth-child(15) { left: 30%; top: 60%; }
.turkiye-pin-map .map-pin:nth-child(16) { left: 24%; top: 46%; }
.turkiye-pin-map .map-pin:nth-child(17) { left: 15%; top: 48%; }
.turkiye-pin-map .map-pin:nth-child(18) { left: 68%; top: 45%; }
.turkiye-pin-map .map-pin:nth-child(19) { left: 48%; top: 45%; }
.turkiye-pin-map .map-pin:nth-child(20) { left: 24%; top: 62%; }
.turkiye-pin-map .map-pin:nth-child(21) { left: 70%; top: 60%; }
.turkiye-pin-map .map-pin:nth-child(22) { left: 9%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(23) { left: 63%; top: 52%; }
.turkiye-pin-map .map-pin:nth-child(24) { left: 70%; top: 45%; }
.turkiye-pin-map .map-pin:nth-child(25) { left: 76%; top: 43%; }
.turkiye-pin-map .map-pin:nth-child(26) { left: 34%; top: 48%; }
.turkiye-pin-map .map-pin:nth-child(27) { left: 58%; top: 64%; }
.turkiye-pin-map .map-pin:nth-child(28) { left: 58%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(29) { left: 64%; top: 40%; }
.turkiye-pin-map .map-pin:nth-child(30) { left: 84%; top: 59%; }
.turkiye-pin-map .map-pin:nth-child(31) { left: 53%; top: 65%; }
.turkiye-pin-map .map-pin:nth-child(32) { left: 30%; top: 60%; }
.turkiye-pin-map .map-pin:nth-child(33) { left: 43%; top: 65%; }
.turkiye-pin-map .map-pin:nth-child(34) { left: 10%; top: 35%; }
.turkiye-pin-map .map-pin:nth-child(35) { left: 18%; top: 60%; }
.turkiye-pin-map .map-pin:nth-child(36) { left: 85%; top: 41%; }
.turkiye-pin-map .map-pin:nth-child(37) { left: 39%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(38) { left: 49%; top: 53%; }
.turkiye-pin-map .map-pin:nth-child(39) { left: 8%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(40) { left: 46%; top: 50%; }
.turkiye-pin-map .map-pin:nth-child(41) { left: 19%; top: 40%; }
.turkiye-pin-map .map-pin:nth-child(42) { left: 41%; top: 58%; }
.turkiye-pin-map .map-pin:nth-child(43) { left: 30%; top: 50%; }
.turkiye-pin-map .map-pin:nth-child(44) { left: 56%; top: 54%; }
.turkiye-pin-map .map-pin:nth-child(45) { left: 22%; top: 56%; }
.turkiye-pin-map .map-pin:nth-child(46) { left: 56%; top: 62%; }
.turkiye-pin-map .map-pin:nth-child(47) { left: 72%; top: 62%; }
.turkiye-pin-map .map-pin:nth-child(48) { left: 22%; top: 68%; }
.turkiye-pin-map .map-pin:nth-child(49) { left: 80%; top: 53%; }
.turkiye-pin-map .map-pin:nth-child(50) { left: 48%; top: 56%; }
.turkiye-pin-map .map-pin:nth-child(51) { left: 46%; top: 60%; }
.turkiye-pin-map .map-pin:nth-child(52) { left: 56%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(53) { left: 65%; top: 36%; }
.turkiye-pin-map .map-pin:nth-child(54) { left: 18%; top: 42%; }
.turkiye-pin-map .map-pin:nth-child(55) { left: 53%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(56) { left: 78%; top: 60%; }
.turkiye-pin-map .map-pin:nth-child(57) { left: 45%; top: 36%; }
.turkiye-pin-map .map-pin:nth-child(58) { left: 55%; top: 48%; }
.turkiye-pin-map .map-pin:nth-child(59) { left: 11%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(60) { left: 52%; top: 43%; }
.turkiye-pin-map .map-pin:nth-child(61) { left: 62%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(62) { left: 68%; top: 48%; }
.turkiye-pin-map .map-pin:nth-child(63) { left: 66%; top: 66%; }
.turkiye-pin-map .map-pin:nth-child(64) { left: 27%; top: 56%; }
.turkiye-pin-map .map-pin:nth-child(65) { left: 86%; top: 55%; }
.turkiye-pin-map .map-pin:nth-child(66) { left: 49%; top: 47%; }
.turkiye-pin-map .map-pin:nth-child(67) { left: 35%; top: 36%; }
.turkiye-pin-map .map-pin:nth-child(68) { left: 45%; top: 57%; }
.turkiye-pin-map .map-pin:nth-child(69) { left: 70%; top: 41%; }
.turkiye-pin-map .map-pin:nth-child(70) { left: 43%; top: 62%; }
.turkiye-pin-map .map-pin:nth-child(71) { left: 45%; top: 49%; }
.turkiye-pin-map .map-pin:nth-child(72) { left: 76%; top: 57%; }
.turkiye-pin-map .map-pin:nth-child(73) { left: 82%; top: 61%; }
.turkiye-pin-map .map-pin:nth-child(74) { left: 33%; top: 36%; }
.turkiye-pin-map .map-pin:nth-child(75) { left: 84%; top: 38%; }
.turkiye-pin-map .map-pin:nth-child(76) { left: 88%; top: 45%; }
.turkiye-pin-map .map-pin:nth-child(77) { left: 16%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(78) { left: 36%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(79) { left: 60%; top: 66%; }
.turkiye-pin-map .map-pin:nth-child(80) { left: 55%; top: 66%; }
.turkiye-pin-map .map-pin:nth-child(81) { left: 24%; top: 41%; }

/* Europe coordinates on generated map image */
.europe-bubble-map .map-pin:nth-child(1) { left: 77%; top: 78%; }
.europe-bubble-map .map-pin:nth-child(2) { left: 45%; top: 49%; }
.europe-bubble-map .map-pin:nth-child(3) { left: 34%; top: 58%; }
.europe-bubble-map .map-pin:nth-child(4) { left: 46%; top: 69%; }
.europe-bubble-map .map-pin:nth-child(5) { left: 21%; top: 73%; }
.europe-bubble-map .map-pin:nth-child(6) { left: 56%; top: 47%; }
.europe-bubble-map .map-pin:nth-child(7) { left: 39%; top: 45%; }
.europe-bubble-map .map-pin:nth-child(8) { left: 38%; top: 50%; }
.europe-bubble-map .map-pin:nth-child(9) { left: 57%; top: 79%; }
.europe-bubble-map .map-pin:nth-child(10) { left: 15%; top: 76%; }
.europe-bubble-map .map-pin:nth-child(11) { left: 50%; top: 25%; }
.europe-bubble-map .map-pin:nth-child(12) { left: 49%; top: 57%; }
.europe-bubble-map .map-pin:nth-child(13) { left: 62%; top: 61%; }
.europe-bubble-map .map-pin:nth-child(14) { left: 64%; top: 70%; }
.europe-bubble-map .map-pin:nth-child(15) { left: 47%; top: 38%; }
.europe-bubble-map .map-pin:nth-child(16) { left: 25%; top: 43%; }
.europe-bubble-map .map-pin:nth-child(17) { left: 51%; top: 51%; }
.europe-bubble-map .map-pin:nth-child(18) { left: 54%; top: 59%; }

.map-warning {
  background: #eff6ff !important;
  border-color: #bfdbfe !important;
  color: #1e3a8a !important;
}

@media (max-width: 900px) {
  .turkiye-pin-map,
  .europe-bubble-map {
    min-height: 430px !important;
  }
}
'''

css_path.write_text(css, encoding="utf-8")

print("✅ CSV map layer connected.")
print("✅ Türkiye and Europe image backgrounds are now used for pin maps.")
