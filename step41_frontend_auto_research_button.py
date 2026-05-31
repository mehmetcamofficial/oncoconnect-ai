from pathlib import Path

p = Path("frontend/src/App.jsx")
s = p.read_text(encoding="utf-8")

anchor = '''  async function openDatasetDetail(id) {'''

fn = r'''
  async function runAutoResearch() {
    setLoading(true);
    setStatus("Auto Research Agent is scanning trusted cancer data sources...");

    try {
      const res = await fetch(`${API}/admin/auto-research`, {
        method: "POST"
      });

      const data = await res.json();

      if (!data.success) {
        setStatus(data.error || "Auto research failed.");
        return;
      }

      setStatus("Auto research completed. Draft dataset created for admin review.");
      await loadDatasets();
      setAdminTab("datasets");
    } catch {
      setStatus("Auto research failed. Check backend.");
    } finally {
      setLoading(false);
    }
  }

'''

if "runAutoResearch" not in s:
    if anchor not in s:
        raise SystemExit("❌ openDatasetDetail function bulunamadı.")
    s = s.replace(anchor, fn + anchor, 1)

old = r'''          <div className="admin-tab-actions-v39">
            <button onClick={() => window.open("http://localhost:5050/public/map-data", "_blank")}>
              Check public JSON
            </button>
            <button onClick={() => window.open("http://localhost:5050/public/map-data.csv", "_blank")}>
              Check public CSV
            </button>
            <button onClick={() => setAdminTab("datasets")}>
              Import manual dataset
            </button>
          </div>'''

new = r'''          <div className="admin-tab-actions-v39">
            <button onClick={runAutoResearch}>
              Auto Research & Integrate
            </button>
            <button onClick={() => window.open("http://localhost:5050/public/map-data", "_blank")}>
              Check public JSON
            </button>
            <button onClick={() => window.open("http://localhost:5050/public/map-data.csv", "_blank")}>
              Check public CSV
            </button>
            <button onClick={() => setAdminTab("datasets")}>
              Import manual dataset
            </button>
          </div>'''

if "Auto Research & Integrate" not in s:
    if old not in s:
        raise SystemExit("❌ Automation button block bulunamadı. Önce Step 39 butonlarının App.jsx içinde görünmesi gerekiyor.")
    s = s.replace(old, new, 1)

p.write_text(s, encoding="utf-8")
print("✅ Auto Research button added to Automation tab.")
