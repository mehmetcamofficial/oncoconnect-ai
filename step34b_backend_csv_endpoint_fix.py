from pathlib import Path

server_path = Path("backend/server.js")
app_path = Path("frontend/src/App.jsx")

server = server_path.read_text(encoding="utf-8")
app = app_path.read_text(encoding="utf-8")

csv_route = r'''

app.get("/public/map-data.csv", (req, res) => {
  const datasets = readDatasets().filter((d) => d.published);
  const rows = datasets.flatMap((d) =>
    d.rows.map((row) => ({
      ...row,
      _datasetId: d.id,
      _datasetName: d.name,
      _qualityFlag: d.qualityFlag,
      _sourceName: d.sourceName,
      _sourceUrl: d.sourceUrl
    }))
  );

  if (!rows.length) {
    res.setHeader("Content-Type", "text/csv; charset=utf-8");
    return res.send("");
  }

  const headers = Array.from(
    rows.reduce((set, row) => {
      Object.keys(row).forEach((key) => set.add(key));
      return set;
    }, new Set())
  );

  const escapeCsv = (value) => {
    const text = String(value ?? "");
    if (text.includes(",") || text.includes('"') || text.includes("\n")) {
      return `"${text.replace(/"/g, '""')}"`;
    }
    return text;
  };

  const csv = [
    headers.join(","),
    ...rows.map((row) => headers.map((h) => escapeCsv(row[h])).join(","))
  ].join("\n");

  res.setHeader("Content-Type", "text/csv; charset=utf-8");
  res.send(csv);
});
'''

if "/public/map-data.csv" not in server:
    listen_idx = server.rfind("app.listen")
    if listen_idx == -1:
        raise RuntimeError("app.listen bulunamadı.")
    server = server[:listen_idx] + csv_route + "\n\n" + server[listen_idx:]
    server_path.write_text(server, encoding="utf-8")
    print("✅ /public/map-data.csv endpoint added.")
else:
    print("ℹ️ CSV endpoint already exists.")

app = app.replace(
    'fetch("http://localhost:5050/public/map-data")',
    'fetch("http://localhost:5050/public/map-data.csv")'
)

app_path.write_text(app, encoding="utf-8")
print("✅ Frontend now reads backend CSV endpoint.")
