from pathlib import Path

p = Path("frontend/src/App.jsx")
cssp = Path("frontend/src/App.css")

s = p.read_text(encoding="utf-8")
css = cssp.read_text(encoding="utf-8")

# AdminPanel state ekleri
target = '  const [loading, setLoading] = React.useState(false);\n'
insert = '''  const [selectedDataset, setSelectedDataset] = React.useState(null);
  const [mapping, setMapping] = React.useState({});
'''
if "selectedDataset" not in s:
    s = s.replace(target, target + insert, 1)

# Detail loader fonksiyonu
api_target = '  async function loadDatasets() {\n'
detail_fn = r'''
  async function openDatasetDetail(id) {
    setLoading(true);
    try {
      const res = await fetch(`${API}/admin/datasets/${id}`);
      const data = await res.json();

      if (!data.success) {
        setStatus(data.error || "Could not load dataset detail.");
        return;
      }

      setSelectedDataset(data.dataset);

      const cols = data.dataset.columns || [];
      const autoMap = {
        region: cols.find(c => c.toLowerCase().includes("bolge")) || "",
        location: cols.find(c => c.toLowerCase().includes("ulke") || c.toLowerCase().includes("sehir")) || "",
        sex: cols.find(c => c.toLowerCase().includes("cinsiyet")) || "",
        cancerType: cols.find(c => c.toLowerCase().includes("kanser")) || "",
        ageGroup: cols.find(c => c.toLowerCase().includes("yas")) || "",
        incidence: cols.find(c => c.toLowerCase().includes("vaka")) || "",
        mortality: cols.find(c => c.toLowerCase().includes("olum")) || "",
        survival: cols.find(c => c.toLowerCase().includes("sagkalim")) || ""
      };

      setMapping(autoMap);
    } catch {
      setStatus("Dataset detail failed. Check backend endpoint.");
    } finally {
      setLoading(false);
    }
  }

'''
if "openDatasetDetail" not in s:
    s = s.replace(api_target, detail_fn + api_target, 1)

# Dataset row actions içine Preview butonu ekle
old = '''<button onClick={() => updateDataset(d.id, { published: true })}>
                  Publish
                </button>'''
new = '''<button onClick={() => openDatasetDetail(d.id)}>
                  Preview
                </button>
                <button onClick={() => updateDataset(d.id, { published: true })}>
                  Publish
                </button>'''
if "openDatasetDetail(d.id)" not in s:
    s = s.replace(old, new, 1)

# Source URL input ekle: sourceName inputundan sonra
old_source = '''<input
                  defaultValue={d.sourceName || ""}
                  placeholder="source name"
                  onBlur={(e) => updateDataset(d.id, { sourceName: e.target.value })}
                />'''
new_source = '''<input
                  defaultValue={d.sourceName || ""}
                  placeholder="source name"
                  onBlur={(e) => updateDataset(d.id, { sourceName: e.target.value })}
                />
                <input
                  defaultValue={d.sourceUrl || ""}
                  placeholder="source URL"
                  onBlur={(e) => updateDataset(d.id, { sourceUrl: e.target.value })}
                />'''
if 'placeholder="source URL"' not in s:
    s = s.replace(old_source, new_source, 1)

# Modal ekle: admin-note öncesine
modal_marker = '''      <section className="admin-note-v35">'''
modal = r'''
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
                    onChange={(e) =>
                      setMapping({ ...mapping, [key]: e.target.value })
                    }
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
              <button
                onClick={() => {
                  setStatus("Mapping saved locally for this admin session.");
                }}
              >
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

'''
if "admin-preview-overlay-v37" not in s:
    s = s.replace(modal_marker, modal + modal_marker, 1)

p.write_text(s, encoding="utf-8")

css += r'''

/* Step 37 Admin Preview + Mapping */

.admin-preview-overlay-v37 {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: rgba(15, 23, 42, .52);
  backdrop-filter: blur(10px);
  display: grid;
  place-items: center;
  padding: 28px;
}

.admin-preview-modal-v37 {
  width: min(1280px, 96vw);
  max-height: 88vh;
  overflow: auto;
  border-radius: 34px;
  background: #ffffff;
  box-shadow: 0 40px 120px rgba(15,23,42,.35);
  border: 1px solid #dbeafe;
  padding: 28px;
}

.admin-preview-head-v37 {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  align-items: flex-start;
  margin-bottom: 22px;
}

.admin-preview-head-v37 small,
.admin-mapping-v37 small {
  letter-spacing: .15em;
  color: #64748b;
  font-weight: 950;
}

.admin-preview-head-v37 h2 {
  margin: 6px 0;
  font-size: 34px;
  color: #0f172a;
}

.admin-preview-head-v37 p,
.admin-mapping-v37 p {
  margin: 0;
  color: #64748b;
  font-weight: 800;
}

.admin-preview-head-v37 button,
.admin-preview-actions-v37 button {
  border: none;
  border-radius: 999px;
  padding: 12px 16px;
  background: #0f172a;
  color: white;
  font-weight: 950;
  cursor: pointer;
}

.admin-mapping-v37 {
  display: grid;
  grid-template-columns: 1.4fr repeat(4, 1fr);
  gap: 14px;
  padding: 20px;
  border-radius: 28px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  margin-bottom: 18px;
}

.admin-mapping-v37 h3 {
  margin: 6px 0;
  font-size: 24px;
}

.admin-mapping-v37 label {
  display: grid;
  gap: 7px;
}

.admin-mapping-v37 label span {
  font-size: 13px;
  font-weight: 950;
  color: #334155;
}

.admin-mapping-v37 select {
  width: 100%;
  border: 1px solid #cbd5e1;
  border-radius: 14px;
  padding: 11px;
  background: white;
  font-weight: 850;
}

.admin-preview-actions-v37 {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  margin-bottom: 16px;
}

.admin-preview-actions-v37 button:first-child {
  background: #2563eb;
}

.admin-preview-actions-v37 button:last-child {
  background: #16a34a;
}

.admin-preview-table-wrap-v37 {
  overflow: auto;
  border-radius: 24px;
  border: 1px solid #e2e8f0;
  max-height: 420px;
}

.admin-preview-table-v37 {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}

.admin-preview-table-v37 th {
  position: sticky;
  top: 0;
  background: #0f172a;
  color: white;
  text-align: left;
  padding: 12px;
  white-space: nowrap;
}

.admin-preview-table-v37 td {
  padding: 10px 12px;
  border-bottom: 1px solid #e2e8f0;
  white-space: nowrap;
  color: #334155;
  font-weight: 700;
}

.admin-preview-table-v37 tr:nth-child(even) td {
  background: #f8fafc;
}

@media (max-width: 1000px) {
  .admin-mapping-v37 {
    grid-template-columns: 1fr;
  }
}
'''

cssp.write_text(css, encoding="utf-8")
print("✅ Step 37 applied: admin dataset preview, source URL and column mapping UI added.")
