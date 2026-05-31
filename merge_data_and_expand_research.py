from pathlib import Path
import re

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")

# ------------------------------------------------------------
# 1) Research feed'i daha büyük ve zengin hale getir
# ------------------------------------------------------------
research_pattern = re.compile(
    r'''const researchFeed = \[[\s\S]*?\];''',
    re.MULTILINE
)

new_research_feed = r'''const researchFeed = [
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
    ];'''

if research_pattern.search(s):
    s = research_pattern.sub(new_research_feed, s, count=1)

# ------------------------------------------------------------
# 2) Unified merged rows hesaplamasını ekle
# ------------------------------------------------------------
needle = '''    const maxValue = Math.max(...ranked.map((row) => row[landingMetric] || 0), 1);'''

insert = '''    const maxValue = Math.max(...ranked.map((row) => row[landingMetric] || 0), 1);

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
    };'''

if needle in s and "const mergedCancerRows" not in s:
    s = s.replace(needle, insert, 1)

# ------------------------------------------------------------
# 3) Eski official + CSV ayrı bloklarını gizlemek yerine yeni merged blok ekle
# ------------------------------------------------------------
chart_marker = '''            <div className="landing-live-chart-title">
              <span>{landingRegion === "turkiye" ? "Türkiye ranking" : "Europe ranking"}</span>
              <strong>{metricLabel[landingMetric]}</strong>
              <small>{grouped.length} areas · showing {ranked.length} · local CSV layer: {normalized.length} rows</small>
            </div>'''

new_chart_header = '''            <div className="landing-live-chart-title merged-title">
              <span>Unified cancer intelligence layer</span>
              <strong>{metricLabel[landingMetric]}</strong>
              <small>
                {mergedCancerRows.length} categorized indicators · official estimates + CSV ranking merged · {normalized.length} source rows
              </small>
            </div>

            <div className="landing-merged-intelligence">
              {mergedCancerRows.map((row, index) => (
                <article
                  className={`merged-data-row ${row.sourceType}`}
                  key={`${row.sourceType}-${row.label}-${index}`}
                  style={{ animationDelay: `${index * 0.055}s` }}
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
            </div>'''

if chart_marker in s and "landing-merged-intelligence" not in s:
    s = s.replace(chart_marker, new_chart_header, 1)

APP.write_text(s, encoding="utf-8")

# ------------------------------------------------------------
# 4) CSS: eski ayrımı gizle, merged tasarımı ve research büyüt
# ------------------------------------------------------------
css = CSS.read_text(encoding="utf-8")

css_patch = r'''

/* MERGED CANCER INTELLIGENCE + EXPANDED RESEARCH PULSE */

/* Eski ayrık official/csv bloklarını görsel olarak kaldır */
.landing-official-bars,
.landing-demo-bars-head,
.landing-live-row {
  display: none !important;
}

/* Unified chart panel */
.landing-live-chart {
  padding: 30px !important;
  border-radius: 36px !important;
  background:
    radial-gradient(circle at 8% 8%, rgba(34,211,238,0.14), transparent 30%),
    radial-gradient(circle at 92% 14%, rgba(124,58,237,0.10), transparent 30%),
    linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
}

.landing-live-chart-title.merged-title {
  display: grid !important;
  grid-template-columns: 1fr auto;
  gap: 10px 18px;
  align-items: end;
  margin-bottom: 22px !important;
}

.landing-live-chart-title.merged-title span {
  color: #155eef !important;
  font-size: 12px !important;
  font-weight: 950 !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase;
}

.landing-live-chart-title.merged-title strong {
  color: #101828 !important;
  font-size: clamp(38px, 4vw, 58px) !important;
  line-height: 1 !important;
  letter-spacing: -0.055em !important;
}

.landing-live-chart-title.merged-title small {
  grid-column: 1 / -1;
  color: #64748b !important;
  font-size: 15px !important;
  font-weight: 850 !important;
}

/* Merged rows */
.landing-merged-intelligence {
  display: grid;
  gap: 14px;
}

.merged-data-row {
  display: grid;
  grid-template-columns: minmax(260px, 0.9fr) minmax(280px, 1fr) 170px;
  gap: 18px;
  align-items: center;
  padding: 18px;
  border-radius: 26px;
  border: 1px solid #e2e8f0;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
  box-shadow: 0 14px 34px rgba(15,23,42,0.06);
  opacity: 0;
  transform: translateY(10px);
  animation: mergedRowIn 0.42s ease forwards;
  position: relative;
  overflow: hidden;
}

.merged-data-row::before {
  content: "";
  position: absolute;
  inset: 0;
  width: 5px;
  background: #155eef;
}

.merged-data-row.official::before {
  background: linear-gradient(180deg, #0ea5e9, #14b8a6);
}

.merged-data-row.csv::before {
  background: linear-gradient(180deg, #7c3aed, #155eef);
}

@keyframes mergedRowIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.merged-data-main span {
  display: inline-flex;
  width: fit-content;
  margin-bottom: 8px;
  padding: 6px 10px;
  border-radius: 999px;
  background: #e0f2fe;
  color: #075985;
  font-size: 11px;
  font-weight: 950;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.merged-data-row.official .merged-data-main span {
  background: #ccfbf1;
  color: #0f766e;
}

.merged-data-row.csv .merged-data-main span {
  background: #ede9fe;
  color: #5b21b6;
}

.merged-data-main h4 {
  margin: 0 0 5px;
  color: #101828;
  font-size: 21px;
  line-height: 1.15;
  letter-spacing: -0.025em;
}

.merged-data-main p {
  margin: 0;
  color: #64748b;
  font-size: 14px;
  line-height: 1.45;
  font-weight: 750;
}

.merged-data-bar {
  height: 16px;
  border-radius: 999px;
  background: #e2e8f0;
  overflow: hidden;
  position: relative;
}

.merged-data-bar i {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, #155eef, #14b8a6, #a5f3fc);
  position: relative;
  transform-origin: left;
  animation: mergedBarGrow 0.85s cubic-bezier(.2,.8,.2,1) both;
}

@keyframes mergedBarGrow {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}

.merged-data-bar i b {
  position: absolute;
  inset: 0;
  width: 36%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.7), transparent);
  transform: translateX(-130%);
  animation: mergedBarLight 1.7s linear infinite;
}

@keyframes mergedBarLight {
  from { transform: translateX(-130%); }
  to { transform: translateX(320%); }
}

.merged-data-row > strong {
  justify-self: end;
  color: #101828;
  font-size: 22px;
  font-weight: 950;
  letter-spacing: -0.02em;
}

/* Research pulse büyütme */
.landing-research-feed-after,
.landing-research-feed {
  margin-top: 26px !important;
  padding: 28px !important;
  border-radius: 36px !important;
  background:
    radial-gradient(circle at 10% 10%, rgba(34,211,238,0.13), transparent 28%),
    radial-gradient(circle at 90% 20%, rgba(124,58,237,0.10), transparent 28%),
    linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
  border: 1px solid #dbeafe !important;
  box-shadow: 0 22px 70px rgba(15,23,42,0.08) !important;
}

.landing-research-feed-head {
  margin-bottom: 22px !important;
}

.landing-research-feed-head span {
  color: #155eef !important;
  font-size: 12px !important;
  font-weight: 950 !important;
  letter-spacing: 0.2em !important;
}

.landing-research-feed-head b {
  color: #101828 !important;
  font-size: clamp(26px, 3vw, 40px) !important;
  line-height: 1.05 !important;
  letter-spacing: -0.045em !important;
}

.landing-research-feed-grid {
  display: grid !important;
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  gap: 18px !important;
}

.landing-research-card {
  min-height: 250px !important;
  padding: 22px !important;
  border-radius: 28px !important;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.98), rgba(241,245,249,0.98)) !important;
  border: 1px solid #dbeafe !important;
  box-shadow: 0 16px 40px rgba(37,99,235,0.08) !important;
  display: grid;
  align-content: space-between;
}

.landing-research-card h4 {
  font-size: 22px !important;
  line-height: 1.18 !important;
  letter-spacing: -0.03em !important;
}

.landing-research-card p {
  font-size: 15px !important;
  line-height: 1.55 !important;
}

.landing-research-card-top span {
  padding: 8px 12px !important;
}

@media (max-width: 1250px) {
  .landing-research-feed-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
}

@media (max-width: 850px) {
  .merged-data-row {
    grid-template-columns: 1fr;
  }

  .merged-data-row > strong {
    justify-self: start;
  }

  .landing-research-feed-grid {
    grid-template-columns: 1fr !important;
  }
}

'''

if "MERGED CANCER INTELLIGENCE" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Official + CSV data merged into one categorized intelligence layer; Research Pulse expanded.")
