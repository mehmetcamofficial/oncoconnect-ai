from pathlib import Path

p = Path("frontend/src/App.jsx")
s = p.read_text(encoding="utf-8")

old_sources = '''{adminTab === "sources" && (
        <section className="admin-panel-placeholder-v38">
          <small>SOURCES</small>
          <h2>Source governance</h2>
          <p>
            Use source name and source URL fields to label every dataset. Distinguish official,
            estimated, simulated and unverified data before publishing.
          </p>
        </section>
      )}'''

new_sources = '''{adminTab === "sources" && (
        <section className="admin-panel-placeholder-v38">
          <small>SOURCES</small>
          <h2>Source governance</h2>
          <p>
            Use source name and source URL fields to label every dataset. Distinguish official,
            estimated, simulated and unverified data before publishing.
          </p>

          <div className="admin-tab-actions-v39">
            <button onClick={() => setAdminTab("datasets")}>Manage source labels</button>
            <button onClick={() => window.open("http://localhost:5050/public/map-data.csv", "_blank")}>
              Open published CSV
            </button>
            <button onClick={loadDatasets}>Reload datasets</button>
          </div>
        </section>
      )}'''

old_automation = '''{adminTab === "automation" && (
        <section className="admin-panel-placeholder-v38">
          <small>AUTO SYNC</small>
          <h2>Automated data sync roadmap</h2>
          <p>
            Next step: add connectors for GLOBOCAN, ECIS or manually approved national registry files.
            Auto-sync should write to draft datasets first, never directly publish.
          </p>
        </section>
      )}'''

new_automation = '''{adminTab === "automation" && (
        <section className="admin-panel-placeholder-v38">
          <small>AUTO SYNC</small>
          <h2>Automated data sync roadmap</h2>
          <p>
            Next step: add connectors for GLOBOCAN, ECIS or manually approved national registry files.
            Auto-sync should write to draft datasets first, never directly publish.
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
              <span>New external data lands as draft, not public.</span>
            </div>
            <div>
              <strong>2. Admin review</strong>
              <span>Quality flag and source URL must be checked.</span>
            </div>
            <div>
              <strong>3. Publish</strong>
              <span>Only approved datasets feed the public map.</span>
            </div>
          </div>
        </section>
      )}'''

old_settings = '''{adminTab === "settings" && (
        <section className="admin-panel-placeholder-v38">
          <small>SETTINGS</small>
          <h2>Admin settings</h2>
          <p>
            Configure default language, quality labels, upload limits and map visibility rules.
            Passwords should later move to environment variables.
          </p>
        </section>
      )}'''

new_settings = '''{adminTab === "settings" && (
        <section className="admin-panel-placeholder-v38">
          <small>SETTINGS</small>
          <h2>Admin settings</h2>
          <p>
            Configure default language, quality labels, upload limits and map visibility rules.
            Passwords should later move to environment variables.
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
      )}'''

changed = False

for old, new in [
    (old_sources, new_sources),
    (old_automation, new_automation),
    (old_settings, new_settings),
]:
    if old in s:
        s = s.replace(old, new, 1)
        changed = True

if not changed:
    raise RuntimeError("Could not find source/automation/settings blocks. AdminPanel may differ.")

p.write_text(s, encoding="utf-8")
print("✅ Step 39 applied: buttons added to Sources, Automation and Settings tabs.")
