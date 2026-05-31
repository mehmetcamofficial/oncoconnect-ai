from pathlib import Path
import re

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")

# ------------------------------------------------------------
# 1) Landing: ranked label düzelt
# ------------------------------------------------------------
s = s.replace(
    '{ranked.length} ranked areas · {normalized.length} CSV rows loaded',
    '{grouped.length} areas · showing {ranked.length} · {normalized.length} CSV rows loaded'
)

# ------------------------------------------------------------
# 2) Landing: Research Pulse'u chart/grid sonrasına taşı
# ------------------------------------------------------------
research_pattern = re.compile(
    r'\n\s*<section className="landing-research-feed">[\s\S]*?</section>\n',
    re.MULTILINE
)

research_block = r'''
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
'''

# Eski research feed bloklarını kaldır
s = research_pattern.sub("\n", s)

# LandingDataDashboard içinde landing-live-grid kapanışından sonra ekle
marker = '''        </div>
      </section>
    );
  };'''

if marker in s and "landing-research-feed-after" not in s:
    s = s.replace(
        marker,
        '''        </div>
''' + research_block + '''
      </section>
    );
  };''',
        1
    )

# ------------------------------------------------------------
# 3) MapPage: official source state ekle
# ------------------------------------------------------------
map_start = s.find("  const MapPage = () => {")
map_end = s.find("  const AdminPanel = () => {", map_start)

if map_start == -1 or map_end == -1:
    raise SystemExit("❌ MapPage / AdminPanel marker bulunamadı.")

map_block = s[map_start:map_end]

if 'const [officialMapRows, setOfficialMapRows]' not in map_block:
    map_block = map_block.replace(
        '    const [rows, setRows] = useState([]);',
        '    const [rows, setRows] = useState([]);\n    const [officialMapRows, setOfficialMapRows] = useState([]);',
        1
    )

if 'const [hoveredArea, setHoveredArea]' not in map_block:
    map_block = map_block.replace(
        '    const [selectedArea, setSelectedArea] = useState(null);',
        '    const [selectedArea, setSelectedArea] = useState(null);\n    const [hoveredArea, setHoveredArea] = useState(null);',
        1
    )

# ------------------------------------------------------------
# 4) MapPage: official source CSV load useEffect ekle
# ------------------------------------------------------------
if 'loadOfficialMapRows' not in map_block:
    load_marker = '''    }, []);

    const fallbackRows = ['''

    official_loader = '''    }, []);

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

    const fallbackRows = ['''

    if load_marker in map_block:
      map_block = map_block.replace(load_marker, official_loader, 1)
    else:
      print("⚠️ Map official loader marker bulunamadı.")

# ------------------------------------------------------------
# 5) MapPage: activeArea tanımı
# ------------------------------------------------------------
if "const activeArea = hoveredArea || selected;" not in map_block:
    map_block = map_block.replace(
        '''    const selected =
      selectedArea
        ? groupedAreas.find((area) => area.name === selectedArea) || sortedAreas[0]
        : sortedAreas[0];''',
        '''    const selected =
      selectedArea
        ? groupedAreas.find((area) => area.name === selectedArea) || sortedAreas[0]
        : sortedAreas[0];

    const activeArea = hoveredArea
      ? groupedAreas.find((area) => area.name === hoveredArea) || selected
      : selectedArea
        ? selected
        : null;''',
        1
    )

# ------------------------------------------------------------
# 6) MapPage: data stream overlay ekle
# ------------------------------------------------------------
overlay_marker = '''              <div className="csv-map-overlay-panel">
                <span>{showMode === "top15" ? "Top 15 mode" : "All areas mode"}</span>
                <strong>{currentMetric.label}</strong>
                <small>{metric === "survival" ? "Lower survival appears first" : "Higher burden appears first"}</small>
              </div>'''

overlay_replacement = '''              <div className="csv-map-overlay-panel">
                <span>{showMode === "top15" ? "Top 15 mode" : "All areas mode"}</span>
                <strong>{currentMetric.label}</strong>
                <small>{metric === "survival" ? "Lower survival appears first" : "Higher burden appears first"}</small>
              </div>

              <div className="csv-map-data-stream">
                <span>CSV + official source stream</span>
                <b>{normalizedRows.length} CSV rows</b>
                <b>{officialMapRows.length} verified rows</b>
                <i></i>
              </div>'''

if overlay_marker in map_block and "csv-map-data-stream" not in map_block:
    map_block = map_block.replace(overlay_marker, overlay_replacement, 1)

# ------------------------------------------------------------
# 7) MapPage: pin hover/click davranışı
# ------------------------------------------------------------
old_pin_click = '''                    className={`csv-map-pin ${selected?.name === area.name ? "selected" : ""}`}
                    style={{ left: `${x}%`, top: `${y}%`, "--pin-scale": scale }}
                    onClick={() => setSelectedArea(area.name)}
                  >'''

new_pin_click = '''                    className={`csv-map-pin ${activeArea?.name === area.name ? "selected" : ""}`}
                    style={{ left: `${x}%`, top: `${y}%`, "--pin-scale": scale }}
                    onMouseEnter={() => setHoveredArea(area.name)}
                    onMouseLeave={() => {
                      setHoveredArea(null);
                      setSelectedArea(null);
                    }}
                    onFocus={() => setHoveredArea(area.name)}
                    onBlur={() => setHoveredArea(null)}
                    onClick={() => setSelectedArea((prev) => prev === area.name ? null : area.name)}
                  >'''

if old_pin_click in map_block:
    map_block = map_block.replace(old_pin_click, new_pin_click, 1)
else:
    print("⚠️ Pin click block bulunamadı.")

# ------------------------------------------------------------
# 8) Floating card activeArea ile çalışsın, sabit kalmasın
# ------------------------------------------------------------
map_block = map_block.replace('{selected && (', '{activeArea && (', 1)

# İlk floating block içindeki selected referanslarını activeArea yap
floating_start = map_block.find('{activeArea && (')
floating_end = map_block.find('              )}', floating_start)

if floating_start != -1 and floating_end != -1:
    floating = map_block[floating_start:floating_end]
    floating = floating.replace('selected.name', 'activeArea.name')
    floating = floating.replace('formatMetric(selected, "incidence")', 'formatMetric(activeArea, "incidence")')
    floating = floating.replace('formatMetric(selected, "mortality")', 'formatMetric(activeArea, "mortality")')
    floating = floating.replace('formatMetric(selected, "survival")', 'formatMetric(activeArea, "survival")')
    map_block = map_block[:floating_start] + floating + map_block[floating_end:]

s = s[:map_start] + map_block + s[map_end:]

APP.write_text(s, encoding="utf-8")

# ------------------------------------------------------------
# 9) CSS: layout, boşluk, data stream, pin büyütme, hover card
# ------------------------------------------------------------
css_patch = r'''

/* FINAL landing + map data stream behavior fix */

/* Landing: remove right empty side, make chart full-width */
.landing-live-grid {
  grid-template-columns: 1fr !important;
}

.landing-live-side {
  display: none !important;
}

.landing-live-chart {
  width: 100% !important;
}

.landing-live-chart-title small {
  color: #64748b !important;
  font-weight: 900 !important;
}

/* Research pulse directly below data chart */
.landing-research-feed-after {
  margin-top: 24px !important;
  margin-bottom: 0 !important;
}

/* Make data rows more compact and use full width */
.landing-live-row {
  grid-template-columns: 46px minmax(0, 1fr) 110px !important;
}

.landing-live-row i {
  height: 12px !important;
}

/* Map: data stream visual connection */
.csv-map-data-stream {
  position: absolute;
  left: 18px;
  right: 18px;
  bottom: 18px;
  z-index: 36;
  display: grid;
  grid-template-columns: auto auto auto 1fr;
  gap: 14px;
  align-items: center;
  padding: 12px 14px;
  border-radius: 999px;
  background: rgba(2, 6, 23, 0.72);
  border: 1px solid rgba(125, 211, 252, 0.28);
  backdrop-filter: blur(18px);
  color: white;
  pointer-events: none;
}

.csv-map-data-stream span {
  color: #a5f3fc;
  font-size: 11px;
  font-weight: 950;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  white-space: nowrap;
}

.csv-map-data-stream b {
  color: rgba(255,255,255,0.86);
  font-size: 12px;
  white-space: nowrap;
}

.csv-map-data-stream i {
  height: 9px;
  border-radius: 999px;
  background:
    linear-gradient(90deg, transparent, rgba(34,211,238,0.95), transparent);
  animation: mapStreamMove 1.6s linear infinite;
}

@keyframes mapStreamMove {
  from {
    transform: translateX(-20%);
    opacity: 0.35;
  }
  50% {
    opacity: 1;
  }
  to {
    transform: translateX(20%);
    opacity: 0.35;
  }
}

/* Bigger map bubbles */
.csv-map-pin {
  transform: translate(-50%, -50%) scale(calc(var(--pin-scale, 1) * 1.18)) !important;
}

.csv-map-pin i {
  width: 22px !important;
  height: 22px !important;
  border-width: 4px !important;
}

.csv-map-pin.selected i,
.csv-map-pin:hover i {
  width: 26px !important;
  height: 26px !important;
  background: #facc15 !important;
  box-shadow:
    0 0 0 14px rgba(250,204,21,0.18),
    0 0 44px rgba(250,204,21,0.95) !important;
}

/* Floating card opens only on hover/click and stays compact */
.csv-floating-card {
  width: 235px !important;
  right: 18px !important;
  top: 90px !important;
  bottom: auto !important;
  padding: 14px !important;
  border-radius: 20px !important;
  transform: none !important;
  animation: floatingCardOpen 0.18s ease both;
}

@keyframes floatingCardOpen {
  from {
    opacity: 0;
    transform: translateY(8px) scale(0.96);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.csv-floating-card h3 {
  font-size: 23px !important;
}

.csv-floating-card div {
  padding: 6px 0 !important;
}

.csv-floating-card strong {
  font-size: 18px !important;
}

.csv-floating-card button,
.csv-floating-hint {
  display: none !important;
}

/* Keep map bottom clean after stream */
.csv-real-map {
  padding-bottom: 0 !important;
}

/* Avoid research feed creating a giant white visual gap */
.landing-live-data {
  padding-bottom: 42px !important;
}

@media (max-width: 850px) {
  .csv-map-data-stream {
    grid-template-columns: 1fr;
    border-radius: 20px;
  }

  .csv-floating-card {
    left: 18px !important;
    right: 18px !important;
    width: auto !important;
  }
}

'''

css = CSS.read_text(encoding="utf-8")
if "FINAL landing + map data stream behavior fix" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Landing research position, ranking width, map official stream, larger bubbles and hover-card behavior fixed.")
