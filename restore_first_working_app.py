from pathlib import Path
import shutil, subprocess

root = Path(".")
app = root / "frontend/src/App.jsx"

candidates = [
    "frontend/src/App.BEFORE_HERO_REPAIR.jsx",
    "frontend/src/App.BEFORE_CHILD_HERO_HARD_REPAIR.jsx",
    "frontend/src/App.SAFE_BACKUP_BEFORE_ONLY_HERO_REPAIR.jsx",
    "frontend/src/App.BEFORE_MAP_FUNCTIONAL_FIX_20260531_001713.jsx",
    "frontend/src/App.BEFORE_FUTURISTIC_MAP_20260531_000729.jsx",
    "frontend/src/App.BEFORE_COPILOT_FUNCTIONAL_RESTORE_20260531_000406.jsx",
]

shutil.copy(app, root / "frontend/src/App.CURRENT_BROKEN_BACKUP.jsx")

for c in candidates:
    p = root / c
    if not p.exists():
        continue

    print(f"Testing: {c}")
    shutil.copy(p, app)

    result = subprocess.run(
        ["npm", "run", "build"],
        cwd=root / "frontend",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    if result.returncode == 0:
        print(f"✅ RESTORED WORKING VERSION: {c}")
        raise SystemExit(0)

    print("❌ Failed")

print("❌ No working backup found. Current broken file saved as App.CURRENT_BROKEN_BACKUP.jsx")
