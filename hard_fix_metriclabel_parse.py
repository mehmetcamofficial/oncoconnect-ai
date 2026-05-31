from pathlib import Path

p = Path("frontend/src/App.jsx")
lines = p.read_text(encoding="utf-8").splitlines()

out = []
i = 0
removed = 0

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    # Açıkta kalmış object fragment:
    # cases: "New cases",
    # deaths: "Deaths",
    # survival: "..."
    # };
    if stripped.startswith('cases: "New cases"'):
        prev_nonempty = ""
        for j in range(len(out) - 1, -1, -1):
            if out[j].strip():
                prev_nonempty = out[j].strip()
                break

        # Eğer hemen öncesinde const metricLabel = { yoksa bu bozuk fragmenttır
        if "const metricLabel" not in prev_nonempty:
            print(f"Removing broken metricLabel fragment starting at line {i+1}")
            while i < len(lines):
                if lines[i].strip() == "};":
                    i += 1
                    break
                i += 1
            removed += 1
            continue

    out.append(line)
    i += 1

p.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"✅ Removed broken fragments: {removed}")
