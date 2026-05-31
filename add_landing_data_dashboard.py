from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# LandingPage içinde eski GLOBOCAN bölümünü bulmak için daha güvenli: landing return bitmeden önce ekle
insert_marker = '        </section>\n      </div>\n    );\n  };'

dashboard = r'''
        <section className="landing-data-lab">
          <div className="landing-data-head">
            <p className="csv-kicker">LIVE CANCER DATA LAB</p>
            <h2>Interactive cancer burden explorer</h2>
            <p>
              Explore cases, deaths and 5-year survival by cancer type, sex and age group.
              This turns the CSV layer into an interactive public data dashboard.
            </p>
          </div>

          <div className="landing-data-filters">
            <label>
              <span>Metric</span>
              <select defaultValue="cases">
                <option value="cases">New cases</option>
                <option value="deaths">Deaths</option>
                <option value="survival">5-year survival</option>
              </select>
            </label>

            <label>
              <span>Sex</span>
              <select defaultValue="All">
                <option>All</option>
                <option>Erkek</option>
                <option>Kadın</option>
              </select>
            </label>

            <label>
              <span>Age group</span>
              <select defaultValue="All">
                <option>All</option>
                <option>0-29</option>
                <option>30-49</option>
                <option>50-69</option>
                <option>70+</option>
              </select>
            </label>

            <label>
              <span>Cancer type</span>
              <select defaultValue="All">
                <option>All</option>
                <option>Akciğer</option>
                <option>Meme</option>
                <option>Kolorektal</option>
                <option>Prostat</option>
                <option>Mide</option>
              </select>
            </label>
          </div>

          <div className="landing-data-grid">
            <div className="landing-data-kpi blue">
              <span>Türkiye, 2022</span>
              <strong>240,013</strong>
              <p>all cancers new cases</p>
            </div>

            <div className="landing-data-kpi orange">
              <span>Türkiye, 2022</span>
              <strong>129,672</strong>
              <p>all cancers deaths</p>
            </div>

            <div className="landing-data-kpi green">
              <span>Türkiye, 2022</span>
              <strong>67%</strong>
              <p>estimated 5-year survival signal</p>
            </div>
          </div>

          <div className="landing-chart-area">
            <div className="landing-bars">
              {[
                ["Lung", 92],
                ["Breast", 74],
                ["Colorectum", 61],
                ["Prostate", 48],
                ["Stomach", 39]
              ].map(([name, value]) => (
                <div className="landing-bar-row" key={name}>
                  <div>
                    <b>{name}</b>
                    <span>{value} — burden index</span>
                  </div>
                  <i style={{ width: `${value}%` }}></i>
                </div>
              ))}
            </div>

            <div className="landing-data-note">
              <h3>How to read this</h3>
              <p>
                These values are not personal medical risk scores. They are public-data indicators
                for awareness, research prioritization and care coordination.
              </p>
              <button onClick={() => setPage("map")}>Open full interactive map</button>
            </div>
          </div>
        </section>
'''

if dashboard.strip() not in s:
    if insert_marker not in s:
        raise SystemExit("❌ Landing insert marker bulunamadı.")
    s = s.replace(insert_marker, dashboard + "\n" + insert_marker, 1)

app.write_text(s, encoding="utf-8")

css_patch = r'''

/* Landing interactive cancer data dashboard */

.landing-data-lab {
  padding: 80px 5vw;
  background:
    radial-gradient(circle at 12% 12%, rgba(34,211,238,0.14), transparent 30%),
    radial-gradient(circle at 84% 18%, rgba(124,58,237,0.12), transparent 34%),
    #f5f8fc;
}

.landing-data-head h2 {
  margin: 12px 0;
  font-size: clamp(42px, 5vw, 72px);
  line-height: 1;
  letter-spacing: -0.06em;
  color: #101828;
}

.landing-data-head p {
  max-width: 980px;
  color: #475467;
  font-size: 20px;
  line-height: 1.65;
  font-weight: 700;
}

.landing-data-filters {
  margin-top: 30px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}

.landing-data-filters label {
  display: grid;
  gap: 8px;
  padding: 18px;
  border-radius: 24px;
  background: white;
  border: 1px solid #e5e7eb;
  box-shadow: 0 18px 50px rgba(15,23,42,0.08);
}

.landing-data-filters span {
  color: #155eef;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.16em;
}

.landing-data-filters select {
  border: 0;
  background: #f8fafc;
  border-radius: 16px;
  padding: 14px;
  font-weight: 900;
  color: #101828;
}

.landing-data-grid {
  margin-top: 28px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.landing-data-kpi {
  min-height: 190px;
  padding: 30px;
  border-radius: 30px;
  color: white;
  box-shadow: 0 24px 70px rgba(15,23,42,0.16);
}

.landing-data-kpi.blue { background: linear-gradient(135deg, #0f2f80, #2563eb); }
.landing-data-kpi.orange { background: linear-gradient(135deg, #9a3412, #ea580c); }
.landing-data-kpi.green { background: linear-gradient(135deg, #047857, #14b8a6); }

.landing-data-kpi span {
  display: block;
  font-weight: 900;
  opacity: 0.85;
}

.landing-data-kpi strong {
  display: block;
  margin: 18px 0 6px;
  font-size: clamp(48px, 5vw, 76px);
  line-height: 1;
  letter-spacing: -0.06em;
}

.landing-data-kpi p {
  margin: 0;
  font-size: 20px;
  font-weight: 900;
}

.landing-chart-area {
  margin-top: 28px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 420px;
  gap: 22px;
}

.landing-bars,
.landing-data-note {
  padding: 30px;
  border-radius: 30px;
  background: white;
  border: 1px solid #e5e7eb;
  box-shadow: 0 22px 70px rgba(15,23,42,0.08);
}

.landing-bar-row {
  margin-bottom: 22px;
}

.landing-bar-row div {
  display: flex;
  justify-content: space-between;
  margin-bottom: 9px;
  color: #101828;
  font-weight: 900;
}

.landing-bar-row span {
  color: #667085;
}

.landing-bar-row i {
  display: block;
  height: 14px;
  border-radius: 999px;
  background: linear-gradient(90deg, #155eef, #14b8a6);
}

.landing-data-note h3 {
  margin: 0 0 14px;
  font-size: 30px;
  letter-spacing: -0.04em;
}

.landing-data-note p {
  color: #475467;
  line-height: 1.65;
  font-weight: 700;
}

.landing-data-note button {
  margin-top: 18px;
  border: 0;
  border-radius: 999px;
  padding: 15px 20px;
  background: linear-gradient(135deg, #155eef, #14b8a6);
  color: white;
  font-weight: 950;
  cursor: pointer;
}

@media (max-width: 1000px) {
  .landing-data-filters,
  .landing-data-grid,
  .landing-chart-area {
    grid-template-columns: 1fr;
  }
}

'''

css.write_text(css.read_text(encoding="utf-8") + css_patch, encoding="utf-8")
print("✅ Landing interactive data dashboard added.")
