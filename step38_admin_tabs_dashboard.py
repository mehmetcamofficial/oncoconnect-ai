from pathlib import Path

p = Path("frontend/src/App.jsx")
cssp = Path("frontend/src/App.css")

s = p.read_text(encoding="utf-8")
css = cssp.read_text(encoding="utf-8")

# active tab state
state_target = '  const [mapping, setMapping] = React.useState({});\n'
state_insert = '  const [adminTab, setAdminTab] = React.useState("overview");\n'
if "adminTab" not in s:
    s = s.replace(state_target, state_target + state_insert, 1)

# hero sonrasına tabs + overview cards
hero_end = '''      </section>

      <section className="admin-upload-v35">'''
tabs_block = r'''      </section>

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

      {adminTab === "overview" && (
        <section className="admin-overview-grid-v38">
          <div className="admin-kpi-v38">
            <small>Total datasets</small>
            <strong>{datasets.length}</strong>
            <p>Uploaded data layers in admin storage.</p>
          </div>
          <div className="admin-kpi-v38">
            <small>Published layers</small>
            <strong>{datasets.filter((d) => d.published).length}</strong>
            <p>Visible on public map endpoints.</p>
          </div>
          <div className="admin-kpi-v38">
            <small>Total rows</small>
            <strong>{datasets.reduce((sum, d) => sum + Number(d.rowCount || 0), 0).toLocaleString()}</strong>
            <p>Rows available across uploaded datasets.</p>
          </div>
          <div className="admin-kpi-v38 accent">
            <small>Data status</small>
            <strong>{datasets.some((d) => d.qualityFlag === "needs_verification") ? "Review" : "Ready"}</strong>
            <p>Keep unverified sources clearly labeled.</p>
          </div>
        </section>
      )}

      {adminTab === "overview" && (
        <section className="admin-command-grid-v38">
          <button onClick={() => setAdminTab("datasets")}>Manage datasets</button>
          <button onClick={() => setAdminTab("mapping")}>Open mapping tools</button>
          <button onClick={() => window.location.reload()}>Open public map preview</button>
        </section>
      )}

      {adminTab === "datasets" && (
        <section className="admin-upload-v35">'''
if "admin-tabs-v38" not in s:
    s = s.replace(hero_end, tabs_block, 1)

# upload section kapanışından sonra datasets section zaten geliyor; datasets tab içine almak için datasets section sonuna kapanış ekle
datasets_note_marker = '''      <section className="admin-note-v35">'''
if '{adminTab === "mapping" && (' not in s:
    replacement = r'''      </section>
      )}

      {adminTab === "mapping" && (
        <section className="admin-panel-placeholder-v38">
          <small>PREVIEW & MAPPING</small>
          <h2>Dataset preview and field mapping</h2>
          <p>
            Select <strong>Datasets</strong>, then click <strong>Preview</strong> on a dataset row.
            The preview modal will open with the first 20 rows and automatic column suggestions.
          </p>
          <button onClick={() => setAdminTab("datasets")}>Go to datasets</button>
        </section>
      )}

      {adminTab === "sources" && (
        <section className="admin-panel-placeholder-v38">
          <small>SOURCES</small>
          <h2>Source governance</h2>
          <p>
            Use source name and source URL fields to label every dataset. This is important because
            the cancer map should clearly distinguish official, estimated, simulated and unverified data.
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

'''
    s = s.replace(datasets_note_marker, replacement + datasets_note_marker, 1)

# admin note sadece overview/settings gibi genel dursun
s = s.replace(
    '<section className="admin-note-v35">',
    '<section className="admin-note-v35">'
)

p.write_text(s, encoding="utf-8")

css += r'''

/* Step 38 Admin Dashboard Tabs */

.admin-tabs-v38 {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin: 24px 0;
  padding: 10px;
  border-radius: 999px;
  background: rgba(255,255,255,.78);
  border: 1px solid #dbeafe;
  box-shadow: 0 18px 45px rgba(15,23,42,.08);
}

.admin-tabs-v38 button {
  border: none;
  border-radius: 999px;
  padding: 13px 18px;
  background: transparent;
  color: #475569;
  font-weight: 950;
  cursor: pointer;
  transition: all .2s ease;
}

.admin-tabs-v38 button:hover {
  background: #eff6ff;
  color: #1d4ed8;
}

.admin-tabs-v38 button.active {
  background: linear-gradient(135deg, #2563eb, #7c3aed);
  color: white;
  box-shadow: 0 14px 32px rgba(37,99,235,.24);
}

.admin-overview-grid-v38 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-bottom: 22px;
}

.admin-kpi-v38 {
  padding: 24px;
  border-radius: 28px;
  background: white;
  border: 1px solid #dbeafe;
  box-shadow: 0 20px 55px rgba(15,23,42,.08);
}

.admin-kpi-v38 small,
.admin-panel-placeholder-v38 small {
  letter-spacing: .14em;
  color: #64748b;
  font-weight: 950;
}

.admin-kpi-v38 strong {
  display: block;
  margin: 10px 0;
  font-size: 46px;
  line-height: 1;
  color: #0f172a;
}

.admin-kpi-v38 p,
.admin-panel-placeholder-v38 p {
  color: #64748b;
  font-weight: 800;
  line-height: 1.5;
}

.admin-kpi-v38.accent {
  background: linear-gradient(135deg, #0f172a, #2563eb);
  color: white;
}

.admin-kpi-v38.accent small,
.admin-kpi-v38.accent strong,
.admin-kpi-v38.accent p {
  color: white;
}

.admin-command-grid-v38 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  margin-bottom: 24px;
}

.admin-command-grid-v38 button,
.admin-panel-placeholder-v38 button {
  border: none;
  border-radius: 24px;
  padding: 22px;
  background: #0f172a;
  color: white;
  font-weight: 950;
  font-size: 18px;
  cursor: pointer;
  box-shadow: 0 18px 45px rgba(15,23,42,.14);
}

.admin-command-grid-v38 button:nth-child(2) {
  background: #2563eb;
}

.admin-command-grid-v38 button:nth-child(3) {
  background: #16a34a;
}

.admin-panel-placeholder-v38 {
  padding: 34px;
  border-radius: 34px;
  background: white;
  border: 1px solid #dbeafe;
  box-shadow: 0 24px 70px rgba(15,23,42,.08);
  margin-bottom: 24px;
}

.admin-panel-placeholder-v38 h2 {
  margin: 8px 0;
  font-size: 36px;
  color: #0f172a;
}

@media (max-width: 1100px) {
  .admin-overview-grid-v38,
  .admin-command-grid-v38 {
    grid-template-columns: 1fr;
  }

  .admin-tabs-v38 {
    border-radius: 24px;
  }
}
'''

cssp.write_text(css, encoding="utf-8")
print("✅ Step 38 applied: admin dashboard tabs and overview added.")

