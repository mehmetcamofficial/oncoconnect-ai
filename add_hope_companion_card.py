from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

target = "Guidance with warmth, not fear."

card = r'''
            <div className="hope-companion-card">
              <div className="hope-companion-image"></div>
              <div className="hope-companion-copy">
                <span>Hope companion</span>
                <h3>Small moments of courage matter.</h3>
                <p>A warm, hopeful support space for children, families and care teams.</p>
              </div>
            </div>
'''

if "hope-companion-card" not in s:
    idx = s.find(target)
    if idx == -1:
        raise SystemExit("❌ Guidance text bulunamadı.")
    insert_at = s.find("</", idx)
    insert_at = s.find(">", insert_at) + 1
    s = s[:insert_at] + "\n" + card + s[insert_at:]

app.write_text(s, encoding="utf-8")

patch = r'''

/* Hope Companion mini card */
.hope-companion-card {
  margin-top: 24px;
  display: grid;
  grid-template-columns: 150px 1fr;
  gap: 18px;
  align-items: center;
  padding: 16px;
  border-radius: 28px;
  background: rgba(255,255,255,0.22);
  border: 1px solid rgba(255,255,255,0.38);
  backdrop-filter: blur(18px);
  box-shadow: 0 22px 60px rgba(15,23,42,0.16);
}

.hope-companion-image {
  height: 130px;
  border-radius: 24px;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.12)),
    url("/assets/hope-child-sunrise.png") center / cover no-repeat;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.24);
}

.hope-companion-copy span {
  color: #a5f3fc;
  font-weight: 950;
  letter-spacing: .14em;
  text-transform: uppercase;
  font-size: 12px;
}

.hope-companion-copy h3 {
  margin: 8px 0 6px;
  color: white;
  font-size: 24px;
  line-height: 1.1;
}

.hope-companion-copy p {
  margin: 0;
  color: rgba(255,255,255,0.82);
  font-size: 15px;
  line-height: 1.45;
  font-weight: 700;
}

@media (max-width: 700px) {
  .hope-companion-card {
    grid-template-columns: 1fr;
  }

  .hope-companion-image {
    height: 190px;
  }
}

'''

text = css.read_text(encoding="utf-8")
if "Hope Companion mini card" not in text:
    css.write_text(text + patch, encoding="utf-8")

print("✅ Hope Companion mini card added.")
