from pathlib import Path

backend = Path("backend")
server_path = backend / "server.js"
package_path = backend / "package.json"

if not server_path.exists():
    raise RuntimeError("backend/server.js bulunamadı.")

data_dir = backend / "data"
uploads_dir = data_dir / "uploads"
data_dir.mkdir(exist_ok=True)
uploads_dir.mkdir(exist_ok=True)

store_path = data_dir / "admin_datasets.json"

if not store_path.exists():
    store_path.write_text("[]", encoding="utf-8")

server = server_path.read_text(encoding="utf-8")

# multer dependency notu
pkg = package_path.read_text(encoding="utf-8") if package_path.exists() else ""
needs_multer = '"multer"' not in pkg

admin_code = r'''

/* ================================
   Admin Data Management API
   Step 33
================================ */

const fs = require("fs");
const path = require("path");
const multer = require("multer");

const ADMIN_DATA_DIR = path.join(__dirname, "data");
const ADMIN_UPLOAD_DIR = path.join(ADMIN_DATA_DIR, "uploads");
const ADMIN_STORE_PATH = path.join(ADMIN_DATA_DIR, "admin_datasets.json");

if (!fs.existsSync(ADMIN_DATA_DIR)) fs.mkdirSync(ADMIN_DATA_DIR);
if (!fs.existsSync(ADMIN_UPLOAD_DIR)) fs.mkdirSync(ADMIN_UPLOAD_DIR);
if (!fs.existsSync(ADMIN_STORE_PATH)) fs.writeFileSync(ADMIN_STORE_PATH, "[]");

const upload = multer({ dest: ADMIN_UPLOAD_DIR });

function readDatasets() {
  try {
    return JSON.parse(fs.readFileSync(ADMIN_STORE_PATH, "utf8"));
  } catch {
    return [];
  }
}

function writeDatasets(data) {
  fs.writeFileSync(ADMIN_STORE_PATH, JSON.stringify(data, null, 2));
}

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/);
  if (!lines.length) return [];

  const headers = lines[0].split(",").map((h) => h.trim());

  return lines.slice(1).filter(Boolean).map((line) => {
    const values = [];
    let current = "";
    let inQuotes = false;

    for (const char of line) {
      if (char === '"') {
        inQuotes = !inQuotes;
      } else if (char === "," && !inQuotes) {
        values.push(current);
        current = "";
      } else {
        current += char;
      }
    }

    values.push(current);

    const row = {};
    headers.forEach((h, i) => {
      row[h] = values[i]?.trim() || "";
    });

    return row;
  });
}

app.get("/admin/datasets", (req, res) => {
  res.json({
    success: true,
    datasets: readDatasets()
  });
});

app.post("/admin/upload", upload.single("file"), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ success: false, error: "No file uploaded" });
    }

    const originalName = req.file.originalname;
    const ext = path.extname(originalName).toLowerCase();

    if (ext !== ".csv") {
      return res.status(400).json({
        success: false,
        error: "For Step 33 only CSV upload is supported. Excel support comes in Step 34."
      });
    }

    const raw = fs.readFileSync(req.file.path, "utf8");
    const rows = parseCsv(raw);

    const dataset = {
      id: `ds_${Date.now()}`,
      name: originalName,
      type: "csv",
      uploadedAt: new Date().toISOString(),
      rowCount: rows.length,
      published: false,
      qualityFlag: "needs_verification",
      sourceName: "manual_upload",
      sourceUrl: "",
      rows
    };

    const datasets = readDatasets();
    datasets.unshift(dataset);
    writeDatasets(datasets);

    res.json({
      success: true,
      dataset: {
        ...dataset,
        rows: rows.slice(0, 20)
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

app.patch("/admin/datasets/:id", (req, res) => {
  const datasets = readDatasets();
  const index = datasets.findIndex((d) => d.id === req.params.id);

  if (index === -1) {
    return res.status(404).json({ success: false, error: "Dataset not found" });
  }

  datasets[index] = {
    ...datasets[index],
    ...req.body,
    updatedAt: new Date().toISOString()
  };

  writeDatasets(datasets);

  res.json({
    success: true,
    dataset: datasets[index]
  });
});

app.delete("/admin/datasets/:id", (req, res) => {
  const datasets = readDatasets();
  const filtered = datasets.filter((d) => d.id !== req.params.id);

  writeDatasets(filtered);

  res.json({
    success: true,
    deleted: req.params.id
  });
});

app.post("/admin/datasets/:id/records", (req, res) => {
  const datasets = readDatasets();
  const dataset = datasets.find((d) => d.id === req.params.id);

  if (!dataset) {
    return res.status(404).json({ success: false, error: "Dataset not found" });
  }

  dataset.rows.unshift({
    ...req.body,
    _manual: true,
    _createdAt: new Date().toISOString()
  });

  dataset.rowCount = dataset.rows.length;
  dataset.updatedAt = new Date().toISOString();

  writeDatasets(datasets);

  res.json({
    success: true,
    dataset
  });
});

app.get("/public/map-data", (req, res) => {
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

  res.json({
    success: true,
    totalRows: rows.length,
    datasets: datasets.map((d) => ({
      id: d.id,
      name: d.name,
      rowCount: d.rowCount,
      qualityFlag: d.qualityFlag,
      sourceName: d.sourceName,
      published: d.published
    })),
    rows
  });
});

app.post("/admin/sync", async (req, res) => {
  res.json({
    success: true,
    message: "Auto-sync placeholder ready. Step 35 will connect GLOBOCAN / ECIS / OWID sources.",
    syncedAt: new Date().toISOString()
  });
});
'''

if "Admin Data Management API" not in server:
    server += "\n" + admin_code
    server_path.write_text(server, encoding="utf-8")
    print("✅ Admin Data API added to backend/server.js")
else:
    print("ℹ️ Admin Data API already exists.")

print("✅ Data store ready:", store_path)

if needs_multer:
    print("⚠️ Run this once: cd backend && npm install multer")
else:
    print("✅ multer already appears in package.json")
