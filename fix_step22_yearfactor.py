from pathlib import Path

path = Path("frontend/src/App.jsx")
s = path.read_text(encoding="utf-8")

# mapData içinde ikinci kez tanımlanan yearFactor satırını kaldır
duplicate_block = '''    // Fallback demo layer
    const yearFactor = 1 + (mapYear - 2020) * 0.045;
    const genderFactor = mapGender === "female" ? 0.92 : mapGender === "male" ? 1.08 : 1;'''

fixed_block = '''    // Fallback demo layer
    const genderFactor = mapGender === "female" ? 0.92 : mapGender === "male" ? 1.08 : 1;'''

if duplicate_block in s:
    s = s.replace(duplicate_block, fixed_block)
    print("✅ Duplicate yearFactor removed.")
else:
    print("⚠️ Exact duplicate block not found. Trying safer line-based cleanup.")

    lines = s.splitlines()
    seen_inside_mapdata = False
    yearfactor_count = 0
    new_lines = []

    for line in lines:
      if "const mapData = useMemo" in line:
        seen_inside_mapdata = True
        yearfactor_count = 0

      if seen_inside_mapdata and "const yearFactor = 1 + (mapYear - 2020) * 0.045;" in line:
        yearfactor_count += 1
        if yearfactor_count > 1:
          print("✅ Removed extra:", line.strip())
          continue

      if seen_inside_mapdata and "const totalMapCases" in line:
        seen_inside_mapdata = False

      new_lines.append(line)

    s = "\n".join(new_lines)

path.write_text(s, encoding="utf-8")
print("✅ App.jsx fixed.")
