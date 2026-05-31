from pathlib import Path
import re

p = Path("backend/server.js")
s = p.read_text(encoding="utf-8")

listen_pattern = r'''
app\.listen\(5050,\s*\(\)\s*=>\s*\{
\s*console\.log\("Server running on port 5050"\);
\s*\}\);
'''

listen_block = '''
app.listen(5050, () => {
  console.log("Server running on port 5050");
});
'''

s2, count = re.subn(listen_pattern, "\n", s, count=1)

if count != 1:
    raise RuntimeError("app.listen block bulunamadı veya format farklı.")

s2 = s2.rstrip() + "\n\n" + listen_block

p.write_text(s2, encoding="utf-8")
print("✅ app.listen en sona taşındı. Admin route'lar artık register edilecek.")
