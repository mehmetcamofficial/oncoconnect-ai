from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# 1) official rows'u data bar grafiğine hazırlayan JS bloğunu ekle
needle = '''    const maxValue = Math.max(...ranked.map((row) => row[landingMetric] || 0), 1);'''

insert = '''    const maxValue = Math.max(...ranked.map((row) => row[landingMetric] || 0), 1);

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
      .map((row) => ({
        label:
          row.indicator === "new_cases_count" ? "Türkiye national new cases" :
          row.indicator === "deaths_count" ? "Türkiye national deaths" :
          row.indicator === "five_year_prevalence_count" ? "Türkiye 5-year prevalence" :
          row.indicator.replaceAll("_", " "),
        value: Number(String(row.value || "0").replace(",", ".")),
        unit: row.unit || "",
        source: row.source_name || "Official source",
        area: row.area || "",
        year: row.year || "",
        url: row.source_url || ""
      }))
      .filter((row) => Number.isFinite(row.value));

    const officialMaxValue = Math.max(...officialMetricRows.map((row) => row.value || 0), 1);'''

if needle in s and "const officialMetricRows =" not in s:
    s = s.replace(needle, insert, 1)

# 2) chart title'dan sonra official source bars ekle
needle = '''            {ranked.map((row, index) => {'''

insert = '''            {officialMetricRows.length > 0 && (
              <div className="landing-official-bars">
                <div className="landing-official-bars-head">
                  <span>Verified official source bars</span>
                  <b>{landingMetric === "survival" ? "5-year prevalence source layer" : metricLabel[landingMetric]}</b>
                </div>

                {officialMetricRows.map((row, index) => {
                  const width = Math.max(8, Math.round((row.value / officialMaxValue) * 100));

                  return (
                    <div
                      className="landing-official-bar"
                      key={`${row.label}-${row.value}-${index}`}
                      style={{ animationDelay: `${index * 0.07}s` }}
                    >
                      <div>
                        <strong>{row.label}</strong>
                        <small>{row.source} · {row.area} · {row.year}</small>
                      </div>

                      <i style={{ width: `${width}%` }}><span></span></i>

                      <em>{row.value.toLocaleString()} {row.unit}</em>
                    </div>
                  );
                })}
              </div>
            )}

            <div className="landing-demo-bars-head">
              <span>{landingRegion === "turkiye" ? "Türkiye city ranking from CSV layer" : "Europe ranking from CSV layer"}</span>
            </div>

            {ranked.map((row, index) => {'''

if needle in s and "landing-official-bars" not in s:
    s = s.replace(needle, insert, 1)

app.write_text(s, encoding="utf-8")

css_patch = r'''

/* Improve official source data bars */

.landing-official-source-strip {
  display: none !important;
}

.landing-official-bars {
  position: relative;
  z-index: 3;
  margin: 18px 0 24px;
  padding: 18px;
  border-radius: 24px;
  background:
    radial-gradient(circle at 12% 20%, rgba(34,211,238,0.18), transparent 34%),
    linear-gradient(135deg, #0f172a, #1e293b);
  color: white;
  border: 1px solid rgba(125,211,252,0.22);
  box-shadow: 0 18px 54px rgba(15,23,42,0.18);
  overflow: hidden;
}

.landing-official-bars::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(120deg, transparent, rgba(34,211,238,0.14), transparent);
  transform: translateX(-100%);
  animation: officialBarScan 4s linear infinite;
  pointer-events: none;
}

@keyframes officialBarScan {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}

.landing-official-bars-head {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 14px;
}

.landing-official-bars-head span {
  color: #a5f3fc;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.18em;
}

.landing-official-bars-head b {
  color: white;
  font-size: 14px;
}

.landing-official-bar {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: minmax(260px, 0.9fr) minmax(220px, 1fr) 190px;
  gap: 16px;
  align-items: center;
  padding: 12px 0;
  border-top: 1px solid rgba(255,255,255,0.10);
  opacity: 0;
  animation: officialBarIn 0.45s ease forwards;
}

@keyframes officialBarIn {
  from {
    opacity: 0;
    transform: translateX(-14px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.landing-official-bar strong,
.landing-official-bar small {
  display: block;
}

.landing-official-bar strong {
  color: white;
  font-size: 15px;
  text-transform: capitalize;
}

.landing-official-bar small {
  margin-top: 3px;
  color: rgba(226,232,240,0.68);
  line-height: 1.35;
}

.landing-official-bar i {
  position: relative;
  height: 12px;
  border-radius: 999px;
  background: linear-gradient(90deg, #22d3ee, #14b8a6, #a5f3fc);
  overflow: hidden;
  box-shadow: 0 0 22px rgba(34,211,238,0.28);
  animation: officialBarGrow 0.8s cubic-bezier(.2,.8,.2,1) both;
  transform-origin: left center;
}

@keyframes officialBarGrow {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}

.landing-official-bar i span {
  position: absolute;
  inset: 0;
  width: 38%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.7), transparent);
  transform: translateX(-120%);
  animation: officialLightRun 1.6s linear infinite;
}

@keyframes officialLightRun {
  from { transform: translateX(-120%); }
  to { transform: translateX(280%); }
}

.landing-official-bar em {
  color: #a5f3fc;
  font-style: normal;
  font-weight: 950;
  text-align: right;
  font-size: 17px;
}

.landing-demo-bars-head {
  margin: 10px 0 6px;
  padding-top: 8px;
  border-top: 1px solid #eef2f7;
}

.landing-demo-bars-head span {
  color: #667085;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.14em;
}

.landing-live-side div {
  display: grid;
  gap: 4px;
}

.landing-live-side div + div {
  margin-top: -8px;
}

@media (max-width: 950px) {
  .landing-official-bar {
    grid-template-columns: 1fr;
  }

  .landing-official-bar em {
    text-align: left;
  }

  .landing-official-bars-head {
    display: grid;
  }
}

'''

css.write_text(css.read_text(encoding="utf-8") + css_patch, encoding="utf-8")
print("✅ Official source rows are now reflected inside the animated data bars.")
