from pathlib import Path

p = Path("frontend/src/App.jsx")
s = p.read_text(encoding="utf-8")

# Login ekranına Back to Home
login_target = '<section className="admin-login-card-v36">'
login_replacement = '''<button className="admin-back-home-v36" onClick={() => setPage("landing")}>
          ← Back to Home
        </button>

        <section className="admin-login-card-v36">'''

if "admin-back-home-v36" not in s:
    s = s.replace(login_target, login_replacement, 1)

# Admin panel topbar'a Home butonu
topbar_target = '<div className="admin-topbar-v35">'
topbar_replacement = '''<div className="admin-topbar-v35">
        <button onClick={() => setPage("landing")}>← Back to Home</button>'''

if 'setPage("landing")}>← Back to Home' not in s:
    s = s.replace(topbar_target, topbar_replacement, 1)

p.write_text(s, encoding="utf-8")
print("✅ Back to Home buttons added to admin login and admin panel.")
