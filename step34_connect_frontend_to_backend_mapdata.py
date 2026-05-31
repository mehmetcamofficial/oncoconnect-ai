from pathlib import Path

p = Path("frontend/src/App.jsx")
s = p.read_text(encoding="utf-8")

old = 'fetch("/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv")'
new = 'fetch("http://localhost:5050/public/map-data")'

if old not in s:
    print("⚠️ Eski CSV fetch satırı bulunamadı. Mevcut fetch satırlarını kontrol et:")
    for line in s.splitlines():
        if "fetch(" in line and ("data" in line or "map" in line):
            print(line)
else:
    s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")
    print("✅ Frontend map data now reads from backend /public/map-data")
