from pathlib import Path
import re

p = Path("backend/server.js")
s = p.read_text(encoding="utf-8")

new_patch = r'''
app.patch("/admin/datasets/:id", (req, res) => {
  try {
    const datasets = readDatasets();
    const dataset = datasets.find((d) => d.id === req.params.id);

    if (!dataset) {
      return res.status(404).json({
        success: false,
        error: "Dataset not found"
      });
    }

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

    const allowedFields = [
      "published",
      "qualityFlag",
      "sourceName",
      "sourceUrl",
      "automationStatus",
      "automationNote"
    ];

    for (const field of allowedFields) {
      if (Object.prototype.hasOwnProperty.call(req.body, field)) {
        dataset[field] = req.body[field];
      }
    }

    dataset.updatedAt = new Date().toISOString();

    writeDatasets(datasets);

    res.json({
      success: true,
      dataset
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      error: "Dataset update failed",
      detail: err.message
    });
  }
});

'''

pattern = r'app\.patch\("/admin/datasets/:id"[\s\S]*?\n\}\);'

matches = list(re.finditer(pattern, s))

if not matches:
    raise SystemExit("❌ PATCH endpoint bulunamadı.")

# İlk PATCH endpoint'ini değiştir.
m = matches[0]
s = s[:m.start()] + new_patch + s[m.end():]

p.write_text(s, encoding="utf-8")
print("✅ PATCH endpoint rebuilt cleanly with auto-research publish guard.")
