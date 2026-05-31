from pathlib import Path
import re

p = Path("backend/server.js")
s = p.read_text(encoding="utf-8")

if "AUTO_REVIEW_REQUIRED" in s and "auto-research dataset contains placeholder values" in s:
    print("ℹ️ Publish guard already exists.")
    raise SystemExit

pattern = r'(app\.patch\("/admin/datasets/:id"[\s\S]*?)(\n\s*res\.json\(\{\s*success:\s*true[\s\S]*?\}\);\s*\n\}\);)'
m = re.search(pattern, s)

if not m:
    raise SystemExit("❌ PATCH endpoint regex ile bulunamadı. grep çıktısını gönder.")

patch_block = r'''
    if (req.body.published === true) {
      const rowsText = JSON.stringify(dataset.rows || []);
      const hasAutoReviewRequired = rowsText.includes("AUTO_REVIEW_REQUIRED");
      const isAutoResearchDataset =
        String(dataset.id || "").startsWith("auto_") ||
        String(dataset.name || "").includes("auto_research") ||
        String(dataset.sourceName || "").toLowerCase().includes("auto research");

      if (hasAutoReviewRequired || isAutoResearchDataset) {
        return res.status(400).json({
          success: false,
          error: "This auto-research dataset contains placeholder values and cannot be published before validation."
        });
      }
    }

'''

# PATCH endpoint içinde dataset bulunduktan sonra, güncellemeden hemen önce ekle.
endpoint = m.group(1)

insert_points = [
    r'(\n\s*const\s+dataset\s*=\s*datasets\.find[\s\S]*?\n\s*\}\s*)',
    r'(\n\s*if\s*\(!dataset\)[\s\S]*?\n\s*\}\s*)'
]

inserted = False
for ip in insert_points:
    mm = re.search(ip, endpoint)
    if mm:
        endpoint = endpoint[:mm.end()] + patch_block + endpoint[mm.end():]
        inserted = True
        break

if not inserted:
    # fallback: res.json öncesine ekle
    endpoint = endpoint + patch_block

s = s[:m.start(1)] + endpoint + m.group(2) + s[m.end(2):]
p.write_text(s, encoding="utf-8")

print("✅ Auto research publish guard added.")
