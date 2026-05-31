from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# 1) Eski forced dashboard componentini interaktif butonlu component ile değiştir
start = s.find("  const LandingDataDashboard = () =>")
end = s.find("\n\n  const LandingPage", start)

if start == -1 or end == -1:
    raise SystemExit("❌ LandingDataDashboard component bulunamadı.")

new_component = r'''  const LandingDataDashboard = () => {
    const [landingMetric, setLandingMetric] = useState("cases");
    const [landingRegion, setLandingRegion] = useState("turkiye");
    const [landingRows, setLandingRows] = useState([]);

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
      const lines = text.replace(/\r/g, "").split("\n").filter(Boolean);
      if (lines.length < 2) return [];
      const headers = parseCsvLine(lines[0]);

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

    useEffect(() => {
      async function loadLandingCsv() {
        try {
          const res = await fetch("/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv");
          const text = await res.text();
          const parsed = parseCsv(text);
          setLandingRows(parsed);
        } catch {
          setLandingRows([]);
        }
      }

      loadLandingCsv();
    }, []);

    const normalized = landingRows.map((row) => {
      const area = row.Ulke_Sehir || row.city || row.country || row.area || "";
      const region = row.Bolge || row.region || "";
      const areaAscii = ascii(area);
      const isTurkey =
        ascii(region).includes("turkiye") ||
        ascii(region).includes("turkey") ||
        turkiyeCitySet.has(areaAscii);

      return {
        area,
        region: isTurkey ? "turkiye" : "europe",
        cancer: row.Kanser_Turu || "Mixed",
        sex: row.Cinsiyet || "All",
        age: row.Yas_Grubu || "All",
        cases: toNumber(row.Yillik_Vaka_Hizi_100Bin),
        deaths: toNumber(row.Yillik_Olum_Hizi_100Bin),
        survival: toNumber(row.Bes_Yillik_Sagkalim_Yuzdesi)
      };
    }).filter((row) => row.area);

    const grouped = (() => {
      const map = new Map();

      normalized
        .filter((row) => row.region === landingRegion)
        .forEach((row) => {
          const item = map.get(row.area) || {
            area: row.area,
            rows: 0,
            cases: [],
            deaths: [],
            survival: [],
            cancers: new Set()
          };

          item.rows += 1;
          if (Number.isFinite(row.cases)) item.cases.push(row.cases);
          if (Number.isFinite(row.deaths)) item.deaths.push(row.deaths);
          if (Number.isFinite(row.survival)) item.survival.push(row.survival);
          if (row.cancer) item.cancers.add(row.cancer);
          map.set(row.area, item);
        });

      const avg = (arr) => arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : null;

      return Array.from(map.values()).map((item) => ({
        area: item.area,
        rows: item.rows,
        cases: avg(item.cases),
        deaths: avg(item.deaths),
        survival: avg(item.survival),
        cancers: Array.from(item.cancers)
      }));
    })();

    const ranked = [...grouped].sort((a, b) => {
      const av = a[landingMetric] ?? -Infinity;
      const bv = b[landingMetric] ?? -Infinity;
      return landingMetric === "survival" ? av - bv : bv - av;
    }).slice(0, 12);

    const metricLabel = {
      cases: "New cases",
      deaths: "Deaths",
      survival: "5-year survival"
    };

    const metricSuffix = {
      cases: " / 100K",
      deaths: " / 100K",
      survival: "%"
    };

    const formatValue = (value) => {
      if (!Number.isFinite(value)) return "-";
      return landingMetric === "survival" ? `${value.toFixed(0)}%` : value.toFixed(1);
    };

    const maxValue = Math.max(...ranked.map((row) => row[landingMetric] || 0), 1);

    return (
      <section className="landing-live-data">
        <div className="landing-live-head">
          <p>LIVE CANCER DATA LAB</p>
          <h2>Interactive cancer burden explorer</h2>
          <span>
            Click a metric to rank Türkiye cities or European countries by public cancer indicators.
            The chart updates instantly from the CSV layer.
          </span>
        </div>

        <div className="landing-live-switches">
          <div>
            <button className={landingMetric === "cases" ? "active" : ""} onClick={() => setLandingMetric("cases")}>New cases</button>
            <button className={landingMetric === "deaths" ? "active" : ""} onClick={() => setLandingMetric("deaths")}>Deaths</button>
            <button className={landingMetric === "survival" ? "active" : ""} onClick={() => setLandingMetric("survival")}>5-year survival</button>
          </div>

          <div>
            <button className={landingRegion === "turkiye" ? "active dark" : ""} onClick={() => setLandingRegion("turkiye")}>Türkiye cities</button>
            <button className={landingRegion === "europe" ? "active dark" : ""} onClick={() => setLandingRegion("europe")}>Europe countries</button>
          </div>
        </div>

        <div className="landing-live-grid">
          <div className="landing-live-chart">
            <div className="landing-live-chart-title">
              <span>{landingRegion === "turkiye" ? "Türkiye ranking" : "Europe ranking"}</span>
              <strong>{metricLabel[landingMetric]}</strong>
              <small>{ranked.length} ranked areas · {normalized.length} CSV rows loaded</small>
            </div>

            {ranked.map((row, index) => {
              const value = row[landingMetric] || 0;
              const width = Math.max(5, Math.round((value / maxValue) * 100));

              return (
                <div className="landing-live-row" key={row.area}>
                  <b>{index + 1}</b>
                  <div>
                    <strong>{row.area}</strong>
                    <small>{row.rows} rows · {row.cancers.slice(0, 2).join(", ")}</small>
                    <i style={{ width: `${width}%` }}></i>
                  </div>
                  <em>{formatValue(value)}</em>
                </div>
              );
            })}
          </div>

          <aside className="landing-live-side">
            <span>Current view</span>
            <h3>{metricLabel[landingMetric]}</h3>
            <p>
              Showing {landingRegion === "turkiye" ? "Türkiye city-level" : "European country-level"} ranking.
              Values are aggregated from the local CSV and should be treated as public-data indicators,
              not personal medical risk scores.
            </p>

            <div>
              <strong>{normalized.length}</strong>
              <small>CSV rows loaded</small>
            </div>

            <button onClick={() => setPage("map")}>Open full interactive map</button>
          </aside>
        </div>
      </section>
    );
  };
'''

s = s[:start] + new_component + s[end:]
app.write_text(s, encoding="utf-8")

# 2) Eski GLOBOCAN landing bölümünü ve eski force dashboard görünümlerini CSS ile gizle
css_patch = r'''

/* CLEAN LANDING DATA EXPERIENCE */

.landing-data-lab-force,
.landing-data-lab,
.research-data-section,
.globocan-section,
.official-data-section {
  display: none !important;
}

.landing-live-data {
  padding: 80px 5vw;
  background:
    radial-gradient(circle at 10% 10%, rgba(34,211,238,0.14), transparent 30%),
    radial-gradient(circle at 88% 20%, rgba(124,58,237,0.12), transparent 34%),
    #f5f8fc;
}

.landing-live-head p {
  color: #155eef;
  font-weight: 950;
  letter-spacing: 0.26em;
}

.landing-live-head h2 {
  margin: 10px 0;
  font-size: clamp(42px, 5vw, 76px);
  line-height: 1;
  letter-spacing: -0.06em;
  color: #101828;
}

.landing-live-head span {
  display: block;
  max-width: 1050px;
  color: #475467;
  font-size: 20px;
  line-height: 1.65;
  font-weight: 700;
}

.landing-live-switches {
  margin-top: 30px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 16px;
  align-items: center;
}

.landing-live-switches > div {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  padding: 12px;
  border-radius: 999px;
  background: white;
  border: 1px solid #e5e7eb;
  box-shadow: 0 18px 50px rgba(15,23,42,0.08);
}

.landing-live-switches button {
  border: 0;
  border-radius: 999px;
  padding: 14px 20px;
  background: #f1f5f9;
  color: #101828;
  font-weight: 950;
  cursor: pointer;
}

.landing-live-switches button.active {
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
  box-shadow: 0 16px 36px rgba(21,94,239,0.22);
}

.landing-live-switches button.dark {
  background: linear-gradient(135deg, #0f172a, #334155);
}

.landing-live-grid {
  margin-top: 26px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 410px;
  gap: 22px;
}

.landing-live-chart,
.landing-live-side {
  padding: 30px;
  border-radius: 32px;
  background: white;
  border: 1px solid #e5e7eb;
  box-shadow: 0 22px 70px rgba(15,23,42,0.08);
}

.landing-live-chart-title {
  margin-bottom: 22px;
}

.landing-live-chart-title span,
.landing-live-side > span {
  display: block;
  color: #155eef;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.18em;
}

.landing-live-chart-title strong {
  display: block;
  margin: 8px 0 4px;
  color: #101828;
  font-size: 34px;
  letter-spacing: -0.045em;
}

.landing-live-chart-title small {
  color: #667085;
  font-weight: 800;
}

.landing-live-row {
  display: grid;
  grid-template-columns: 44px 1fr 90px;
  gap: 16px;
  align-items: center;
  padding: 13px 0;
  border-top: 1px solid #eef2f7;
  animation: liveRowIn 0.36s ease both;
}

@keyframes liveRowIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.landing-live-row > b {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: #dbeafe;
  color: #155eef;
}

.landing-live-row strong,
.landing-live-row small {
  display: block;
}

.landing-live-row strong {
  color: #101828;
}

.landing-live-row small {
  color: #667085;
  margin: 3px 0 8px;
  font-weight: 750;
}

.landing-live-row i {
  display: block;
  height: 11px;
  border-radius: 999px;
  background: linear-gradient(90deg, #155eef, #14b8a6);
  transition: width 0.42s ease;
}

.landing-live-row em {
  color: #101828;
  font-style: normal;
  font-weight: 950;
  text-align: right;
}

.landing-live-side h3 {
  margin: 10px 0 14px;
  font-size: 34px;
  letter-spacing: -0.04em;
}

.landing-live-side p {
  color: #475467;
  line-height: 1.65;
  font-weight: 700;
}

.landing-live-side div {
  margin: 20px 0;
  padding: 18px;
  border-radius: 20px;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
}

.landing-live-side div strong {
  display: block;
  color: #155eef;
  font-size: 38px;
}

.landing-live-side div small {
  color: #667085;
  font-weight: 850;
}

.landing-live-side button {
  border: 0;
  border-radius: 999px;
  padding: 15px 20px;
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
  font-weight: 950;
  cursor: pointer;
}

@media (max-width: 1050px) {
  .landing-live-switches,
  .landing-live-grid {
    grid-template-columns: 1fr;
  }
}

'''

css.write_text(css.read_text(encoding="utf-8") + css_patch, encoding="utf-8")
print("✅ Landing data dashboard converted to button-based interactive ranking.")
