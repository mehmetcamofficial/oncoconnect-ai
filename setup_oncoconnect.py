from pathlib import Path

root = Path.cwd()
frontend = root / "frontend" / "src"
backend = root / "backend"

# ---------- Frontend files ----------
(frontend / "index.css").write_text("""
* {
  box-sizing: border-box;
}

html,
body,
#root {
  margin: 0;
  padding: 0;
  width: 100%;
  min-height: 100%;
}

body {
  font-family: Inter, Arial, sans-serif;
  background: #f5f7fb;
}
""".strip() + "\n", encoding="utf-8")

(frontend / "App.css").write_text("""
.page {
  min-height: 100vh;
  background: #f5f7fb;
}

.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0f172a, #1e3a8a, #7c3aed);
  color: white;
}

.hero-content {
  max-width: 1000px;
  text-align: center;
  padding: 40px;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 3px;
  opacity: 0.8;
}

h1 {
  font-size: 56px;
  line-height: 1.1;
  margin: 16px 0 24px;
  color: white;
}

.subtitle {
  font-size: 22px;
  line-height: 1.7;
  color: rgba(255,255,255,0.9);
}

.buttons {
  margin-top: 32px;
}

button {
  padding: 14px 24px;
  margin: 10px;
  border-radius: 12px;
  border: none;
  font-size: 16px;
  cursor: pointer;
}

.secondary {
  background: white;
  color: #111827;
}
""".strip() + "\n", encoding="utf-8")

(frontend / "App.jsx").write_text("""
import "./App.css";

function App() {
  return (
    <div className="page">
      <section className="hero">
        <div className="hero-content">
          <p className="eyebrow">OncoConnect AI</p>

          <h1>
            Kanser Hastaları ve Hasta Yakınları İçin
            <br />
            Akıllı Destek Platformu
          </h1>

          <p className="subtitle">
            Semptomlarınızı takip edin, doktor görüşmelerine hazırlanın ve
            güvenilir destek kaynaklarına erişin.
          </p>

          <div className="buttons">
            <button>Hasta Olarak Başla</button>
            <button className="secondary">Hasta Yakını Olarak Başla</button>
          </div>
        </div>
      </section>
    </div>
  );
}

export default App;
""".strip() + "\n", encoding="utf-8")

# ---------- Backend test file ----------
(backend / "server.js").write_text("""
const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("OncoConnect Backend Running");
});

app.listen(5050, () => {
  console.log("Server running on port 5050");
});
""".strip() + "\n", encoding="utf-8")

print("✅ OncoConnect files updated successfully.")
print("Next:")
print("1) backend: cd backend && node server.js")
print("2) frontend: cd frontend && npm run dev")	
