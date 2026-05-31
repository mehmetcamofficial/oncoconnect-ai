from pathlib import Path

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# 1) Calm card içine direkt companion ekle
if "landing-companion-child-v31" not in app:
    target = "Calm, clear and safe guidance"
    idx = app.find(target)
    if idx == -1:
        print("⚠️ Calm card text bulunamadı")
    else:
        # Bu başlıktan sonraki paragraf kapanışından sonra eklemeye çalış
        insert_at = app.find("</p>", idx)
        if insert_at != -1:
            insert_at += len("</p>")
            app = app[:insert_at] + '''
              <div className="landing-companion-child-v31">
                <div className="child-face-v31">😊</div>
                <div>
                  <strong>Safe companion</strong>
                  <span>Guidance with warmth, not fear.</span>
                </div>
              </div>
''' + app[insert_at:]
            print("✅ Calm card companion inserted")

# 2) How it works sonrası interaktif simülasyon paneli ekle
if "how-simulation-v31" not in app:
    target = "A safe path from information to action"
    idx = app.find(target)
    if idx == -1:
        print("⚠️ How it works title bulunamadı")
    else:
        # 4. kart metninden sonra eklemek için Splunk metnini bul
        end_text = "Support teams monitor high-risk cases in dashboards."
        end_idx = app.find(end_text, idx)
        if end_idx != -1:
            insert_at = app.find("</div>", end_idx)
            insert_at = app.find("</div>", insert_at + 6)
            if insert_at != -1:
                insert_at += len("</div>")
                app = app[:insert_at] + '''
              <div className="how-simulation-v31">
                <div className="sim-node active">Patient</div>
                <div className="sim-line"></div>
                <div className="sim-node">Symptoms</div>
                <div className="sim-line"></div>
                <div className="sim-node ai">AI Copilot</div>
                <div className="sim-line"></div>
                <div className="sim-node splunk">Splunk</div>
                <div className="sim-score">
                  <small>Live risk signal</small>
                  <strong>37</strong>
                  <span>Critical case routed to support team</span>
                </div>
              </div>
''' + app[insert_at:]
                print("✅ How simulation inserted")

# 3) OncoKids character-stage direkt replace
start = app.find('<div className="character-stage">')
if start != -1 and "lumi-companion-stage-v31" not in app:
    i = start
    depth = 0
    end = None
    while i < len(app):
        if app.startswith("<div", i):
            depth += 1
            i += 4
        elif app.startswith("</div>", i):
            depth -= 1
            i += 6
            if depth == 0:
                end = i
                break
        else:
            i += 1

    if end:
        block = '''<div className="character-stage lumi-companion-stage-v31">
            <div className="lumi-character-v31">
              <div className="lumi-head-v31">😊</div>
              <div className="lumi-body-v31"></div>
            </div>

            <div className="lumi-bubble-v31">
              <strong>Lumi says</strong>
              <span>Pick a quest, collect Hope Points and practice brave questions.</span>
            </div>

            <div className="lumi-actions-v31">
              <button onClick={() => addPoints(15, "feel", "💛")}>💛 Feelings</button>
              <button onClick={() => addPoints(20, "ask", "❓")}>❓ Ask Lumi</button>
              <button onClick={() => addPoints(25, "hero", "🏆")}>🏆 Badge</button>
            </div>

            <div className="lumi-float-star one">⭐</div>
            <div className="lumi-float-star two">🌈</div>
            <div className="lumi-float-star three">🎈</div>
          </div>'''
        app = app[:start] + block + app[end:]
        print("✅ OncoKids character-stage replaced")
else:
    print("ℹ️ character-stage yok veya zaten değiştirilmiş")

css += r'''

/* Step 31 force JSX components */

/* Calm card child companion */
.landing-companion-child-v31 {
  margin-top: 28px;
  display: inline-flex;
  align-items: center;
  gap: 16px;
  padding: 14px 18px;
  border-radius: 999px;
  background: rgba(255,255,255,.28);
  border: 1px solid rgba(255,255,255,.48);
  color: white;
  box-shadow: 0 18px 50px rgba(15,23,42,.16);
}

.child-face-v31 {
  width: 70px;
  height: 70px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 32% 28%, #fff, #dbeafe 48%, #99f6e4);
  font-size: 38px;
  animation: v31Float 4s ease-in-out infinite;
}

.landing-companion-child-v31 strong,
.landing-companion-child-v31 span {
  display: block;
}

.landing-companion-child-v31 strong {
  font-size: 18px;
}

.landing-companion-child-v31 span {
  opacity: .9;
  font-weight: 750;
}

/* How simulation */
.how-simulation-v31 {
  margin: 32px auto 0;
  max-width: 1080px;
  display: grid;
  grid-template-columns: auto 1fr auto 1fr auto 1fr auto 260px;
  gap: 12px;
  align-items: center;
  padding: 20px;
  border-radius: 32px;
  background: white;
  border: 1px solid #dbeafe;
  box-shadow: 0 24px 70px rgba(37,99,235,.12);
}

.sim-node {
  min-width: 110px;
  text-align: center;
  padding: 14px 16px;
  border-radius: 999px;
  background: #eff6ff;
  color: #1d4ed8;
  font-weight: 950;
}

.sim-node.ai {
  background: #f3e8ff;
  color: #7e22ce;
}

.sim-node.splunk {
  background: #dcfce7;
  color: #166534;
}

.sim-line {
  height: 5px;
  border-radius: 999px;
  background: linear-gradient(90deg, #2563eb, #14b8a6);
  position: relative;
  overflow: hidden;
}

.sim-line::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, white, transparent);
  animation: simFlow 2.2s linear infinite;
}

.sim-score {
  border-radius: 24px;
  background: #0f172a;
  color: white;
  padding: 16px;
}

.sim-score small,
.sim-score strong,
.sim-score span {
  display: block;
}

.sim-score strong {
  font-size: 42px;
  line-height: 1;
  margin: 5px 0;
}

.sim-score span {
  color: #cbd5e1;
  font-size: 13px;
}

/* OncoKids real companion */
.lumi-companion-stage-v31 {
  position: relative !important;
  min-height: 560px !important;
  border-radius: 46px !important;
  overflow: hidden !important;
  background:
    radial-gradient(circle at 50% 16%, rgba(255,255,255,.98), transparent 22%),
    linear-gradient(180deg, rgba(186,230,253,.9), rgba(254,243,199,.84)) !important;
  border: 1px solid rgba(255,255,255,.95);
  box-shadow: 0 28px 90px rgba(15,23,42,.14);
}

.lumi-companion-stage-v31::before,
.lumi-companion-stage-v31::after {
  display: none !important;
}

.lumi-character-v31 {
  position: absolute;
  left: 50%;
  top: 38%;
  transform: translate(-50%, -50%);
  animation: v31Float 4s ease-in-out infinite;
}

.lumi-head-v31 {
  width: 190px;
  height: 190px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: radial-gradient(circle at 35% 28%, #fff, #fff7ed 48%, #fed7aa);
  border: 6px solid rgba(251,146,60,.38);
  box-shadow: 0 28px 80px rgba(15,23,42,.18);
  font-size: 98px;
}

.lumi-body-v31 {
  width: 120px;
  height: 110px;
  margin: -18px auto 0;
  border-radius: 42px 42px 54px 54px;
  background: linear-gradient(135deg, #60a5fa, #a78bfa);
}

.lumi-bubble-v31 {
  position: absolute;
  left: 36px;
  right: 36px;
  bottom: 112px;
  padding: 18px 20px;
  border-radius: 26px;
  background: rgba(255,255,255,.9);
  color: #7c2d12;
  box-shadow: 0 18px 46px rgba(15,23,42,.12);
}

.lumi-bubble-v31 strong,
.lumi-bubble-v31 span {
  display: block;
}

.lumi-bubble-v31 strong {
  color: #0f172a;
  font-size: 20px;
}

.lumi-bubble-v31 span {
  margin-top: 5px;
  font-weight: 850;
}

.lumi-actions-v31 {
  position: absolute;
  left: 36px;
  right: 36px;
  bottom: 34px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.lumi-actions-v31 button {
  border: none;
  border-radius: 999px;
  padding: 12px 10px;
  background: #fff7ed;
  color: #7c2d12;
  font-weight: 950;
  cursor: pointer;
}

.lumi-float-star {
  position: absolute;
  font-size: 34px;
  animation: v31Star 5s ease-in-out infinite;
}

.lumi-float-star.one { left: 18%; top: 18%; }
.lumi-float-star.two { right: 18%; top: 22%; animation-delay: .8s; }
.lumi-float-star.three { right: 20%; top: 58%; animation-delay: 1.4s; }

@keyframes v31Float {
  0%, 100% { transform: translate(-50%, -50%) translateY(0) rotate(-1deg); }
  50% { transform: translate(-50%, -50%) translateY(-16px) rotate(2deg); }
}

@keyframes v31Star {
  0%, 100% { transform: translateY(0) rotate(-6deg); opacity: .85; }
  50% { transform: translateY(-14px) rotate(8deg); opacity: 1; }
}

@keyframes simFlow {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}

@media (max-width: 1000px) {
  .how-simulation-v31 {
    grid-template-columns: 1fr;
  }

  .sim-line {
    height: 32px;
    width: 5px;
    justify-self: center;
  }

  .lumi-companion-stage-v31 {
    min-height: 420px !important;
  }

  .lumi-head-v31 {
    width: 135px;
    height: 135px;
    font-size: 70px;
  }

  .lumi-body-v31 {
    width: 86px;
    height: 78px;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Step 31 applied: direct JSX insertion completed.")
