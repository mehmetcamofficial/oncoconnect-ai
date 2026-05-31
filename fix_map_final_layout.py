from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# 1) KnowledgePage varsa KnowledgeGraphPage ismine çevir
s = s.replace("const KnowledgePage = () =>", "const KnowledgeGraphPage = () =>")
s = s.replace('return <KnowledgePage />;', 'return <KnowledgeGraphPage />;')

# 2) Route knowledge yoksa ekle
if 'if (page === "knowledge") return <KnowledgeGraphPage />;' not in s:
    s = s.replace(
        'if (page === "map") return <MapPage />;',
        'if (page === "knowledge") return <KnowledgeGraphPage />;\n  if (page === "map") return <MapPage />;',
        1
    )

# 3) Floating card içindeki gereksiz AI butonu tamamen kaldır
s = s.replace('<button onClick={() => setPage("copilot")}>Use in AI Copilot</button>', '')
s = s.replace('<small className="csv-floating-hint">Click another pin to compare.</small>', '')

app.write_text(s, encoding="utf-8")

css_patch = r'''

/* FINAL MAP CLEANUP — compact controls, no empty bottom, smaller floating card */

.csv-map-controls {
  margin: -18px auto 18px !important;
}

.csv-control-row {
  grid-template-columns: 1fr !important;
  gap: 12px !important;
}

.csv-year-control {
  max-width: 520px !important;
  margin-left: auto !important;
  margin-right: 0 !important;
  padding: 12px 18px !important;
  border-radius: 22px !important;
  transform: translateY(0) !important;
}

.csv-year-control strong {
  font-size: 28px !important;
}

.csv-map-layout {
  grid-template-columns: minmax(0, 1fr) 420px !important;
  align-items: start !important;
  padding-bottom: 20px !important;
  margin-bottom: 0 !important;
}

.csv-map-card {
  padding: 16px !important;
  margin-bottom: 0 !important;
}

.csv-real-map {
  height: 540px !important;
  min-height: 540px !important;
  max-height: 540px !important;
}

.csv-real-map img {
  inset: 28px 24px 28px 24px !important;
  width: calc(100% - 48px) !important;
  height: calc(100% - 56px) !important;
  object-fit: contain !important;
}

.csv-map-overlay-panel {
  transform: scale(0.78) !important;
  transform-origin: top left !important;
  left: 14px !important;
  top: 14px !important;
  min-width: 190px !important;
  padding: 12px 14px !important;
}

.csv-map-overlay-panel strong {
  font-size: 21px !important;
}

.csv-floating-card {
  width: 210px !important;
  right: 18px !important;
  bottom: 18px !important;
  padding: 14px !important;
  border-radius: 18px !important;
  transform: scale(0.9) !important;
  transform-origin: bottom right !important;
}

.csv-floating-card h3 {
  font-size: 22px !important;
  margin: 4px 0 8px !important;
}

.csv-floating-card div {
  padding: 5px 0 !important;
}

.csv-floating-card strong {
  font-size: 17px !important;
}

.csv-floating-card button,
.csv-floating-hint {
  display: none !important;
}

.csv-map-pin {
  transform: translate(-50%, -50%) scale(0.82) !important;
}

.csv-map-pin i {
  width: 15px !important;
  height: 15px !important;
  border-width: 3px !important;
}

.csv-map-summary {
  margin-bottom: 12px !important;
}

.csv-map-summary div {
  padding: 12px !important;
}

.csv-selected-card,
.csv-rank-card {
  padding: 20px !important;
}

.csv-rank-list {
  max-height: 390px !important;
  overflow-y: auto !important;
}

.csv-rank-list button {
  padding: 11px !important;
}

.csv-source-note {
  margin-top: 12px !important;
}

@media (max-width: 1100px) {
  .csv-map-layout {
    grid-template-columns: 1fr !important;
  }

  .csv-year-control {
    margin-left: 0 !important;
    max-width: none !important;
  }
}

'''

css.write_text(css.read_text(encoding="utf-8") + css_patch, encoding="utf-8")
print("✅ Final map layout cleanup applied.")
