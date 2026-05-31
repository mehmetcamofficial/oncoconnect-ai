from pathlib import Path

p = Path("backend/server.js")
s = p.read_text(encoding="utf-8")

block = r'''

/* ================================
   Admin Authentication
================================ */

const ADMIN_USER = "admin";
const ADMIN_PASSWORD = "OncoConnect2026!";

app.post("/admin/login", (req, res) => {
  const { username, password } = req.body || {};

  if (
    username === ADMIN_USER &&
    password === ADMIN_PASSWORD
  ) {
    return res.json({
      success: true,
      token: "oncoconnect-admin-session"
    });
  }

  return res.status(401).json({
    success: false,
    error: "Invalid credentials"
  });
});

'''

if '/admin/login' not in s:
    idx = s.rfind('app.listen')
    s = s[:idx] + block + "\n" + s[idx:]
    p.write_text(s, encoding="utf-8")
    print("✅ Admin login endpoint added")
else:
    print("ℹ️ Login endpoint already exists")
