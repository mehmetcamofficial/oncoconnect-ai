from pathlib import Path
import shutil

ROOT = Path(".")
APP = ROOT / "frontend/src/App.jsx"
CSS = ROOT / "frontend/src/App.css"
PUBLIC_ASSETS = ROOT / "frontend/public/assets"

if not APP.exists():
    raise SystemExit("❌ frontend/src/App.jsx bulunamadı.")

if not CSS.exists():
    raise SystemExit("❌ frontend/src/App.css bulunamadı.")

PUBLIC_ASSETS.mkdir(parents=True, exist_ok=True)

# 1) Harita görsellerini public/assets içine standart isimle kopyala
image_files = [
    p for p in (ROOT / "frontend").rglob("*")
    if p.is_file() and p.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]
]

turkey_candidates = [
    p for p in image_files
    if any(k in p.name.lower() for k in [
        "turkiye", "türkiye", "turkey", "futuristic_map_of_turkey", "map_of_turkey"
    ])
]

europe_candidates = [
    p for p in image_files
    if any(k in p.name.lower() for k in [
        "europe", "avrupa", "futuristic_neon_map_of_europe", "map_of_europe"
    ])
]

if turkey_candidates:
    dst = PUBLIC_ASSETS / "map-turkiye.png"
    if turkey_candidates[0].resolve() != dst.resolve():
        shutil.copy(turkey_candidates[0], dst)
        print(f"✅ Türkiye map asset copied: {turkey_candidates[0]}")
    else:
        print(f"✅ Türkiye map asset already exists: {dst}")
else:
    print("⚠️ Türkiye map asset bulunamadı. /assets/map-turkiye.png yoksa soyut zemin görünür.")

if europe_candidates:
    dst = PUBLIC_ASSETS / "map-europe.png"
    if europe_candidates[0].resolve() != dst.resolve():
        shutil.copy(europe_candidates[0], dst)
        print(f"✅ Europe map asset copied: {europe_candidates[0]}")
    else:
        print(f"✅ Europe map asset already exists: {dst}")
else:
    print("⚠️ Europe map asset bulunamadı. /assets/map-europe.png yoksa soyut zemin görünür.")

# 2) App.jsx içindeki MapPage'i değiştir
s = APP.read_text(encoding="utf-8")

start = s.find("  const MapPage = () => {")
end = s.find("  const AdminPanel = () => {", start)

if start == -1 or end == -1:
    raise SystemExit("❌ MapPage veya AdminPanel marker bulunamadı. App.jsx yapısı değişmiş olabilir.")

new_map_page = r'''  const MapPage = () => {
    const [rows, setRows] = useState([]);
    const [status, setStatus] = useState("Loading CSV data...");
    const [view, setView] = useState("turkiye");
    const [metric, setMetric] = useState("incidence");
    const [showMode, setShowMode] = useState("top15");
    const [year, setYear] = useState(2024);
    const [selectedArea, setSelectedArea] = useState(null);
    const [selectedCancer, setSelectedCancer] = useState("All");
    const [selectedAge, setSelectedAge] = useState("All");
    const [selectedSex, setSelectedSex] = useState("All");

    const parseCsvLine = (line) => {
      const result = [];
      let current = "";
      let insideQuotes = false;

      for (let i = 0; i < line.length; i++) {
        const char = line[i];
        const next = line[i + 1];

        if (char === '"' && insideQuotes && next === '"') {
          current += '"';
          i++;
        } else if (char === '"') {
          insideQuotes = !insideQuotes;
        } else if ((char === "," || char === ";") && !insideQuotes) {
          result.push(current.trim());
          current = "";
        } else {
          current += char;
        }
      }

      result.push(current.trim());
      return result;
    };

    const parseCsv = (text) => {
      const lines = text
        .replace(/\r/g, "")
        .split("\n")
        .filter((line) => line.trim().length > 0);

      if (lines.length < 2) return [];

      const headers = parseCsvLine(lines[0]).map((h) => h.trim());

      return lines.slice(1).map((line) => {
        const values = parseCsvLine(line);
        const row = {};
        headers.forEach((header, index) => {
          row[header] = values[index] ?? "";
        });
        return row;
      });
    };

    const toNumber = (value) => {
      const n = Number(String(value ?? "").replace(",", ".").trim());
      return Number.isFinite(n) ? n : null;
    };

    const normalizeAreaName = (name) => {
      const raw = String(name || "").trim();

      const aliases = {
        "Istanbul": "İstanbul",
        "istanbul": "İstanbul",
        "İstanbul": "İstanbul",
        "Ankara": "Ankara",
        "Izmir": "İzmir",
        "İzmir": "İzmir",
        "Almanya": "Germany",
        "Germany": "Germany",
        "Fransa": "France",
        "France": "France",
        "Italya": "Italy",
        "İtalya": "Italy",
        "Italy": "Italy",
        "Ispanya": "Spain",
        "İspanya": "Spain",
        "Spain": "Spain",
        "Polonya": "Poland",
        "Poland": "Poland",
        "Hollanda": "Netherlands",
        "Netherlands": "Netherlands",
        "Yunanistan": "Greece",
        "Greece": "Greece"
      };

      return aliases[raw] || raw;
    };

    useEffect(() => {
      async function loadCsv() {
        const csvPaths = [
          "/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv",
          "/turkiye_avrupa_kanser_istatistikleri_detayli.csv"
        ];

        for (const path of csvPaths) {
          try {
            const res = await fetch(path);
            if (!res.ok) continue;

            const text = await res.text();
            const parsed = parseCsv(text);

            if (parsed.length) {
              setRows(parsed);
              setStatus(`${parsed.length} CSV rows loaded from ${path}`);
              return;
            }
          } catch {
            // try next path
          }
        }

        try {
          const res = await fetch(`${API}/public/map-data`);
          const data = await res.json();

          const extracted =
            Array.isArray(data) ? data :
            Array.isArray(data.rows) ? data.rows :
            Array.isArray(data.data) ? data.data :
            Array.isArray(data.records) ? data.records :
            [];

          setRows(extracted);
          setStatus(`${extracted.length} rows loaded from backend public endpoint`);
        } catch {
          setRows([]);
          setStatus("No CSV/backend data found. Showing fallback simulation.");
        }
      }

      loadCsv();
    }, []);

    const fallbackRows = [
      { Bolge: "Türkiye", Ulke_Sehir: "İstanbul", Cinsiyet: "Total", Kanser_Turu: "Meme", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 48.2, Yillik_Olum_Hizi_100Bin: 13.4, Bes_Yillik_Sagkalim_Yuzdesi: 82 },
      { Bolge: "Türkiye", Ulke_Sehir: "Ankara", Cinsiyet: "Total", Kanser_Turu: "Akciğer", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 44.8, Yillik_Olum_Hizi_100Bin: 21.1, Bes_Yillik_Sagkalim_Yuzdesi: 37 },
      { Bolge: "Türkiye", Ulke_Sehir: "İzmir", Cinsiyet: "Total", Kanser_Turu: "Kolorektal", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 39.6, Yillik_Olum_Hizi_100Bin: 14.8, Bes_Yillik_Sagkalim_Yuzdesi: 64 },
      { Bolge: "Türkiye", Ulke_Sehir: "Antalya", Cinsiyet: "Total", Kanser_Turu: "Prostat", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 36.5, Yillik_Olum_Hizi_100Bin: 9.2, Bes_Yillik_Sagkalim_Yuzdesi: 89 },
      { Bolge: "Türkiye", Ulke_Sehir: "Trabzon", Cinsiyet: "Total", Kanser_Turu: "Mide", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 31.3, Yillik_Olum_Hizi_100Bin: 15.1, Bes_Yillik_Sagkalim_Yuzdesi: 45 },
      { Bolge: "Europe", Ulke_Sehir: "Germany", Cinsiyet: "Total", Kanser_Turu: "Breast", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 61.4, Yillik_Olum_Hizi_100Bin: 15.7, Bes_Yillik_Sagkalim_Yuzdesi: 86 },
      { Bolge: "Europe", Ulke_Sehir: "France", Cinsiyet: "Total", Kanser_Turu: "Lung", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 52.1, Yillik_Olum_Hizi_100Bin: 24.2, Bes_Yillik_Sagkalim_Yuzdesi: 39 },
      { Bolge: "Europe", Ulke_Sehir: "Italy", Cinsiyet: "Total", Kanser_Turu: "Colorectal", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 47.8, Yillik_Olum_Hizi_100Bin: 16.4, Bes_Yillik_Sagkalim_Yuzdesi: 67 },
      { Bolge: "Europe", Ulke_Sehir: "Spain", Cinsiyet: "Total", Kanser_Turu: "Prostate", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 45.7, Yillik_Olum_Hizi_100Bin: 10.8, Bes_Yillik_Sagkalim_Yuzdesi: 90 },
      { Bolge: "Europe", Ulke_Sehir: "Poland", Cinsiyet: "Total", Kanser_Turu: "All", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 43.2, Yillik_Olum_Hizi_100Bin: 20.4, Bes_Yillik_Sagkalim_Yuzdesi: 58 }
    ];

    const sourceRows = rows.length ? rows : fallbackRows;

    const normalizedRows = sourceRows.map((row) => ({
      region: String(row.Bolge || row.region || "").trim(),
      area: normalizeAreaName(row.Ulke_Sehir || row.city || row.country || row.area || ""),
      sex: String(row.Cinsiyet || row.sex || "All").trim(),
      cancerType: String(row.Kanser_Turu || row.cancerType || row.cancer_type || "All").trim(),
      ageGroup: String(row.Yas_Grubu || row.ageGroup || row.age_group || "All").trim(),
      incidence: toNumber(row.Yillik_Vaka_Hizi_100Bin ?? row.incidence),
      mortality: toNumber(row.Yillik_Olum_Hizi_100Bin ?? row.mortality),
      survival: toNumber(row.Bes_Yillik_Sagkalim_Yuzdesi ?? row.survival)
    })).filter((row) => row.area);

    const turkiyeCitySet = new Set([
      "adana","adiyaman","afyonkarahisar","agri","amasya","ankara","antalya","artvin","aydin","balikesir",
      "bilecik","bingol","bitlis","bolu","burdur","bursa","canakkale","cankiri","corum","denizli",
      "diyarbakir","edirne","elazig","erzincan","erzurum","eskisehir","gaziantep","giresun","gumushane",
      "hakkari","hatay","isparta","mersin","istanbul","izmir","kars","kastamonu","kayseri","kirklareli",
      "kirsehir","kocaeli","konya","kutahya","malatya","manisa","kahramanmaras","mardin","mugla","mus",
      "nevsehir","nigde","ordu","rize","sakarya","samsun","siirt","sinop","sivas","tekirdag","tokat",
      "trabzon","tunceli","sanliurfa","usak","van","yozgat","zonguldak","aksaray","bayburt","karaman",
      "kirikkale","batman","sirnak","bartin","ardahan","igdir","yalova","karabuk","kilis","osmaniye","duzce"
    ]);

    const ascii = (value) =>
      String(value || "")
        .toLowerCase()
        .replaceAll("ı", "i")
        .replaceAll("ğ", "g")
        .replaceAll("ü", "u")
        .replaceAll("ş", "s")
        .replaceAll("ö", "o")
        .replaceAll("ç", "c")
        .replaceAll("İ", "i");

    const isTurkeyRow = (row) => {
      const region = ascii(row.region);
      const area = ascii(row.area);
      return (
        region.includes("turkiye") ||
        region.includes("turkey") ||
        region.includes("tr") ||
        turkiyeCitySet.has(area)
      );
    };

    const cancerOptions = [
      "All",
      ...Array.from(new Set(normalizedRows.map((row) => row.cancerType).filter(Boolean))).sort()
    ].slice(0, 80);

    const ageOptions = [
      "All",
      ...Array.from(new Set(normalizedRows.map((row) => row.ageGroup).filter(Boolean))).sort()
    ].slice(0, 80);

    const sexOptions = [
      "All",
      ...Array.from(new Set(normalizedRows.map((row) => row.sex).filter(Boolean))).sort()
    ].slice(0, 20);

    const filteredRows = normalizedRows.filter((row) => {
      const viewOk = view === "turkiye" ? isTurkeyRow(row) : !isTurkeyRow(row);
      const cancerOk = selectedCancer === "All" || row.cancerType === selectedCancer;
      const ageOk = selectedAge === "All" || row.ageGroup === selectedAge;
      const sexOk = selectedSex === "All" || row.sex === selectedSex;
      return viewOk && cancerOk && ageOk && sexOk;
    });

    const groupedAreas = useMemo(() => {
      const map = new Map();

      filteredRows.forEach((row) => {
        const current = map.get(row.area) || {
          name: row.area,
          rows: 0,
          incidenceValues: [],
          mortalityValues: [],
          survivalValues: [],
          cancerTypes: new Set(),
          sexValues: new Set(),
          ageGroups: new Set()
        };

        current.rows += 1;
        if (Number.isFinite(row.incidence)) current.incidenceValues.push(row.incidence);
        if (Number.isFinite(row.mortality)) current.mortalityValues.push(row.mortality);
        if (Number.isFinite(row.survival)) current.survivalValues.push(row.survival);
        if (row.cancerType) current.cancerTypes.add(row.cancerType);
        if (row.sex) current.sexValues.add(row.sex);
        if (row.ageGroup) current.ageGroups.add(row.ageGroup);

        map.set(row.area, current);
      });

      const avg = (values) => {
        if (!values.length) return null;
        return values.reduce((a, b) => a + b, 0) / values.length;
      };

      return Array.from(map.values()).map((area) => {
        const simulationMultiplier = 1 + ((year - 2024) * 0.018);

        const incidenceBase = avg(area.incidenceValues);
        const mortalityBase = avg(area.mortalityValues);
        const survivalBase = avg(area.survivalValues);

        return {
          ...area,
          incidence: incidenceBase == null ? null : incidenceBase * simulationMultiplier,
          mortality: mortalityBase == null ? null : mortalityBase * simulationMultiplier,
          survival: survivalBase == null ? null : Math.max(5, Math.min(98, survivalBase - ((year - 2024) * 0.25))),
          cancerTypes: Array.from(area.cancerTypes),
          sexValues: Array.from(area.sexValues),
          ageGroups: Array.from(area.ageGroups)
        };
      });
    }, [filteredRows, year]);

    const metricConfig = {
      incidence: {
        label: "New cases",
        short: "Vaka",
        field: "incidence",
        suffix: " / 100K",
        explanation: "Annual case-rate signal. Higher values indicate higher observed burden in the selected dataset."
      },
      mortality: {
        label: "Deaths",
        short: "Ölüm",
        field: "mortality",
        suffix: " / 100K",
        explanation: "Annual mortality-rate signal. It helps identify where care coordination and earlier support matter most."
      },
      survival: {
        label: "5-year survival",
        short: "Sağkalım",
        field: "survival",
        suffix: "%",
        explanation: "Five-year survival percentage when available. Lower values can guide support and awareness planning."
      }
    };

    const currentMetric = metricConfig[metric];

    const sortedAreas = [...groupedAreas].sort((a, b) => {
      const av = a[metric] ?? -Infinity;
      const bv = b[metric] ?? -Infinity;
      return metric === "survival" ? av - bv : bv - av;
    });

    const visibleAreas = showMode === "top15" ? sortedAreas.slice(0, 15) : sortedAreas;

    const selected =
      selectedArea
        ? groupedAreas.find((area) => area.name === selectedArea) || sortedAreas[0]
        : sortedAreas[0];

    const totalSignal = groupedAreas.reduce((sum, area) => {
      const value = area[metric];
      return sum + (Number.isFinite(value) ? value : 0);
    }, 0);

    const formatMetric = (area, key = metric) => {
      const value = area?.[key];
      if (!Number.isFinite(value)) return "-";
      if (key === "survival") return `${value.toFixed(0)}%`;
      return value.toFixed(1);
    };

    const coordinateSeed = (name) => {
      let hash = 0;
      for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
      return Math.abs(hash);
    };

    const fixedTurkeyCoords = {
      "İstanbul": [25, 50],
      "Istanbul": [25, 50],
      "Ankara": [47, 47],
      "İzmir": [20, 62],
      "Izmir": [20, 62],
      "Bursa": [28, 48],
      "Antalya": [36, 70],
      "Adana": [54, 66],
      "Samsun": [55, 37],
      "Trabzon": [79, 39],
      "Erzurum": [82, 47],
      "Diyarbakır": [74, 62],
      "Diyarbakir": [74, 62],
      "Mersin": [51, 68],
      "Konya": [44, 60],
      "Kayseri": [57, 55],
      "Gaziantep": [67, 67],
      "Aydın": [24, 65],
      "Aydin": [24, 65],
      "Muğla": [26, 72],
      "Mugla": [26, 72],
      "Manisa": [23, 58],
      "Kocaeli": [29, 48],
      "Sakarya": [32, 47],
      "Edirne": [18, 44],
      "Van": [89, 56]
    };

    const fixedEuropeCoords = {
      "Germany": [50, 42],
      "France": [39, 52],
      "Italy": [50, 65],
      "Spain": [28, 67],
      "Poland": [59, 39],
      "Netherlands": [43, 38],
      "Greece": [58, 74],
      "Sweden": [54, 22],
      "Norway": [46, 18],
      "Denmark": [48, 32],
      "Belgium": [42, 43],
      "Austria": [55, 52],
      "Portugal": [22, 68],
      "Ireland": [27, 39],
      "United Kingdom": [32, 36],
      "Türkiye": [70, 75],
      "Turkiye": [70, 75],
      "Turkey": [70, 75]
    };

    const getCoords = (areaName, index) => {
      const fixed = view === "turkiye" ? fixedTurkeyCoords[areaName] : fixedEuropeCoords[areaName];
      if (fixed) return fixed;

      const seed = coordinateSeed(areaName + index);
      const x = view === "turkiye"
        ? 18 + (seed % 68)
        : 20 + (seed % 62);
      const y = view === "turkiye"
        ? 35 + ((seed >> 3) % 38)
        : 18 + ((seed >> 4) % 58);

      return [x, y];
    };

    return (
      <div className="csv-map-page">
        <nav className="csv-map-nav">
          <button onClick={() => setPage("landing")}>← Home</button>
          <button onClick={() => setPage("knowledge")}>Knowledge Graph</button>
          <button onClick={() => setPage("copilot")}>AI Copilot</button>
          <button onClick={() => setPage("admin")}>Admin</button>

          <div className="csv-map-status">
            <span></span>
            {status}
          </div>
        </nav>

        <section className="csv-map-hero">
          <div>
            <p className="csv-kicker">INTERACTIVE CANCER MAP</p>
            <h1>Türkiye–Europe cancer burden simulation</h1>
            <p>
              CSV-powered cancer indicators with interactive pins, metric switching,
              year simulation, Top 15 / All view and futuristic area cards.
            </p>
          </div>

          <div className="csv-hero-data">
            <span>CSV / Public data rows</span>
            <strong>{normalizedRows.length}</strong>
            <small>{filteredRows.length} rows after current filters</small>
          </div>
        </section>

        <section className="csv-map-controls">
          <div className="csv-control-row">
            <div className="csv-segment">
              <button className={view === "turkiye" ? "active" : ""} onClick={() => { setView("turkiye"); setSelectedArea(null); }}>
                Türkiye — 81 cities
              </button>
              <button className={view === "europe" ? "active" : ""} onClick={() => { setView("europe"); setSelectedArea(null); }}>
                Europe
              </button>
              <button className={showMode === "top15" ? "active dark" : ""} onClick={() => setShowMode("top15")}>
                Show Top 15
              </button>
              <button className={showMode === "all" ? "active dark" : ""} onClick={() => setShowMode("all")}>
                Show All
              </button>
            </div>

            <div className="csv-year-control">
              <span>Simulation year</span>
              <strong>{year}</strong>
              <input min="2024" max="2030" type="range" value={year} onChange={(e) => setYear(Number(e.target.value))} />
            </div>
          </div>

          <div className="csv-metric-row">
            {Object.entries(metricConfig).map(([key, item]) => (
              <button key={key} className={metric === key ? "active" : ""} onClick={() => setMetric(key)}>
                <small>{item.short}</small>
                <strong>{item.label}</strong>
              </button>
            ))}
          </div>

          <div className="csv-filter-row">
            <label>
              <span>Cancer type</span>
              <select value={selectedCancer} onChange={(e) => { setSelectedCancer(e.target.value); setSelectedArea(null); }}>
                {cancerOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </label>

            <label>
              <span>Age group</span>
              <select value={selectedAge} onChange={(e) => { setSelectedAge(e.target.value); setSelectedArea(null); }}>
                {ageOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </label>

            <label>
              <span>Sex</span>
              <select value={selectedSex} onChange={(e) => { setSelectedSex(e.target.value); setSelectedArea(null); }}>
                {sexOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </label>
          </div>
        </section>

        <section className="csv-map-layout">
          <div className="csv-map-card">
            <div className="csv-map-summary">
              <div><span>View</span><strong>{view === "turkiye" ? "Türkiye" : "Europe"}</strong></div>
              <div><span>Metric</span><strong>{currentMetric.label}</strong></div>
              <div><span>Areas</span><strong>{groupedAreas.length}</strong></div>
              <div><span>Total signal</span><strong>{totalSignal.toFixed(1)}</strong></div>
            </div>

            <div className={`csv-real-map ${view}`}>
              <div className="csv-map-grid"></div>
              <img
                src={view === "turkiye" ? "/assets/map-turkiye.png" : "/assets/map-europe.png"}
                alt={view === "turkiye" ? "Türkiye map" : "Europe map"}
                onError={(e) => { e.currentTarget.style.display = "none"; }}
              />

              <div className="csv-map-overlay-panel">
                <span>{showMode === "top15" ? "Top 15 mode" : "All areas mode"}</span>
                <strong>{currentMetric.label}</strong>
                <small>{metric === "survival" ? "Lower survival appears first" : "Higher burden appears first"}</small>
              </div>

              {visibleAreas.map((area, index) => {
                const [x, y] = getCoords(area.name, index);
                const value = area[metric];
                const scale = Math.max(
                  0.82,
                  Math.min(1.65, Number.isFinite(value) ? value / (metric === "survival" ? 55 : 32) : 1)
                );

                return (
                  <button
                    key={`${area.name}-${index}`}
                    className={`csv-map-pin ${selected?.name === area.name ? "selected" : ""}`}
                    style={{ left: `${x}%`, top: `${y}%`, "--pin-scale": scale }}
                    onClick={() => setSelectedArea(area.name)}
                  >
                    <i></i>
                    <span>{area.name}</span>
                    <b>{formatMetric(area)}</b>
                  </button>
                );
              })}

              {selected && (
                <div className="csv-floating-card">
                  <span>Selected area</span>
                  <h3>{selected.name}</h3>
                  <div><small>New cases</small><strong>{formatMetric(selected, "incidence")}</strong></div>
                  <div><small>Deaths</small><strong>{formatMetric(selected, "mortality")}</strong></div>
                  <div><small>5-year survival</small><strong>{formatMetric(selected, "survival")}</strong></div>
                  <button onClick={() => setPage("copilot")}>Use in AI Copilot</button>
                </div>
              )}
            </div>
          </div>

          <aside className="csv-map-side">
            <div className="csv-selected-card">
              <span>Selected area</span>
              <h2>{selected?.name || "Select a pin"}</h2>
              <p>{currentMetric.explanation}</p>

              <div className="csv-selected-metrics">
                <button className={metric === "incidence" ? "active" : ""} onClick={() => setMetric("incidence")}>
                  <small>Annual cases</small>
                  <strong>{formatMetric(selected, "incidence")}</strong>
                </button>
                <button className={metric === "mortality" ? "active" : ""} onClick={() => setMetric("mortality")}>
                  <small>Annual deaths</small>
                  <strong>{formatMetric(selected, "mortality")}</strong>
                </button>
                <button className={metric === "survival" ? "active" : ""} onClick={() => setMetric("survival")}>
                  <small>5-year survival</small>
                  <strong>{formatMetric(selected, "survival")}</strong>
                </button>
              </div>

              <div className="csv-source-note">
                <strong>{filteredRows.length}</strong>
                <span>filtered rows from CSV/backend</span>
              </div>
            </div>

            <div className="csv-rank-card">
              <span>Ranked areas</span>
              <h3>{currentMetric.label}</h3>

              <div className="csv-rank-list">
                {sortedAreas.slice(0, 12).map((area, index) => (
                  <button key={area.name} className={selected?.name === area.name ? "active" : ""} onClick={() => setSelectedArea(area.name)}>
                    <b>{index + 1}</b>
                    <span>
                      <strong>{area.name}</strong>
                      <small>{area.rows} rows · {area.cancerTypes.slice(0, 2).join(", ") || "mixed"}</small>
                    </span>
                    <em>{formatMetric(area)}</em>
                  </button>
                ))}
              </div>
            </div>
          </aside>
        </section>
      </div>
    );
  };


'''

s = s[:start] + new_map_page + s[end:]
APP.write_text(s, encoding="utf-8")
print("✅ MapPage replaced with CSV-powered interactive Türkiye–Europe map.")

# 3) CSS ekle
css = r'''

/* CSV-powered Futuristic MapPage */

.csv-map-page {
  min-height: 100vh;
  background:
    radial-gradient(circle at 14% 8%, rgba(34, 211, 238, 0.16), transparent 30%),
    radial-gradient(circle at 88% 18%, rgba(124, 58, 237, 0.14), transparent 34%),
    #f5f8fc;
  color: #101828;
}

.csv-map-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  min-height: 62px;
  padding: 0 34px;
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(8, 17, 31, 0.92);
  color: white;
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.csv-map-nav button {
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 999px;
  padding: 10px 15px;
  background: rgba(255,255,255,0.08);
  color: white;
  font-weight: 950;
  cursor: pointer;
}

.csv-map-status {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 10px;
  color: rgba(255,255,255,0.78);
  font-weight: 800;
  font-size: 13px;
}

.csv-map-status span {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: #22c55e;
  box-shadow: 0 0 18px rgba(34,197,94,0.8);
}

.csv-map-hero {
  padding: 78px 6vw 52px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 320px;
  gap: 34px;
  align-items: end;
  color: white;
  background:
    linear-gradient(135deg, rgba(15,23,42,0.96), rgba(30,64,175,0.88)),
    radial-gradient(circle at 80% 20%, rgba(34,211,238,0.28), transparent 34%);
}

.csv-kicker {
  color: #a5f3fc;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.3em;
}

.csv-map-hero h1 {
  margin: 16px 0;
  max-width: 1100px;
  font-size: clamp(46px, 5.5vw, 86px);
  line-height: 0.98;
  letter-spacing: -0.065em;
  color: white;
}

.csv-map-hero p {
  max-width: 980px;
  color: rgba(226,232,240,0.86);
  font-size: 20px;
  line-height: 1.7;
  font-weight: 700;
}

.csv-hero-data {
  padding: 28px;
  border-radius: 28px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.18);
  backdrop-filter: blur(20px);
}

.csv-hero-data span,
.csv-hero-data small {
  display: block;
  color: #a5f3fc;
  font-weight: 900;
}

.csv-hero-data strong {
  display: block;
  color: white;
  font-size: 58px;
  line-height: 1;
  margin: 12px 0;
}

.csv-map-controls {
  width: min(1540px, 94vw);
  margin: -28px auto 28px;
  position: relative;
  z-index: 6;
  display: grid;
  gap: 16px;
}

.csv-control-row {
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 16px;
}

.csv-segment,
.csv-year-control,
.csv-metric-row,
.csv-filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  padding: 14px;
  border-radius: 28px;
  background: white;
  border: 1px solid rgba(15,23,42,0.08);
  box-shadow: 0 22px 70px rgba(15,23,42,0.08);
}

.csv-segment button,
.csv-metric-row button {
  border: 0;
  border-radius: 999px;
  padding: 14px 18px;
  background: #f1f5f9;
  color: #334155;
  font-weight: 950;
  cursor: pointer;
}

.csv-segment button.active,
.csv-metric-row button.active {
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
  box-shadow: 0 16px 36px rgba(21,94,239,0.22);
}

.csv-segment button.dark {
  background: linear-gradient(135deg, #0f172a, #334155);
}

.csv-year-control {
  display: grid;
  grid-template-columns: 1fr 80px;
  align-items: center;
}

.csv-year-control span {
  color: #475467;
  font-weight: 950;
}

.csv-year-control strong {
  color: #155eef;
  font-size: 32px;
  text-align: right;
}

.csv-year-control input {
  grid-column: 1 / -1;
  width: 100%;
  accent-color: #155eef;
}

.csv-metric-row button {
  min-width: 190px;
  text-align: left;
}

.csv-metric-row small,
.csv-metric-row strong {
  display: block;
}

.csv-metric-row small {
  opacity: 0.72;
  font-size: 12px;
}

.csv-filter-row label {
  display: grid;
  gap: 7px;
  min-width: 240px;
  flex: 1;
}

.csv-filter-row span {
  color: #475467;
  font-weight: 900;
}

.csv-filter-row select {
  border: 1px solid #d0d5dd;
  border-radius: 18px;
  padding: 14px 16px;
  background: #f8fafc;
  color: #101828;
  font-weight: 850;
}

.csv-map-layout {
  width: min(1540px, 94vw);
  margin: 0 auto;
  padding: 24px 0 90px;
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(420px, 0.62fr);
  gap: 28px;
  align-items: start;
}

.csv-map-card,
.csv-map-side > div {
  border-radius: 34px;
  background: white;
  border: 1px solid rgba(15,23,42,0.08);
  box-shadow: 0 24px 80px rgba(15,23,42,0.08);
}

.csv-map-card {
  padding: 24px;
}

.csv-map-summary {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-bottom: 20px;
}

.csv-map-summary div {
  padding: 18px;
  border-radius: 20px;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
}

.csv-map-summary span,
.csv-selected-card > span,
.csv-rank-card > span,
.csv-floating-card > span {
  display: block;
  color: #155eef;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.16em;
}

.csv-map-summary strong {
  display: block;
  margin-top: 6px;
  font-size: 22px;
  color: #101828;
}

.csv-real-map {
  position: relative;
  height: 660px;
  border-radius: 30px;
  overflow: hidden;
  background:
    radial-gradient(circle at 30% 20%, rgba(34,211,238,0.24), transparent 26%),
    radial-gradient(circle at 78% 40%, rgba(99,102,241,0.22), transparent 28%),
    linear-gradient(135deg, #020617, #0f2b6f 54%, #082f49);
  border: 1px solid rgba(34,211,238,0.18);
}

.csv-map-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px);
  background-size: 44px 44px;
  opacity: 0.56;
  animation: csvGridMove 16s linear infinite;
}

@keyframes csvGridMove {
  from { transform: translate3d(0,0,0); }
  to { transform: translate3d(44px,44px,0); }
}

.csv-real-map img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  opacity: 0.95;
  z-index: 2;
  filter:
    drop-shadow(0 0 34px rgba(34,211,238,0.34))
    drop-shadow(0 0 70px rgba(37,99,235,0.2));
  pointer-events: none;
}

.csv-map-overlay-panel {
  position: absolute;
  left: 22px;
  top: 22px;
  z-index: 30;
  min-width: 230px;
  padding: 16px 18px;
  border-radius: 22px;
  background: rgba(2, 6, 23, 0.74);
  border: 1px solid rgba(125,211,252,0.26);
  color: white;
  backdrop-filter: blur(18px);
}

.csv-map-overlay-panel span,
.csv-map-overlay-panel small {
  display: block;
  color: #a5f3fc;
  font-weight: 850;
}

.csv-map-overlay-panel strong {
  display: block;
  font-size: 24px;
  margin: 5px 0;
}

.csv-map-pin {
  position: absolute;
  transform: translate(-50%, -50%) scale(var(--pin-scale));
  border: 0;
  background: transparent;
  cursor: pointer;
  z-index: 12;
  color: white;
}

.csv-map-pin i {
  display: block;
  width: 23px;
  height: 23px;
  border-radius: 999px;
  background: #22d3ee;
  border: 4px solid rgba(255,255,255,0.9);
  box-shadow:
    0 0 0 10px rgba(34,211,238,0.16),
    0 0 30px rgba(34,211,238,0.85);
  animation: csvPinPulse 2.2s ease-in-out infinite;
}

@keyframes csvPinPulse {
  0%, 100% { box-shadow: 0 0 0 8px rgba(34,211,238,0.14), 0 0 26px rgba(34,211,238,0.75); }
  50% { box-shadow: 0 0 0 18px rgba(34,211,238,0.04), 0 0 40px rgba(34,211,238,1); }
}

.csv-map-pin.selected i {
  background: #facc15;
  box-shadow:
    0 0 0 13px rgba(250,204,21,0.18),
    0 0 40px rgba(250,204,21,0.95);
}

.csv-map-pin span,
.csv-map-pin b {
  display: none;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  white-space: nowrap;
  background: rgba(2,6,23,0.94);
  border: 1px solid rgba(255,255,255,0.18);
  padding: 7px 10px;
  border-radius: 999px;
  font-size: 12px;
  z-index: 40;
}

.csv-map-pin span {
  bottom: 32px;
}

.csv-map-pin b {
  top: 32px;
  color: #a5f3fc;
}

.csv-map-pin:hover span,
.csv-map-pin:hover b,
.csv-map-pin.selected span,
.csv-map-pin.selected b {
  display: block;
}

.csv-floating-card {
  position: absolute;
  right: 24px;
  bottom: 24px;
  z-index: 45;
  width: 285px;
  padding: 20px;
  border-radius: 24px;
  background: rgba(2, 6, 23, 0.8);
  border: 1px solid rgba(125, 211, 252, 0.28);
  backdrop-filter: blur(20px);
  box-shadow: 0 24px 80px rgba(0,0,0,0.32);
  color: white;
}

.csv-floating-card h3 {
  margin: 8px 0 14px;
  color: white;
  font-size: 28px;
  letter-spacing: -0.04em;
}

.csv-floating-card div {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 0;
  border-top: 1px solid rgba(255,255,255,0.1);
}

.csv-floating-card small {
  color: rgba(226,232,240,0.76);
  font-weight: 800;
}

.csv-floating-card strong {
  color: #a5f3fc;
  font-size: 20px;
}

.csv-floating-card button {
  width: 100%;
  margin-top: 14px;
  border: 0;
  border-radius: 999px;
  padding: 13px 16px;
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
  font-weight: 950;
  cursor: pointer;
}

.csv-map-side {
  display: grid;
  gap: 22px;
}

.csv-selected-card,
.csv-rank-card {
  padding: 28px;
}

.csv-selected-card h2 {
  margin: 10px 0 12px;
  color: #101828;
  font-size: 34px;
  letter-spacing: -0.04em;
}

.csv-selected-card p {
  color: #475467;
  line-height: 1.65;
  font-weight: 700;
}

.csv-selected-metrics {
  display: grid;
  gap: 12px;
  margin-top: 20px;
}

.csv-selected-metrics button {
  text-align: left;
  border: 1px solid #e5e7eb;
  border-radius: 20px;
  padding: 18px;
  background: #f8fafc;
  cursor: pointer;
}

.csv-selected-metrics button.active {
  background: #eef4ff;
  border-color: #155eef;
}

.csv-selected-metrics small,
.csv-selected-metrics strong {
  display: block;
}

.csv-selected-metrics small {
  color: #667085;
  font-weight: 850;
}

.csv-selected-metrics strong {
  color: #101828;
  font-size: 30px;
  margin-top: 4px;
}

.csv-source-note {
  margin-top: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  border-radius: 18px;
  background: #eef4ff;
  border: 1px solid rgba(21,94,239,0.16);
}

.csv-source-note strong {
  font-size: 26px;
  color: #155eef;
}

.csv-source-note span {
  color: #475467;
  font-weight: 850;
}

.csv-rank-card h3 {
  margin: 10px 0 18px;
  font-size: 26px;
}

.csv-rank-list {
  display: grid;
  gap: 12px;
}

.csv-rank-list button {
  display: grid;
  grid-template-columns: 44px 1fr auto;
  gap: 14px;
  align-items: center;
  border: 0;
  border-radius: 20px;
  padding: 14px;
  background: #f8fafc;
  cursor: pointer;
  text-align: left;
}

.csv-rank-list button.active {
  background: #eef4ff;
  box-shadow: 0 0 0 2px rgba(21,94,239,0.12);
}

.csv-rank-list b {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: #dbeafe;
  color: #155eef;
}

.csv-rank-list strong,
.csv-rank-list small {
  display: block;
}

.csv-rank-list small {
  color: #667085;
  margin-top: 3px;
}

.csv-rank-list em {
  color: #101828;
  font-style: normal;
  font-weight: 950;
}

@media (max-width: 1100px) {
  .csv-map-hero,
  .csv-control-row,
  .csv-map-layout {
    grid-template-columns: 1fr;
  }

  .csv-map-summary {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 720px) {
  .csv-map-nav {
    position: static;
    flex-wrap: wrap;
    padding: 14px;
  }

  .csv-map-summary {
    grid-template-columns: 1fr;
  }

  .csv-real-map {
    height: 520px;
  }

  .csv-map-hero h1 {
    font-size: 44px;
  }

  .csv-floating-card {
    left: 18px;
    right: 18px;
    width: auto;
  }
}

'''

CSS.write_text(CSS.read_text(encoding="utf-8") + css, encoding="utf-8")
print("✅ Map CSS appended.")
