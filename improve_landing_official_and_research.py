from pathlib import Path
import re

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

if not APP.exists():
    print("❌ frontend/src/App.jsx bulunamadı.")
    raise SystemExit(1)

if not CSS.exists():
    print("❌ frontend/src/App.css bulunamadı.")
    raise SystemExit(1)

s = APP.read_text(encoding="utf-8")
css = CSS.read_text(encoding="utf-8")

# ------------------------------------------------------------------
# 1) Helper block ekle
# ------------------------------------------------------------------
helper_marker = '    const metricLabel = {'
helper_insert_after = '''    const metricLabel = {
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
        summary: "Tracks current oncology trials for immunotherapy combinations, biomarker-driven treatment arms and precision medicine strategies.",
        meta: "Solid tumors · Hematology · Recruitment updates"
      },
      {
        type: "Innovative drug",
        title: "Antibody-drug conjugate pipeline",
        source: "ESMO / ASCO coverage",
        badge: "Drug updates",
        summary: "A compact feed for emerging ADC strategies across breast, lung and gastrointestinal cancers.",
        meta: "ADC · HER2-low · Lung · Breast"
      },
      {
        type: "Research article",
        title: "Early detection and ctDNA monitoring",
        source: "Nature Medicine / NEJM",
        badge: "Research",
        summary: "Highlights studies around liquid biopsy, recurrence monitoring and stratified follow-up pathways.",
        meta: "ctDNA · Screening · Monitoring"
      },
      {
        type: "Care innovation",
        title: "Supportive care and symptom management",
        source: "JCO / Lancet Oncology",
        badge: "Care pathway",
        summary: "Focuses on fatigue, pain, appetite loss, psycho-oncology and better patient-support coordination.",
        meta: "Quality of life · Symptom burden"
      }
    ];

    const prettyOfficialIndicator = (indicator = "") => {
      const normalized = String(indicator)
        .replaceAll("_", " ")
        .replace(/\\bcount\\b/gi, "")
        .replace(/\\brate per 100000\\b/gi, "")
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

      return custom[normalized] || normalized.replace(/\\b\\w/g, (c) => c.toUpperCase());
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
'''

if helper_marker in s and "const researchFeed = [" not in s:
    s = s.replace(helper_marker, helper_insert_after, 1)

# ------------------------------------------------------------------
# 2) officialMetricRows bloğunu daha iyi hale getir
# ------------------------------------------------------------------
pattern_metric_rows = re.compile(
    r'''const officialMetricRows = officialRows[\s\S]*?const officialMaxValue = Math\.max\([\s\S]*?\);''',
    re.MULTILINE
)

replacement_metric_rows = '''const officialMetricRows = officialRows
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
    );'''

if "normalizedValue" not in s and pattern_metric_rows.search(s):
    s = pattern_metric_rows.sub(replacement_metric_rows, s, count=1)

# ------------------------------------------------------------------
# 3) Official bars render bloğunu değiştir
# ------------------------------------------------------------------
start_marker = '{officialMetricRows.length > 0 && ('
end_marker = '<div className="landing-demo-bars-head">'

start_idx = s.find(start_marker)
end_idx = s.find(end_marker, start_idx)

new_render_block = '''{officialMetricRows.length > 0 && (
              <>
                <section className="landing-official-bars">
                  <div className="landing-official-bars-head">
                    <span>Verified official source bars</span>
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
                              <small>{row.source} · {row.area} · {row.year}</small>
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

                <section className="landing-research-feed">
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
              </>
            )}

            <div className="landing-demo-bars-head">'''

if start_idx != -1 and end_idx != -1:
    s = s[:start_idx] + new_render_block + s[end_idx + len(end_marker):]

# ------------------------------------------------------------------
# 4) Kötü görünen eski strip varsa gizle
# ------------------------------------------------------------------
css_patch = r'''

/* ===== Improved official bars + research feed ===== */

.landing-official-source-strip {
  display: none !important;
}

.landing-official-bars {
  margin: 18px 0 22px;
  padding: 20px;
  border-radius: 28px;
  background:
    radial-gradient(circle at 12% 20%, rgba(34,211,238,0.16), transparent 30%),
    linear-gradient(135deg, #0f172a 0%, #172554 55%, #1e293b 100%);
  border: 1px solid rgba(125, 211, 252, 0.18);
  box-shadow: 0 22px 60px rgba(15, 23, 42, 0.18);
  overflow: hidden;
  position: relative;
}

.landing-official-bars::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(110deg, transparent, rgba(255,255,255,0.05), transparent);
  transform: translateX(-100%);
  animation: officialScan 5s linear infinite;
  pointer-events: none;
}

@keyframes officialScan {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}

.landing-official-bars-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 14px;
}

.landing-official-bars-head span {
  color: #bae6fd;
  font-size: 12px;
  letter-spacing: 0.18em;
  font-weight: 900;
  text-transform: uppercase;
}

.landing-official-bars-head b {
  color: #ffffff;
  font-size: 16px;
  font-weight: 900;
}

.landing-official-bars-list {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
}

.landing-official-bar {
  padding: 16px 18px;
  border-radius: 22px;
  background: rgba(15, 23, 42, 0.42);
  border: 1px solid rgba(148, 163, 184, 0.18);
  backdrop-filter: blur(10px);
  opacity: 0;
  transform: translateY(14px);
  animation: officialBarFadeIn 0.45s ease forwards;
}

@keyframes officialBarFadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.landing-official-bar-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 18px;
  margin-bottom: 12px;
}

.landing-official-bar strong {
  display: block;
  color: #ffffff;
  font-size: 18px;
  line-height: 1.2;
  margin-bottom: 4px;
}

.landing-official-bar small {
  display: block;
  color: rgba(226, 232, 240, 0.72);
  font-size: 13px;
  line-height: 1.45;
}

.landing-official-bar em {
  color: #b6f4ff;
  font-style: normal;
  font-size: 18px;
  font-weight: 900;
  text-align: right;
  white-space: nowrap;
}

.landing-official-bar-track {
  width: 100%;
  height: 12px;
  border-radius: 999px;
  background: rgba(148, 163, 184, 0.16);
  overflow: hidden;
  position: relative;
}

.landing-official-bar-track i {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, #38bdf8, #2dd4bf, #dbeafe);
  box-shadow: 0 0 28px rgba(45,212,191,0.25);
  position: relative;
  transform-origin: left center;
  animation: officialBarGrow 0.9s cubic-bezier(.2,.8,.2,1) both;
}

@keyframes officialBarGrow {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}

.landing-official-bar-track i span {
  position: absolute;
  inset: 0;
  width: 30%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.75), transparent);
  transform: translateX(-130%);
  animation: officialBarLight 1.8s linear infinite;
}

@keyframes officialBarLight {
  from { transform: translateX(-130%); }
  to { transform: translateX(320%); }
}

/* Research feed */
.landing-research-feed {
  margin: 0 0 24px;
  padding: 18px;
  border-radius: 26px;
  background:
    radial-gradient(circle at 85% 20%, rgba(96,165,250,0.12), transparent 26%),
    linear-gradient(180deg, rgba(255,255,255,0.96), rgba(248,250,252,0.98));
  border: 1px solid #e2e8f0;
  box-shadow: 0 18px 44px rgba(15, 23, 42, 0.08);
}

.landing-research-feed-head {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
  margin-bottom: 14px;
}

.landing-research-feed-head span {
  color: #2563eb;
  font-size: 12px;
  letter-spacing: 0.18em;
  font-weight: 900;
  text-transform: uppercase;
}

.landing-research-feed-head b {
  color: #0f172a;
  font-size: 16px;
  font-weight: 900;
}

.landing-research-feed-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 14px;
}

.landing-research-card {
  padding: 16px;
  border-radius: 22px;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.98), rgba(241,245,249,0.96));
  border: 1px solid #dbeafe;
  box-shadow: 0 12px 30px rgba(37, 99, 235, 0.06);
  opacity: 0;
  transform: translateY(12px);
  animation: researchCardIn 0.4s ease forwards;
}

@keyframes researchCardIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.landing-research-card-top {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  align-items: center;
  margin-bottom: 12px;
}

.landing-research-card-top span {
  display: inline-flex;
  align-items: center;
  padding: 7px 10px;
  border-radius: 999px;
  background: linear-gradient(90deg, #dbeafe, #ccfbf1);
  color: #0f172a;
  font-size: 12px;
  font-weight: 900;
}

.landing-research-card-top small {
  color: #64748b;
  font-size: 12px;
  font-weight: 700;
}

.landing-research-card h4 {
  margin: 0 0 10px;
  color: #0f172a;
  font-size: 18px;
  line-height: 1.25;
}

.landing-research-card p {
  margin: 0 0 14px;
  color: #475569;
  font-size: 14px;
  line-height: 1.55;
}

.landing-research-card-bottom {
  display: grid;
  gap: 5px;
}

.landing-research-card-bottom b {
  color: #0f172a;
  font-size: 13px;
}

.landing-research-card-bottom em {
  color: #2563eb;
  font-style: normal;
  font-size: 12px;
  font-weight: 700;
}

@media (max-width: 920px) {
  .landing-official-bar-top,
  .landing-official-bars-head,
  .landing-research-feed-head {
    display: grid;
  }

  .landing-official-bar em {
    text-align: left;
  }
}

'''

if "Improved official bars + research feed" not in css:
    css += css_patch

APP.write_text(s, encoding="utf-8")
CSS.write_text(css, encoding="utf-8")

print("✅ Official bars compactlaştırıldı, sağ boşluk azaltıldı, research feed eklendi.")
