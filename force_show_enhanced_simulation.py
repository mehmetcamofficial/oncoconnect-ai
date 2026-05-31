from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# 1) Component var mı kontrol
if "const EnhancedFlowSimulation" not in s:
    print("❌ EnhancedFlowSimulation component yok. Önceki script component'i eklememiş.")
    raise SystemExit(1)

# 2) LandingPage içinde render yoksa güvenli yere ekle
if "<EnhancedFlowSimulation />" not in s:
    # LandingDataDashboard varsa hemen önüne koy
    if "<LandingDataDashboard />" in s:
        s = s.replace(
            "<LandingDataDashboard />",
            "<EnhancedFlowSimulation />\n        <LandingDataDashboard />",
            1
        )
        print("✅ EnhancedFlowSimulation LandingDataDashboard önüne eklendi.")
    else:
        # fallback: LandingPage içindeki ilk büyük section sonrasına ekle
        lp_start = s.find("  const LandingPage")
        next_const = s.find("\n  const ", lp_start + 5)

        if lp_start == -1 or next_const == -1:
            print("❌ LandingPage sınırı bulunamadı.")
            raise SystemExit(1)

        block = s[lp_start:next_const]
        insert_pos = block.find("</section>")

        if insert_pos == -1:
            print("❌ LandingPage içinde section kapanışı bulunamadı.")
            raise SystemExit(1)

        block = block[:insert_pos + len("</section>")] + "\n        <EnhancedFlowSimulation />" + block[insert_pos + len("</section>"):]
        s = s[:lp_start] + block + s[next_const:]
        print("✅ EnhancedFlowSimulation LandingPage içine zorla eklendi.")
else:
    print("✅ EnhancedFlowSimulation zaten render ediliyor.")

app.write_text(s, encoding="utf-8")

# 3) CSS gizleniyorsa zorla görünür yap
css_patch = r'''

/* FORCE SHOW enhanced simulation */

.enhanced-flow-sim {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  position: relative !important;
  z-index: 50 !important;
  min-height: 780px !important;
}

.enhanced-flow-sim * {
  visibility: visible;
}

.enhanced-flow-canvas {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  min-height: 560px !important;
}

.flow-step-row {
  display: grid !important;
  visibility: visible !important;
  opacity: 1 !important;
}

.flow-step-card {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
}

.flow-output-panel {
  display: grid !important;
  visibility: visible !important;
  opacity: 1 !important;
}

.flow-stream-line,
.flow-grid-bg {
  display: block !important;
}

'''

css_text = css.read_text(encoding="utf-8")
if "FORCE SHOW enhanced simulation" not in css_text:
    css.write_text(css_text + css_patch, encoding="utf-8")

print("✅ Force visibility CSS added.")
