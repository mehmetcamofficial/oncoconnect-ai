from pathlib import Path
import re

APP = Path("frontend/src/App.jsx")
CSS = Path("frontend/src/App.css")

s = APP.read_text(encoding="utf-8")

# 1) Landing chart subtitle: CSV rows ile official estimate ayrımı
s = s.replace(
    '{grouped.length} areas · showing {ranked.length} · {normalized.length} CSV rows loaded',
    '{grouped.length} areas · showing {ranked.length} · local CSV layer: {normalized.length} rows'
)

# 2) Official bars title daha net olsun
s = s.replace(
    '<span>Verified official source bars</span>',
    '<span>Official national estimates</span>'
)

# 3) Official bar labels daha temiz
s = s.replace(
    'row.source} · {row.area} · {row.year}',
    'row.area} · {row.year} · {row.source}'
)

# 4) Map dış slider kartını gizleyeceğiz; onun yerine map içine slider ekle
map_start = s.find("  const MapPage = () => {")
map_end = s.find("  const AdminPanel = () => {", map_start)

if map_start == -1 or map_end == -1:
    raise SystemExit("❌ MapPage marker bulunamadı.")

map_block = s[map_start:map_end]

overlay_marker = '''              <div className="csv-map-overlay-panel">
                <span>{showMode === "top15" ? "Top 15 mode" : "All areas mode"}</span>
                <strong>{currentMetric.label}</strong>
                <small>{metric === "survival" ? "Lower survival appears first" : "Higher burden appears first"}</small>
              </div>'''

overlay_new = '''              <div className="csv-map-overlay-panel">
                <span>{showMode === "top15" ? "Top 15 mode" : "All areas mode"}</span>
                <strong>{currentMetric.label}</strong>
                <small>{metric === "survival" ? "Lower survival appears first" : "Higher burden appears first"}</small>
              </div>

              <div className="csv-map-year-inline">
                <span>Simulation year</span>
                <strong>{year}</strong>
                <input min="2024" max="2030" type="range" value={year} onChange={(e) => setYear(Number(e.target.value))} />
              </div>'''

if overlay_marker in map_block and "csv-map-year-inline" not in map_block:
    map_block = map_block.replace(overlay_marker, overlay_new, 1)

# 5) Pin koordinatlarını harita içine daha kontrollü çek
coord_pattern = re.compile(
    r'''const turkeyAutoCoords = \[[\s\S]*?\];\n\n    const europeAutoCoords = \[[\s\S]*?\];''',
    re.MULTILINE
)

coord_replacement = '''const turkeyAutoCoords = [
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
    ];'''

if coord_pattern.search(map_block):
    map_block = coord_pattern.sub(coord_replacement, map_block, count=1)

# 6) Fixed turkey coords dışa taşanları içeri al
fixed_replacements = {
    '"Erzurum": [82, 47]': '"Erzurum": [78, 47]',
    '"Trabzon": [79, 39]': '"Trabzon": [76, 40]',
    '"Van": [89, 56]': '"Van": [80, 56]',
    '"Diyarbakır": [74, 62]': '"Diyarbakır": [72, 61]',
    '"Diyarbakir": [74, 62]': '"Diyarbakir": [72, 61]',
    '"Gaziantep": [67, 67]': '"Gaziantep": [65, 64]',
    '"Adana": [54, 66]': '"Adana": [53, 64]'
}

for old, new in fixed_replacements.items():
    map_block = map_block.replace(old, new)

s = s[:map_start] + map_block + s[map_end:]

APP.write_text(s, encoding="utf-8")

css = CSS.read_text(encoding="utf-8")

css_patch = r'''

/* POLISH: map slider placement, pins, and official data design */

/* Hide old detached year slider card */
.csv-year-control {
  display: none !important;
}

/* Map inline year slider */
.csv-map-year-inline {
  position: absolute;
  top: 16px;
  right: 18px;
  z-index: 38;
  width: 260px;
  padding: 12px 14px;
  border-radius: 20px;
  background: rgba(2, 6, 23, 0.74);
  border: 1px solid rgba(125, 211, 252, 0.28);
  backdrop-filter: blur(18px);
  color: white;
  box-shadow: 0 18px 54px rgba(0,0,0,0.22);
}

.csv-map-year-inline span {
  display: block;
  color: #a5f3fc;
  font-size: 11px;
  font-weight: 950;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.csv-map-year-inline strong {
  display: block;
  margin: 3px 0 7px;
  color: white;
  font-size: 26px;
  line-height: 1;
}

.csv-map-year-inline input {
  width: 100%;
  accent-color: #22d3ee;
}

/* Map card proportions */
.csv-real-map {
  height: 560px !important;
}

.csv-real-map img {
  inset: 34px 42px 48px 42px !important;
  width: calc(100% - 84px) !important;
  height: calc(100% - 82px) !important;
  object-fit: contain !important;
}

/* Pins: larger but controlled */
.csv-map-pin {
  transform: translate(-50%, -50%) scale(calc(var(--pin-scale, 1) * 1.05)) !important;
}

.csv-map-pin i {
  width: 20px !important;
  height: 20px !important;
  border-width: 4px !important;
}

.csv-map-pin.selected i,
.csv-map-pin:hover i {
  width: 24px !important;
  height: 24px !important;
}

/* Stream: cleaner and not too dominant */
.csv-map-data-stream {
  left: 24px !important;
  right: 24px !important;
  bottom: 16px !important;
  padding: 10px 14px !important;
  opacity: 0.94;
}

/* Landing: remove visual mismatch and make official data beautiful */
.landing-live-chart {
  padding: 26px !important;
  border-radius: 34px !important;
  background:
    radial-gradient(circle at 12% 10%, rgba(34,211,238,0.10), transparent 28%),
    linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
}

.landing-live-chart-title {
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: end;
  gap: 14px;
  margin-bottom: 18px !important;
}

.landing-live-chart-title strong {
  font-size: 38px !important;
}

.landing-live-chart-title small {
  grid-column: 1 / -1;
  color: #64748b !important;
  font-size: 14px !important;
}

/* Official section as premium analytics cards */
.landing-official-bars {
  margin: 18px 0 24px !important;
  padding: 18px !important;
  border-radius: 30px !important;
  background:
    radial-gradient(circle at 92% 12%, rgba(20,184,166,0.22), transparent 26%),
    linear-gradient(135deg, #0f172a 0%, #172554 52%, #0f172a 100%) !important;
  border: 1px solid rgba(125,211,252,0.20) !important;
  box-shadow: 0 26px 70px rgba(15,23,42,0.18) !important;
}

.landing-official-bars-head {
  display: grid !important;
  grid-template-columns: 1fr auto;
  align-items: center;
  margin-bottom: 16px !important;
}

.landing-official-bars-head span {
  color: #a5f3fc !important;
  letter-spacing: 0.2em !important;
}

.landing-official-bars-head b {
  padding: 7px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,0.08);
  color: white !important;
  font-size: 13px !important;
}

.landing-official-bars-list {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 14px !important;
}

.landing-official-bar {
  min-height: 138px;
  display: grid;
  align-content: space-between;
  padding: 18px !important;
  border-radius: 24px !important;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.09), rgba(255,255,255,0.045)) !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.10);
}

.landing-official-bar-top {
  display: grid !important;
  grid-template-columns: 1fr !important;
  gap: 8px !important;
  margin-bottom: 12px !important;
}

.landing-official-bar strong {
  color: white !important;
  font-size: 18px !important;
  line-height: 1.2 !important;
}

.landing-official-bar small {
  color: rgba(226,232,240,0.72) !important;
  font-size: 12px !important;
}

.landing-official-bar em {
  order: -1;
  justify-self: start;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(165,243,252,0.12);
  color: #a5f3fc !important;
  font-size: 20px !important;
  font-weight: 950 !important;
}

.landing-official-bar-track {
  height: 10px !important;
  background: rgba(148,163,184,0.20) !important;
}

.landing-official-bar-track i {
  background: linear-gradient(90deg, #38bdf8, #2dd4bf, #f0f9ff) !important;
}

/* CSV ranking looks cleaner below official cards */
.landing-demo-bars-head {
  margin-top: 22px !important;
  padding-top: 18px !important;
}

.landing-live-row {
  padding: 15px 10px !important;
  border-radius: 18px;
}

.landing-live-row:hover {
  background: rgba(219,234,254,0.65) !important;
}

/* Research feed closer and softer */
.landing-research-feed-after {
  margin-top: 22px !important;
  border-radius: 32px !important;
}

@media (max-width: 980px) {
  .landing-official-bars-list {
    grid-template-columns: 1fr !important;
  }

  .csv-map-year-inline {
    left: 18px;
    right: 18px;
    top: 78px;
    width: auto;
  }
}

'''

if "POLISH: map slider placement" not in css:
    CSS.write_text(css + css_patch, encoding="utf-8")

print("✅ Polished map slider, pin bounds, official bars, and metric labels.")
