from pathlib import Path

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

start = app.find('<div className="character-stage">')
if start == -1:
    raise RuntimeError("character-stage bulunamadı.")

# matching div bul
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

if end is None:
    raise RuntimeError("character-stage kapanışı bulunamadı.")

new_block = r'''<div className="character-stage lumi-companion-stage">
            <div className="lumi-sky-orb"></div>
            <div className="lumi-character">
              <div className="lumi-face">😊</div>
              <div className="lumi-body"></div>
              <div className="lumi-shadow"></div>
            </div>

            <div className="lumi-speech">
              <strong>Lumi says</strong>
              <span>Pick a quest, collect hope points and practice brave questions.</span>
            </div>

            <div className="lumi-mini-actions">
              <button onClick={() => addPoints(15, "feel", "💛")}>💛 Feelings</button>
              <button onClick={() => addPoints(20, "ask", "❓")}>❓ Ask</button>
              <button onClick={() => addPoints(25, "hero", "🏆")}>🏆 Badge</button>
            </div>

            <div className="floating-star s1">⭐</div>
            <div className="floating-star s2">🌈</div>
            <div className="floating-star s3">🎈</div>
          </div>'''

app = app[:start] + new_block + app[end:]

css += r'''

/* Step 30: real OncoKids animated cartoon companion */

.lumi-companion-stage {
  position: relative !important;
  min-height: 560px !important;
  border-radius: 46px !important;
  overflow: hidden !important;
  background:
    radial-gradient(circle at 50% 18%, rgba(255,255,255,.98), transparent 22%),
    linear-gradient(180deg, rgba(186,230,253,.88), rgba(254,243,199,.82)) !important;
  border: 1px solid rgba(255,255,255,.95) !important;
  box-shadow: 0 28px 90px rgba(15,23,42,.14) !important;
}

.lumi-companion-stage::before,
.lumi-companion-stage::after {
  display: none !important;
}

.lumi-sky-orb {
  position: absolute;
  width: 210px;
  height: 210px;
  border-radius: 999px;
  left: 50%;
  top: 36%;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle at 35% 30%, #fff, #dbeafe 45%, #99f6e4);
  filter: blur(4px);
  opacity: .55;
  animation: lumiOrb 5s ease-in-out infinite;
}

.lumi-character {
  position: absolute;
  left: 50%;
  top: 38%;
  transform: translate(-50%, -50%);
  animation: lumiFloatReal 4s ease-in-out infinite;
}

.lumi-face {
  width: 180px;
  height: 180px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 35% 28%, #fff, #fff7ed 48%, #fed7aa);
  border: 6px solid rgba(251,146,60,.38);
  box-shadow: 0 28px 80px rgba(15,23,42,.18);
  font-size: 92px;
  position: relative;
  z-index: 3;
}

.lumi-body {
  width: 118px;
  height: 108px;
  margin: -18px auto 0;
  border-radius: 42px 42px 54px 54px;
  background: linear-gradient(135deg, #60a5fa, #a78bfa);
  box-shadow: 0 24px 55px rgba(15,23,42,.16);
}

.lumi-shadow {
  width: 160px;
  height: 28px;
  border-radius: 999px;
  margin: 16px auto 0;
  background: rgba(15,23,42,.14);
  filter: blur(6px);
}

.lumi-speech {
  position: absolute;
  left: 34px;
  right: 34px;
  bottom: 112px;
  border-radius: 26px;
  padding: 18px 20px;
  background: rgba(255,255,255,.9);
  color: #7c2d12;
  box-shadow: 0 18px 46px rgba(15,23,42,.12);
}

.lumi-speech strong,
.lumi-speech span {
  display: block;
}

.lumi-speech strong {
  font-size: 20px;
  color: #0f172a;
}

.lumi-speech span {
  margin-top: 5px;
  font-weight: 850;
  line-height: 1.45;
}

.lumi-mini-actions {
  position: absolute;
  left: 34px;
  right: 34px;
  bottom: 34px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.lumi-mini-actions button {
  border: none;
  border-radius: 999px;
  padding: 12px 10px;
  background: #fff7ed;
  color: #7c2d12;
  font-weight: 950;
  cursor: pointer;
  box-shadow: 0 10px 28px rgba(15,23,42,.10);
}

.lumi-mini-actions button:hover {
  transform: translateY(-2px);
  background: #ffedd5;
}

.floating-star {
  position: absolute;
  font-size: 34px;
  animation: starFloat 5s ease-in-out infinite;
}

.floating-star.s1 { left: 18%; top: 18%; }
.floating-star.s2 { right: 18%; top: 22%; animation-delay: .8s; }
.floating-star.s3 { right: 20%; top: 58%; animation-delay: 1.4s; }

@keyframes lumiFloatReal {
  0%, 100% { transform: translate(-50%, -50%) translateY(0) rotate(-1deg); }
  50% { transform: translate(-50%, -50%) translateY(-16px) rotate(2deg); }
}

@keyframes lumiOrb {
  0%, 100% { transform: translate(-50%, -50%) scale(1); }
  50% { transform: translate(-50%, -50%) scale(1.08); }
}

@keyframes starFloat {
  0%, 100% { transform: translateY(0) rotate(-6deg); opacity: .85; }
  50% { transform: translateY(-14px) rotate(8deg); opacity: 1; }
}

@media (max-width: 1000px) {
  .lumi-companion-stage {
    min-height: 420px !important;
  }

  .lumi-face {
    width: 130px;
    height: 130px;
    font-size: 68px;
  }

  .lumi-body {
    width: 86px;
    height: 78px;
  }
}
'''

app_path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ OncoKids character-stage replaced with real animated Lumi companion.")
