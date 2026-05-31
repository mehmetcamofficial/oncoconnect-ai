import React, { useEffect, useMemo, useState } from "react";
import "./App.css";

const API = "http://localhost:5050";

function safeNumber(value, fallback = 0) {
  const cleaned = String(value ?? "").replace(",", ".").trim();
  const n = Number(cleaned);
  return Number.isFinite(n) ? n : fallback;
}

function App() {
  const [page, setPage] = useState("landing");
  const [lang, setLang] = useState("en");

  const t = {
    langLabel: lang === "tr" ? "Dil" : "Language",
    home: lang === "tr" ? "Ana Sayfa" : "Home",
    admin: lang === "tr" ? "Admin Panel" : "Admin Panel",
    map: lang === "tr" ? "Harita" : "Map",
    kids: "Onco Kids",
  };


  const LandingDataDashboard = () => {
    const [landingMetric, setLandingMetric] = useState("cases");
    const [landingRegion, setLandingRegion] = useState("turkiye");
    const [landingRows, setLandingRows] = useState([]);
    const [officialRows, setOfficialRows] = useState([]);

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

        try {
          const officialRes = await fetch("/data/official_cancer_sources.csv");
          const officialText = await officialRes.text();
          const officialParsed = parseCsv(officialText);
          setOfficialRows(officialParsed);
        } catch {
          setOfficialRows([]);
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
      survival: "5-year prevalence"
    };

    const researchFeed = [
      {
        type: "Clinical trial",
        title: "Immunotherapy and targeted combinations",
        source: "ClinicalTrials.gov",
        badge: "Trials",
        summary: "Tracks oncology studies involving checkpoint inhibitors, combination regimens and biomarker-selected treatment arms.",
        meta: "Solid tumors · Hematology · Recruitment"
      },
      {
        type: "Innovative drug",
        title: "Antibody-drug conjugate pipeline",
        source: "ESMO / ASCO coverage",
        badge: "Drug updates",
        summary: "Emerging ADC strategies across breast, lung, gastric and colorectal cancer, including HER2-low and target-specific approaches.",
        meta: "ADC · HER2 · Trop-2 · Breast · Lung"
      },
      {
        type: "Research article",
        title: "Early detection and ctDNA monitoring",
        source: "Nature Medicine / NEJM",
        badge: "Research",
        summary: "Liquid biopsy, minimal residual disease, recurrence monitoring and stratified follow-up pathways.",
        meta: "ctDNA · MRD · Screening · Follow-up"
      },
      {
        type: "Funding call",
        title: "Cancer research grants and innovation funds",
        source: "EU4Health / Horizon Europe / Mission Cancer",
        badge: "Funding",
        summary: "Potential grant and consortium opportunities for prevention, screening, data infrastructure and patient-support innovation.",
        meta: "EU grants · Mission Cancer · NGOs · Research"
      },
      {
        type: "Precision medicine",
        title: "Molecular tumor boards and biomarker pathways",
        source: "ESMO Precision Medicine",
        badge: "Precision",
        summary: "Clinical decision pathways using genomic profiling, molecular boards and targeted therapy matching.",
        meta: "NGS · Biomarkers · Targeted therapy"
      },
      {
        type: "AI oncology",
        title: "AI-assisted cancer navigation and triage",
        source: "Digital health research",
        badge: "AI",
        summary: "Decision-support tools for symptom burden, care navigation, research awareness and operational monitoring.",
        meta: "AI copilot · Triage · Monitoring"
      },
      {
        type: "Screening innovation",
        title: "Population screening and early diagnosis",
        source: "CanScreen5 / WHO / IARC",
        badge: "Screening",
        summary: "Organized screening pathways, participation indicators, early diagnosis and public-health coordination.",
        meta: "Breast · Cervical · Colorectal"
      },
      {
        type: "Supportive care",
        title: "Symptom management and survivorship",
        source: "JCO / Lancet Oncology",
        badge: "Care",
        summary: "Fatigue, pain, appetite, psycho-oncology and caregiver support pathways for better quality of life.",
        meta: "Survivorship · Quality of life · Caregiver"
      }
    ];

    const prettyOfficialIndicator = (indicator = "") => {
      const normalized = String(indicator)
        .replaceAll("_", " ")
        .replace(/\bcount\b/gi, "")
        .replace(/\brate per 100000\b/gi, "")
        .trim();

      const custom = {
        "new cases": "Türkiye national new cases",
        "deaths": "Türkiye national deaths",
        "five year prevalence": "Türkiye 5-year prevalence",
        "overall incidence": "Overall incidence rate",
        "overall mortality": "Overall mortality rate",
        "female breast incidence": "Female breast incidence rate",
        "female breast mortality": "Female breast mortality rate",
        "male lung incidence": "Male lung incidence rate"
      };

      return custom[normalized] || normalized.replace(/\b\w/g, (c) => c.toUpperCase());
    };

    const prettyUnit = (unit = "") => {
      const u = String(unit).toLowerCase();
      if (u === "count") return "cases";
      if (u === "rate_per_100000") return "/100k";
      return unit;
    };

    const formatOfficialValue = (value, unit = "") => {
      const n = Number(String(value || "0").replace(",", "."));
      if (!Number.isFinite(n)) return value;

      if (String(unit).toLowerCase() === "count") {
        return new Intl.NumberFormat("tr-TR").format(n);
      }

      if (String(unit).toLowerCase() === "rate_per_100000") {
        return new Intl.NumberFormat("tr-TR", {
          minimumFractionDigits: 0,
          maximumFractionDigits: 1
        }).format(n);
      }

      return new Intl.NumberFormat("tr-TR").format(n);
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

    const unifiedOfficialRows = officialRows
      .filter((row) => {
        const indicator = String(row.indicator || "").toLowerCase();

        if (landingMetric === "cases") {
          return indicator.includes("new_cases") || indicator.includes("incidence");
        }

        if (landingMetric === "deaths") {
          return indicator.includes("deaths") || indicator.includes("mortality");
        }

        return indicator.includes("prevalence") || indicator.includes("survival");
      })
      .map((row) => {
        const value = Number(String(row.value || "0").replace(",", "."));
        const unit = row.unit || "";

        return {
          label:
            row.indicator === "new_cases_count" ? "Türkiye national new cases" :
            row.indicator === "deaths_count" ? "Türkiye national deaths" :
            row.indicator === "five_year_prevalence_count" ? "Türkiye 5-year prevalence" :
            row.indicator.replaceAll("_", " "),
          category:
            String(row.indicator || "").includes("incidence") ? "Screening / incidence indicator" :
            String(row.indicator || "").includes("mortality") ? "Mortality indicator" :
            "Official national estimate",
          area: row.area || "Türkiye",
          source: row.source_name || "Official source",
          year: row.year || "",
          value,
          unit,
          sourceType: "official"
        };
      })
      .filter((row) => Number.isFinite(row.value));

    const unifiedCsvRows = ranked.slice(0, 8).map((row) => ({
      label: row.area,
      category: landingRegion === "turkiye" ? "Türkiye city ranking" : "Europe comparison",
      area: row.area,
      source: "Local CSV cancer layer",
      year: "simulation layer",
      value: row[landingMetric],
      unit: landingMetric === "survival" ? "%" : "rate_per_100000",
      rows: row.rows,
      cancers: row.cancers,
      sourceType: "csv"
    })).filter((row) => Number.isFinite(row.value));

    const mergedCancerRows = [...unifiedOfficialRows, ...unifiedCsvRows];

    const mergedMax = Math.max(
      ...mergedCancerRows.map((row) => {
        if (String(row.unit).toLowerCase() === "count") {
          return Math.log10((row.value || 0) + 1);
        }
        return row.value || 0;
      }),
      1
    );

    const formatMergedValue = (row) => {
      const value = row.value;
      const unit = String(row.unit || "").toLowerCase();

      if (!Number.isFinite(value)) return "-";

      const formatted = new Intl.NumberFormat("tr-TR", {
        maximumFractionDigits: unit === "count" ? 0 : 1
      }).format(value);

      if (unit === "count") return `${formatted} cases`;
      if (unit === "rate_per_100000") return `${formatted} /100k`;
      if (unit === "%") return `${formatted}%`;
      return `${formatted} ${row.unit || ""}`.trim();
    };

    const mergedWidth = (row) => {
      const raw =
        String(row.unit).toLowerCase() === "count"
          ? Math.log10((row.value || 0) + 1)
          : row.value || 0;

      return Math.max(8, Math.round((raw / mergedMax) * 100));
    };

    const officialMetricRows = officialRows
      .filter((row) => {
        const indicator = String(row.indicator || "").toLowerCase();

        if (landingMetric === "cases") {
          return indicator.includes("new_cases") || indicator.includes("incidence");
        }

        if (landingMetric === "deaths") {
          return indicator.includes("deaths") || indicator.includes("mortality");
        }

        return indicator.includes("prevalence") || indicator.includes("survival");
      })
      .map((row) => {
        const rawValue = Number(String(row.value || "0").replace(",", "."));
        const unit = row.unit || "";
        const normalizedValue =
          String(unit).toLowerCase() === "count"
            ? Math.log10((rawValue || 0) + 1)
            : rawValue;

        return {
          label: prettyOfficialIndicator(row.indicator || ""),
          value: rawValue,
          normalizedValue,
          unit,
          source: row.source_name || "Official source",
          area: row.area || "",
          year: row.year || "",
          url: row.source_url || ""
        };
      })
      .filter((row) => Number.isFinite(row.value) && row.value > 0)
      .sort((a, b) => b.value - a.value);

    const officialMaxValue = Math.max(
      ...officialMetricRows.map((row) => row.normalizedValue || 0),
      1
    );

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

        <div className="landing-live-signal">
          <span>Live data stream</span>
          <div>
            <i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i>
          </div>
          <b>{landingRegion === "turkiye" ? "Türkiye city layer" : "Europe country layer"} · {metricLabel[landingMetric]}</b>
        </div>

        <div className="landing-live-grid" key={`${landingRegion}-${landingMetric}`}>
          <div className="landing-live-chart">
            <div className="landing-live-chart-title merged-title">
              <span>Unified cancer intelligence layer</span>
              <strong>{metricLabel[landingMetric]}</strong>
              <small>
                {mergedCancerRows.length} categorized indicators · official estimates + CSV ranking merged · {normalized.length} source rows
              </small>
            </div>

            <div className="landing-merged-intelligence" key={`${landingMetric}-${landingRegion}-${mergedCancerRows.length}`}>
              {mergedCancerRows.map((row, index) => (
                <article
                  className={`merged-data-row ${row.sourceType}`}
                  key={`${landingMetric}-${landingRegion}-${row.sourceType}-${row.label}-${index}`}
                  style={{
                    animationDelay: `${index * 0.075}s`,
                    "--row-delay": `${index * 0.075}s`
                  }}
                >
                  <div className="merged-data-main">
                    <span>{row.category}</span>
                    <h4>{row.label}</h4>
                    <p>
                      {row.sourceType === "csv"
                        ? `${row.rows || 0} rows · ${(row.cancers || []).slice(0, 2).join(", ") || "mixed cancer types"}`
                        : `${row.area} · ${row.year} · ${row.source}`}
                    </p>
                  </div>

                  <div className="merged-data-bar">
                    <i style={{ width: `${mergedWidth(row)}%` }}>
                      <b></b>
                    </i>
                  </div>

                  <strong>{formatMergedValue(row)}</strong>
                </article>
              ))}
            </div>

            {officialMetricRows.length > 0 && (
              <>
                <section className="landing-official-bars">
                  <div className="landing-official-bars-head">
                    <span>Official national estimates</span>
                    <b>{metricLabel[landingMetric]}</b>
                  </div>

                  <div className="landing-official-bars-list">
                    {officialMetricRows.map((row, index) => {
                      const width = Math.max(
                        18,
                        Math.round((row.normalizedValue / officialMaxValue) * 100)
                      );

                      return (
                        <article
                          className="landing-official-bar"
                          key={`${row.label}-${row.value}-${index}`}
                          style={{ animationDelay: `${index * 0.08}s` }}
                        >
                          <div className="landing-official-bar-top">
                            <div>
                              <strong>{row.label}</strong>
                              <small>{row.area} · {row.year} · {row.source}</small>
                            </div>

                            <em>
                              {formatOfficialValue(row.value, row.unit)}{" "}
                              {prettyUnit(row.unit)}
                            </em>
                          </div>

                          <div className="landing-official-bar-track">
                            <i style={{ width: `${width}%` }}>
                              <span></span>
                            </i>
                          </div>
                        </article>
                      );
                    })}
                  </div>
                </section>
              </>
            )}

            <div className="landing-demo-bars-head">
              <span>{landingRegion === "turkiye" ? "Türkiye city ranking from CSV layer" : "Europe ranking from CSV layer"}</span>
            </div>

            {ranked.map((row, index) => {
              const value = row[landingMetric] || 0;
              const width = Math.max(5, Math.round((value / maxValue) * 100));

              return (
                <div
                  className="landing-live-row"
                  key={row.area}
                  style={{ animationDelay: `${index * 0.055}s` }}
                >
                  <b>{index + 1}</b>
                  <div>
                    <strong>{row.area}</strong>
                    <small>{row.rows} rows · {row.cancers.slice(0, 2).join(", ")}</small>
                    <i style={{ width: `${width}%` }}><span></span></i>
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

            <div>
              <strong>{officialRows.length}</strong>
              <small>official source-backed rows</small>
            </div>

            <button onClick={() => setPage("map")}>Open full interactive map</button>
          </aside>
        </div>

        <div className="landing-official-source-strip">
          <span>Official source-backed layer</span>
          <div>
            {officialRows.slice(0, 8).map((row) => (
              <article key={`${row.source_id}-${row.indicator}-${row.value}`}>
                <b>{row.indicator}</b>
                <strong>{row.value} {row.unit}</strong>
                <small>{row.source_name} · {row.area} · {row.year}</small>
              </article>
            ))}
          </div>
        </div>

        <section className="landing-research-feed landing-research-feed-after">
          <div className="landing-research-feed-head">
            <span>Research pulse</span>
            <b>Innovative drugs, trials and oncology reading flow</b>
          </div>

          <div className="landing-research-feed-grid">
            {researchFeed.map((item, index) => (
              <article
                className="landing-research-card"
                key={`${item.title}-${index}`}
                style={{ animationDelay: `${index * 0.07}s` }}
              >
                <div className="landing-research-card-top">
                  <span>{item.badge}</span>
                  <small>{item.type}</small>
                </div>

                <h4>{item.title}</h4>
                <p>{item.summary}</p>

                <div className="landing-research-card-bottom">
                  <b>{item.source}</b>
                  <em>{item.meta}</em>
                </div>
              </article>
            ))}
          </div>
        </section>

      </section>
    );
  };



  const EnhancedFlowSimulation = () => {
    const [scenario, setScenario] = useState("critical");
    const [activeStep, setActiveStep] = useState(0);
    const [isRunning, setIsRunning] = useState(true);
    const [eventCount, setEventCount] = useState(128);

    const scenarios = {
      stable: {
        label: "Stable patient",
        score: 18,
        status: "Stable",
        symptoms: "Fatigue 3 · Pain 2 · Mood 3",
        recommendation: "Continue tracking symptoms and prepare questions for the next visit."
      },
      review: {
        label: "Needs review",
        score: 46,
        status: "Needs review",
        symptoms: "Fatigue 6 · Pain 5 · Mood 6",
        recommendation: "Monitor symptoms closely and share the structured note with the care team."
      },
      critical: {
        label: "High support priority",
        score: 82,
        status: "Critical",
        symptoms: "Fatigue 9 · Pain 8 · Mood 7",
        recommendation: "Contact care team if symptoms are new, worsening or hard to tolerate."
      }
    };

    const current = scenarios[scenario];

    const steps = [
      {
        title: "Patient input",
        subtitle: "Role, symptoms and support need entered",
        detail: current.symptoms,
        icon: "01"
      },
      {
        title: "AI Copilot reasoning",
        subtitle: "Symptom burden is converted into a support signal",
        detail: `Support score ${current.score}/100 · ${current.status}`,
        icon: "02"
      },
      {
        title: "Doctor-ready note",
        subtitle: "Questions and next actions are generated",
        detail: current.recommendation,
        icon: "03"
      },
      {
        title: "Splunk event stream",
        subtitle: "Operational support event is prepared",
        detail: `source=oncoconnect_ai score=${current.score} status=${current.status}`,
        icon: "04"
      }
    ];

    useEffect(() => {
      if (!isRunning) return;

      const timer = setInterval(() => {
        setActiveStep((prev) => (prev + 1) % steps.length);
        setEventCount((prev) => prev + 1);
      }, 1800);

      return () => clearInterval(timer);
    }, [isRunning, scenario]);

    const resetSimulation = () => {
      setActiveStep(0);
      setEventCount(128);
      setIsRunning(true);
    };

    return (
      <EnhancedFlowSimulation />
    );
  };



  const InteractiveFlowSimulation = () => {
    const scenarios = {
      critical: {
        label: "Critical scenario",
        score: 82,
        status: "Critical",
        symptoms: "Fatigue 9 · Pain 8 · Mood 7",
        action: "Support outreach recommended",
        color: "critical"
      },
      review: {
        label: "Needs review",
        score: 46,
        status: "Needs review",
        symptoms: "Fatigue 6 · Pain 5 · Mood 6",
        action: "Monitor symptoms and prepare doctor questions",
        color: "review"
      },
      stable: {
        label: "Stable",
        score: 18,
        status: "Stable",
        symptoms: "Fatigue 3 · Pain 2 · Mood 3",
        action: "Continue tracking symptoms",
        color: "stable"
      }
    };

    const [scenario, setScenario] = useState("critical");
    const [running, setRunning] = useState(true);
    const [step, setStep] = useState(0);
    const [events, setEvents] = useState(128);

    const current = scenarios[scenario];

    const steps = [
      {
        title: "Patient input",
        subtitle: "Role and symptoms entered",
        detail: current.symptoms
      },
      {
        title: "AI Copilot reasoning",
        subtitle: "Support signal calculated",
        detail: `Risk score ${current.score}/100 · ${current.status}`
      },
      {
        title: "Doctor-ready note",
        subtitle: "Questions and next steps generated",
        detail: current.action
      },
      {
        title: "Splunk event",
        subtitle: "Monitoring event streamed",
        detail: `source=oncoconnect_ai status=${current.status}`
      }
    ];

    useEffect(() => {
      if (!running) return;

      const timer = setInterval(() => {
        setStep((prev) => (prev + 1) % steps.length);
        setEvents((prev) => prev + 1);
      }, 1600);

      return () => clearInterval(timer);
    }, [running, scenario]);

    const changeScenario = (key) => {
      setScenario(key);
      setStep(0);
      setEvents((prev) => prev + 3);
      setRunning(true);
    };

    return (
      <section className="inline-live-simulation interactive-flow-live">
        <div className="inline-sim-head">
          <div>
            <p>LIVE FLOW SIMULATION</p>
            <h2>AI support flow running in real time</h2>
            <span>
              Select a scenario and watch how symptom input becomes AI guidance,
              doctor-ready action and Splunk-ready monitoring.
            </span>
          </div>

          <div className={`inline-risk-chip ${current.color}`}>
            <small>Live risk signal</small>
            <strong>{current.score}</strong>
            <b>{current.status}</b>
          </div>
        </div>

        <div className="inline-sim-controls">
          {Object.entries(scenarios).map(([key, item]) => (
            <button
              key={key}
              type="button"
              className={scenario === key ? "active" : ""}
              onClick={() => changeScenario(key)}
            >
              {item.label}
            </button>
          ))}

          <button
            type="button"
            className={`dark ${running ? "active-running" : ""}`}
            onClick={() => setRunning((value) => !value)}
          >
            {running ? "Pause simulation" : "Auto-running"}
          </button>
        </div>

        <div className="inline-sim-canvas">
          <div className="inline-sim-grid"></div>

          <div className={`inline-sim-stream ${running ? "running" : "paused"}`}>
            <i></i>
            <i></i>
            <i></i>
            <i></i>
          </div>

          <div className="inline-sim-steps">
            {steps.map((item, index) => (
              <article
                key={item.title}
                className={step === index ? "active" : step > index ? "done" : ""}
                onClick={() => setStep(index)}
              >
                <b>{String(index + 1).padStart(2, "0")}</b>
                <h3>{item.title}</h3>
                <p>{item.detail}</p>
                <span>{item.subtitle}</span>
              </article>
            ))}
          </div>

          <div className="inline-sim-output">
            <div>
              <span>AI current recommendation</span>
              <h3>{steps[step].title}</h3>
              <p>{steps[step].detail}</p>
            </div>

            <pre>{`{
  source: "oncoconnect_ai",
  scenario: "${scenario}",
  step: "${steps[step].title}",
  risk_score: ${current.score},
  status: "${current.status}",
  event_count: ${events}
}`}</pre>
          </div>
        </div>
      </section>
    );
  };


  const LandingPage = () => (
    <div className="old-home-page">
      <nav className="old-home-nav">
        <div className="old-home-brand">OncoConnect AI</div>

        <div className="old-home-links">
          <button onClick={() => setPage("landing")}>Home</button>
          <a href="#what-is-it">What is it?</a>
          <a href="#how-it-works">How it works</a>
          <a href="#cancer-burden">Cancer Burden</a>
          <a href="#research">Research</a>
          <button type="button" onClick={() => setPage("copilot")}>AI Copilot</button>
          <button type="button" onClick={() => setPage("kids")}>Onco Kids</button>
          <button onClick={() => setPage("admin")}>Admin</button>
          <button onClick={() => setPage("showcase")}>Platform</button>
        </div>

        <div className="old-home-lang">
          <label>{t.langLabel}</label>
          <select value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">English</option>
            <option value="tr">Türkçe</option>
          </select>
        </div>
      </nav>

      <section className="old-portal-hero">
        <div className="old-portal-copy">
          <p className="old-eyebrow">ONCOCONNECT AI PUBLIC PORTAL</p>

          <h1>
            Safe cancer support, research awareness and AI guidance
          </h1>

          <p>
            A two-layer platform for patients, caregivers, clinicians, researchers and NGOs:
            first trusted information, then AI Copilot and Splunk-powered operational monitoring.
          </p>

          <div className="old-hero-actions">
            <button type="button" onClick={() => setPage("copilot")}>Launch AI Copilot</button>
            <button onClick={() => setPage("map")}>Open Knowledge Graph</button>
            <button onClick={() => setPage("kids")}>Onco Kids</button>
          </div>

          <div className="old-disclaimer">
            This platform does not provide diagnosis or treatment advice. It supports doctor-visit
            preparation, trusted source navigation and support coordination.
          </div>
        </div>

        <div className="old-hero-card">
          <div className="old-orb"></div>
          <h3>Calm, clear and safe guidance</h3>
          <p>
            The goal is not to create fear; it is to prepare better questions, surface support
            needs and give care teams more structured information.
          </p>

          <div className="old-companion-pill">
            <span>😊</span>
            <div>
              <strong>Safe companion</strong>
              <small>Guidance with warmth, not fear.</small>
            </div>
          </div>
        </div>
      </section>

      <section id="what-is-it" className="old-section">
        <div className="old-section-head">
          <h2>Patient support portal + AI Copilot + operational monitoring</h2>
          <p>
            OncoConnect AI helps cancer patients and caregivers make symptoms easier to understand,
            prepare for doctor visits and help support teams identify high-risk cases when needed.
          </p>
        </div>

        <div className="old-grid old-grid-3">
          <div className="old-info-card">
            <h3>I want to understand my symptoms</h3>
            <p>AI Copilot explains symptom burden, creates a risk signal and prepares doctor questions.</p>
          </div>
          <div className="old-info-card">
            <h3>I want to prepare for a doctor visit</h3>
            <p>Turns symptoms into a structured conversation note.</p>
          </div>
          <div className="old-info-card">
            <h3>I want simple information for my child</h3>
            <p>Onco Kids provides gentler, hopeful explanations for children and families.</p>
          </div>
          <div className="old-info-card">
            <h3>I want to follow new cancer research</h3>
            <p>A safe source-aware feed for trials, immunotherapy, early detection and patient support.</p>
          </div>
          <div className="old-info-card">
            <h3>I am an NGO or support team</h3>
            <p>Prioritizes high-risk cases through Splunk dashboards and AI summaries.</p>
          </div>
          <div className="old-info-card">
            <h3>I want to see the ecosystem</h3>
            <p>Shows the flow between patients, clinicians, researchers, NGOs, datasets and Splunk.</p>
          </div>
        </div>
      </section>

      
        <InteractiveFlowSimulation />


      <section id="cancer-burden" className="old-section">
        <p className="old-eyebrow dark">CANCER BURDEN</p>
        <h2>Data is not for fear, it is for earlier support and coordination</h2>

        <div className="old-burden-grid">
          <div className="old-burden-card blue water-fill-card">
            <span>Worldwide, 2022</span>
            <strong>~20M</strong>
            <b>new cancer cases</b>
            <p>GLOBOCAN 2022 estimates around 20 million new cancer cases worldwide.</p>
          </div>

          <div className="old-burden-card blue water-fill-card">
            <span>Worldwide, 2022</span>
            <strong>~9.7M</strong>
            <b>cancer deaths</b>
            <p>This highlights the importance of support, awareness, screening and care coordination.</p>
          </div>

          <div className="old-burden-card teal water-fill-card">
            <span>Türkiye context</span>
            <strong>Türkiye</strong>
            <b>country-level cancer statistics</b>
            <p>Lung, breast and colorectal cancers are among key cancer burden areas for Türkiye.</p>
          </div>

          <div className="old-burden-card purple water-fill-card">
            <span>EU Cancer Mission</span>
            <strong>2030</strong>
            <b>quality of life and care goals</b>
            <p>The EU approach emphasizes prevention, cure, quality of life and family support.</p>
          </div>
        </div>
      </section>

      <section id="research" className="old-section old-research-section">
        <p className="old-eyebrow dark">RESEARCH DATA</p>
        <h2>GLOBOCAN 2022 data connected for Türkiye</h2>
        <p className="old-section-desc">
          This section shows source-backed national data. The 81-city map remains a demo distribution
          until official province-level open data is available.
        </p>

        <div className="old-source-grid">
          <div>
            <strong>GLOBOCAN 2022</strong>
            <p>Türkiye total new cases, deaths and 5-year prevalence</p>
          </div>
          <div>
            <strong>ECIS</strong>
            <p>Cancer burden indicators for European countries</p>
          </div>
          <div>
            <strong>HSGM</strong>
            <p>Türkiye official annual cancer statistics reports</p>
          </div>
        </div>

        <div className="old-turkiye-stats">
          <div>
            <span>Türkiye, 2022</span>
            <strong>240,013</strong>
            <b>all cancers new cases</b>
          </div>
          <div>
            <span>Türkiye, 2022</span>
            <strong>129,672</strong>
            <b>all cancers deaths</b>
          </div>
          <div>
            <span>Türkiye, 2022</span>
            <strong>679,335</strong>
            <b>5-year prevalence</b>
          </div>
        </div>

        <div className="old-research-actions">
          <button onClick={() => setPage("map")}>Open Interactive Cancer Map</button>
          <button onClick={() => setPage("admin")}>Open Admin Data Console</button>
        </div>
      </section>
        <LandingDataDashboard />
    </div>
  );


  const CopilotPage = () => {
    const [role, setRole] = useState("patient");
    const [goal, setGoal] = useState("doctor");
    const [cancerType, setCancerType] = useState("all");
    const [treatmentStage, setTreatmentStage] = useState("chemotherapy");
    const [mainConcern, setMainConcern] = useState("fatigue");
    const [city, setCity] = useState("İstanbul");
    const [ageGroup, setAgeGroup] = useState("All");
    const [fatigue, setFatigue] = useState(6);
    const [pain, setPain] = useState(4);
    const [nausea, setNausea] = useState(3);
    const [mood, setMood] = useState(5);
    const [activeInsight, setActiveInsight] = useState("ai");
    const [eventSent, setEventSent] = useState(false);
    const [mapRows, setMapRows] = useState([]);

    useEffect(() => {
      async function loadPublicRows() {
        try {
          const res = await fetch(`${API}/public/map-data`);
          const data = await res.json();

          const rows =
            Array.isArray(data) ? data :
            Array.isArray(data.rows) ? data.rows :
            Array.isArray(data.data) ? data.data :
            Array.isArray(data.records) ? data.records :
            [];

          setMapRows(rows);
        } catch {
          setMapRows([]);
        }
      }

      loadPublicRows();
    }, []);

    const roleLabels = {
      patient: "I am a patient",
      caregiver: "I am a family member / caregiver",
      support: "I am a support team"
    };

    const goalLabels = {
      symptoms: "Understand my symptoms",
      doctor: "Prepare for my doctor visit",
      urgent: "Know when to ask for urgent support",
      child: "Explain this gently to a child"
    };

    const cancerLabels = {
      all: "All cancer types",
      breast: "Breast cancer",
      lung: "Lung cancer",
      colorectal: "Colorectal cancer",
      prostate: "Prostate cancer",
      leukemia: "Leukemia / blood cancer",
      other: "Other / not sure"
    };

    const cancerMatch = {
      all: "",
      breast: "Meme",
      lung: "Akciğer",
      colorectal: "Kolorektal",
      prostate: "Prostat",
      leukemia: "Lösemi",
      other: ""
    };

    const stageLabels = {
      diagnosis: "Recently diagnosed",
      chemotherapy: "Receiving chemotherapy",
      radiotherapy: "Receiving radiotherapy",
      surgery: "Before / after surgery",
      followup: "Follow-up / remission",
      palliative: "Supportive / palliative care"
    };

    const concernLabels = {
      fatigue: "Fatigue / weakness",
      pain: "Pain",
      nausea: "Nausea / appetite",
      anxiety: "Fear / anxiety",
      sleep: "Sleep problems",
      questions: "I do not know what to ask"
    };

    const cityOptions = Array.from(
      new Set(
        mapRows
          .map((row) => row.Ulke_Sehir || row.city || row.country)
          .filter(Boolean)
      )
    ).slice(0, 120);

    const ageOptions = [
      "All",
      ...Array.from(
        new Set(
          mapRows
            .map((row) => row.Yas_Grubu)
            .filter(Boolean)
        )
      )
    ].slice(0, 40);

    const filteredRows = mapRows.filter((row) => {
      const rowCity = row.Ulke_Sehir || row.city || row.country || "";
      const rowAge = row.Yas_Grubu || "";
      const rowCancer = row.Kanser_Turu || "";
      const cancerNeedle = cancerMatch[cancerType];

      const cityOk = !city || rowCity === city;
      const ageOk = ageGroup === "All" || rowAge === ageGroup;
      const cancerOk = !cancerNeedle || rowCancer.toLowerCase().includes(cancerNeedle.toLowerCase());

      return cityOk && ageOk && cancerOk;
    });

    const avg = (key) => {
      const nums = filteredRows
        .map((row) => safeNumber(row[key], NaN))
        .filter((n) => Number.isFinite(n));

      if (!nums.length) return null;
      return nums.reduce((a, b) => a + b, 0) / nums.length;
    };

    const incidenceAvg = avg("Yillik_Vaka_Hizi_100Bin");
    const mortalityAvg = avg("Yillik_Olum_Hizi_100Bin");
    const survivalAvg = avg("Bes_Yillik_Sagkalim_Yuzdesi");

    const symptomScore = Math.round(fatigue * 2.2 + pain * 2.4 + nausea * 1.8 + mood * 2.1);
    const dataSignal =
      incidenceAvg && mortalityAvg
        ? Math.min(30, Math.round((incidenceAvg + mortalityAvg) / 7))
        : 8;

    const supportScore = Math.min(100, symptomScore + dataSignal);

    const supportLevel =
      supportScore >= 72 ? "High support priority" :
      supportScore >= 45 ? "Needs attention" :
      "Stable today";

    const supportClass =
      supportScore >= 72 ? "high" :
      supportScore >= 45 ? "medium" :
      "low";

    const doctorQuestions = [
      "Which of my symptoms are expected, and which ones should I report immediately?",
      "At what point should I call the clinic or seek urgent support?",
      "Could fatigue, pain or nausea be related to my treatment?",
      "What should I track daily before my next visit?",
      "Is there anything my caregiver should watch for at home?"
    ];

    const actionSteps =
      supportScore >= 72
        ? [
            "Do not ignore today’s symptoms.",
            "Contact your care team or clinic if symptoms are new, worsening or hard to tolerate.",
            "Share the structured note below with a doctor, nurse or caregiver.",
            "Ask clearly: “When should I seek urgent support?”"
          ]
        : supportScore >= 45
        ? [
            "Track your symptoms today and tomorrow.",
            "Prepare the doctor questions below before your visit.",
            "Tell a trusted caregiver how you are feeling.",
            "Ask your care team which symptoms should trigger a call."
          ]
        : [
            "Continue tracking symptoms calmly.",
            "Use the questions below for your next doctor visit.",
            "Share changes early if symptoms increase.",
            "Keep this note as a simple visit-preparation summary."
          ];

    const aiRecommendation =
      supportScore >= 72
        ? "Your answers suggest that extra support may be needed today. This does not mean a diagnosis or emergency by itself, but it is strong enough to contact a care team, especially if symptoms are new, worsening, or difficult to tolerate."
        : supportScore >= 45
        ? "Your answers suggest that you should monitor symptoms closely and prepare clear questions for your doctor. A caregiver or support team can help you track changes."
        : "Your answers look relatively stable today. Keep tracking symptoms and use the doctor-visit note to communicate clearly at your next appointment.";

    const patientSummary = `ONCOCONNECT AI — Doctor Visit Note

Role: ${roleLabels[role]}
Goal: ${goalLabels[goal]}
Location / data context: ${city || "Not selected"}
Age group: ${ageGroup}
Cancer context: ${cancerLabels[cancerType]}
Treatment stage: ${stageLabels[treatmentStage]}
Main concern: ${concernLabels[mainConcern]}

Symptoms today:
- Fatigue / weakness: ${fatigue}/10
- Pain: ${pain}/10
- Nausea / appetite problem: ${nausea}/10
- Fear, worry or low mood: ${mood}/10

Data signal:
- Matching public data rows: ${filteredRows.length}
- Average annual incidence: ${incidenceAvg ? incidenceAvg.toFixed(2) : "not available"}
- Average annual mortality: ${mortalityAvg ? mortalityAvg.toFixed(2) : "not available"}
- Five-year survival: ${survivalAvg ? survivalAvg.toFixed(1) + "%" : "not available"}

Support priority:
${supportScore}/100 — ${supportLevel}

AI recommendation:
${aiRecommendation}`;

    const copySummary = async () => {
      try {
        await navigator.clipboard.writeText(patientSummary);
        alert("Doctor visit note copied.");
      } catch {
        alert(patientSummary);
      }
    };

    const sendEvent = () => {
      setEventSent(true);
      setActiveInsight("splunk");
      setTimeout(() => setEventSent(false), 2600);
    };

    return (
      <div className="patient-copilot-page">
        <nav className="patient-copilot-nav">
          <button onClick={() => setPage("landing")}>← Home</button>
          <button onClick={() => setPage("map")}>Türkiye / Europe Map</button>
          <button onClick={() => setPage("kids")}>Onco Kids</button>

          <div className="patient-copilot-lang">
            <label>{t.langLabel}</label>
            <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">English</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>
        </nav>

        <section className="patient-copilot-hero">
          <div>
            <p className="patient-kicker">ONCOCONNECT AI COPILOT</p>
            <h1>Simple cancer support guidance, step by step</h1>
            <p>
              Choose your situation, select your city and age group, enter symptoms,
              then generate an AI recommendation, risk explanation, doctor note and Splunk support event.
            </p>

            <div className="patient-hero-actions">
              <button onClick={() => setActiveInsight("ai")} className={activeInsight === "ai" ? "active" : ""}>
                AI Recommendation
              </button>
              <button onClick={() => setActiveInsight("risk")} className={activeInsight === "risk" ? "active" : ""}>
                Risk Assessment
              </button>
              <button onClick={() => setActiveInsight("note")} className={activeInsight === "note" ? "active" : ""}>
                Doctor Note
              </button>
              <button onClick={sendEvent} className={activeInsight === "splunk" ? "active" : ""}>
                Send Splunk Event
              </button>
            </div>
          </div>

          <div className="patient-hero-card">
            <span>How to use this page</span>
            <ol>
              <li>Choose who you are.</li>
              <li>Select what you want to learn.</li>
              <li>Pick city, age group and cancer context.</li>
              <li>Move symptom sliders.</li>
              <li>Click AI Recommendation or Risk Assessment.</li>
            </ol>
          </div>
        </section>

        <section className="patient-copilot-layout">
          <div className="patient-input-panel">
            <div className="patient-block">
              <div className="patient-block-title">
                <b>1</b>
                <div>
                  <h2>Who are you?</h2>
                  <p>Choose the perspective. The explanation changes based on this.</p>
                </div>
              </div>

              <div className="patient-choice-grid">
                {Object.entries(roleLabels).map(([key, label]) => (
                  <button
                    key={key}
                    className={role === key ? "selected" : ""}
                    onClick={() => setRole(key)}
                  >
                    {label}
                  </button>
                ))}
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>2</b>
                <div>
                  <h2>What do you want to learn today?</h2>
                  <p>Choose one simple goal.</p>
                </div>
              </div>

              <div className="patient-choice-grid two">
                {Object.entries(goalLabels).map(([key, label]) => (
                  <button
                    key={key}
                    className={goal === key ? "selected" : ""}
                    onClick={() => setGoal(key)}
                  >
                    {label}
                  </button>
                ))}
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>3</b>
                <div>
                  <h2>Select data context</h2>
                  <p>City, age group and cancer type are read from the public dataset when available.</p>
                </div>
              </div>

              <div className="patient-dropdown-grid">
                <label>
                  <span>City / country</span>
                  <select value={city} onChange={(e) => setCity(e.target.value)}>
                    <option value="">All locations</option>
                    {(cityOptions.length ? cityOptions : ["İstanbul", "Ankara", "İzmir", "Türkiye"]).map((item) => (
                      <option key={item} value={item}>{item}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Age group</span>
                  <select value={ageGroup} onChange={(e) => setAgeGroup(e.target.value)}>
                    {ageOptions.map((item) => (
                      <option key={item} value={item}>{item}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Cancer type</span>
                  <select value={cancerType} onChange={(e) => setCancerType(e.target.value)}>
                    {Object.entries(cancerLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Treatment stage</span>
                  <select value={treatmentStage} onChange={(e) => setTreatmentStage(e.target.value)}>
                    {Object.entries(stageLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>Main concern today</span>
                  <select value={mainConcern} onChange={(e) => setMainConcern(e.target.value)}>
                    {Object.entries(concernLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>4</b>
                <div>
                  <h2>How strong are your symptoms today?</h2>
                  <p>0 means none. 10 means very strong.</p>
                </div>
              </div>

              <div className="patient-slider-list">
                {[
                  ["Fatigue / weakness", fatigue, setFatigue],
                  ["Pain", pain, setPain],
                  ["Nausea / appetite problem", nausea, setNausea],
                  ["Fear, worry or low mood", mood, setMood]
                ].map(([label, value, setter]) => (
                  <label key={label}>
                    <div>
                      <span>{label}</span>
                      <strong>{value}/10</strong>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={value}
                      onChange={(e) => setter(Number(e.target.value))}
                    />
                  </label>
                ))}
              </div>

              <div className="patient-primary-actions">
                <button onClick={() => setActiveInsight("ai")}>Generate AI recommendation</button>
                <button onClick={() => setActiveInsight("risk")}>Run risk assessment</button>
                <button onClick={() => setActiveInsight("note")}>Create doctor note</button>
                <button onClick={sendEvent}>Send to Splunk</button>
              </div>
            </div>
          </div>

          <aside className="patient-output-panel">
            <div className={`patient-score-card ${supportClass}`}>
              <span>Support priority</span>
              <strong>{supportScore}</strong>
              <b>{supportLevel}</b>
              <p>
                This is not a diagnosis. It is a support-priority signal combining your symptom inputs
                with the selected public data context.
              </p>
            </div>

            <div className="patient-data-card">
              <span>Dataset signal</span>
              <h2>{city || "All locations"} · {ageGroup}</h2>
              <div className="patient-data-grid">
                <div>
                  <small>Rows</small>
                  <strong>{filteredRows.length}</strong>
                </div>
                <div>
                  <small>Incidence</small>
                  <strong>{incidenceAvg ? incidenceAvg.toFixed(1) : "-"}</strong>
                </div>
                <div>
                  <small>Mortality</small>
                  <strong>{mortalityAvg ? mortalityAvg.toFixed(1) : "-"}</strong>
                </div>
                <div>
                  <small>5-year survival</small>
                  <strong>{survivalAvg ? `${survivalAvg.toFixed(0)}%` : "-"}</strong>
                </div>
              </div>
            </div>

            <div className="patient-insight-tabs">
              <button className={activeInsight === "ai" ? "active" : ""} onClick={() => setActiveInsight("ai")}>AI</button>
              <button className={activeInsight === "risk" ? "active" : ""} onClick={() => setActiveInsight("risk")}>Risk</button>
              <button className={activeInsight === "actions" ? "active" : ""} onClick={() => setActiveInsight("actions")}>Actions</button>
              <button className={activeInsight === "note" ? "active" : ""} onClick={() => setActiveInsight("note")}>Note</button>
              <button className={activeInsight === "splunk" ? "active" : ""} onClick={() => setActiveInsight("splunk")}>Splunk</button>
            </div>

            {activeInsight === "ai" && (
              <div className="patient-result-card">
                <span>AI recommendation</span>
                <h2>What should I understand?</h2>
                <p>{aiRecommendation}</p>
              </div>
            )}

            {activeInsight === "risk" && (
              <div className="patient-result-card">
                <span>Risk assessment</span>
                <h2>Why this priority?</h2>
                <p>
                  The score combines today’s symptom strength with the selected data context.
                  Higher symptom values and higher public incidence/mortality signal increase the support priority.
                </p>
                <ul>
                  <li>Symptom signal: {symptomScore}/70</li>
                  <li>Dataset signal: {dataSignal}/30</li>
                  <li>Total support priority: {supportScore}/100</li>
                </ul>
              </div>
            )}

            {activeInsight === "actions" && (
              <div className="patient-result-card">
                <span>Next steps</span>
                <h2>What should I do now?</h2>
                <ul>
                  {actionSteps.map((step) => <li key={step}>{step}</li>)}
                </ul>
              </div>
            )}

            {activeInsight === "note" && (
              <div className="patient-note-card">
                <span>Doctor visit note</span>
                <pre>{patientSummary}</pre>

                <div className="patient-note-actions">
                  <button onClick={copySummary}>Copy note</button>
                  <button onClick={() => setActiveInsight("actions")}>Show next steps</button>
                </div>
              </div>
            )}

            {activeInsight === "splunk" && (
              <div className="patient-note-card">
                <span>Splunk event preview</span>
                <pre>{`{
  "source": "oncoconnect_ai_copilot",
  "role": "${role}",
  "goal": "${goal}",
  "city": "${city}",
  "age_group": "${ageGroup}",
  "cancer_type": "${cancerType}",
  "support_score": ${supportScore},
  "support_level": "${supportLevel}",
  "incidence": "${incidenceAvg ? incidenceAvg.toFixed(2) : "NA"}",
  "mortality": "${mortalityAvg ? mortalityAvg.toFixed(2) : "NA"}",
  "survival": "${survivalAvg ? survivalAvg.toFixed(1) : "NA"}"
}`}</pre>

                <div className="patient-note-actions">
                  <button onClick={sendEvent}>Send support event</button>
                  <button onClick={() => setActiveInsight("note")}>Create doctor note</button>
                </div>

                {eventSent && (
                  <div className="patient-event-success">
                    Splunk support event prepared successfully.
                  </div>
                )}
              </div>
            )}

            <div className="patient-result-card">
              <span>Doctor visit preparation</span>
              <h2>Questions to ask</h2>
              <ul>
                {doctorQuestions.map((question) => <li key={question}>{question}</li>)}
              </ul>
            </div>
          </aside>

        <section className="landing-data-lab">
          <div className="landing-data-head">
            <p className="csv-kicker">LIVE CANCER DATA LAB</p>
            <h2>Interactive cancer burden explorer</h2>
            <p>
              Explore cases, deaths and 5-year survival by cancer type, sex and age group.
              This turns the CSV layer into an interactive public data dashboard.
            </p>
          </div>

          <div className="landing-data-filters">
            <label>
              <span>Metric</span>
              <select defaultValue="cases">
                <option value="cases">New cases</option>
                <option value="deaths">Deaths</option>
                <option value="survival">5-year survival</option>
              </select>
            </label>

            <label>
              <span>Sex</span>
              <select defaultValue="All">
                <option>All</option>
                <option>Erkek</option>
                <option>Kadın</option>
              </select>
            </label>

            <label>
              <span>Age group</span>
              <select defaultValue="All">
                <option>All</option>
                <option>0-29</option>
                <option>30-49</option>
                <option>50-69</option>
                <option>70+</option>
              </select>
            </label>

            <label>
              <span>Cancer type</span>
              <select defaultValue="All">
                <option>All</option>
                <option>Akciğer</option>
                <option>Meme</option>
                <option>Kolorektal</option>
                <option>Prostat</option>
                <option>Mide</option>
              </select>
            </label>
          </div>

          <div className="landing-data-grid">
            <div className="landing-data-kpi blue">
              <span>Türkiye, 2022</span>
              <strong>240,013</strong>
              <p>all cancers new cases</p>
            </div>

            <div className="landing-data-kpi orange">
              <span>Türkiye, 2022</span>
              <strong>129,672</strong>
              <p>all cancers deaths</p>
            </div>

            <div className="landing-data-kpi green">
              <span>Türkiye, 2022</span>
              <strong>67%</strong>
              <p>estimated 5-year survival signal</p>
            </div>
          </div>

          <div className="landing-chart-area">
            <div className="landing-bars">
              {[
                ["Lung", 92],
                ["Breast", 74],
                ["Colorectum", 61],
                ["Prostate", 48],
                ["Stomach", 39]
              ].map(([name, value]) => (
                <div className="landing-bar-row" key={name}>
                  <div>
                    <b>{name}</b>
                    <span>{value} — burden index</span>
                  </div>
                  <i style={{ width: `${value}%` }}></i>
                </div>
              ))}
            </div>

            <div className="landing-data-note">
              <h3>How to read this</h3>
              <p>
                These values are not personal medical risk scores. They are public-data indicators
                for awareness, research prioritization and care coordination.
              </p>
              <button onClick={() => setPage("map")}>Open full interactive map</button>
            </div>
          </div>
        </section>

        </section>
      </div>
    );
  };



  const KnowledgeGraphPage = () => (
    <div className="knowledge-page">
      <nav className="future-map-nav">
        <button onClick={() => setPage("landing")}>← Home</button>
        <button onClick={() => setPage("map")}>Türkiye–Europe Map</button>
        <button onClick={() => setPage("copilot")}>AI Copilot</button>
      </nav>

      <section className="knowledge-hero">
        <p className="future-kicker">KNOWLEDGE GRAPH</p>
        <h1>Cancer support ecosystem graph</h1>
        <p>
          This page shows how patients, caregivers, clinicians, NGOs, datasets,
          AI Copilot, public map and Splunk monitoring are connected.
        </p>
      </section>

      <section className="knowledge-canvas">
        <div className="kg-node patient">Patient</div>
        <div className="kg-node caregiver">Caregiver</div>
        <div className="kg-node copilot">AI Copilot</div>
        <div className="kg-node doctor">Clinician</div>
        <div className="kg-node dataset">Cancer Dataset</div>
        <div className="kg-node map">Public Map</div>
        <div className="kg-node ngo">NGO / Support Team</div>
        <div className="kg-node splunk">Splunk Monitoring</div>

        <svg className="kg-lines" viewBox="0 0 1000 560" preserveAspectRatio="none">
          <line x1="160" y1="150" x2="500" y2="250" />
          <line x1="220" y1="390" x2="500" y2="250" />
          <line x1="500" y1="250" x2="790" y2="150" />
          <line x1="500" y1="250" x2="790" y2="390" />
          <line x1="500" y1="250" x2="500" y2="470" />
          <line x1="500" y1="470" x2="790" y2="470" />
          <line x1="500" y1="470" x2="210" y2="470" />
        </svg>
      </section>
    </div>
  );


  const MapPage = () => {
    const [rows, setRows] = useState([]);
    const [officialMapRows, setOfficialMapRows] = useState([]);
    const [status, setStatus] = useState("Loading CSV data...");
    const [view, setView] = useState("turkiye");
    const [metric, setMetric] = useState("incidence");
    const [showMode, setShowMode] = useState("top15");
    const [year, setYear] = useState(2024);
    const [selectedArea, setSelectedArea] = useState(null);
    const [hoveredArea, setHoveredArea] = useState(null);
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

    useEffect(() => {
      async function loadOfficialMapRows() {
        try {
          const res = await fetch("/data/official_cancer_sources.csv");
          const text = await res.text();
          const parsed = parseCsv(text);
          setOfficialMapRows(parsed);
        } catch {
          setOfficialMapRows([]);
        }
      }

      loadOfficialMapRows();
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

    const activeArea = hoveredArea
      ? groupedAreas.find((area) => area.name === hoveredArea) || selected
      : selectedArea
        ? selected
        : null;

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
      "Adana": [53, 64],
      "Samsun": [55, 37],
      "Trabzon": [76, 40],
      "Erzurum": [78, 47],
      "Diyarbakır": [72, 61],
      "Diyarbakir": [72, 61],
      "Mersin": [51, 68],
      "Konya": [44, 60],
      "Kayseri": [57, 55],
      "Gaziantep": [65, 64],
      "Aydın": [24, 65],
      "Aydin": [24, 65],
      "Muğla": [26, 72],
      "Mugla": [26, 72],
      "Manisa": [23, 58],
      "Kocaeli": [29, 48],
      "Sakarya": [32, 47],
      "Edirne": [18, 44],
      "Van": [80, 56]
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

    const turkeyAutoCoords = [
      [24, 52], [27, 57], [31, 49], [34, 60], [38, 54], [41, 47], [44, 61],
      [48, 53], [51, 46], [54, 58], [58, 51], [61, 62], [64, 55], [67, 46],
      [70, 56], [73, 50], [76, 59], [79, 52], [81, 46], [82, 56],
      [33, 66], [43, 66], [53, 66], [63, 64], [73, 64],
      [36, 40], [46, 39], [56, 38], [66, 39], [76, 40]
    ];

    const europeAutoCoords = [
      [34, 40], [39, 48], [45, 37], [50, 51], [56, 42], [61, 55], [67, 45],
      [43, 62], [52, 67], [31, 58], [58, 30], [48, 27], [70, 61], [38, 32],
      [63, 35], [73, 52], [28, 46], [46, 72], [57, 73], [68, 70]
    ];

    const getCoords = (areaName, index) => {
      const fixed = view === "turkiye" ? fixedTurkeyCoords[areaName] : fixedEuropeCoords[areaName];
      if (fixed) return fixed;

      const list = view === "turkiye" ? turkeyAutoCoords : europeAutoCoords;
      return list[index % list.length];
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

              <div className="csv-map-year-inline">
                <span>Simulation year</span>
                <strong>{year}</strong>
                <input min="2024" max="2030" type="range" value={year} onChange={(e) => setYear(Number(e.target.value))} />
              </div>

              <div className="csv-map-data-stream">
                <span>CSV + official source stream</span>
                <b>{normalizedRows.length} CSV rows</b>
                <b>{officialMapRows.length} verified rows</b>
                <i></i>
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
                    className={`csv-map-pin ${activeArea?.name === area.name ? "selected" : ""}`}
                    style={{ left: `${x}%`, top: `${y}%`, "--pin-scale": scale }}
                    onMouseEnter={() => setHoveredArea(area.name)}
                    onMouseLeave={() => {
                      setHoveredArea(null);
                      setSelectedArea(null);
                    }}
                    onFocus={() => setHoveredArea(area.name)}
                    onBlur={() => setHoveredArea(null)}
                    onClick={() => setSelectedArea((prev) => prev === area.name ? null : area.name)}
                  >
                    <i></i>
                    <span>{area.name}</span>
                    <b>{formatMetric(area)}</b>
                  </button>
                );
              })}

              {activeArea && (
                <div className="csv-floating-card">
                  <span>Selected area</span>
                  <h3>{activeArea.name}</h3>
                  <div><small>New cases</small><strong>{formatMetric(activeArea, "incidence")}</strong></div>
                  <div><small>Deaths</small><strong>{formatMetric(activeArea, "mortality")}</strong></div>
                  <div><small>5-year survival</small><strong>{formatMetric(activeArea, "survival")}</strong></div>
                  
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


  const AdminPanel = () => {
    const [datasets, setDatasets] = useState([]);
    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("");
    const [loading, setLoading] = useState(false);
    const [tab, setTab] = useState("datasets");

    async function loadDatasets() {
      try {
        const res = await fetch(`${API}/admin/datasets`);
        const data = await res.json();
        setDatasets(Array.isArray(data) ? data : data.datasets || []);
      } catch (err) {
        setStatus(err.message || "Dataset load failed");
      }
    }

    useEffect(() => {
      loadDatasets();
    }, []);

    async function uploadDataset() {
      if (!file) {
        setStatus("Please select a CSV file first.");
        return;
      }

      setLoading(true);
      setStatus("Uploading dataset...");

      try {
        const form = new FormData();
        form.append("file", file);

        const res = await fetch(`${API}/admin/upload`, {
          method: "POST",
          body: form
        });

        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Upload failed");

        setStatus(`Uploaded: ${data.dataset?.name || file.name}`);
        setFile(null);
        await loadDatasets();
      } catch (err) {
        setStatus(err.message || "Upload failed");
      } finally {
        setLoading(false);
      }
    }

    async function updateDataset(id, patch) {
      setLoading(true);
      try {
        const res = await fetch(`${API}/admin/datasets/${id}`, {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(patch)
        });

        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Update failed");

        setStatus("Dataset updated.");
        await loadDatasets();
      } catch (err) {
        setStatus(err.message || "Update failed");
      } finally {
        setLoading(false);
      }
    }

    async function deleteDataset(id) {
      if (!confirm("Delete this dataset?")) return;

      setLoading(true);
      try {
        const res = await fetch(`${API}/admin/datasets/${id}`, {
          method: "DELETE"
        });

        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Delete failed");

        setStatus("Dataset deleted.");
        await loadDatasets();
      } catch (err) {
        setStatus(err.message || "Delete failed");
      } finally {
        setLoading(false);
      }
    }

    async function runAutoResearch() {
      setLoading(true);
      setStatus("Auto Research Agent is scanning trusted cancer data sources...");

      try {
        const res = await fetch(`${API}/admin/auto-research`, { method: "POST" });
        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Auto research failed");

        setStatus(data.message || "Auto research draft generated.");
        await loadDatasets();
        setTab("datasets");
      } catch (err) {
        setStatus(err.message || "Auto research failed");
      } finally {
        setLoading(false);
      }
    }

    async function runOfficialIngest() {
      setLoading(true);
      setStatus("Official Data Ingestion Agent is fetching, normalizing and validating indicators...");

      try {
        const res = await fetch(`${API}/admin/auto-ingest`, { method: "POST" });
        const data = await res.json();

        if (!data.success) throw new Error(data.error || "Official ingestion failed");

        setStatus(
          `Official ingestion draft generated: ${data.dataset?.rowCount || 0} validated rows`
        );
        await loadDatasets();
        setTab("datasets");
      } catch (err) {
        setStatus(err.message || "Official ingestion failed");
      } finally {
        setLoading(false);
      }
    }

    const totalRows = datasets.reduce((sum, d) => sum + safeNumber(d.rowCount), 0);
    const publishedCount = datasets.filter((d) => d.published).length;

    return (
      <div className="admin-page-v35">
        <header className="admin-topbar-v35">
          <button onClick={() => setPage("landing")}>
            {lang === "tr" ? "← Ana Sayfa" : "← Home"}
          </button>
          <strong>OncoConnect Admin Console</strong>
          <button onClick={loadDatasets}>Refresh</button>
        </header>

        <section className="admin-hero-v35">
          <div>
            <p className="eyebrow">DATA OPERATIONS</p>
            <h1>Dataset Governance Console</h1>
            <p>
              Upload, validate, publish and monitor datasets powering the public cancer map.
            </p>
          </div>
        </section>

        <section className="admin-kpi-grid-v35">
          <div><strong>{datasets.length}</strong><span>Total datasets</span></div>
          <div><strong>{publishedCount}</strong><span>Published</span></div>
          <div><strong>{totalRows}</strong><span>Total rows</span></div>
        </section>

        <section className="admin-tabs-v38">
          {["datasets", "automation", "sources", "settings"].map((item) => (
            <button
              key={item}
              className={tab === item ? "active" : ""}
              onClick={() => setTab(item)}
            >
              {item}
            </button>
          ))}
        </section>

        {status && <section className="admin-status-v35">{status}</section>}

        {tab === "datasets" && (
          <section className="admin-card-v35">
            <h2>Datasets</h2>

            <div className="admin-upload-row-v35">
              <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files?.[0] || null)} />
              <button onClick={uploadDataset} disabled={loading}>Upload CSV</button>
            </div>

            <div className="admin-table-wrap-v35">
              <table>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Rows</th>
                    <th>Quality</th>
                    <th>Source</th>
                    <th>Published</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {datasets.map((d) => (
                    <tr key={d.id}>
                      <td>{d.name || d.originalName}</td>
                      <td>{d.rowCount || d.rows?.length || 0}</td>
                      <td>{d.qualityFlag || "-"}</td>
                      <td>{d.sourceName || "-"}</td>
                      <td>{d.published ? "Yes" : "No"}</td>
                      <td>
                        <button
                          onClick={() => updateDataset(d.id, { published: !d.published })}
                          disabled={loading}
                        >
                          {d.published ? "Unpublish" : "Publish"}
                        </button>
                        <button onClick={() => deleteDataset(d.id)} disabled={loading}>
                          Delete
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {tab === "automation" && (
          <section className="admin-card-v35">
            <h2>Automation</h2>
            <p>
              Research candidate sources, normalize official indicators and generate reviewable draft datasets.
            </p>

            <div className="admin-tab-actions-v39">
              <button onClick={runAutoResearch} disabled={loading}>
                Find Candidate Sources
              </button>
              <button onClick={runOfficialIngest} disabled={loading}>
                Fetch & Normalize Official Data
              </button>
              <button onClick={() => window.open(`${API}/public/map-data`, "_blank")}>
                Open Public JSON
              </button>
              <button onClick={() => window.open(`${API}/public/map-data.csv`, "_blank")}>
                Open Public CSV
              </button>
            </div>
          </section>
        )}

        {tab === "sources" && (
          <section className="admin-card-v35">
            <h2>Official Sources</h2>
            <p>ECIS, GCO / GLOBOCAN and future official registry connectors.</p>
            <div className="admin-tab-actions-v39">
              <button onClick={() => window.open(`${API}/admin/sources`, "_blank")}>
                View Source Registry
              </button>
              <button onClick={runOfficialIngest} disabled={loading}>
                Test Official Ingest
              </button>
            </div>
          </section>
        )}

        {tab === "settings" && (
          <section className="admin-card-v35">
            <h2>Settings</h2>
            <p>Recovery admin panel restored after App.jsx overwrite.</p>
            <div className="admin-tab-actions-v39">
              <button onClick={() => setPage("landing")}>Back Home</button>
              <button onClick={loadDatasets}>Reload Datasets</button>
            </div>
          </section>
        )}
      </div>
    );
  };

  const OncoKidsPage = () => {
    const [hopePoints, setHopePoints] = useState(120);
    const [activeQuest, setActiveQuest] = useState("learn");
    const [feeling, setFeeling] = useState(lang === "tr" ? "Umutlu" : "Hopeful");
    const [quizAnswer, setQuizAnswer] = useState(null);
    const [badges, setBadges] = useState(["🌈"]);
    const [checkedPrep, setCheckedPrep] = useState([]);

    const kidText = {
      tr: {
        home: "← Ana Sayfa",
        title: "Onco Kids",
        subtitle: "Çocuklar ve aileler için yumuşak, güven veren ve oyunlaştırılmış destek alanı.",
        start: "Macaraya Başla",
        restart: "Yeniden Başlat",
        points: "Umut Puanı",
        journey: "Umut Yolculuğu",
        helper: "Lumi diyor ki",
        helperText: "Küçük sorular büyük güçlere dönüşür. Hazırsan birlikte öğrenelim.",
        safety: "Bu alan tıbbi karar vermez. Çocukların duygularını konuşmasına ve ailelerin doktor görüşmesine hazırlanmasına yardımcı olur.",
        quizGood: "Harika! Soru sormak cesur bir davranıştır.",
        quizTry: "Tekrar deneyebilirsin. Burada hata yapmak sorun değil."
      },
      en: {
        home: "← Home",
        title: "Onco Kids",
        subtitle: "A gentle, safe and gamified support space for children and families.",
        start: "Start Adventure",
        restart: "Restart",
        points: "Hope Points",
        journey: "Hope Journey",
        helper: "Lumi says",
        helperText: "Small questions can become big strengths. Let’s learn together.",
        safety: "This space does not make medical decisions. It helps children talk about feelings and helps families prepare for doctor conversations.",
        quizGood: "Great! Asking questions is brave.",
        quizTry: "Try again. Making mistakes is okay here."
      }
    }[lang];

    const feelings = lang === "tr"
      ? ["Korkmuş", "Meraklı", "Üzgün", "Umutlu", "Yorgun", "Cesur"]
      : ["Scared", "Curious", "Sad", "Hopeful", "Tired", "Brave"];

    const addPoints = (amount, quest, badge = null) => {
      setHopePoints((p) => p + amount);
      setActiveQuest(quest);
      if (badge) {
        setBadges((current) => current.includes(badge) ? current : [...current, badge]);
      }
    };

    const resetAdventure = () => {
      setHopePoints(120);
      setActiveQuest("learn");
      setFeeling(lang === "tr" ? "Umutlu" : "Hopeful");
      setQuizAnswer(null);
      setBadges(["🌈"]);
      setCheckedPrep([]);
    };

    const togglePrep = (item) => {
      setCheckedPrep((current) =>
        current.includes(item)
          ? current.filter((entry) => entry !== item)
          : [...current, item]
      );

      if (!checkedPrep.includes(item)) {
        addPoints(6, "hero", "🎒");
      }
    };

    const journeySteps = [
      ["learn", "🌈", lang === "tr" ? "Öğren" : "Learn", "📘"],
      ["ask", "❓", lang === "tr" ? "Sor" : "Ask", "❓"],
      ["feel", "💛", lang === "tr" ? "Hislerini Seç" : "Choose Feeling", "💛"],
      ["breathe", "☁️", lang === "tr" ? "Nefes Al" : "Breathe", "☁️"],
      ["hero", "🏆", lang === "tr" ? "Cesur Kahraman" : "Brave Hero", "🏆"]
    ];

    return (
      <div className="kids-game-page advanced-kids">
        <header className="kids-game-nav">
          <button className="ghost-btn" onClick={() => setPage("landing")}>{kidText.home}</button>

          <div className="kids-points">
            ⭐ {kidText.points}: <strong>{hopePoints}</strong>
          </div>

          <div className="language-control kids-lang">
            <label>{t.langLabel}</label>
            <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">English</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>
        </header>

        <section className="kids-game-hero advanced">
          <div className="kids-hero-overlay">
            <p className="eyebrow dark">ONCO KIDS</p>
            <h1>{kidText.title}</h1>
            <p>{kidText.subtitle}</p>

            <div className="kids-hero-actions">
              <button className="kids-main-btn" onClick={() => addPoints(25, "learn", "📘")}>
                {kidText.start}
              </button>
              <button className="kids-reset-btn" onClick={resetAdventure}>
                {kidText.restart}
              </button>
            </div>

            <div className="badge-row">
              {badges.map((badge) => <span key={badge}>{badge}</span>)}
            </div>

            <div className="lumi-card">
              <div className="lumi-avatar moving">🌟</div>
              <div>
                <strong>{kidText.helper}</strong>
                <span>{kidText.helperText}</span>
              </div>
            </div>
          </div>

          <div className="character-stage lumi-companion-stage">
            <div className="lumi-sky-orb"></div>
            <div className="lumi-character">
              <div className="lumi-face">😊</div>
              <div className="lumi-body"></div>
              <div className="lumi-shadow"></div>
            </div>

            <div className="lumi-speech">
              <strong>{kidText.helper}</strong>
              <span>
                {lang === "tr"
                  ? "Bir görev seç, umut puanı topla ve cesur sorular hazırla."
                  : "Pick a quest, collect hope points and practice brave questions."}
              </span>
            </div>
          </div>
        </section>

        <section className="hope-journey advanced">
          <h2>{kidText.journey}</h2>

          <div className="journey-path">
            {journeySteps.map(([key, icon, label, badge], index) => (
              <button
                key={key}
                className={`journey-step ${activeQuest === key ? "active" : ""}`}
                onClick={() => addPoints(10 + index * 5, key, badge)}
              >
                <span>{icon}</span>
                <strong>{label}</strong>
              </button>
            ))}
          </div>
        </section>

        <section className="kids-game-grid advanced">
          <div className="kids-game-card story-card">
            <h3>{lang === "tr" ? "Hikâye Görevi" : "Story Quest"}</h3>
            <p>
              {lang === "tr"
                ? "Elif hastane ziyaretinden önce biraz meraklı ve biraz endişeli. Ona hangi soruları sorabileceğini birlikte hazırlayalım."
                : "Elif feels curious and a little worried before a hospital visit. Let’s help her prepare gentle questions."}
            </p>
            <div className="choice-grid">
              <button onClick={() => addPoints(18, "ask", "❓")}>
                {lang === "tr" ? "Doktora soru hazırla" : "Prepare a doctor question"}
              </button>
              <button onClick={() => addPoints(18, "feel", "💬")}>
                {lang === "tr" ? "Duygusunu söylemesine yardım et" : "Help her name a feeling"}
              </button>
            </div>
          </div>

          <div className="kids-game-card quiz-card">
            <h3>Mini Quiz</h3>
            <p>
              {lang === "tr"
                ? "Hastaneye gitmeden önce soru sormak iyi midir?"
                : "Is it okay to ask questions before going to the hospital?"}
            </p>

            <div className="choice-grid">
              <button onClick={() => { setQuizAnswer("good"); addPoints(30, "hero", "🏆"); }}>
                {lang === "tr" ? "Evet, soru sormak iyidir" : "Yes, questions are good"}
              </button>
              <button onClick={() => { setQuizAnswer("try"); addPoints(5, "learn"); }}>
                {lang === "tr" ? "Hayır, hiç sormamalıyız" : "No, we should not ask"}
              </button>
            </div>

            {quizAnswer && (
              <div className={`quiz-result ${quizAnswer}`}>
                {quizAnswer === "good" ? kidText.quizGood : kidText.quizTry}
              </div>
            )}
          </div>

          <div className="kids-game-card knowledge-card">
            <h3>{lang === "tr" ? "Bilgi Baloncukları" : "Knowledge Bubbles"}</h3>
            <div className="bubble-map">
              {[
                lang === "tr" ? "Doktorlar yardım eder" : "Doctors help",
                lang === "tr" ? "İlaçlar planlıdır" : "Medicines have plans",
                lang === "tr" ? "Aile yanında" : "Family is near",
                lang === "tr" ? "Soru sormak iyidir" : "Questions are good",
                lang === "tr" ? "Dinlenmek önemlidir" : "Rest matters",
                lang === "tr" ? "Duygular konuşulabilir" : "Feelings can be shared"
              ].map((item) => (
                <button key={item} onClick={() => addPoints(12, "learn", "✨")}>{item}</button>
              ))}
            </div>
          </div>

          <div className="kids-game-card feeling-card">
            <h3>{lang === "tr" ? "Duygu Bahçesi" : "Emotion Garden"}</h3>
            <div className="feeling-grid game">
              {feelings.map((item) => (
                <button
                  key={item}
                  className={feeling === item ? "selected" : ""}
                  onClick={() => {
                    setFeeling(item);
                    addPoints(8, "feel", "💛");
                  }}
                >
                  {item}
                </button>
              ))}
            </div>
            <p className="feeling-result">
              {lang === "tr"
                ? `${feeling} hissetmek normal. Bunu güvendiğin bir yetişkinle paylaşabilirsin.`
                : `Feeling ${feeling.toLowerCase()} is okay. You can share it with a trusted adult.`}
            </p>
          </div>

          <div className="kids-game-card breathing-card wide">
            <h3>{lang === "tr" ? "Sakin Nefes Oyunu" : "Calm Breathing Game"}</h3>
            <div className="breathing-game-row">
              <div className="breathing-circle">
                {lang === "tr" ? "nefes al" : "inhale"}<br />
                {lang === "tr" ? "yavaşça ver" : "exhale"}
              </div>
              <div>
                <p>
                  {lang === "tr"
                    ? "Yavaşça nefes al, gökyüzüne bak ve içinden üç güzel şey düşün."
                    : "Breathe slowly, look at the sky and think of three kind things."}
                </p>
                <button onClick={() => addPoints(20, "breathe", "☁️")}>
                  {lang === "tr" ? "Nefes görevini tamamladım" : "I completed the breathing quest"}
                </button>
              </div>
            </div>
          </div>

          <div className="kids-game-card reward-card">
            <h3>{lang === "tr" ? "Rozetlerim" : "My Badges"}</h3>
            <div className="reward-badges">
              {badges.map((badge) => <span key={badge}>{badge}</span>)}
            </div>
            <p>{lang === "tr" ? "Her görev küçük bir cesaret adımıdır." : "Each quest is a small step of courage."}</p>
          </div>

          <div className="kids-game-card prep-card wide">
            <h3>{lang === "tr" ? "Tedavi Günü Çantam" : "My Treatment Day Bag"}</h3>
            <p>
              {lang === "tr"
                ? "Hastane gününden önce küçük bir hazırlık listesi yapmak çocuğun kendini daha güvende hissetmesine yardımcı olabilir."
                : "A simple preparation list can help a child feel safer before a hospital day."}
            </p>

            <div className="kids-checklist">
              {[
                lang === "tr" ? "Sevdiğim küçük oyuncak" : "My favorite small toy",
                lang === "tr" ? "Doktora soracağım bir soru" : "One question for the doctor",
                lang === "tr" ? "Rahat kıyafet" : "Comfortable clothes",
                lang === "tr" ? "Su veya izin verilen atıştırmalık" : "Water or approved snack",
                lang === "tr" ? "Bana eşlik edecek kişi" : "The person coming with me"
              ].map((item) => (
                <button
                  key={item}
                  className={checkedPrep.includes(item) ? "checked" : ""}
                  onClick={() => togglePrep(item)}
                >
                  <span>{checkedPrep.includes(item) ? "✅" : "⬜"}</span>
                  {item}
                </button>
              ))}
            </div>
          </div>

          <div className="kids-game-card doctor-question-card">
            <h3>{lang === "tr" ? "Doktora Sorabileceğim Sorular" : "Questions I Can Ask"}</h3>
            <div className="question-chip-list">
              {[
                lang === "tr" ? "Bugün ne olacak?" : "What will happen today?",
                lang === "tr" ? "Acıyacak mı?" : "Will it hurt?",
                lang === "tr" ? "Ne zaman dinlenebilirim?" : "When can I rest?",
                lang === "tr" ? "Korkarsam kime söyleyebilirim?" : "Who can I tell if I feel scared?"
              ].map((item) => (
                <button key={item} onClick={() => addPoints(10, "ask", "❓")}>
                  {item}
                </button>
              ))}
            </div>
          </div>

          <div className="kids-game-card family-guide-card">
            <h3>{lang === "tr" ? "Aile İçin Mini Rehber" : "Mini Guide for Families"}</h3>
            <div className="family-guide-list">
              <div>
                <strong>{lang === "tr" ? "Basit anlat" : "Use simple words"}</strong>
                <p>{lang === "tr" ? "Kısa, sakin ve yaşına uygun cümleler kur." : "Use short, calm, age-appropriate sentences."}</p>
              </div>
              <div>
                <strong>{lang === "tr" ? "Duyguyu kabul et" : "Validate feelings"}</strong>
                <p>{lang === "tr" ? "Korku, merak veya yorgunluk normaldir." : "Fear, curiosity or tiredness can be normal."}</p>
              </div>
              <div>
                <strong>{lang === "tr" ? "Doktora hazır git" : "Prepare for the visit"}</strong>
                <p>{lang === "tr" ? "Çocuğun sorularını birlikte not alın." : "Write the child’s questions together."}</p>
              </div>
            </div>
          </div>
        </section>

        <section className="kids-safety-note">
          {kidText.safety}
        </section>
      </div>
    );
  };

  if (page === "landing") return <LandingPage />;
  if (page === "copilot") return <CopilotPage />;
  if (page === "knowledge") return <KnowledgeGraphPage />;
  if (page === "map") return <MapPage />;
  if (page === "admin") return <AdminPanel />;
  if (page === "kids") return <OncoKidsPage />;

  return <LandingPage />;
}

export default App;
