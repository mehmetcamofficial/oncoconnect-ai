from pathlib import Path
import shutil, subprocess

app = Path("frontend/src/App.jsx")

feature_candidates = [
    Path("frontend/src/App.BEFORE_HERO_REPAIR.jsx"),
    Path("frontend/src/App.BEFORE_CHILD_HERO_HARD_REPAIR.jsx"),
]

safe_hero_file = Path("frontend/src/App.SAFE_BACKUP_BEFORE_ONLY_HERO_REPAIR.jsx")

def extract_hero(text):
    start = text.find('<section className="old-portal-hero">')
    end = text.find('<section id="what-is-it"', start)
    if start == -1 or end == -1:
        return None
    return text[start:end]

safe_text = safe_hero_file.read_text(encoding="utf-8")
safe_hero = extract_hero(safe_text)

if not safe_hero:
    raise SystemExit("❌ Safe hero bulunamadı.")

shutil.copy(app, "frontend/src/App.BEFORE_115K_RESTORE_ATTEMPT.jsx")

for src in feature_candidates:
    if not src.exists():
        continue

    print(f"Trying feature source: {src}")

    text = src.read_text(encoding="utf-8")
    hero = extract_hero(text)

    if not hero:
        print("❌ Hero sınırı yok, geçiliyor.")
        continue

    start = text.find('<section className="old-portal-hero">')
    end = text.find('<section id="what-is-it"', start)

    repaired = text[:start] + safe_hero + text[end:]
    app.write_text(repaired, encoding="utf-8")

    result = subprocess.run(
        ["npm", "run", "build"],
        cwd="frontend",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    if result.returncode == 0:
        print(f"✅ RESTORED 115K FEATURES FROM: {src}")
        print("✅ Safe hero inserted.")
        raise SystemExit(0)

    print("❌ Build failed for this candidate:")
    print(result.stdout[-1600:])

print("❌ Hiçbir 115K aday build geçmedi.")
