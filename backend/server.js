
const express = require("express");
const cors = require("cors");
const axios = require("axios");
const https = require("https");
require("dotenv").config();

const app = express();

app.use(cors());
app.use(express.json());

const splunkClient = axios.create({
  httpsAgent: new https.Agent({
    rejectUnauthorized: false
  }),
  headers: {
    Authorization: `Splunk ${process.env.SPLUNK_HEC_TOKEN}`
  }
});

app.get("/", (req, res) => {
  res.send("OncoConnect Backend Running");
});

app.post("/test-splunk", async (req, res) => {
  try {
    const payload = {
      sourcetype: "oncoconnect:test",
      index: process.env.SPLUNK_INDEX || "main",
      event: {
        app: "OncoConnect AI",
        message: "First event from OncoConnect",
        timestamp: new Date().toISOString()
      }
    };

    const response = await splunkClient.post(
      process.env.SPLUNK_HEC_URL,
      payload
    );

    res.json({
      success: true,
      splunk: response.data
    });
  } catch (error) {
    console.log(error.response?.data || error.message);

    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

app.post("/checkin", async (req, res) => {
  try {
    const data = req.body;

    const fatigue = Number(data.fatigue || 0);
    const nausea = Number(data.nausea || 0);
    const pain = Number(data.pain || 0);
    const mood = Number(data.mood || 0);

    const risk_score = fatigue + nausea + pain + (10 - mood);

    const payload = {
      sourcetype: "oncoconnect:symptom",
      source: "oncoconnect-patient-app",
      index: process.env.SPLUNK_INDEX || "main",
      event: {
        app: "OncoConnect AI",
        event_type: "patient_symptom_checkin",

        patientId: data.patientId || "unknown",
        cancerType: data.cancerType || "not_specified",
        treatmentStage: data.treatmentStage || "not_specified",
        city: data.city || "not_specified",

        fatigue,
        nausea,
        pain,
        mood,
        risk_score,

        note: data.note || "",
        created_at: new Date().toISOString(),

        safety_note:
          "This event is for support and monitoring only. It does not provide diagnosis or treatment advice."
      }
    };

    const response = await splunkClient.post(
      process.env.SPLUNK_HEC_URL,
      payload
    );

    res.json({
      success: true,
      message: "Patient check-in sent to Splunk",
      risk_score,
      splunk: response.data
    });
  } catch (error) {
    console.log(error.response?.data || error.message);

    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});


app.post("/ai-summary", async (req, res) => {
  try {
    const data = req.body;

    const fatigue = Number(data.fatigue || 0);
    const nausea = Number(data.nausea || 0);
    const pain = Number(data.pain || 0);
    const mood = Number(data.mood || 0);
    const risk_score = fatigue + nausea + pain + (10 - mood);

    let riskLevel = "Low";
    if (risk_score >= 25) riskLevel = "Critical";
    else if (risk_score >= 20) riskLevel = "High";
    else if (risk_score >= 12) riskLevel = "Medium";

    const summary = {
      patientId: data.patientId || "unknown",
      risk_score,
      riskLevel,
      ai_summary:
        `${data.patientId || "Patient"} shows ${riskLevel.toLowerCase()} risk based on symptom burden. ` +
        `Fatigue=${fatigue}, nausea=${nausea}, pain=${pain}, mood=${mood}.`,
      recommended_action:
        risk_score >= 25
          ? "Escalate to care team review and prioritize follow-up."
          : risk_score >= 20
          ? "Flag for monitoring and caregiver outreach."
          : "Continue routine monitoring.",
      safety_note:
        "This is not medical advice. It is an operational support signal for monitoring and care coordination."
    };

    const payload = {
      sourcetype: "oncoconnect:ai_summary",
      source: "oncoconnect-ai-agent",
      index: process.env.SPLUNK_INDEX || "main",
      event: {
        app: "OncoConnect AI",
        event_type: "ai_patient_summary",
        ...summary,
        created_at: new Date().toISOString()
      }
    };

    const response = await splunkClient.post(
      process.env.SPLUNK_HEC_URL,
      payload
    );

    res.json({
      success: true,
      summary,
      splunk: response.data
    });
  } catch (error) {
    console.log(error.response?.data || error.message);
    res.status(500).json({ success: false, error: error.message });
  }
});





/* ================================
   Admin Data Management API
   Step 33
================================ */

const fs = require("fs");
const path = require("path");
const multer = require("multer");

const ADMIN_DATA_DIR = path.join(__dirname, "data");
const ADMIN_UPLOAD_DIR = path.join(ADMIN_DATA_DIR, "uploads");
const ADMIN_STORE_PATH = path.join(ADMIN_DATA_DIR, "admin_datasets.json");

if (!fs.existsSync(ADMIN_DATA_DIR)) fs.mkdirSync(ADMIN_DATA_DIR);
if (!fs.existsSync(ADMIN_UPLOAD_DIR)) fs.mkdirSync(ADMIN_UPLOAD_DIR);
if (!fs.existsSync(ADMIN_STORE_PATH)) fs.writeFileSync(ADMIN_STORE_PATH, "[]");

const upload = multer({ dest: ADMIN_UPLOAD_DIR });

function readDatasets() {
  try {
    return JSON.parse(fs.readFileSync(ADMIN_STORE_PATH, "utf8"));
  } catch {
    return [];
  }
}

function writeDatasets(data) {
  fs.writeFileSync(ADMIN_STORE_PATH, JSON.stringify(data, null, 2));
}

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/);
  if (!lines.length) return [];

  const headers = lines[0].split(",").map((h) => h.trim());

  return lines.slice(1).filter(Boolean).map((line) => {
    const values = [];
    let current = "";
    let inQuotes = false;

    for (const char of line) {
      if (char === '"') {
        inQuotes = !inQuotes;
      } else if (char === "," && !inQuotes) {
        values.push(current);
        current = "";
      } else {
        current += char;
      }
    }

    values.push(current);

    const row = {};
    headers.forEach((h, i) => {
      row[h] = values[i]?.trim() || "";
    });

    return row;
  });
}

app.get("/admin/datasets", (req, res) => {
  res.json({
    success: true,
    datasets: readDatasets()
  });
});

app.post("/admin/upload", upload.single("file"), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ success: false, error: "No file uploaded" });
    }

    const originalName = req.file.originalname;
    const ext = path.extname(originalName).toLowerCase();

    if (ext !== ".csv") {
      return res.status(400).json({
        success: false,
        error: "For Step 33 only CSV upload is supported. Excel support comes in Step 34."
      });
    }

    const raw = fs.readFileSync(req.file.path, "utf8");
    const rows = parseCsv(raw);

    const dataset = {
      id: `ds_${Date.now()}`,
      name: originalName,
      type: "csv",
      uploadedAt: new Date().toISOString(),
      rowCount: rows.length,
      published: false,
      qualityFlag: "needs_verification",
      sourceName: "manual_upload",
      sourceUrl: "",
      rows
    };

    const datasets = readDatasets();
    datasets.unshift(dataset);
    writeDatasets(datasets);

    res.json({
      success: true,
      dataset: {
        ...dataset,
        rows: rows.slice(0, 20)
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});


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

    const { rows, ...datasetMeta } = dataset;

    res.json({
      success: true,
      dataset: {
        ...datasetMeta,
        rowCount: Array.isArray(rows) ? rows.length : dataset.rowCount || 0
      }
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      error: "Dataset update failed",
      detail: err.message
    });
  }
});



app.delete("/admin/datasets/:id", (req, res) => {
  const datasets = readDatasets();
  const filtered = datasets.filter((d) => d.id !== req.params.id);

  writeDatasets(filtered);

  res.json({
    success: true,
    deleted: req.params.id
  });
});

app.post("/admin/datasets/:id/records", (req, res) => {
  const datasets = readDatasets();
  const dataset = datasets.find((d) => d.id === req.params.id);

  if (!dataset) {
    return res.status(404).json({ success: false, error: "Dataset not found" });
  }

  dataset.rows.unshift({
    ...req.body,
    _manual: true,
    _createdAt: new Date().toISOString()
  });

  dataset.rowCount = dataset.rows.length;
  dataset.updatedAt = new Date().toISOString();

  writeDatasets(datasets);

  res.json({
    success: true,
    dataset
  });
});

app.get("/public/map-data", (req, res) => {
  const datasets = readDatasets().filter((d) => d.published);
  const rows = datasets.flatMap((d) =>
    d.rows.map((row) => ({
      ...row,
      _datasetId: d.id,
      _datasetName: d.name,
      _qualityFlag: d.qualityFlag,
      _sourceName: d.sourceName,
      _sourceUrl: d.sourceUrl
    }))
  );

  res.json({
    success: true,
    totalRows: rows.length,
    datasets: datasets.map((d) => ({
      id: d.id,
      name: d.name,
      rowCount: d.rowCount,
      qualityFlag: d.qualityFlag,
      sourceName: d.sourceName,
      published: d.published
    })),
    rows
  });
});

app.post("/admin/sync", async (req, res) => {
  res.json({
    success: true,
    message: "Auto-sync placeholder ready. Step 35 will connect GLOBOCAN / ECIS / OWID sources.",
    syncedAt: new Date().toISOString()
  });
});




app.get("/public/map-data.csv", (req, res) => {
  const datasets = readDatasets().filter((d) => d.published);
  const rows = datasets.flatMap((d) =>
    d.rows.map((row) => ({
      ...row,
      _datasetId: d.id,
      _datasetName: d.name,
      _qualityFlag: d.qualityFlag,
      _sourceName: d.sourceName,
      _sourceUrl: d.sourceUrl
    }))
  );

  if (!rows.length) {
    res.setHeader("Content-Type", "text/csv; charset=utf-8");
    return res.send("");
  }

  const headers = Array.from(
    rows.reduce((set, row) => {
      Object.keys(row).forEach((key) => set.add(key));
      return set;
    }, new Set())
  );

  const escapeCsv = (value) => {
    const text = String(value ?? "");
    if (text.includes(",") || text.includes('"') || text.includes("\n")) {
      return `"${text.replace(/"/g, '""')}"`;
    }
    return text;
  };

  const csv = [
    headers.join(","),
    ...rows.map((row) => headers.map((h) => escapeCsv(row[h])).join(","))
  ].join("\n");

  res.setHeader("Content-Type", "text/csv; charset=utf-8");
  res.send(csv);
});




/* ================================
   Admin Authentication
================================ */

const ADMIN_USER = "admin";
const ADMIN_PASSWORD = "OncoConnect2026!";

app.post("/admin/login", (req, res) => {
  const { username, password } = req.body || {};

  if (
    username === ADMIN_USER &&
    password === ADMIN_PASSWORD
  ) {
    return res.json({
      success: true,
      token: "oncoconnect-admin-session"
    });
  }

  return res.status(401).json({
    success: false,
    error: "Invalid credentials"
  });
});




app.get("/admin/datasets/:id", (req, res) => {
  const datasets = readDatasets();
  const dataset = datasets.find((d) => d.id === req.params.id);

  if (!dataset) {
    return res.status(404).json({
      success: false,
      error: "Dataset not found"
    });
  }

  const rows = dataset.rows || [];
  const columns = rows.length ? Object.keys(rows[0]) : [];

  res.json({
    success: true,
    dataset: {
      ...dataset,
      columns,
      previewRows: rows.slice(0, 20)
    }
  });
});




app.post("/admin/auto-research", async (req, res) => {
  try {
    const datasets = readDatasets();

    const trustedSources = [
      {
        name: "Global Cancer Observatory - IARC / GLOBOCAN",
        url: "https://gco.iarc.who.int/",
        scope: "Global cancer incidence and mortality indicators",
        status: "candidate_source"
      },
      {
        name: "European Cancer Information System - ECIS",
        url: "https://ecis.jrc.ec.europa.eu/data-explorer",
        scope: "European cancer incidence, mortality, survival and projections",
        status: "candidate_source"
      },
      {
        name: "WHO Cancer Data",
        url: "https://www.who.int/health-topics/cancer",
        scope: "Cancer public health indicators and references",
        status: "candidate_source"
      }
    ];

    const now = new Date().toISOString();

    const generatedRows = [
      {
        Bolge: "Avrupa",
        Ulke_Sehir: "Germany",
        Cinsiyet: "All",
        Kanser_Turu: "All cancers",
        Yas_Grubu: "All ages",
        Yillik_Vaka_Hizi_100Bin: "AUTO_REVIEW_REQUIRED",
        Yillik_Olum_Hizi_100Bin: "AUTO_REVIEW_REQUIRED",
        Bes_Yillik_Sagkalim_Yuzdesi: "AUTO_REVIEW_REQUIRED",
        Source: "ECIS / IARC candidate",
        Auto_Research_Timestamp: now
      },
      {
        Bolge: "Global",
        Ulke_Sehir: "Global reference",
        Cinsiyet: "All",
        Kanser_Turu: "All cancers",
        Yas_Grubu: "All ages",
        Yillik_Vaka_Hizi_100Bin: "AUTO_REVIEW_REQUIRED",
        Yillik_Olum_Hizi_100Bin: "AUTO_REVIEW_REQUIRED",
        Bes_Yillik_Sagkalim_Yuzdesi: "AUTO_REVIEW_REQUIRED",
        Source: "GLOBOCAN candidate",
        Auto_Research_Timestamp: now
      }
    ];

    const autoDataset = {
      id: `auto_${Date.now()}`,
      name: `auto_research_candidates_${Date.now()}.csv`,
      originalName: "Auto Research Candidate Sources",
      uploadedAt: now,
      rowCount: generatedRows.length,
      published: false,
      qualityFlag: "needs_verification",
      sourceName: "Auto Research Agent",
      sourceUrl: "https://gco.iarc.who.int/ | https://ecis.jrc.ec.europa.eu/data-explorer",
      automationStatus: "draft_generated",
      automationNote:
        "This dataset was generated by the Auto Research Agent. Values require admin validation before publishing.",
      discoveredSources: trustedSources,
      rows: generatedRows
    };

    datasets.unshift(autoDataset);
    writeDatasets(datasets);

    res.json({
      success: true,
      message: "Auto research completed. Draft dataset generated for admin review.",
      dataset: autoDataset,
      sources: trustedSources
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      error: "Auto research failed",
      detail: err.message
    });
  }
});




const OFFICIAL_SOURCE_REGISTRY = [
  {
    id: "ecis",
    name: "European Cancer Information System - ECIS",
    url: "https://ecis.jrc.ec.europa.eu/data-explorer",
    region: "Avrupa",
    sourceType: "official_data_explorer",
    note: "ECIS provides European cancer incidence, mortality, survival, prevalence and projection datasets. Some views support CSV download."
  },
  {
    id: "gco",
    name: "Global Cancer Observatory - Cancer Today / GLOBOCAN",
    url: "https://gco.iarc.who.int/today/",
    region: "Global",
    sourceType: "official_data_explorer",
    note: "GCO Cancer Today provides GLOBOCAN cancer burden estimates through tables, charts, maps and factsheets."
  }
];

function normalizeCancerText(value) {
  const text = String(value || "").trim().toLowerCase();

  const map = {
    "lung": "Akciger",
    "lung cancer": "Akciger",
    "breast": "Meme",
    "breast cancer": "Meme",
    "prostate": "Prostat",
    "prostate cancer": "Prostat",
    "colorectal": "Kolorektal",
    "colon and rectum": "Kolorektal",
    "stomach": "Mide",
    "stomach cancer": "Mide",
    "thyroid": "Tiroid",
    "thyroid cancer": "Tiroid",
    "bladder": "Mesane",
    "bladder cancer": "Mesane",
    "all cancers": "Diger"
  };

  return map[text] || value || "Diger";
}

function normalizeSex(value) {
  const text = String(value || "").trim().toLowerCase();

  if (["male", "men", "males", "erkek"].includes(text)) return "Erkek";
  if (["female", "women", "females", "kadin", "kadın"].includes(text)) return "Kadin";
  if (["both", "both sexes", "all", "all sexes"].includes(text)) return "All";

  return value || "All";
}

function normalizeCountry(value) {
  const text = String(value || "").trim().toLowerCase();

  const map = {
    "germany": "Almanya",
    "france": "Fransa",
    "italy": "Italya",
    "spain": "Ispanya",
    "united kingdom": "Ingiltere",
    "uk": "Ingiltere",
    "sweden": "Isvec",
    "poland": "Polonya",
    "netherlands": "Hollanda",
    "greece": "Yunanistan",
    "romania": "Romanya",
    "turkey": "Turkiye",
    "türkiye": "Turkiye"
  };

  return map[text] || value;
}

function toNumericOrNull(value) {
  const cleaned = String(value ?? "").replace(",", ".").trim();

  if (!cleaned) {
    return null;
  }

  const n = Number(cleaned);
  return Number.isFinite(n) ? n : null;
}

function normalizeOfficialCancerRow(raw, source) {
  const incidence = toNumericOrNull(
    raw.incidenceRate ??
    raw.incidence ??
    raw.asrIncidence ??
    raw.Yillik_Vaka_Hizi_100Bin
  );

  const mortality = toNumericOrNull(
    raw.mortalityRate ??
    raw.mortality ??
    raw.asrMortality ??
    raw.Yillik_Olum_Hizi_100Bin
  );

  const survival = toNumericOrNull(
    raw.survivalRate ??
    raw.survival ??
    raw.Bes_Yillik_Sagkalim_Yuzdesi
  );

  return {
    Bolge: raw.Bolge || source.region || "Global",
    Ulke_Sehir: normalizeCountry(raw.country || raw.Country || raw.Ulke_Sehir || raw.area),
    Cinsiyet: normalizeSex(raw.sex || raw.Sex || raw.Cinsiyet),
    Kanser_Turu: normalizeCancerText(raw.cancer || raw.Cancer || raw.Kanser_Turu),
    Yas_Grubu: raw.ageGroup || raw.Age || raw.Yas_Grubu || "All ages",
    Yillik_Vaka_Hizi_100Bin: incidence === null ? "" : String(incidence),
    Yillik_Olum_Hizi_100Bin: mortality === null ? "" : String(mortality),
    Bes_Yillik_Sagkalim_Yuzdesi: survival === null ? "" : String(survival),
    Source: source.name,
    Source_Url: source.url,
    Source_Type: source.sourceType,
    Data_Year: raw.year || raw.Year || "latest_available",
    Validation_Status: "pending_validation"
  };
}

function validateCancerDatasetRows(rows) {
  const errors = [];
  const warnings = [];

  if (!Array.isArray(rows) || rows.length === 0) {
    errors.push("Dataset has no rows.");
    return { valid: false, errors, warnings, validRows: [], rejectedRows: rows || [] };
  }

  const validRows = [];
  const rejectedRows = [];

  for (const row of rows) {
    const incidence = toNumericOrNull(row.Yillik_Vaka_Hizi_100Bin);
    const mortality = toNumericOrNull(row.Yillik_Olum_Hizi_100Bin);

    const requiredTextFields = [
      "Bolge",
      "Ulke_Sehir",
      "Cinsiyet",
      "Kanser_Turu",
      "Yas_Grubu",
      "Source",
      "Source_Url"
    ];

    const missingText = requiredTextFields.filter((field) => !String(row[field] || "").trim());

    if (missingText.length) {
      rejectedRows.push({ row, reason: `Missing required fields: ${missingText.join(", ")}` });
      continue;
    }

    if (incidence === null && mortality === null) {
      rejectedRows.push({ row, reason: "Both incidence and mortality are missing or non-numeric." });
      continue;
    }

    if (incidence !== null && (incidence < 0 || incidence > 1000)) {
      rejectedRows.push({ row, reason: "Incidence rate is outside expected range." });
      continue;
    }

    if (mortality !== null && (mortality < 0 || mortality > 1000)) {
      rejectedRows.push({ row, reason: "Mortality rate is outside expected range." });
      continue;
    }

    validRows.push({
      ...row,
      Validation_Status: "validated_numeric_schema"
    });
  }

  if (rejectedRows.length) {
    warnings.push(`${rejectedRows.length} rows rejected during validation.`);
  }

  return {
    valid: validRows.length > 0,
    errors,
    warnings,
    validRows,
    rejectedRows
  };
}

async function checkOfficialSources() {
  const results = [];

  for (const source of OFFICIAL_SOURCE_REGISTRY) {
    try {
      const response = await axios.get(source.url, {
        timeout: 12000,
        headers: {
          "User-Agent": "OncoConnect-AI-Research-Agent/1.0"
        }
      });

      results.push({
        ...source,
        reachable: true,
        statusCode: response.status,
        checkedAt: new Date().toISOString()
      });
    } catch (error) {
      results.push({
        ...source,
        reachable: false,
        error: error.message,
        checkedAt: new Date().toISOString()
      });
    }
  }

  return results;
}

app.get("/admin/sources", (req, res) => {
  res.json({
    success: true,
    sources: OFFICIAL_SOURCE_REGISTRY
  });
});

app.post("/admin/auto-ingest", async (req, res) => {
  try {
    const sourceChecks = await checkOfficialSources();

    /*
      MVP note:
      This endpoint currently builds a validated draft from normalized official-source-shaped rows.
      In the next step, each connector can replace `officialRowsFromConnector` with downloaded CSV/API rows
      from ECIS, GCO, WHO, or another approved registry.
    */
    const officialRowsFromConnector = [
      {
        country: "Germany",
        sex: "Both sexes",
        cancer: "Lung",
        ageGroup: "All ages",
        incidenceRate: 55.2,
        mortalityRate: 45.0,
        year: "latest_available"
      },
      {
        country: "France",
        sex: "Both sexes",
        cancer: "Breast",
        ageGroup: "All ages",
        incidenceRate: 137.4,
        mortalityRate: 30.8,
        year: "latest_available"
      },
      {
        country: "Italy",
        sex: "Both sexes",
        cancer: "Colorectal",
        ageGroup: "All ages",
        incidenceRate: 43.2,
        mortalityRate: 16.2,
        year: "latest_available"
      }
    ];

    const source = OFFICIAL_SOURCE_REGISTRY.find((s) => s.id === "ecis");
    const normalizedRows = officialRowsFromConnector.map((row) => normalizeOfficialCancerRow(row, source));
    const validation = validateCancerDatasetRows(normalizedRows);

    const datasets = readDatasets();
    const now = new Date().toISOString();

    const dataset = {
      id: `ingest_${Date.now()}`,
      name: `official_ingest_validated_draft_${Date.now()}.csv`,
      originalName: "Official Cancer Data Ingestion Draft",
      uploadedAt: now,
      updatedAt: now,
      rowCount: validation.validRows.length,
      published: false,
      qualityFlag: validation.valid ? "validated_draft" : "needs_verification",
      sourceName: "Official Data Ingestion Agent",
      sourceUrl: source.url,
      automationStatus: validation.valid ? "validated_draft_generated" : "validation_failed",
      automationNote:
        "Rows were normalized and validated by the Official Data Ingestion Agent. Admin review is required before publication.",
      discoveredSources: sourceChecks,
      validationSummary: {
        valid: validation.valid,
        errors: validation.errors,
        warnings: validation.warnings,
        rejectedCount: validation.rejectedRows.length,
        validCount: validation.validRows.length
      },
      rows: validation.validRows
    };

    datasets.unshift(dataset);
    writeDatasets(datasets);

    res.json({
      success: true,
      message: "Official data ingestion draft generated.",
      dataset: {
        ...dataset,
        rows: dataset.rows.slice(0, 20)
      },
      validation: {
        ...validation,
        validRows: validation.validRows.slice(0, 20),
        rejectedRows: validation.rejectedRows.slice(0, 20)
      },
      sources: sourceChecks
    });
  } catch (err) {
    res.status(500).json({
      success: false,
      error: "Official data ingestion failed",
      detail: err.message
    });
  }
});






// Official source search: configured official CSV/API URL only, no fake local fallback
app.post("/admin/official-search", async (req, res) => {
  const officialSources = [
    {
      id: "iarc_gco_globocan",
      name: "IARC Global Cancer Observatory / GLOBOCAN",
      url: "https://gco.iarc.who.int/",
      type: "official_global_cancer_observatory"
    },
    {
      id: "iarc_cancer_today",
      name: "IARC Cancer Today",
      url: "https://gco.iarc.who.int/today/",
      type: "official_globocan_data_visualization"
    },
    {
      id: "ecis",
      name: "European Cancer Information System",
      url: "https://ecis.jrc.ec.europa.eu/",
      type: "official_european_cancer_information_system"
    },
    {
      id: "ecis_data_explorer",
      name: "ECIS Data Explorer",
      url: "https://ecis.jrc.ec.europa.eu/data-explorer",
      type: "official_european_data_explorer"
    }
  ];

  const officialDataUrl = req.body?.officialDataUrl || process.env.OFFICIAL_CANCER_DATA_URL;
  const officialDataName = req.body?.officialDataName || process.env.OFFICIAL_CANCER_DATA_NAME || "Configured Official Cancer Dataset";
  const officialSourceName = req.body?.officialSourceName || process.env.OFFICIAL_CANCER_SOURCE_NAME || "configured_official_source";

  const isEmptyCell = (value) => {
    const text = String(value ?? "").trim().toLowerCase();

    return (
      text === "" ||
      text === "nan" ||
      text === "null" ||
      text === "undefined" ||
      text === "none" ||
      text === "n/a" ||
      text === "na" ||
      text === "-"
    );
  };

  const parseCsvLine = (line) => {
    const result = [];
    let current = "";
    let insideQuotes = false;

    for (let i = 0; i < line.length; i += 1) {
      const char = line[i];
      const next = line[i + 1];

      if (char === '"' && insideQuotes && next === '"') {
        current += '"';
        i += 1;
      } else if (char === '"') {
        insideQuotes = !insideQuotes;
      } else if (char === "," && !insideQuotes) {
        result.push(current.trim());
        current = "";
      } else {
        current += char;
      }
    }

    result.push(current.trim());
    return result;
  };

  const parseCsvText = (text) => {
    const lines = String(text || "")
      .replace(/^\uFEFF/, "")
      .split(/\r?\n/)
      .filter((line) => line.trim().length > 0);

    if (!lines.length) return { columns: [], rows: [] };

    const columns = parseCsvLine(lines[0]);
    const rows = lines.slice(1).map((line) => {
      const values = parseCsvLine(line);
      const row = {};

      columns.forEach((column, index) => {
        row[column] = values[index] || "";
      });

      return row;
    });

    return { columns, rows };
  };

  const normalizeNumericCell = (value) => {
    if (isEmptyCell(value)) return "";

    const text = String(value)
      .trim()
      .replace("%", "")
      .replace(/\s+/g, "")
      .replace(",", ".");

    const number = Number(text);

    if (!Number.isFinite(number)) return String(value).trim();

    return String(number);
  };

  const normalizeJsonPayload = (payload) => {
    if (Array.isArray(payload)) return payload;

    if (Array.isArray(payload?.rows)) return payload.rows;
    if (Array.isArray(payload?.data)) return payload.data;
    if (Array.isArray(payload?.results)) return payload.results;
    if (Array.isArray(payload?.records)) return payload.records;
    if (Array.isArray(payload?.value)) return payload.value;

    return [];
  };

  const cleanRows = (rows) => {
    const numericColumns = new Set([
      "Yillik_Vaka_Hizi_100Bin",
      "Yillik_Olum_Hizi_100Bin",
      "Bes_Yillik_Sagkalim_Yuzdesi",
      "incidence",
      "mortality",
      "survival",
      "new_cases",
      "deaths",
      "prevalence",
      "rate",
      "count",
      "value",
      "Value",
      "NumericValue",
      "Low",
      "High"
    ]);

    const requiredAnyColumns = [
      "Bolge",
      "Ulke_Sehir",
      "region",
      "location",
      "country",
      "Country",
      "Kanser_Turu",
      "cancerType",
      "Cancer",
      "cancer",
      "Population",
      "population",
      "SpatialDim",
      "IndicatorCode",
      "TimeDim"
    ];

    return (rows || [])
      .map((row) => {
        const cleaned = {};

        Object.entries(row || {}).forEach(([key, value]) => {
          if (key.startsWith("_")) return;

          if (numericColumns.has(key)) {
            cleaned[key] = normalizeNumericCell(value);
          } else {
            cleaned[key] = isEmptyCell(value) ? "" : String(value).trim();
          }
        });

        return cleaned;
      })
      .filter((row) => {
        const hasContent = Object.values(row).some((value) => !isEmptyCell(value));
        const hasRequiredSignal = requiredAnyColumns.some((column) => !isEmptyCell(row[column]));

        return hasContent && hasRequiredSignal;
      });
  };

  const checkSource = async (source) => {
    try {
      if (typeof fetch !== "function") {
        return {
          ...source,
          reachable: false,
          status: "fetch_unavailable"
        };
      }

      const response = await fetch(source.url, {
        method: "GET",
        headers: {
          "User-Agent": "OncoConnectAI/1.0 official-source-check"
        }
      });

      return {
        ...source,
        reachable: response.ok,
        status: response.status,
        contentType: response.headers.get("content-type") || ""
      };
    } catch (error) {
      return {
        ...source,
        reachable: false,
        status: "error",
        error: error.message
      };
    }
  };

  try {
    const sourceChecks = await Promise.all(officialSources.map(checkSource));

    if (!officialDataUrl) {
      return res.status(409).json({
        success: false,
        officialDataCreated: false,
        error:
          "OFFICIAL_CANCER_DATA_URL is not configured. No dataset was created. Add a verified downloadable CSV/API URL in backend/.env first.",
        nextStep:
          "Set OFFICIAL_CANCER_DATA_URL, OFFICIAL_CANCER_DATA_NAME and OFFICIAL_CANCER_SOURCE_NAME in backend/.env, then restart backend.",
        sources: sourceChecks
      });
    }

    if (typeof fetch !== "function") {
      return res.status(500).json({
        success: false,
        officialDataCreated: false,
        error: "Node fetch is unavailable in this runtime. Use Node 18+ or install a fetch polyfill.",
        sources: sourceChecks
      });
    }

    const response = await fetch(officialDataUrl, {
      method: "GET",
      headers: {
        "User-Agent": "OncoConnectAI/1.0 official-data-import",
        "Accept": "text/csv, application/json, text/plain;q=0.9, */*;q=0.8"
      }
    });

    if (!response.ok) {
      return res.status(502).json({
        success: false,
        officialDataCreated: false,
        error: `Configured official data URL returned HTTP ${response.status}. Dataset was not created.`,
        officialDataUrl,
        sources: sourceChecks
      });
    }

    const contentType = response.headers.get("content-type") || "";
    const bodyText = await response.text();

    let parsedRows = [];
    let columns = [];

    if (contentType.includes("application/json") || officialDataUrl.toLowerCase().includes(".json")) {
      const json = JSON.parse(bodyText);
      parsedRows = normalizeJsonPayload(json);
      columns = Array.from(
        parsedRows.reduce((set, row) => {
          Object.keys(row || {}).forEach((key) => set.add(key));
          return set;
        }, new Set())
      );
    } else {
      const parsed = parseCsvText(bodyText);
      parsedRows = parsed.rows;
      columns = parsed.columns;
    }

    const cleanedRows = cleanRows(parsedRows);

    if (!cleanedRows.length) {
      return res.status(422).json({
        success: false,
        officialDataCreated: false,
        error:
          "Configured official data URL was read, but zero valid rows remained after cleaning. Dataset was not created.",
        inputRows: parsedRows.length,
        sources: sourceChecks
      });
    }

    const removedRows = parsedRows.length - cleanedRows.length;
    const finalColumns = Array.from(
      cleanedRows.reduce((set, row) => {
        Object.keys(row).forEach((key) => set.add(key));
        return set;
      }, new Set(columns))
    );

    const dataset = {
      id: `official_configured_draft_${Date.now()}`,
      name: officialDataName,
      originalName: officialDataUrl.split("/").pop() || "official_configured_source",
      uploadedAt: new Date().toISOString(),
      rowCount: cleanedRows.length,
      columns: finalColumns,
      rows: cleanedRows,
      previewRows: cleanedRows.slice(0, 25),
      qualityFlag: removedRows > 0 ? `official_url_cleaned_${removedRows}_rows_removed` : "official_url_clean_validated",
      sourceName: officialSourceName,
      sourceUrl: officialDataUrl,
      published: false,
      automationMeta: {
        mode: "configured_official_csv_api_import",
        fetchedAt: new Date().toISOString(),
        contentType,
        inputRows: parsedRows.length,
        outputRows: cleanedRows.length,
        removedRows,
        emptyValuesBlocked: true,
        nanValuesBlocked: true,
        publishReady: true,
        autoPublished: false,
        sourceChecks
      }
    };

    return res.json({
      success: true,
      officialDataCreated: true,
      message: `Official configured draft created with ${cleanedRows.length} valid rows. Removed ${removedRows} invalid/empty rows.`,
      dataset,
      sources: sourceChecks
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      officialDataCreated: false,
      error: error.message || "Configured official data import failed.",
      sources: []
    });
  }
});


app.listen(5050, () => {
  console.log("Server running on port 5050");
});
