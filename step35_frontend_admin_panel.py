from pathlib import Path

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) page state admin destekliyorsa geç; yoksa ekle
if 'setPage("admin")' not in app:
    app = app.replace(
        '<button onClick={() => setPage("kids")}>Onco Kids</button>',
        '<button onClick={() => setPage("kids")}>Onco Kids</button>\n            <button onClick={() => setPage("admin")}>Admin</button>'
    )

# 2) AdminPage component ekle
if "function AdminPanel()" not in app:
    insert_before = app.rfind("export default")
    if insert_before == -1:
        raise RuntimeError("export default bulunamadı.")

    admin_component = r'''

function AdminPanel() {
  const [datasets, setDatasets] = React.useState([]);
  const [file, setFile] = React.useState(null);
  const [status, setStatus] = React.useState("");
  const [loading, setLoading] = React.useState(false);

  const API = "http://localhost:5050";

  async function loadDatasets() {
    setLoading(true);
    try {
      const res = await fetch(`${API}/admin/datasets`);
      const data = await res.json();
      setDatasets(data.datasets || []);
    } catch (err) {
      setStatus("Could not load datasets. Is backend running on port 5050?");
    } finally {
      setLoading(false);
    }
  }

  React.useEffect(() => {
    loadDatasets();
  }, []);

  async function uploadDataset() {
    if (!file) {
      setStatus("Please choose a CSV file first.");
      return;
    }

    const form = new FormData();
    form.append("file", file);

    setStatus("Uploading dataset...");
    setLoading(true);

    try {
      const res = await fetch(`${API}/admin/upload`, {
        method: "POST",
        body: form
      });

      const data = await res.json();

      if (!data.success) {
        setStatus(data.error || "Upload failed.");
        return;
      }

      setStatus(`Uploaded ${data.dataset.name} with ${data.dataset.rowCount} rows.`);
      setFile(null);
      await loadDatasets();
    } catch (err) {
      setStatus("Upload failed. Check backend.");
    } finally {
      setLoading(false);
    }
  }

  async function updateDataset(id, patch) {
    setLoading(true);
    try {
      const res = await fetch(`${API}/admin/datasets/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(patch)
      });

      const data = await res.json();

      if (!data.success) {
        setStatus(data.error || "Update failed.");
        return;
      }

      setStatus("Dataset updated.");
      await loadDatasets();
    } catch (err) {
      setStatus("Update failed.");
    } finally {
      setLoading(false);
    }
  }

  async function deleteDataset(id) {
    if (!window.confirm("Delete this dataset from admin storage?")) return;

    setLoading(true);
    try {
      await fetch(`${API}/admin/datasets/${id}`, { method: "DELETE" });
      setStatus("Dataset deleted.");
      await loadDatasets();
    } catch (err) {
      setStatus("Delete failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="admin-page-v35">
      <div className="admin-topbar-v35">
        <button onClick={() => window.location.reload()}>↻ Refresh</button>
        <button onClick={() => window.history.back()}>← Back</button>
      </div>

      <section className="admin-hero-v35">
        <div>
          <small>ONCOCONNECT AI ADMIN</small>
          <h1>Data Control Center</h1>
          <p>
            Upload CSV datasets, publish verified layers, manage source labels,
            and control what appears on the public cancer burden map.
          </p>
        </div>

        <div className="admin-health-v35">
          <span className={loading ? "pulse" : ""}></span>
          <strong>{loading ? "Working..." : "Backend connected"}</strong>
          <p>Port 5050 · Express Admin API</p>
        </div>
      </section>

      <section className="admin-upload-v35">
        <div>
          <h2>Upload dataset</h2>
          <p>CSV is supported now. Excel support can be added next.</p>
        </div>

        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
        />

        <button onClick={uploadDataset}>Upload CSV</button>
      </section>

      {status && <div className="admin-status-v35">{status}</div>}

      <section className="admin-datasets-v35">
        <div className="admin-section-title-v35">
          <div>
            <small>DATASETS</small>
            <h2>Published and draft data layers</h2>
          </div>
          <button onClick={loadDatasets}>Reload</button>
        </div>

        <div className="admin-table-v35">
          <div className="admin-row-v35 admin-head-v35">
            <span>Name</span>
            <span>Rows</span>
            <span>Status</span>
            <span>Quality</span>
            <span>Source</span>
            <span>Actions</span>
          </div>

          {datasets.length === 0 && (
            <div className="admin-empty-v35">
              No datasets yet. Upload a CSV to create the first map layer.
            </div>
          )}

          {datasets.map((d) => (
            <div className="admin-row-v35" key={d.id}>
              <span>
                <strong>{d.name}</strong>
                <small>{d.id}</small>
              </span>

              <span>{d.rowCount}</span>

              <span>
                <button
                  className={d.published ? "published-v35" : "draft-v35"}
                  onClick={() => updateDataset(d.id, { published: !d.published })}
                >
                  {d.published ? "Published" : "Draft"}
                </button>
              </span>

              <span>
                <select
                  value={d.qualityFlag || "needs_verification"}
                  onChange={(e) => updateDataset(d.id, { qualityFlag: e.target.value })}
                >
                  <option value="official">official</option>
                  <option value="estimated">estimated</option>
                  <option value="simulated">simulated</option>
                  <option value="needs_verification">needs_verification</option>
                </select>
              </span>

              <span>
                <input
                  defaultValue={d.sourceName || ""}
                  placeholder="source name"
                  onBlur={(e) => updateDataset(d.id, { sourceName: e.target.value })}
                />
              </span>

              <span className="admin-actions-v35">
                <button onClick={() => updateDataset(d.id, { published: true })}>
                  Publish
                </button>
                <button onClick={() => updateDataset(d.id, { published: false })}>
                  Unpublish
                </button>
                <button className="danger-v35" onClick={() => deleteDataset(d.id)}>
                  Delete
                </button>
              </span>
            </div>
          ))}
        </div>
      </section>

      <section className="admin-note-v35">
        <strong>Important:</strong> Published datasets feed the map through
        <code> /public/map-data.csv </code>. Keep simulated or unverified sources clearly labeled.
      </section>
    </main>
  );
}

'''
    app = app[:insert_before] + admin_component + "\n" + app[insert_before:]

# 3) page render içine admin ekle
if 'page === "admin"' not in app:
    # kids render yakınında eklemeye çalış
    app = app.replace(
        'if (page === "kids") return <OncoKidsPage',
        'if (page === "admin") return <AdminPanel />;\n  if (page === "kids") return <OncoKidsPage'
    )

css += r'''

/* Step 35 Admin Panel */

.admin-page-v35 {
  min-height: 100vh;
  padding: 34px;
  background:
    radial-gradient(circle at 20% 10%, rgba(59,130,246,.16), transparent 28%),
    linear-gradient(135deg, #f8fafc, #eef6ff);
  color: #0f172a;
}

.admin-topbar-v35 {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-bottom: 20px;
}

.admin-topbar-v35 button,
.admin-upload-v35 button,
.admin-section-title-v35 button,
.admin-actions-v35 button,
.admin-row-v35 button {
  border: none;
  border-radius: 999px;
  padding: 10px 14px;
  font-weight: 900;
  cursor: pointer;
  background: #2563eb;
  color: white;
}

.admin-hero-v35 {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 24px;
  padding: 34px;
  border-radius: 36px;
  background: linear-gradient(135deg, #0f172a, #1d4ed8);
  color: white;
  box-shadow: 0 28px 90px rgba(15,23,42,.22);
}

.admin-hero-v35 small,
.admin-section-title-v35 small {
  letter-spacing: .16em;
  font-weight: 950;
  opacity: .75;
}

.admin-hero-v35 h1 {
  margin: 8px 0 12px;
  font-size: clamp(42px, 6vw, 84px);
  line-height: .95;
}

.admin-hero-v35 p {
  max-width: 760px;
  font-size: 20px;
  line-height: 1.55;
  color: #dbeafe;
}

.admin-health-v35 {
  border-radius: 28px;
  padding: 24px;
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.22);
  align-self: center;
}

.admin-health-v35 span {
  width: 18px;
  height: 18px;
  border-radius: 999px;
  display: inline-block;
  background: #22c55e;
  margin-right: 8px;
}

.admin-health-v35 .pulse {
  animation: adminPulseV35 1s infinite;
}

.admin-health-v35 strong {
  font-size: 22px;
}

.admin-upload-v35 {
  margin-top: 26px;
  display: grid;
  grid-template-columns: 1fr 360px auto;
  gap: 18px;
  align-items: center;
  padding: 24px;
  border-radius: 30px;
  background: white;
  border: 1px solid #dbeafe;
  box-shadow: 0 18px 50px rgba(15,23,42,.08);
}

.admin-upload-v35 h2,
.admin-section-title-v35 h2 {
  margin: 0;
  font-size: 28px;
}

.admin-upload-v35 p {
  margin: 6px 0 0;
  color: #64748b;
  font-weight: 750;
}

.admin-upload-v35 input {
  padding: 12px;
  border: 1px solid #cbd5e1;
  border-radius: 18px;
  background: #f8fafc;
}

.admin-status-v35 {
  margin-top: 18px;
  padding: 16px 18px;
  border-radius: 22px;
  background: #ecfeff;
  color: #0f766e;
  font-weight: 950;
  border: 1px solid #a5f3fc;
}

.admin-datasets-v35 {
  margin-top: 28px;
  padding: 26px;
  border-radius: 34px;
  background: rgba(255,255,255,.96);
  border: 1px solid #dbeafe;
  box-shadow: 0 24px 70px rgba(15,23,42,.08);
}

.admin-section-title-v35 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
}

.admin-table-v35 {
  display: grid;
  gap: 10px;
}

.admin-row-v35 {
  display: grid;
  grid-template-columns: 2.1fr .6fr .9fr 1fr 1.2fr 2fr;
  gap: 12px;
  align-items: center;
  padding: 14px;
  border-radius: 20px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
}

.admin-head-v35 {
  background: #0f172a;
  color: white;
  font-weight: 950;
}

.admin-row-v35 strong,
.admin-row-v35 small {
  display: block;
}

.admin-row-v35 small {
  color: #64748b;
  margin-top: 4px;
}

.admin-head-v35 small {
  color: white;
}

.admin-row-v35 select,
.admin-row-v35 input {
  width: 100%;
  border: 1px solid #cbd5e1;
  border-radius: 14px;
  padding: 10px;
  background: white;
  font-weight: 800;
}

.published-v35 {
  background: #16a34a !important;
}

.draft-v35 {
  background: #f59e0b !important;
}

.admin-actions-v35 {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.admin-actions-v35 button {
  padding: 8px 11px;
  font-size: 13px;
}

.danger-v35 {
  background: #dc2626 !important;
}

.admin-empty-v35 {
  padding: 30px;
  border-radius: 24px;
  background: #f8fafc;
  color: #64748b;
  font-weight: 900;
  text-align: center;
}

.admin-note-v35 {
  margin-top: 22px;
  padding: 20px;
  border-radius: 24px;
  background: #fff7ed;
  border: 1px solid #fed7aa;
  color: #9a3412;
  font-weight: 850;
}

.admin-note-v35 code {
  background: rgba(255,255,255,.7);
  padding: 4px 8px;
  border-radius: 8px;
}

@keyframes adminPulseV35 {
  0%, 100% { transform: scale(1); opacity: .7; }
  50% { transform: scale(1.35); opacity: 1; }
}

@media (max-width: 1000px) {
  .admin-hero-v35,
  .admin-upload-v35,
  .admin-row-v35 {
    grid-template-columns: 1fr;
  }

  .admin-page-v35 {
    padding: 18px;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Step 35 applied: Admin Panel added to frontend.")
