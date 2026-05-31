from pathlib import Path

path = Path("frontend/src/App.jsx")
s = path.read_text(encoding="utf-8")

start = s.find('<div className="how-simulation-v31">')

if start == -1:
    print("how-simulation-v31 bulunamadı, dosyada yok.")
else:
    i = start
    depth = 0
    end = None

    while i < len(s):
        if s.startswith("<div", i):
            depth += 1
            i += 4
        elif s.startswith("</div>", i):
            depth -= 1
            i += 6
            if depth == 0:
                end = i
                break
        else:
            i += 1

    if end is None:
        raise RuntimeError("how-simulation-v31 kapanışı bulunamadı.")

    s = s[:start] + s[end:]
    path.write_text(s, encoding="utf-8")
    print("✅ Bozuk how-simulation-v31 bloğu kaldırıldı.")
