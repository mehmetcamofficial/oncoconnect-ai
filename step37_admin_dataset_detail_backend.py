from pathlib import Path

p = Path("backend/server.js")
s = p.read_text(encoding="utf-8")

block = r'''

app.get("/admin/datasets/:id", (req, res) => {
  const datasets = readDatasets();
  const dataset = datasets.find((d) => d.id === req.params.id);

  if (!dataset) {
    return res.status(404).json({
      success: false,
      error: "Dataset not found"
    });
  }

  const rows = dataset.rows || [];
  const columns = rows.length ? Object.keys(rows[0]) : [];

  res.json({
    success: true,
    dataset: {
      ...dataset,
      columns,
      previewRows: rows.slice(0, 20)
    }
  });
});

'''

if 'app.get("/admin/datasets/:id"' not in s:
    idx = s.rfind("app.listen")
    s = s[:idx] + block + "\n" + s[idx:]
    p.write_text(s, encoding="utf-8")
    print("✅ Dataset detail endpoint added.")
else:
    print("ℹ️ Dataset detail endpoint already exists.")
