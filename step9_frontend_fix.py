from pathlib import Path

path = Path("frontend/src/App.jsx")
content = path.read_text(encoding="utf-8")

# 1) useState üstüne patient presets ekle
content = content.replace(
'''const API_URL = "http://localhost:5050";

function App() {''',
'''const API_URL = "http://localhost:5050";

const patientPresets = {
  P999: { patientId: "P999", cancerType: "Breast Cancer", treatmentStage: "Chemotherapy", city: "Istanbul", fatigue: 10, nausea: 9, pain: 9, mood: 1, note: "Critical symptom escalation detected during demo." },
  P001: { patientId: "P001", cancerType: "Breast Cancer", treatmentStage: "Chemotherapy", city: "Izmir", fatigue: 8, nausea: 7, pain: 3, mood: 2, note: "Kemoterapi sonrası halsizlik ve bulantı arttı." },
  P002: { patientId: "P002", cancerType: "Lung Cancer", treatmentStage: "Radiotherapy", city: "Ankara", fatigue: 6, nausea: 4, pain: 5, mood: 5, note: "Fatigue continues after radiotherapy." },
  P010: { patientId: "P010", cancerType: "Breast Cancer", treatmentStage: "Chemotherapy", city: "Istanbul", fatigue: 7, nausea: 5, pain: 6, mood: 3, note: "High symptom burden." },
  P011: { patientId: "P011", cancerType: "Lung Cancer", treatmentStage: "Radiotherapy", city: "Ankara", fatigue: 8, nausea: 7, pain: 5, mood: 2, note: "Pain and fatigue increasing." },
  P012: { patientId: "P012", cancerType: "Colon Cancer", treatmentStage: "Follow-up", city: "Izmir", fatigue: 4, nausea: 3, pain: 2, mood: 7, note: "Stable follow-up condition." },
  P013: { patientId: "P013", cancerType: "Lymphoma", treatmentStage: "Immunotherapy", city: "Bursa", fatigue: 5, nausea: 3, pain: 2, mood: 6, note: "Feeling better today." }
};

function App() {'''
)

# 2) update fonksiyonundan sonra preset fonksiyonu ekle
content = content.replace(
'''  const update = (key, value) => {
    setForm({ ...form, [key]: value });
  };''',
'''  const update = (key, value) => {
    setForm({ ...form, [key]: value });
  };

  const selectPatient = (patientId) => {
    setForm(patientPresets[patientId]);
    setResult(null);
    setAiSummary(null);
  };'''
)

# 3) patient dropdown onChange değiştir
content = content.replace(
'''<select value={form.patientId} onChange={(e) => update("patientId", e.target.value)}>''',
'''<select value={form.patientId} onChange={(e) => selectPatient(e.target.value)}>'''
)

Path("frontend/src/App.jsx").write_text(content, encoding="utf-8")

css_path = Path("frontend/src/App.css")
css = css_path.read_text(encoding="utf-8")

# Hero ve layout ayarları
css = css.replace("min-height: 68vh;", "min-height: 58vh;")
css = css.replace("padding: 64px;", "padding: 42px 56px 120px;")
css = css.replace("font-size: 64px;", "font-size: 56px;")
css = css.replace("font-size: 22px;", "font-size: 18px;")
css = css.replace("margin: -70px auto 40px;", "margin: -95px auto 40px;")

# Form kartları biraz yukarı ve dengeli
css = css.replace(
'''.workspace {
  display: grid;
  grid-template-columns: 1.3fr 0.8fr;''',
'''.workspace {
  display: grid;
  grid-template-columns: 1.25fr 0.85fr;'''
)

# Hero card daha kompakt
css = css.replace("padding: 28px;", "padding: 22px;")
css = css.replace("font-size: 28px;", "font-size: 24px;")

# Stats kartları taşmasın
css = css.replace("font-size: 30px;", "font-size: 26px;")

css_path.write_text(css, encoding="utf-8")

print("✅ Frontend fixed: patient presets, layout height, card positioning.")
