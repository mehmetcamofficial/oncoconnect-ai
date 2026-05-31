from pathlib import Path

p = Path("frontend/src/App.jsx")
s = p.read_text(encoding="utf-8")

start = s.find("function AdminPanel() {")
end = s.find("\nexport default", start)

if start == -1 or end == -1:
    raise RuntimeError("AdminPanel veya export default bulunamadı.")

new_admin = r'''
function AdminPanel() {
  const API = "http://localhost:5050";

  const [authenticated, setAuthenticated] = React.useState(
    localStorage.getItem("admin-auth") === "true"
  );
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [datasets, setDatasets] = React.useState([]);
  const [file, setFile] = React.useState(null);
  const [status, setStatus] = React.useState("");
  const [loading, setLoading] = React.useState(false);
  const [selectedDataset, setSelectedDataset] = React.useState(null);
  const [mapping, setMapping] = React.useState({});
  const [adminTab, setAdminTab] = React.useState("overview");

  async function login() {
    try {
      const res = await fetch(`${API}/admin/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });

      const data = await res.json();

      if (!data.success) {
        setStatus("Invalid admin credentials.");
        return;
      }

      localStorage.setItem("admin-auth", "true");
      setAuthenticated(true);
      setStatus("Admin login successful.");
    } catch {
      setStatus("Login failed. Check backend.");
    }
  }

  function logout() {
    localStorage.removeItem("admin-auth");
    setAuthenticated(false);
    setUsername("");
    setPassword("");
  }

  async function loadDatasets() {
    setLoading(true);
    try {
      const res = await fetch(`${API}/admin/datasets`);
      const data = await res.json();
      setDatasets(data.datasets || []);
    } catch {
      setStatus("Could not load datasets. Is backend running on port 5050?");
    } finally {
      setLoading(false);
    }
  }

  React.useEffect(() => {
    if (authenticated) loadDatasets();
  }, [authenticated]);

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
    } catch {
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
    } catch {
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
    } catch {
      setStatus("Delete failed.");
    } finally {
      setLoading(false);
    }
  }

  async function openDatasetDetail(id) {
    setLoading(true);
    try {
      const res = await fetch(`${API}/admin/datasets/${id}`);
      const data = await res.json();

      if (!data.success) {
        setStatus(data.error || "Could not load dataset detail.");
        return;
      }

      const dataset = data.dataset;
      setSelectedDataset(dataset);

      const cols = dataset.columns || [];
      setMapping({
        region: cols.find((c) => c.toLowerCase().includes("bolge")) || "",
        location: cols.find((c) => c.toLowerCase().includes("ulke") || c.toLowerCase().includes("sehir")) || "",
        sex: cols.find((c) => c.toLowerCase().includes("cinsiyet")) || "",
        cancerType: cols.find((c) => c.toLowerCase().includes("kanser")) || "",
        ageGroup: cols.find((c) => c.toLowerCase().includes("yas")) || "",
        incidence: cols.find((c) => c.toLowerCase().includes("vaka")) || "",
        mortality: cols.find((c) => c.toLowerCase().includes("olum")) || "",
        survival: cols.find((c) => c.toLowerCase().includes("sagkalim")) || ""
      });
    } catch {
      setStatus("Dataset detail failed. Check backend endpoint.");
    } finally {
      setLoading(false);
    }
  }

  const totalRows = datasets.reduce((sum, d) => sum + Number(d.rowCount || 0), 0);
  const publishedCount = datasets.filter((d) => d.published).length;
  const needsReview = datasets.some((d) => d.qualityFlag === "needs_verification");

  if (!authenticated) {
    return (
      <main className="admin-page-v35 admin-login-page-v36">
        <button className="admin-back-home-v36" onClick={() => window.location.reload()}>
          🏠 Home
        </button>

        <section className="admin-login-card-v36">
          <small>ONCOCONNECT AI ADMIN</small>
          <h1>Admin Login</h1>
          <p>Sign in to manage datasets, map layers and source labels.</p>

          <input
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") login();
            }}
          />

          <button onClick={login}>Login</button>

          {status && <div className="admin-status-v35">{status}</div>}

          <div className="admin-login-hint-v36">
            Demo credentials: <strong>admin</strong> / <strong>OncoConnect2026!</strong>
          </div>
        </section>
      </main>
    );
  }

  return (
    <main className="admin-page-v35">
      <div className="admin-topbar-v35">
        <button onClick={() => window.location.reload()}>🏠 Home</button>
        <button onClick={loadDatasets}>↻ Refresh</button>
        <button onClick={logout}>Logout</button>
      </div>

      <section className="admin-hero-v35">
        <div>
          <small>ONCOCONNECT AI ADMIN</small>
          <h1>Data Control Center</h1>
          <p>
            Upload datasets, publish verified layers, manage source labels,
            preview data quality and control what appears on the public cancer burden map.
          </p>
        </div>

        <div className="admin-health-v35">
          <span className={loading ? "pulse" : ""}></span>
          <strong>{loading ? "Working..." : "Backend connected"}</strong>
          <p>Port 5050 · Express Admin API</p>
        </div>
      </section>

      <section className="admin-tabs-v38">
        {[
          ["overview", "Overview"],
          ["datasets", "Datasets"],
          ["mapping", "Preview & Mapping"],
          ["sources", "Sources"],
          ["automation", "Automation"],
          ["settings", "Settings"]
        ].map(([key, label]) => (
          <button
            key={key}
            className={adminTab === key ? "active" : ""}
            onClick={() => setAdminTab(key)}
          >
            {label}
          </button>
        ))}
      </section>

      {status && <div className="admin-status-v35">{status}</div>}

      {adminTab === "overview" && (
        <>
          <section className="admin-overview-grid-v38">
            <div className="admin-kpi-v38">
              <small>Total datasets</small>
              <strong>{datasets.length}</strong>
              <p>Uploaded data layers in admin storage.</p>
            </div>

            <div className="admin-kpi-v38">
              <small>Published layers</small>
              <strong>{publishedCount}</strong>
              <p>Visible on public map endpoints.</p>
            </div>

            <div className="admin-kpi-v38">
              <small>Total rows</small>
              <strong>{totalRows.toLocaleString()}</strong>
              <p>Rows available across uploaded datasets.</p>
            </div>

            <div className="admin-kpi-v38 accent">
              <small>Data status</small>
              <strong>{needsReview ? "Review" : "Ready"}</strong>
              <p>Keep unverified sources clearly labeled.</p>
            </div>
          </section>

          <section className="admin-command-grid-v38">
            <button onClick={() => setAdminTab("datasets")}>Manage datasets</button>
            <button onClick={() => setAdminTab("mapping")}>Open mapping tools</button>
            <button onClick={() => window.location.reload()}>Open public map preview</button>
          </section>
        </>
      )}

      {adminTab === "datasets" && (
        <section className="admin-datasets-tab-v38">
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
                    <input
                      defaultValue={d.sourceUrl || ""}
                      placeholder="source URL"
                      onBlur={(e) => updateDataset(d.id, { sourceUrl: e.target.value })}
                    />
                  </span>

                  <span className="admin-actions-v35">
                    <button onClick={() => openDatasetDetail(d.id)}>Preview</button>
                    <button onClick={() => updateDataset(d.id, { published: true })}>Publish</button>
                    <button onClick={() => updateDataset(d.id, { published: false })}>Unpublish</button>
                    <button className="danger-v35" onClick={() => deleteDataset(d.id)}>Delete</button>
                  </span>
                </div>
              ))}
            </div>
          </section>
        </section>
      )}

      {adminTab === "mapping" && (
        <section className="admin-panel-placeholder-v38">
          <small>PREVIEW & MAPPING</small>
          <h2>Dataset preview and field mapping</h2>
          <p>
            Select <strong>Datasets</strong>, then click <strong>Preview</strong> on a dataset row.
            The preview modal opens with the first 20 rows and automatic column suggestions.
          </p>
          <button onClick={() => setAdminTab("datasets")}>Go to datasets</button>
        </section>
      )}

      {adminTab === "sources" && (
        <section className="admin-panel-placeholder-v38">
          <small>SOURCES</small>
          <h2>Source governance</h2>
          <p>
            Use source name and source URL fields to label every dataset. Distinguish official,
            estimated, simulated and unverified data before publishing.
          </p>
        </section>
      )}

      {adminTab === "automation" && (
        <section className="admin-panel-placeholder-v38">
          <small>AUTO SYNC</small>
          <h2>Automated data sync roadmap</h2>
          <p>
            Next step: add connectors for GLOBOCAN, ECIS or manually approved national registry files.
            Auto-sync should write to draft datasets first, never directly publish.
          </p>
        </section>
      )}

      {adminTab === "settings" && (
        <section className="admin-panel-placeholder-v38">
          <small>SETTINGS</small>
          <h2>Admin settings</h2>
          <p>
            Configure default language, quality labels, upload limits and map visibility rules.
            Passwords should later move to environment variables.
          </p>
        </section>
      )}

      {selectedDataset && (
        <section className="admin-preview-overlay-v37">
          <div className="admin-preview-modal-v37">
            <div className="admin-preview-head-v37">
              <div>
                <small>DATASET PREVIEW</small>
                <h2>{selectedDataset.name}</h2>
                <p>{selectedDataset.rowCount} rows · {selectedDataset.qualityFlag}</p>
              </div>
              <button onClick={() => setSelectedDataset(null)}>Close</button>
            </div>

            <div className="admin-mapping-v37">
              <div>
                <small>COLUMN MAPPING</small>
                <h3>Map dataset fields</h3>
                <p>
                  These mappings explain how the platform reads your CSV before
                  visualizing it on the cancer burden map.
                </p>
              </div>

              {[
                ["region", "Region"],
                ["location", "City / Country"],
                ["sex", "Sex"],
                ["cancerType", "Cancer Type"],
                ["ageGroup", "Age Group"],
                ["incidence", "Incidence Rate"],
                ["mortality", "Mortality Rate"],
                ["survival", "5-Year Survival"]
              ].map(([key, label]) => (
                <label key={key}>
                  <span>{label}</span>
                  <select
                    value={mapping[key] || ""}
                    onChange={(e) => setMapping({ ...mapping, [key]: e.target.value })}
                  >
                    <option value="">Select column</option>
                    {(selectedDataset.columns || []).map((c) => (
                      <option key={c} value={c}>{c}</option>
                    ))}
                  </select>
                </label>
              ))}
            </div>

            <div className="admin-preview-actions-v37">
              <button onClick={() => setStatus("Mapping saved locally for this admin session.")}>
                Save Mapping
              </button>
              <button onClick={() => window.location.reload()}>
                Open Map Preview
              </button>
            </div>

            <div className="admin-preview-table-wrap-v37">
              <table className="admin-preview-table-v37">
                <thead>
                  <tr>
                    {(selectedDataset.columns || []).map((c) => (
                      <th key={c}>{c}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {(selectedDataset.previewRows || []).map((row, i) => (
                    <tr key={i}>
                      {(selectedDataset.columns || []).map((c) => (
                        <td key={c}>{row[c]}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </section>
      )}

      <section className="admin-note-v35">
        <strong>Important:</strong> Published datasets feed the map through
        <code> /public/map-data.csv </code>. Keep simulated or unverified sources clearly labeled.
      </section>
    </main>
  );
}

'''

s = s[:start] + new_admin + s[end:]
p.write_text(s, encoding="utf-8")
print("✅ AdminPanel rebuilt cleanly.")
