from pathlib import Path
import shutil, subprocess

app = Path("frontend/src/App.jsx")

latest_candidates = [
    Path("frontend/src/App.CURRENT_BROKEN_BACKUP.jsx"),
    Path("frontend/src/App.BEFORE_HERO_REPAIR.jsx"),
    Path("frontend/src/App.BEFORE_CHILD_HERO_HARD_REPAIR.jsx"),
]

hero_source = Path("frontend/src/App.SAFE_BACKUP_BEFORE_ONLY_HERO_REPAIR.jsx")

latest = next((p for p in latest_candidates if p.exists()), None)
if latest is None:
    raise SystemExit("❌ Latest büyük backup bulunamadı.")

if not hero_source.exists():
    raise SystemExit("❌ Çalışan hero backup bulunamadı.")

broken = latest.read_text(encoding="utf-8")
safe = hero_source.read_text(encoding="utf-8")

def extract_hero(text):
    start = text.find('<section className="old-portal-hero">')
    end = text.find('<section id="what-is-it"', start)
    if start == -1 or end == -1:
        raise ValueError("hero sınırı bulunamadı")
    return text[start:end]

safe_hero = extract_hero(safe)

start = broken.find('<section className="old-portal-hero">')
end = broken.find('<section id="what-is-it"', start)

if start == -1 or end == -1:
    raise SystemExit("❌ Büyük dosyada hero sınırı bulunamadı.")

restored = broken[:start] + safe_hero + broken[end:]

shutil.copy(app, "frontend/src/App.BEFORE_RESTORE_LATEST_FEATURES.jsx")
app.write_text(restored, encoding="utf-8")

print(f"✅ Latest features restored from: {latest}")
print("✅ Only hero replaced from working backup.")

result = subprocess.run(
    ["npm", "run", "build"],
    cwd="frontend",
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

if result.returncode == 0:
    print("✅ Build passed.")
else:
    print("❌ Build failed. Output:")
    print(result.stdout[-4000:])
