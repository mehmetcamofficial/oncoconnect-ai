from pathlib import Path

p = Path("frontend/src/App.jsx")
s = p.read_text(encoding="utf-8")

start = s.find("function AdminPanel() {")
if start == -1:
    raise RuntimeError("AdminPanel bulunamadı.")

# State ekle
needle = "function AdminPanel() {\n"
inject = '''function AdminPanel() {
  const [authenticated, setAuthenticated] = React.useState(
    localStorage.getItem("admin-auth") === "true"
  );
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
'''
if "admin-auth" not in s:
    s = s.replace(needle, inject, 1)

# Login/logout fonksiyonlarını API const sonrasına ekle
api_needle = '  const API = "http://localhost:5050";\n'
login_block = r'''
  async function login() {
    try {
      const res = await fetch(`${API}/admin/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });

      const data = await res.json();

      if (!data.success) {
        setStatus("Invalid admin credentials.");
        return;
      }

      localStorage.setItem("admin-auth", "true");
      setAuthenticated(true);
      setStatus("Admin login successful.");
    } catch {
      setStatus("Login failed. Check backend.");
    }
  }

  function logout() {
    localStorage.removeItem("admin-auth");
    setAuthenticated(false);
    setUsername("");
    setPassword("");
  }

'''
if "async function login()" not in s:
    s = s.replace(api_needle, api_needle + login_block, 1)

# return öncesine auth guard ekle
return_needle = "  return (\n    <main className=\"admin-page-v35\">"
auth_block = r'''  if (!authenticated) {
    return (
      <main className="admin-page-v35 admin-login-page-v36">
        <section className="admin-login-card-v36">
          <small>ONCOCONNECT AI ADMIN</small>
          <h1>Admin Login</h1>
          <p>Sign in to manage datasets, map layers and source labels.</p>

          <input
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") login();
            }}
          />

          <button onClick={login}>Login</button>

          {status && <div className="admin-status-v35">{status}</div>}

          <div className="admin-login-hint-v36">
            Demo credentials: <strong>admin</strong> / <strong>OncoConnect2026!</strong>
          </div>
        </section>
      </main>
    );
  }

  return (
    <main className="admin-page-v35">'''
if "admin-login-card-v36" not in s:
    s = s.replace(return_needle, auth_block, 1)

# Logout butonu ekle
topbar_needle = '<button onClick={() => window.location.reload()}>↻ Refresh</button>'
if "Logout</button>" not in s:
    s = s.replace(
        topbar_needle,
        topbar_needle + '\n        <button onClick={logout}>Logout</button>',
        1
    )

p.write_text(s, encoding="utf-8")
print("✅ Step 36B applied: frontend admin login added.")
