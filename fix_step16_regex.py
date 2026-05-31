from pathlib import Path

p = Path("step16_landing_nav_kids_stats.py")
s = p.read_text(encoding="utf-8")

old = '''pattern = r"  const LandingPage = \\(\\) => \\{[\\s\\S]*?\\n  const KnowledgeGraph = \\(\\) => \\("
app, count = re.subn(pattern, new_landing + "\\n\\n" + kids_component + "\\n  const KnowledgeGraph = () => (", app)

if count != 1:
    raise RuntimeError("Could not replace LandingPage block. Make sure previous landing page exists.")'''

new = '''# More flexible replacement: works whether LandingPage is written as () => ( or () => {
start = app.find("const LandingPage")
end = app.find("const KnowledgeGraph")

if start == -1 or end == -1 or end <= start:
    raise RuntimeError("Could not find LandingPage or KnowledgeGraph in App.jsx.")

# Keep indentation consistent
app = app[:start] + new_landing.lstrip() + "\\n\\n" + kids_component + "\\n  " + app[end:]'''

if old not in s:
    print("⚠️ Exact old block not found. Applying fallback replacement.")
    s = s.replace(
        '''pattern = r"  const LandingPage = \\(\\) => \\{[\\s\\S]*?\\n  const KnowledgeGraph = \\(\\) => \\("
app, count = re.subn(pattern, new_landing + "\\n\\n" + kids_component + "\\n  const KnowledgeGraph = () => (", app)''',
        '''start = app.find("const LandingPage")
end = app.find("const KnowledgeGraph")

if start == -1 or end == -1 or end <= start:
    raise RuntimeError("Could not find LandingPage or KnowledgeGraph in App.jsx.")

app = app[:start] + new_landing.lstrip() + "\\n\\n" + kids_component + "\\n  " + app[end:]'''
    )
    s = s.replace(
        '''if count != 1:
    raise RuntimeError("Could not replace LandingPage block. Make sure previous landing page exists.")''',
        ''
    )
else:
    s = s.replace(old, new)

p.write_text(s, encoding="utf-8")
print("✅ step16 script fixed.")
