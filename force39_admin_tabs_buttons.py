from pathlib import Path

p = Path("frontend/src/App.jsx")
s = p.read_text(encoding="utf-8")

sources_start = s.find('{adminTab === "sources" && (')
automation_start = s.find('{adminTab === "automation" && (')
settings_start = s.find('{adminTab === "settings" && (')
selected_start = s.find('{selectedDataset && (')

if sources_start == -1 or automation_start == -1 or settings_start == -1 or selected_start == -1:
    raise RuntimeError("Admin tab blokları bulunamadı.")

new_tabs = r'''{adminTab === "sources" && (
        <section className="admin-panel-placeholder-v38">
          <small>SOURCES</small>
          <h2>Source governance</h2>
          <p>
            Manage source names, source URLs and verification labels before publishing data to the map.
          </p>

          <div className="admin-tab-actions-v39">
            <button onClick={() => setAdminTab("datasets")}>Manage source labels</button>
            <button onClick={() => window.open("http://localhost:5050/public/map-data.csv", "_blank")}>
              Open published CSV
            </button>
            <button onClick={loadDatasets}>Reload datasets</button>
          </div>
        </section>
      )}

      {adminTab === "automation" && (
        <section className="admin-panel-placeholder-v38">
          <small>AUTO SYNC</small>
          <h2>Automated data sync roadmap</h2>
          <p>
            External sources should enter the system as draft datasets first. Admin review is required before publishing.
          </p>

          <div className="admin-tab-actions-v39">
            <button onClick={() => window.open("http://localhost:5050/public/map-data", "_blank")}>
              Check public JSON
            </button>
            <button onClick={() => window.open("http://localhost:5050/public/map-data.csv", "_blank")}>
              Check public CSV
            </button>
            <button onClick={() => setAdminTab("datasets")}>
              Import manual dataset
            </button>
          </div>

          <div className="admin-roadmap-v39">
            <div>
              <strong>1. Draft sync</strong>
              <span>New external data lands as draft.</span>
            </div>
            <div>
              <strong>2. Admin review</strong>
              <span>Quality flag and source URL are checked.</span>
            </div>
            <div>
              <strong>3. Publish</strong>
              <span>Only approved layers feed the public map.</span>
            </div>
          </div>
        </section>
      )}

      {adminTab === "settings" && (
        <section className="admin-panel-placeholder-v38">
          <small>SETTINGS</small>
          <h2>Admin settings</h2>
          <p>
            Manage admin session, backend status and map endpoint visibility.
          </p>

          <div className="admin-settings-grid-v39">
            <div>
              <strong>Current admin mode</strong>
              <span>Demo login with local session</span>
            </div>
            <div>
              <strong>Backend</strong>
              <span>http://localhost:5050</span>
            </div>
            <div>
              <strong>Map data endpoint</strong>
              <span>/public/map-data.csv</span>
            </div>
          </div>

          <div className="admin-tab-actions-v39">
            <button onClick={logout}>Logout</button>
            <button
              onClick={() => {
                localStorage.removeItem("admin-auth");
                window.location.reload();
              }}
            >
              Clear session
            </button>
            <button onClick={() => window.location.reload()}>
              Back Home
            </button>
          </div>
        </section>
      )}

      '''

s = s[:sources_start] + new_tabs + s[selected_start:]

p.write_text(s, encoding="utf-8")
print("✅ Force Step 39 applied.")
