from pathlib import Path
import re

app = Path("frontend/src/App.jsx")
s = app.read_text(encoding="utf-8")

# Açıkta kalmış eski metricLabel fragment'ını temizle
s = re.sub(
    r'''
\n\s*cases:\s*"New cases",\s*
\n\s*deaths:\s*"Deaths",\s*
\n\s*survival:\s*"5-year survival"\s*
\n\s*};\s*
''',
    "\n",
    s,
    count=1,
    flags=re.VERBOSE
)

# Aynı problem "5-year prevalence" varyantıyla kaldıysa onu da temizle
s = re.sub(
    r'''
\n\s*cases:\s*"New cases",\s*
\n\s*deaths:\s*"Deaths",\s*
\n\s*survival:\s*"5-year prevalence"\s*
\n\s*};\s*
''',
    "\n",
    s,
    count=1,
    flags=re.VERBOSE
)

app.write_text(s, encoding="utf-8")
print("✅ Parse error cleanup applied.")
