from pathlib import Path

path = Path("frontend/src/App.jsx")
content = path.read_text(encoding="utf-8")

content = content.replace(
'''            <input value={form.patientId} onChange={(e) => update("patientId", e.target.value)} placeholder="Patient ID" />
            <input value={form.city} onChange={(e) => update("city", e.target.value)} placeholder="City" />
            <input value={form.cancerType} onChange={(e) => update("cancerType", e.target.value)} placeholder="Cancer Type" />
            <input value={form.treatmentStage} onChange={(e) => update("treatmentStage", e.target.value)} placeholder="Treatment Stage" />''',
'''            <select value={form.patientId} onChange={(e) => update("patientId", e.target.value)}>
              <option value="P999">P999 — Critical Demo Patient</option>
              <option value="P001">P001 — Breast Cancer / Izmir</option>
              <option value="P002">P002 — Lung Cancer / Ankara</option>
              <option value="P010">P010 — Breast Cancer / Istanbul</option>
              <option value="P011">P011 — Lung Cancer / Ankara</option>
              <option value="P012">P012 — Colon Cancer / Izmir</option>
              <option value="P013">P013 — Lymphoma / Bursa</option>
            </select>

            <select value={form.city} onChange={(e) => update("city", e.target.value)}>
              <option value="Istanbul">Istanbul</option>
              <option value="Izmir">Izmir</option>
              <option value="Ankara">Ankara</option>
              <option value="Bursa">Bursa</option>
            </select>

            <select value={form.cancerType} onChange={(e) => update("cancerType", e.target.value)}>
              <option value="Breast Cancer">Breast Cancer</option>
              <option value="Lung Cancer">Lung Cancer</option>
              <option value="Colon Cancer">Colon Cancer</option>
              <option value="Lymphoma">Lymphoma</option>
              <option value="Leukemia">Leukemia</option>
            </select>

            <select value={form.treatmentStage} onChange={(e) => update("treatmentStage", e.target.value)}>
              <option value="Chemotherapy">Chemotherapy</option>
              <option value="Radiotherapy">Radiotherapy</option>
              <option value="Immunotherapy">Immunotherapy</option>
              <option value="Follow-up">Follow-up</option>
              <option value="Post-surgery follow-up">Post-surgery follow-up</option>
            </select>'''
)

css_path = Path("frontend/src/App.css")
css = css_path.read_text(encoding="utf-8")

css = css.replace(
'''input,
textarea {''',
'''input,
select,
textarea {'''
)

css = css.replace(
'''  font-size: 15px;
}''',
'''  font-size: 15px;
  background: white;
}

select {
  cursor: pointer;
}''',
1
)

# Hero çok uzun görünmesin diye biraz küçültme
css = css.replace("min-height: 88vh;", "min-height: 68vh;")
css = css.replace("font-size: 76px;", "font-size: 64px;")
css = css.replace("margin: -90px auto 40px;", "margin: -70px auto 40px;")

path.write_text(content, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Dropdowns added and hero height adjusted.")
