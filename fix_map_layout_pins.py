from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# 1) Floating card içindeki Use in AI Copilot butonunu kaldır
s = s.replace(
'''                  <button onClick={() => setPage("copilot")}>Use in AI Copilot</button>''',
'''                  <small className="csv-floating-hint">Click another pin to compare.</small>'''
)

# 2) Harita yüksekliğini daha kontrollü yapmak için class aynı kalıyor, CSS override yapacağız

# 3) Rastgele pin dağılımını Türkiye haritası sınırlarına daha iyi oturt
old = '''    const getCoords = (areaName, index) => {
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
    };'''

new = '''    const turkeyAutoCoords = [
      [22, 52], [25, 58], [29, 49], [31, 62], [35, 55], [38, 47], [40, 61],
      [44, 53], [47, 46], [50, 58], [54, 50], [57, 62], [60, 54], [64, 45],
      [67, 56], [70, 49], [73, 60], [76, 52], [79, 45], [82, 56], [85, 49],
      [33, 68], [43, 68], [53, 68], [63, 66], [73, 66],
      [36, 39], [46, 38], [56, 37], [66, 38], [76, 39]
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
    };'''

if old not in s:
    print("⚠️ getCoords block bulunamadı; sadece CSS düzeltmesi uygulanacak.")
else:
    s = s.replace(old, new, 1)

app.write_text(s, encoding="utf-8")

css_patch = r'''

/* Map layout + pin cleanup v2 */

.csv-map-layout {
  align-items: start !important;
  padding-bottom: 36px !important;
}

.csv-map-card {
  padding: 18px !important;
}

.csv-real-map {
  height: 590px !important;
  border-radius: 30px !important;
}

.csv-real-map img {
  inset: 42px 28px 36px 28px !important;
  width: calc(100% - 56px) !important;
  height: calc(100% - 78px) !important;
  object-fit: contain !important;
}

.csv-map-grid {
  opacity: 0.38 !important;
}

.csv-map-overlay-panel {
  left: 18px !important;
  top: 18px !important;
  min-width: 210px !important;
  padding: 14px 16px !important;
  border-radius: 20px !important;
  transform: scale(0.88);
  transform-origin: top left;
}

.csv-map-overlay-panel strong {
  font-size: 22px !important;
}

.csv-map-pin {
  z-index: 20 !important;
}

.csv-map-pin i {
  width: 18px !important;
  height: 18px !important;
  border-width: 4px !important;
}

.csv-map-pin span,
.csv-map-pin b {
  font-size: 11px !important;
}

.csv-floating-card {
  right: 20px !important;
  bottom: 20px !important;
  width: 235px !important;
  padding: 16px !important;
  border-radius: 22px !important;
  z-index: 50 !important;
}

.csv-floating-card h3 {
  font-size: 24px !important;
  margin: 6px 0 10px !important;
}

.csv-floating-card div {
  padding: 7px 0 !important;
}

.csv-floating-card strong {
  font-size: 18px !important;
}

.csv-floating-card button {
  display: none !important;
}

.csv-floating-hint {
  display: block !important;
  margin-top: 12px;
  color: rgba(226,232,240,0.72) !important;
  font-weight: 800;
}

.csv-map-summary {
  grid-template-columns: repeat(4, minmax(120px, 1fr)) !important;
  margin-bottom: 14px !important;
}

.csv-map-summary div {
  padding: 14px !important;
}

.csv-map-summary strong {
  font-size: 20px !important;
}

.csv-map-side {
  gap: 16px !important;
}

.csv-selected-card,
.csv-rank-card {
  padding: 22px !important;
}

.csv-selected-card h2 {
  font-size: 30px !important;
}

.csv-selected-metrics {
  gap: 10px !important;
}

.csv-selected-metrics button {
  padding: 14px !important;
}

.csv-selected-metrics strong {
  font-size: 26px !important;
}

.csv-rank-list {
  max-height: 520px;
  overflow-y: auto;
  padding-right: 4px;
}

.csv-control-row {
  grid-template-columns: 1fr 320px !important;
}

.csv-year-control {
  padding: 12px 14px !important;
  border-radius: 24px !important;
}

.csv-year-control strong {
  font-size: 28px !important;
}

@media (max-width: 1100px) {
  .csv-real-map {
    height: 540px !important;
  }

  .csv-floating-card {
    width: 220px !important;
  }
}

@media (max-width: 720px) {
  .csv-real-map {
    height: 500px !important;
  }

  .csv-floating-card {
    left: 16px !important;
    right: 16px !important;
    bottom: 16px !important;
    width: auto !important;
  }
}

'''

css.write_text(css.read_text(encoding="utf-8") + css_patch, encoding="utf-8")
print("✅ Map layout, floating card, pins and AI button fixed.")
