from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

if "const LandingDataDashboard" not in s:
    insert_at = s.find("  const LandingPage")
    if insert_at == -1:
        raise SystemExit("❌ LandingPage bulunamadı.")

    component = r'''
  const LandingDataDashboard = () => (
    <section className="landing-data-lab-force">
      <div className="landing-data-head-force">
        <p>LIVE CANCER DATA LAB</p>
        <h2>Interactive cancer burden explorer</h2>
        <span>
          Filter cancer indicators by metric, sex, age group and cancer type. This area is designed
          for the landing page so users can immediately understand case, death and survival patterns.
        </span>
      </div>

      <div className="landing-data-filters-force">
        <label><span>Metric</span><select><option>New cases</option><option>Deaths</option><option>5-year survival</option></select></label>
        <label><span>Sex</span><select><option>All</option><option>Erkek</option><option>Kadın</option></select></label>
        <label><span>Age group</span><select><option>All</option><option>0-29</option><option>30-49</option><option>50-69</option><option>70+</option></select></label>
        <label><span>Cancer type</span><select><option>All</option><option>Akciğer</option><option>Meme</option><option>Kolorektal</option><option>Prostat</option></select></label>
      </div>

      <div className="landing-data-kpis-force">
        <div className="blue"><small>Türkiye, 2022</small><strong>240,013</strong><b>new cases</b></div>
        <div className="orange"><small>Türkiye, 2022</small><strong>129,672</strong><b>deaths</b></div>
        <div className="green"><small>Türkiye, 2022</small><strong>67%</strong><b>5-year survival signal</b></div>
      </div>

      <div className="landing-data-chart-force">
        {[
          ["Lung", 92],
          ["Breast", 74],
          ["Colorectum", 61],
          ["Prostate", 48],
          ["Stomach", 39]
        ].map(([name, value]) => (
          <div className="landing-data-bar-force" key={name}>
            <div><b>{name}</b><span>{value} burden index</span></div>
            <i style={{ width: `${value}%` }}></i>
          </div>
        ))}
      </div>
    </section>
  );


'''
    s = s[:insert_at] + component + s[insert_at:]

# LandingPage içine component çağrısı ekle
if "<LandingDataDashboard />" not in s:
    lp_start = s.find("  const LandingPage")
    next_const = s.find("\n  const ", lp_start + 5)

    if lp_start == -1 or next_const == -1:
        raise SystemExit("❌ LandingPage sınırı bulunamadı.")

    landing_block = s[lp_start:next_const]

    # LandingPage içindeki son kapanan section/div öncesine ekle
    pos = landing_block.rfind("</section>")
    if pos == -1:
        pos = landing_block.rfind("</div>")
    if pos == -1:
        raise SystemExit("❌ LandingPage içinde ekleme noktası bulunamadı.")

    landing_block = landing_block[:pos+10] + "\n        <LandingDataDashboard />" + landing_block[pos+10:]
    s = s[:lp_start] + landing_block + s[next_const:]

app.write_text(s, encoding="utf-8")

css_patch = r'''

/* FORCE landing data dashboard */

.landing-data-lab-force {
  padding: 80px 5vw;
  background: #f5f8fc;
}

.landing-data-head-force p {
  color: #155eef;
  font-weight: 950;
  letter-spacing: 0.25em;
}

.landing-data-head-force h2 {
  margin: 10px 0;
  font-size: clamp(42px, 5vw, 76px);
  line-height: 1;
  letter-spacing: -0.06em;
  color: #101828;
}

.landing-data-head-force span {
  display: block;
  max-width: 1000px;
  color: #475467;
  font-size: 20px;
  line-height: 1.6;
  font-weight: 700;
}

.landing-data-filters-force {
  margin-top: 30px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}

.landing-data-filters-force label {
  display: grid;
  gap: 8px;
  padding: 18px;
  border-radius: 24px;
  background: white;
  border: 1px solid #e5e7eb;
  box-shadow: 0 18px 50px rgba(15,23,42,0.08);
}

.landing-data-filters-force span {
  color: #155eef;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.16em;
}

.landing-data-filters-force select {
  border: 0;
  background: #f8fafc;
  border-radius: 16px;
  padding: 14px;
  font-weight: 900;
  color: #101828;
}

.landing-data-kpis-force {
  margin-top: 28px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.landing-data-kpis-force div {
  min-height: 190px;
  padding: 30px;
  border-radius: 30px;
  color: white;
  box-shadow: 0 24px 70px rgba(15,23,42,0.16);
}

.landing-data-kpis-force .blue { background: linear-gradient(135deg, #0f2f80, #2563eb); }
.landing-data-kpis-force .orange { background: linear-gradient(135deg, #9a3412, #ea580c); }
.landing-data-kpis-force .green { background: linear-gradient(135deg, #047857, #14b8a6); }

.landing-data-kpis-force small {
  font-weight: 900;
  opacity: 0.85;
}

.landing-data-kpis-force strong {
  display: block;
  margin: 18px 0 6px;
  font-size: clamp(48px, 5vw, 76px);
  line-height: 1;
  letter-spacing: -0.06em;
}

.landing-data-kpis-force b {
  font-size: 20px;
}

.landing-data-chart-force {
  margin-top: 28px;
  padding: 30px;
  border-radius: 30px;
  background: white;
  border: 1px solid #e5e7eb;
  box-shadow: 0 22px 70px rgba(15,23,42,0.08);
}

.landing-data-bar-force {
  margin-bottom: 22px;
}

.landing-data-bar-force div {
  display: flex;
  justify-content: space-between;
  margin-bottom: 9px;
  color: #101828;
  font-weight: 900;
}

.landing-data-bar-force span {
  color: #667085;
}

.landing-data-bar-force i {
  display: block;
  height: 14px;
  border-radius: 999px;
  background: linear-gradient(90deg, #155eef, #14b8a6);
}

@media (max-width: 1000px) {
  .landing-data-filters-force,
  .landing-data-kpis-force {
    grid-template-columns: 1fr;
  }
}

'''

css.write_text(css.read_text(encoding="utf-8") + css_patch, encoding="utf-8")

print("✅ LandingDataDashboard force-added.")
