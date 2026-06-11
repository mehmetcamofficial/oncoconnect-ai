import React, { useEffect, useMemo, useState } from "react";
import "./App.css";





const ONCOCONNECT_CARE_JOURNEY_DOM_FIX_V131 = `
html body .onco-care-journey-fixed-v131 {
  position: relative !important;
  padding-top: 28px !important;
}

html body .onco-care-journey-title-v131 {
  display: block !important;
  position: relative !important;
  z-index: 20 !important;
  margin: 0 0 34px 0 !important;
  padding: 0 !important;
  line-height: 1.15 !important;
  background: transparent !important;
}

html body .onco-care-journey-title-v131 + * {
  margin-top: 8px !important;
}

html body .onco-care-journey-fixed-v131 [class*="step"],
html body .onco-care-journey-fixed-v131 [class*="journey"] {
  position: relative !important;
}
`;

function applyOncoCareJourneyDomFixV131() {
  if (typeof document === "undefined") return;

  if (!document.getElementById("onco-care-journey-dom-fix-v131")) {
    const style = document.createElement("style");
    style.id = "onco-care-journey-dom-fix-v131";
    style.textContent = ONCOCONNECT_CARE_JOURNEY_DOM_FIX_V131;
    document.head.appendChild(style);
  }

  const candidates = Array.from(document.querySelectorAll("h1,h2,h3,h4,b,strong,div,span"));
  const title = candidates.find((el) =>
    (el.textContent || "").trim() === "Your Care Journey at a Glance"
  );

  if (!title) return;

  title.classList.add("onco-care-journey-title-v131");

  const card =
    title.closest("section") ||
    title.closest("article") ||
    title.parentElement;

  if (card) {
    card.classList.add("onco-care-journey-fixed-v131");
  }

  const next = title.nextElementSibling;
  if (next) {
    next.style.marginTop = "10px";
    next.style.position = "relative";
    next.style.zIndex = "5";
  }
}

if (typeof window !== "undefined") {
  window.setTimeout(applyOncoCareJourneyDomFixV131, 50);
  window.setTimeout(applyOncoCareJourneyDomFixV131, 300);
  window.setTimeout(applyOncoCareJourneyDomFixV131, 900);
  window.addEventListener("load", applyOncoCareJourneyDomFixV131);
}


const ONCOCONNECT_CARE_JOURNEY_TITLE_FIX_V130 = `
html body .care-journey-v42,
html body .care-journey-v43,
html body [class*="care-journey"] {
  position: relative !important;
  padding-top: 34px !important;
}

html body .care-journey-v42 h3,
html body .care-journey-v43 h3,
html body [class*="care-journey"] h3 {
  position: relative !important;
  z-index: 5 !important;
  margin: 0 0 22px 0 !important;
  padding-left: 0 !important;
  line-height: 1.12 !important;
}

html body .care-journey-v42 > div,
html body .care-journey-v43 > div,
html body [class*="care-journey"] > div {
  position: relative !important;
  z-index: 2 !important;
}

html body .care-journey-v42 .journey-step,
html body .care-journey-v43 .journey-step,
html body [class*="journey"] .journey-step {
  margin-top: 0 !important;
}
`;

if (typeof document !== "undefined" && !document.getElementById("onco-care-journey-title-fix-v130")) {
  const style = document.createElement("style");
  style.id = "onco-care-journey-title-fix-v130";
  style.textContent = ONCOCONNECT_CARE_JOURNEY_TITLE_FIX_V130;
  document.head.appendChild(style);
}





const ONCOCONNECT_JOURNEY_COMPACT_FIX_V134 = `
html body .cc-journey-v42 {
  padding: 20px 30px 18px 30px !important;
  min-height: 118px !important;
  gap: 18px !important;
  align-items: start !important;
}

html body .cc-journey-title-v133 {
  margin: 0 0 12px 0 !important;
  font-size: 19px !important;
  line-height: 1.05 !important;
}

html body .cc-journey-v42 > div {
  gap: 3px !important;
}

html body .cc-journey-v42 > div > b {
  width: 46px !important;
  height: 46px !important;
  min-width: 46px !important;
  min-height: 46px !important;
  margin-bottom: 8px !important;
  font-size: 19px !important;
}

html body .cc-journey-v42 > div > span {
  font-size: 15px !important;
  line-height: 1.05 !important;
}

html body .cc-journey-v42 > div > small {
  font-size: 11.5px !important;
  line-height: 1.1 !important;
}
`;

if (typeof document !== "undefined" && !document.getElementById("onco-journey-compact-fix-v134")) {
  const style = document.createElement("style");
  style.id = "onco-journey-compact-fix-v134";
  style.textContent = ONCOCONNECT_JOURNEY_COMPACT_FIX_V134;
  document.head.appendChild(style);
}


const ONCOCONNECT_JOURNEY_REAL_TITLE_FIX_V133 = `
html body .cc-journey-v42 {
  position: relative !important;
  display: grid !important;
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  gap: 22px !important;
  align-items: start !important;
  padding: 28px 34px 26px 34px !important;
  min-height: 150px !important;
}

html body .cc-journey-v42::before {
  content: none !important;
  display: none !important;
}

html body .cc-journey-title-v133 {
  grid-column: 1 / -1 !important;
  margin: 0 0 8px 0 !important;
  padding: 0 !important;
  font-size: 20px !important;
  line-height: 1.1 !important;
  font-weight: 900 !important;
  color: #0f172a !important;
  position: relative !important;
  z-index: 10 !important;
}

html body .cc-journey-v42 > div {
  position: relative !important;
  z-index: 2 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  gap: 4px !important;
  min-width: 0 !important;
}

html body .cc-journey-v42 > div > b {
  width: 52px !important;
  height: 52px !important;
  min-width: 52px !important;
  min-height: 52px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 999px !important;
  margin-bottom: 10px !important;
}

html body .cc-journey-v42 > div > span {
  display: block !important;
  font-size: 16px !important;
  line-height: 1.05 !important;
  font-weight: 900 !important;
  color: #0f172a !important;
}

html body .cc-journey-v42 > div > small {
  display: block !important;
  font-size: 12px !important;
  line-height: 1.15 !important;
  font-weight: 750 !important;
  color: #64748b !important;
}
`;

if (typeof document !== "undefined" && !document.getElementById("onco-journey-real-title-fix-v133")) {
  const style = document.createElement("style");
  style.id = "onco-journey-real-title-fix-v133";
  style.textContent = ONCOCONNECT_JOURNEY_REAL_TITLE_FIX_V133;
  document.head.appendChild(style);
}


const ONCOCONNECT_CC_JOURNEY_DIRECT_FIX_V132 = `
html body .cc-journey-v42 {
  position: relative !important;
  padding: 54px 28px 24px 28px !important;
  display: grid !important;
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  align-items: start !important;
  gap: 22px !important;
  min-height: 160px !important;
}

html body .cc-journey-v42::before {
  content: "Your Care Journey at a Glance" !important;
  position: absolute !important;
  left: 28px !important;
  top: 20px !important;
  z-index: 5 !important;
  font-size: 20px !important;
  line-height: 1.1 !important;
  font-weight: 900 !important;
  color: #0f172a !important;
  white-space: nowrap !important;
  pointer-events: none !important;
}

html body .cc-journey-v42 > div {
  position: relative !important;
  z-index: 2 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  gap: 4px !important;
  min-width: 0 !important;
}

html body .cc-journey-v42 > div > b {
  width: 52px !important;
  height: 52px !important;
  min-width: 52px !important;
  min-height: 52px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 999px !important;
  margin-bottom: 10px !important;
  position: relative !important;
  z-index: 2 !important;
}

html body .cc-journey-v42 > div > span {
  display: block !important;
  font-size: 16px !important;
  line-height: 1.05 !important;
  font-weight: 900 !important;
  color: #0f172a !important;
}

html body .cc-journey-v42 > div > small {
  display: block !important;
  font-size: 12px !important;
  line-height: 1.15 !important;
  font-weight: 750 !important;
  color: #64748b !important;
}
`;

if (typeof document !== "undefined" && !document.getElementById("onco-cc-journey-direct-fix-v132")) {
  const style = document.createElement("style");
  style.id = "onco-cc-journey-direct-fix-v132";
  style.textContent = ONCOCONNECT_CC_JOURNEY_DIRECT_FIX_V132;
  document.head.appendChild(style);
}


const ONCOCONNECT_COMPACT_RUNTIME_STYLE_V124 = `
html body .cc-mid-v42 {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) !important;
  align-items: start !important;
  gap: 16px !important;
  margin-bottom: 14px !important;
}

html body .cc-mid-v42 .cc-trend-v42,
html body .cc-mid-v42 .cc-score-v42 {
  height: 330px !important;
  min-height: 330px !important;
  max-height: 330px !important;
  overflow: hidden !important;
  align-self: start !important;
  padding: 16px 20px !important;
}

html body .cc-trend-v42 .trend-head-v51 {
  margin-bottom: 0 !important;
}

html body .cc-trend-v42 h3 {
  margin: 0 0 6px !important;
  line-height: 1.02 !important;
}

html body .cc-trend-v42 p {
  margin: 0 !important;
  line-height: 1.05 !important;
}

html body .cc-trend-v42 .trend-chart-v51 {
  width: 100% !important;
  height: 175px !important;
  max-height: 175px !important;
  margin: 0 !important;
  display: block !important;
  transform: translateY(-4px) !important;
}

html body .cc-trend-v42 .trend-legend-v51 {
  margin-top: -2px !important;
  padding-top: 0 !important;
}

html body .cc-score-v42 .cc-card-title-v42 {
  margin-bottom: 8px !important;
}

html body .cc-score-v42 .cc-score-body-v42 {
  margin-top: 6px !important;
  gap: 18px !important;
  align-items: center !important;
  display: grid !important;
  grid-template-columns: 118px minmax(0, 1fr) !important;
}

html body .cc-score-v42 .cc-donut-v42 {
  width: 112px !important;
  height: 112px !important;
  min-width: 112px !important;
}

html body .cc-score-v42 .cc-score-body-v42 ul,
html body .cc-score-v42 .cc-score-body-v42 li {
  min-width: 0 !important;
}

html body .cc-score-v42 .cc-score-body-v42 li {
  gap: 10px !important;
  padding: 7px 0 !important;
}

html body .cc-score-v42 .cc-score-body-v42 li span {
  white-space: normal !important;
  line-height: 1.1 !important;
}

html body .cc-score-v42 .cc-score-guide-v42 {
  margin-top: 10px !important;
  gap: 12px !important;
}

html body .cc-score-v42 .cc-score-guide-v42 div {
  min-width: 0 !important;
}

html body .cc-network-v42 {
  margin-top: 0 !important;
}

html body .cc-journey-v42 {
  margin-top: 10px !important;
  min-height: 96px !important;
  padding: 16px 24px !important;
}
`;

if (typeof document !== "undefined" && !document.getElementById("onco-compact-runtime-style-v124")) {
  const style = document.createElement("style");
  style.id = "onco-compact-runtime-style-v124";
  style.textContent = ONCOCONNECT_COMPACT_RUNTIME_STYLE_V124;
  document.head.appendChild(style);
}


// ONCOCONNECT_API_BASE_V1
// Uses the hosted API in production and localhost during local development.
const API =
  import.meta.env.VITE_API_BASE_URL?.replace(/\/$/, "") ||
  "http://localhost:5050";

function safeNumber(value, fallback = 0) {
  const cleaned = String(value ?? "").replace(",", ".").trim();
  const n = Number(cleaned);
  return Number.isFinite(n) ? n : fallback;
}

function App() {

  if (typeof window !== "undefined" && !window.__oncoconnectAdminPublishedBridge) {
    window.__oncoconnectAdminPublishedBridge = true;

    const originalFetch = window.fetch.bind(window);
    const PUBLISHED_ROWS_KEY = "oncoconnect_published_cancer_rows_v1";

    const getAdminPublishedRows = () => {
      try {
        const raw = localStorage.getItem(PUBLISHED_ROWS_KEY);

        if (raw === null) {
          return null;
        }

        const parsed = JSON.parse(raw);
        return Array.isArray(parsed) ? parsed : [];
      } catch {
        return [];
      }
    };

    const csvEscape = (value) => {
      const text = String(value ?? "");

      if (/[",\n\r]/.test(text)) {
        return `"${text.replace(/"/g, '""')}"`;
      }

      return text;
    };

    const rowsToCsv = (rows) => {
      const fallbackColumns = [
        "Bolge",
        "Ulke_Sehir",
        "Cinsiyet",
        "Kanser_Turu",
        "Yas_Grubu",
        "Yillik_Vaka_Hizi_100Bin",
        "Yillik_Olum_Hizi_100Bin",
        "Bes_Yillik_Sagkalim_Yuzdesi"
      ];

      const columns = rows.length
        ? Array.from(
            rows.reduce((set, row) => {
              Object.keys(row || {})
                .filter((key) => !key.startsWith("_"))
                .forEach((key) => set.add(key));

              return set;
            }, new Set())
          )
        : fallbackColumns;

      const header = columns.map(csvEscape).join(",");
      const body = rows.map((row) =>
        columns.map((column) => csvEscape(row?.[column])).join(",")
      );

      return [header, ...body].join("\n");
    };

    window.fetch = async (input, init) => {
      const url = typeof input === "string" ? input : input?.url || "";
      const publishedRows = getAdminPublishedRows();

      const isCancerCsvRequest =
        url.includes("turkiye_avrupa_kanser_istatistikleri_detayli.csv") ||
        url.includes("/public/map-data.csv");

      const isCancerJsonRequest =
        url.includes("/public/map-data") &&
        !url.includes(".csv");

      if (publishedRows !== null && isCancerCsvRequest) {
        return new Response(rowsToCsv(publishedRows), {
          status: 200,
          headers: {
            "Content-Type": "text/csv; charset=utf-8",
            "X-OncoConnect-Source": "admin-published-localStorage"
          }
        });
      }

      if (publishedRows !== null && isCancerJsonRequest) {
        return new Response(JSON.stringify({
          success: true,
          source: "admin-published-localStorage",
          rows: publishedRows,
          data: publishedRows,
          datasets: [],
          count: publishedRows.length
        }), {
          status: 200,
          headers: {
            "Content-Type": "application/json; charset=utf-8",
            "X-OncoConnect-Source": "admin-published-localStorage"
          }
        });
      }

      return originalFetch(input, init);
    };
  }


  const [page, setPage] = useState("landing");
  const [showAllVisibleCancerRows, setShowAllVisibleCancerRows] = useState(false);
  const [lang, setLang] = useState("en");
  // CRITICAL REAL I18N v1 START
  const trText = (en, tr) => (lang === "tr" ? tr : en);
  // CRITICAL REAL I18N v1 END

  const t = {
    langLabel: lang === "tr" ? "Dil" : "Language",
    home: lang === "tr" ? "Ana Sayfa" : "Home",
    admin: lang === "tr" ? "Admin Panel" : "Admin Panel",
    map: lang === "tr" ? "Harita" : "Map",
    kids: "Onco Kids",
  };




  const LandingMapPreview = () => {
    const [previewMap, setPreviewMap] = useState("turkiye");
    const [activePin, setActivePin] = useState("ankara");

    const pinData = {
      turkiye: [
        {
          id: "istanbul",
          label: "İstanbul",
          x: 30,
          y: 39,
          title: "İstanbul cancer support signal",
          metric: "High-population city layer",
          value: "Urban monitoring point",
          text: "This card shows how a city pin can open a quick cancer burden explanation before the user enters the full interactive map.",
          action: "Open full map for all Türkiye pins"
        },
        {
          id: "ankara",
          label: "Ankara",
          x: 48,
          y: 47,
          title: trText("Ankara national comparison signal", "Ankara ulusal karşılaştırma sinyali"),
          metric: "Central coordination layer",
          value: "Türkiye benchmark point",
          text: trText("A central Türkiye pin for explaining national comparison, public indicators and regional cancer intelligence in a simple card.", "Ulusal karşılaştırma, kamu göstergeleri ve bölgesel kanser zekâsını sade bir kartta açıklamak için merkezi Türkiye işareti."),
          action: trText("Open full map for deeper comparison", "Daha derin karşılaştırma için tam haritayı aç")
        },
        {
          id: "izmir",
          label: "İzmir",
          x: 25,
          y: 58,
          title: "İzmir regional outreach signal",
          metric: "Aegean regional layer",
          value: "Local awareness point",
          text: "A local showcase card for demonstrating how regional cancer signals can support awareness, navigation and outreach planning.",
          action: "Open full map to inspect regional data"
        }
      ],
      europe: [
        {
          id: "germany",
          label: "Germany",
          x: 52,
          y: 45,
          title: "Germany benchmark signal",
          metric: "Central Europe comparison",
          value: "Country-level indicator",
          text: "A European country pin showing how the same map interface supports country-level public cancer burden comparison.",
          action: "Open full Europe map"
        },
        {
          id: "france",
          label: "France",
          x: 42,
          y: 55,
          title: "France comparison signal",
          metric: "Western Europe layer",
          value: "Cross-country insight",
          text: "This card explains the Europe layer before users open the full map for broader cancer intelligence exploration.",
          action: "Open full map for country comparison"
        },
        {
          id: "turkiye-europe",
          label: "Türkiye",
          x: 67,
          y: 64,
          title: "Türkiye–Europe bridge signal",
          metric: "Regional bridge layer",
          value: "Cross-region comparison",
          text: "A bridge point connecting Türkiye-focused indicators with the wider Europe comparison layer.",
          action: "Open full map for Türkiye and Europe"
        }
      ]
    };

    const pins = pinData[previewMap];
    const active = pins.find((pin) => pin.id === activePin) || pins[0];

    const switchPreviewMap = (nextMap) => {
      setPreviewMap(nextMap);
      setActivePin(pinData[nextMap][0].id);
    };

    return (
      <section className="landing-map-compact-v51 landing-active-map-v58">
        <div className="landing-map-copy-v51">
          <p>{trText("PUBLIC MAP PREVIEW", "KAMU HARİTA ÖNİZLEMESİ")}</p>
          <h2>{trText("Türkiye and Europe map intelligence", "Türkiye ve Avrupa harita zekâsı")}</h2>
          <span>
            {trText("Click a glowing city or country pin to preview what the full interactive map explains.", "Tam interaktif haritanın ne anlattığını görmek için parlayan şehir veya ülke işaretine tıklayın.")}
          </span>

          <div className="landing-map-switch-v51">
            <button
              type="button"
              className={previewMap === "turkiye" ? "active" : ""}
              onClick={() => switchPreviewMap("turkiye")}
            >
              {trText("Türkiye map", "Türkiye haritası")}
            </button>
            <button
              type="button"
              className={previewMap === "europe" ? "active" : ""}
              onClick={() => switchPreviewMap("europe")}
            >
              {trText("Europe map", "Avrupa haritası")}
            </button>
            <button type="button" onClick={() => setPage("map")}>
              {trText("Open full map", "Tam haritayı aç")}
            </button>
          </div>
        </div>

        <div className="landing-map-stage-v51 landing-active-map-stage-v58">
          <img
            src={previewMap === "turkiye" ? "/assets/map-turkiye.png" : "/assets/map-europe.png"}
            alt={previewMap === "turkiye" ? "Türkiye cancer map preview" : "Europe cancer map preview"}
          />

          {pins.map((pin) => (
            <button
              type="button"
              key={pin.id}
              className={`landing-active-pin-v58 ${activePin === pin.id ? "active" : ""}`}
              style={{ left: `${pin.x}%`, top: `${pin.y}%` }}
              onClick={() => setActivePin(pin.id)}
            >
              <i></i>
              <span>{pin.label}</span>
            </button>
          ))}

          <div className="landing-active-map-card-v58">
            <small>{active.metric}</small>
            <h3>{active.title}</h3>
            <b>{active.value}</b>
            <p>{active.text}</p>
            <button type="button" onClick={() => setPage("map")}>
              {active.action}
            </button>
          </div>
        </div>
      </section>
    );
  };



  const LandingDataDashboard = () => {
    const [landingMetric, setLandingMetric] = useState("cases");
    const [landingRegion, setLandingRegion] = useState("turkiye");
    const [showAllLandingDataRows, setShowAllLandingDataRows] = useState(false);
    const [landingRows, setLandingRows] = useState([]);
    const [officialRows, setOfficialRows] = useState([]);

    const parseCsvLine = (line) => {
      const result = [];
      let current = "";
      let insideQuotes = false;

      for (let i = 0; i < line.length; i++) {
        const char = line[i];
        const next = line[i + 1];

        if (char === '"' && insideQuotes && next === '"') {
          current += '"';
          i++;
        } else if (char === '"') {
          insideQuotes = !insideQuotes;
        } else if ((char === "," || char === ";") && !insideQuotes) {
          result.push(current.trim());
          current = "";
        } else {
          current += char;
        }
      }

      result.push(current.trim());
      return result;
    };

    const parseCsv = (text) => {
      const lines = text.replace(/\r/g, "").split("\n").filter(Boolean);
      if (lines.length < 2) return [];
      const headers = parseCsvLine(lines[0]);

      return lines.slice(1).map((line) => {
        const values = parseCsvLine(line);
        const row = {};
        headers.forEach((header, index) => {
          row[header] = values[index] ?? "";
        });
        return row;
      });
    };

    const toNumber = (value) => {
      const n = Number(String(value ?? "").replace(",", ".").trim());
      return Number.isFinite(n) ? n : null;
    };

    const ascii = (value) =>
      String(value || "")
        .toLowerCase()
        .replaceAll("ı", "i")
        .replaceAll("ğ", "g")
        .replaceAll("ü", "u")
        .replaceAll("ş", "s")
        .replaceAll("ö", "o")
        .replaceAll("ç", "c")
        .replaceAll("İ", "i");

    const turkiyeCitySet = new Set([
      "adana","adiyaman","afyonkarahisar","agri","amasya","ankara","antalya","artvin","aydin","balikesir",
      "bilecik","bingol","bitlis","bolu","burdur","bursa","canakkale","cankiri","corum","denizli",
      "diyarbakir","edirne","elazig","erzincan","erzurum","eskisehir","gaziantep","giresun","gumushane",
      "hakkari","hatay","isparta","mersin","istanbul","izmir","kars","kastamonu","kayseri","kirklareli",
      "kirsehir","kocaeli","konya","kutahya","malatya","manisa","kahramanmaras","mardin","mugla","mus",
      "nevsehir","nigde","ordu","rize","sakarya","samsun","siirt","sinop","sivas","tekirdag","tokat",
      "trabzon","tunceli","sanliurfa","usak","van","yozgat","zonguldak","aksaray","bayburt","karaman",
      "kirikkale","batman","sirnak","bartin","ardahan","igdir","yalova","karabuk","kilis","osmaniye","duzce"
    ]);

    useEffect(() => {
      async function loadLandingCsv() {
        try {
          const res = await fetch("/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv");
          const text = await res.text();
          const parsed = parseCsv(text);
          setLandingRows(parsed);
        } catch {
          setLandingRows([]);
        }

        try {
          const officialRes = await fetch("/data/official_cancer_sources.csv");
          const officialText = await officialRes.text();
          const officialParsed = parseCsv(officialText);
          setOfficialRows(officialParsed);
        } catch {
          setOfficialRows([]);
        }
      }

      loadLandingCsv();
    }, []);

    const normalized = landingRows.map((row) => {
      const area = row.Ulke_Sehir || row.city || row.country || row.area || "";
      const region = row.Bolge || row.region || "";
      const areaAscii = ascii(area);
      const isTurkey =
        ascii(region).includes("turkiye") ||
        ascii(region).includes("turkey") ||
        turkiyeCitySet.has(areaAscii);

      return {
        area,
        region: isTurkey ? "turkiye" : "europe",
        cancer: row.Kanser_Turu || "Mixed",
        sex: row.Cinsiyet || "All",
        age: row.Yas_Grubu || "All",
        cases: toNumber(row.Yillik_Vaka_Hizi_100Bin),
        deaths: toNumber(row.Yillik_Olum_Hizi_100Bin),
        survival: toNumber(row.Bes_Yillik_Sagkalim_Yuzdesi)
      };
    }).filter((row) => row.area);

    const grouped = (() => {
      const map = new Map();

      normalized
        .filter((row) => row.region === landingRegion)
        .forEach((row) => {
          const item = map.get(row.area) || {
            area: row.area,
            rows: 0,
            cases: [],
            deaths: [],
            survival: [],
            cancers: new Set()
          };

          item.rows += 1;
          if (Number.isFinite(row.cases)) item.cases.push(row.cases);
          if (Number.isFinite(row.deaths)) item.deaths.push(row.deaths);
          if (Number.isFinite(row.survival)) item.survival.push(row.survival);
          if (row.cancer) item.cancers.add(row.cancer);
          map.set(row.area, item);
        });

      const avg = (arr) => arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : null;

      return Array.from(map.values()).map((item) => ({
        area: item.area,
        rows: item.rows,
        cases: avg(item.cases),
        deaths: avg(item.deaths),
        survival: avg(item.survival),
        cancers: Array.from(item.cancers)
      }));
    })();

    const ranked = [...grouped].sort((a, b) => {
      const av = a[landingMetric] ?? -Infinity;
      const bv = b[landingMetric] ?? -Infinity;
      return landingMetric === "survival" ? av - bv : bv - av;
    }).slice(0, 12);

    const metricLabel = {
      cases: "New cases",
      deaths: "Deaths",
      survival: "5-year prevalence"
    };

    const researchFeed = [
      {
        type: "Clinical trial",
        title: trText("Immunotherapy and targeted combinations", "İmmünoterapi ve hedefe yönelik kombinasyonlar"),
        source: trText("ClinicalTrials.gov", "ClinicalTrials.gov"),
        badge: trText("Trials", "Klinik çalışmalar"),
        summary: trText("Tracks oncology studies involving checkpoint inhibitors, combination regimens and biomarker-selected treatment arms.", "Kontrol noktası inhibitörleri, kombinasyon rejimleri ve biyobelirteç seçimli tedavi kollarını içeren onkoloji çalışmalarını izler."),
        meta: trText("Solid tumors · Hematology · Recruitment", "Solid tümörler · Hematoloji · Hasta alımı")
      },
      {
        type: "Innovative drug",
        title: trText("Antibody-drug conjugate pipeline", "Antikor-ilaç konjugatı geliştirme hattı"),
        source: trText("ESMO / ASCO coverage", "ESMO / ASCO kapsamı"),
        badge: trText("Drug updates", "İlaç güncellemeleri"),
        summary: trText("Emerging ADC strategies across breast, lung, gastric and colorectal cancer, including HER2-low and target-specific approaches.", "Meme, akciğer, mide ve kolorektal kanserde HER2-low ve hedefe özgü yaklaşımlar dahil yeni ADC stratejileri."),
        meta: trText("ADC · HER2 · Trop-2 · Breast · Lung", "ADC · HER2 · Trop-2 · Meme · Akciğer")
      },
      {
        type: "Research article",
        title: trText("Early detection and ctDNA monitoring", "Erken tanı ve ctDNA izleme"),
        source: trText("Nature Medicine / NEJM", "Nature Medicine / NEJM"),
        badge: trText("Research", "Araştırma"),
        summary: trText("Liquid biopsy, minimal residual disease, recurrence monitoring and stratified follow-up pathways.", "Sıvı biyopsi, minimal rezidüel hastalık, nüks izleme ve katmanlı takip yolları."),
        meta: trText("ctDNA · MRD · Screening · Follow-up", "ctDNA · MRD · Tarama · Takip")
      },
      {
        type: "Funding call",
        title: trText("Cancer research grants and innovation funds", "Kanser araştırma hibeleri ve inovasyon fonları"),
        source: trText("EU4Health / Horizon Europe / Mission Cancer", "EU4Health / Horizon Europe / Kanser Misyonu"),
        badge: trText("Funding", "Fonlama"),
        summary: trText("Potential grant and consortium opportunities for prevention, screening, data infrastructure and patient-support innovation.", "Önleme, tarama, veri altyapısı ve hasta destek inovasyonu için potansiyel hibe ve konsorsiyum fırsatları."),
        meta: trText("EU grants · Mission Cancer · NGOs · Research", "AB hibeleri · Kanser Misyonu · STK’lar · Araştırma")
      },
      {
        type: "Precision medicine",
        title: trText("Molecular tumor boards and biomarker pathways", "Moleküler tümör konseyleri ve biyobelirteç yolları"),
        source: trText("ESMO Precision Medicine", "ESMO Hassas Tıp"),
        badge: trText("Precision", "Hassas tıp"),
        summary: trText("Clinical decision pathways using genomic profiling, molecular boards and targeted therapy matching.", "Genomik profilleme, moleküler konseyler ve hedefe yönelik tedavi eşleştirmesi kullanan klinik karar yolları."),
        meta: trText("NGS · Biomarkers · Targeted therapy", "NGS · Biyobelirteçler · Hedefe yönelik tedavi")
      },
      {
        type: "AI oncology",
        title: trText("AI-assisted cancer navigation and triage", "AI destekli kanser yönlendirme ve triyaj"),
        source: trText("Digital health research", "Dijital sağlık araştırması"),
        badge: "AI",
        summary: trText("Decision-support tools for symptom burden, care navigation, research awareness and operational monitoring.", "Semptom yükü, bakım yönlendirme, araştırma farkındalığı ve operasyonel izleme için karar destek araçları."),
        meta: trText("AI copilot · Triage · Monitoring", "AI yardımcı pilot · Triyaj · İzleme")
      },
      {
        type: "Screening innovation",
        title: trText("Population screening and early diagnosis", "Toplum taraması ve erken tanı"),
        source: trText("CanScreen5 / WHO / IARC", "CanScreen5 / WHO / IARC"),
        badge: trText("Screening", "Tarama"),
        summary: trText("Organized screening pathways, participation indicators, early diagnosis and public-health coordination.", "Organize tarama yolları, katılım göstergeleri, erken tanı ve halk sağlığı koordinasyonu."),
        meta: trText("Breast · Cervical · Colorectal", "Meme · Serviks · Kolorektal")
      },
      {
        type: "Supportive care",
        title: trText("Symptom management and survivorship", "Semptom yönetimi ve sağkalım sonrası bakım"),
        source: trText("JCO / Lancet Oncology", "JCO / Lancet Oncology"),
        badge: trText("Care", "Bakım"),
        summary: trText("Fatigue, pain, appetite, psycho-oncology and caregiver support pathways for better quality of life.", "Yorgunluk, ağrı, iştah, psiko-onkoloji ve bakım veren destek yollarıyla daha iyi yaşam kalitesi."),
        meta: trText("Survivorship · Quality of life · Caregiver", "Sağkalım sonrası bakım · Yaşam kalitesi · Bakım veren")
      }
    ];

    const prettyOfficialIndicator = (indicator = "") => {
      const normalized = String(indicator)
        .replaceAll("_", " ")
        .replace(/\bcount\b/gi, "")
        .replace(/\brate per 100000\b/gi, "")
        .trim();

      const custom = {
        "new cases": "Türkiye national new cases",
        "deaths": "Türkiye national deaths",
        "five year prevalence": "Türkiye 5-year prevalence",
        "overall incidence": "Overall incidence rate",
        "overall mortality": "Overall mortality rate",
        "female breast incidence": "Female breast incidence rate",
        "female breast mortality": "Female breast mortality rate",
        "male lung incidence": "Male lung incidence rate"
      };

      return custom[normalized] || normalized.replace(/\b\w/g, (c) => c.toUpperCase());
    };

    const prettyUnit = (unit = "") => {
      const u = String(unit).toLowerCase();
      if (u === "count") return "cases";
      if (u === "rate_per_100000") return "/100k";
      return unit;
    };

    const formatOfficialValue = (value, unit = "") => {
      const n = Number(String(value || "0").replace(",", "."));
      if (!Number.isFinite(n)) return value;

      if (String(unit).toLowerCase() === "count") {
        return new Intl.NumberFormat("tr-TR").format(n);
      }

      if (String(unit).toLowerCase() === "rate_per_100000") {
        return new Intl.NumberFormat("tr-TR", {
          minimumFractionDigits: 0,
          maximumFractionDigits: 1
        }).format(n);
      }

      return new Intl.NumberFormat("tr-TR").format(n);
    };


    const metricSuffix = {
      cases: " / 100K",
      deaths: " / 100K",
      survival: "%"
    };

    const formatValue = (value) => {
      if (!Number.isFinite(value)) return "-";
      return landingMetric === "survival" ? `${value.toFixed(0)}%` : value.toFixed(1);
    };

    const maxValue = Math.max(...ranked.map((row) => row[landingMetric] || 0), 1);

    const unifiedOfficialRows = officialRows
      .filter((row) => {
        const indicator = String(row.indicator || "").toLowerCase();

        if (landingMetric === "cases") {
          return indicator.includes("new_cases") || indicator.includes("incidence");
        }

        if (landingMetric === "deaths") {
          return indicator.includes("deaths") || indicator.includes("mortality");
        }

        return indicator.includes("prevalence") || indicator.includes("survival");
      })
      .map((row) => {
        const value = Number(String(row.value || "0").replace(",", "."));
        const unit = row.unit || "";

        return {
          label:
            row.indicator === "new_cases_count" ? "Türkiye national new cases" :
            row.indicator === "deaths_count" ? "Türkiye national deaths" :
            row.indicator === "five_year_prevalence_count" ? "Türkiye 5-year prevalence" :
            row.indicator.replaceAll("_", " "),
          category:
            String(row.indicator || "").includes("incidence") ? "Screening / incidence indicator" :
            String(row.indicator || "").includes("mortality") ? "Mortality indicator" :
            "Official national estimate",
          area: row.area || "Türkiye",
          source: row.source_name || "Official source",
          year: row.year || "",
          value,
          unit,
          sourceType: "official"
        };
      })
      .filter((row) => Number.isFinite(row.value));

    const unifiedCsvRows = ranked.slice(0, 8).map((row) => ({
      label: row.area,
      category: landingRegion === "turkiye" ? "Türkiye city ranking" : "Europe comparison",
      area: row.area,
      source: "Local CSV cancer layer",
      year: "simulation layer",
      value: row[landingMetric],
      unit: landingMetric === "survival" ? "%" : "rate_per_100000",
      rows: row.rows,
      cancers: row.cancers,
      sourceType: "csv"
    })).filter((row) => Number.isFinite(row.value));

    const baseMergedCancerRows = [...unifiedOfficialRows, ...unifiedCsvRows];

    const landingRowText = (row) =>
      Object.values(row || {})
        .join(" ")
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "");

    const europeKeywords = [
      "europe", "avrupa", "france", "germany", "italy", "spain", "poland",
      "netherlands", "belgium", "austria", "sweden", "norway", "denmark",
      "finland", "greece", "portugal", "romania", "bulgaria", "croatia",
      "hungary", "czech", "slovakia", "slovenia", "ireland", "estonia",
      "latvia", "lithuania"
    ];

    const turkiyeKeywords = [
      "turkiye", "turkey", "türkiye", "adana", "ankara", "istanbul", "izmir",
      "aydin", "mersin", "mus", "sirnak", "trabzon", "zonguldak", "nevsehir", "sakarya"
    ];

    const isEuropeCountryRow = (row) => {
      const text = landingRowText(row);
      const hasEurope = europeKeywords.some((keyword) => text.includes(keyword));
      const hasTurkiye = turkiyeKeywords.some((keyword) => text.includes(keyword));

      return hasEurope && !hasTurkiye;
    };

    const isTurkiyeRow = (row) => {
      const text = landingRowText(row);
      return turkiyeKeywords.some((keyword) => text.includes(keyword)) || !isEuropeCountryRow(row);
    };

    const regionFilteredCancerRows =
      landingRegion === "europe"
        ? baseMergedCancerRows.filter(isEuropeCountryRow)
        : baseMergedCancerRows.filter(isTurkiyeRow);

    const mergedCancerRows = regionFilteredCancerRows.length
      ? regionFilteredCancerRows
      : baseMergedCancerRows;
    const [showAllCancerRows, setShowAllCancerRows] = useState(false);
    const visibleMergedCancerRows = showAllLandingDataRows ? mergedCancerRows : mergedCancerRows.slice(0, 5);

    const mergedMax = Math.max(
      ...mergedCancerRows.map((row) => {
        if (String(row.unit).toLowerCase() === "count") {
          return Math.log10((row.value || 0) + 1);
        }
        return row.value || 0;
      }),
      1
    );

    const formatMergedValue = (row) => {
      const value = row.value;
      const unit = String(row.unit || "").toLowerCase();

      if (!Number.isFinite(value)) return "-";

      const formatted = new Intl.NumberFormat("tr-TR", {
        maximumFractionDigits: unit === "count" ? 0 : 1
      }).format(value);

      if (unit === "count") return `${formatted} cases`;
      if (unit === "rate_per_100000") return `${formatted} /100k`;
      if (unit === "%") return `${formatted}%`;
      return `${formatted} ${row.unit || ""}`.trim();
    };

    const mergedWidth = (row) => {
      const raw =
        String(row.unit).toLowerCase() === "count"
          ? Math.log10((row.value || 0) + 1)
          : row.value || 0;

      return Math.max(8, Math.round((raw / mergedMax) * 100));
    };

    const officialMetricRows = officialRows
      .filter((row) => {
        const indicator = String(row.indicator || "").toLowerCase();

        if (landingMetric === "cases") {
          return indicator.includes("new_cases") || indicator.includes("incidence");
        }

        if (landingMetric === "deaths") {
          return indicator.includes("deaths") || indicator.includes("mortality");
        }

        return indicator.includes("prevalence") || indicator.includes("survival");
      })
      .map((row) => {
        const rawValue = Number(String(row.value || "0").replace(",", "."));
        const unit = row.unit || "";
        const normalizedValue =
          String(unit).toLowerCase() === "count"
            ? Math.log10((rawValue || 0) + 1)
            : rawValue;

        return {
          label: prettyOfficialIndicator(row.indicator || ""),
          value: rawValue,
          normalizedValue,
          unit,
          source: row.source_name || "Official source",
          area: row.area || "",
          year: row.year || "",
          url: row.source_url || ""
        };
      })
      .filter((row) => Number.isFinite(row.value) && row.value > 0)
      .sort((a, b) => b.value - a.value);

    const officialMaxValue = Math.max(
      ...officialMetricRows.map((row) => row.normalizedValue || 0),
      1
    );

    return (
      <section className="landing-live-data">
        <div className="landing-live-head">
          <p>{trText("LIVE CANCER DATA LAB", "CANLI KANSER VERİ LABORATUVARI")}</p>
          <h2>{trText("Interactive cancer burden explorer", "İnteraktif kanser yükü keşif aracı")}</h2>
          <span>
            Click a metric to rank Türkiye cities or European countries by public cancer indicators.
            The chart updates instantly from the CSV layer.
          </span>
        </div>

        <div className="landing-live-switches">
          <div>
            <button className={landingMetric === "cases" ? "active" : ""} onClick={() => { setLandingMetric("cases"); setShowAllLandingDataRows(false); }}>{trText("New cases", "Yeni vakalar")}</button>
            <button className={landingMetric === "deaths" ? "active" : ""} onClick={() => { setLandingMetric("deaths"); setShowAllLandingDataRows(false); }}>{trText("Deaths", "Ölümler")}</button>
            <button className={landingMetric === "survival" ? "active" : ""} onClick={() => { setLandingMetric("survival"); setShowAllLandingDataRows(false); }}>{trText("5-year survival", "5 yıllık sağkalım")}</button>
          </div>

          <div>
            <button className={landingRegion === "turkiye" ? "active dark" : ""} onClick={() => { setLandingRegion("turkiye"); setShowAllLandingDataRows(false); }}>Türkiye cities</button>
            <button className={landingRegion === "europe" ? "active dark" : ""} onClick={() => { setLandingRegion("europe"); setShowAllLandingDataRows(false); }}>Europe countries</button>
          </div>
        </div>

        <div className="landing-live-signal">
          <span>Live data stream</span>
          <div>
            <i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i>
          </div>
          <b>{landingRegion === "turkiye" ? "Türkiye city layer" : "Europe country layer"} · {metricLabel[landingMetric]}</b>
        </div>

        <div className="landing-live-grid" key={`${landingRegion}-${landingMetric}`}>
          <div className="landing-live-chart">
            <div className="landing-live-chart-title merged-title">
              <span>Unified cancer intelligence layer</span>
              <strong>{metricLabel[landingMetric]}</strong>
              <small>
                {mergedCancerRows.length} categorized indicators · official estimates + CSV ranking merged · {normalized.length} source rows
              </small>

              {mergedCancerRows.length > 5 && (
                <button
                  type="button"
                  className="landing-live-showmore-v58"
                  onClick={() => setShowAllLandingDataRows((value) => !value)}
                >
                  {showAllLandingDataRows
                    ? "Show less — first 5 key indicators"
                    : `Show ${mergedCancerRows.length - 5} more indicators`}
                </button>
              )}
            </div>

            <div className={`landing-merged-intelligence ${showAllLandingDataRows ? "show-all-v58" : "collapsed-v58"}`} key={`${landingMetric}-${landingRegion}-${mergedCancerRows.length}`}>
              {visibleMergedCancerRows.map((row, index) => (
                <article
                  className={`merged-data-row ${row.sourceType}`}
                  key={`${landingMetric}-${landingRegion}-${row.sourceType}-${row.label}-${index}`}
                  style={{
                    animationDelay: `${index * 0.075}s`,
                    "--row-delay": `${index * 0.075}s`
                  }}
                >
                  <div className="merged-data-main">
                    <span>{row.category}</span>
                    <h4>{row.label}</h4>
                    <p>
                      {row.sourceType === "csv"
                        ? `${row.rows || 0} rows · ${(row.cancers || []).slice(0, 2).join(", ") || "mixed cancer types"}`
                        : `${row.area} · ${row.year} · ${row.source}`}
                    </p>
                  </div>

                  <div className="merged-data-bar">
                    <i style={{ width: `${mergedWidth(row)}%` }}>
                      <b></b>
                    </i>
                  </div>

                  <strong>{formatMergedValue(row)}</strong>
                </article>
              ))}
            </div>

            {officialMetricRows.length > 0 && (
              <>
                <section className="landing-official-bars">
                  <div className="landing-official-bars-head">
                    <span>Official national estimates</span>
                    <b>{metricLabel[landingMetric]}</b>
                  </div>

                  <div className="landing-official-bars-list">
                    {officialMetricRows.map((row, index) => {
                      const width = Math.max(
                        18,
                        Math.round((row.normalizedValue / officialMaxValue) * 100)
                      );

                      return (
                        <article
                          className="landing-official-bar"
                          key={`${row.label}-${row.value}-${index}`}
                          style={{ animationDelay: `${index * 0.08}s` }}
                        >
                          <div className="landing-official-bar-top">
                            <div>
                              <strong>{row.label}</strong>
                              <small>{row.area} · {row.year} · {row.source}</small>
                            </div>

                            <em>
                              {formatOfficialValue(row.value, row.unit)}{" "}
                              {prettyUnit(row.unit)}
                            </em>
                          </div>

                          <div className="landing-official-bar-track">
                            <i style={{ width: `${width}%` }}>
                              <span></span>
                            </i>
                          </div>
                        </article>
                      );
                    })}
                  </div>
                </section>
              </>
            )}

            <div className="landing-demo-bars-head">
              <span>{landingRegion === "turkiye" ? "Türkiye city ranking from CSV layer" : "Europe ranking from CSV layer"}</span>
            </div>

            {ranked.map((row, index) => {
              const value = row[landingMetric] || 0;
              const width = Math.max(5, Math.round((value / maxValue) * 100));

              return (
                <div
                  className="landing-live-row"
                  key={row.area}
                  style={{ animationDelay: `${index * 0.055}s` }}
                >
                  <b>{index + 1}</b>
                  <div>
                    <strong>{row.area}</strong>
                    <small>{row.rows} rows · {row.cancers.slice(0, 2).join(", ")}</small>
                    <i style={{ width: `${width}%` }}><span></span></i>
                  </div>
                  <em>{formatValue(value)}</em>
                </div>
              );
            })}
          </div>

          <aside className="landing-live-side">
            <span>Current view</span>
            <h3>{metricLabel[landingMetric]}</h3>
            <p>
              Showing {landingRegion === "turkiye" ? "Türkiye city-level" : "European country-level"} ranking.
              Values are aggregated from the local CSV and should be treated as public-data indicators,
              not personal medical risk scores.
            </p>

            <div>
              <strong>{normalized.length}</strong>
              <small>CSV rows loaded</small>
            </div>

            <div>
              <strong>{officialRows.length}</strong>
              <small>official source-backed rows</small>
            </div>

            {mergedCancerRows.length > 5 && (
              <button
                type="button"
                className="landing-data-show-more-v50"
                onClick={() => setShowAllCancerRows((value) => !value)}
              >
                {showAllCancerRows
                  ? "Show first 5 key indicators"
                  : `Show ${mergedCancerRows.length - 5} more indicators`}
              </button>
            )}

            {mergedCancerRows.length > 5 && (
              <button
                type="button"
                className="landing-real-showmore-v56"
                onClick={() => setShowAllLandingDataRows((value) => !value)}
              >
                {showAllLandingDataRows
                  ? "Show less — first 5 key indicators"
                  : `Show ${mergedCancerRows.length - 5} more indicators`}
              </button>
            )}

            <button onClick={() => setPage("map")}>{trText("Open full interactive map", "Tam interaktif haritayı aç")}</button>
          </aside>
        </div>

        <div className="landing-official-source-strip">
          <span>Official source-backed layer</span>
          <div>
            {officialRows.slice(0, 8).map((row) => (
              <article key={`${row.source_id}-${row.indicator}-${row.value}`}>
                <b>{row.indicator}</b>
                <strong>{row.value} {row.unit}</strong>
                <small>{row.source_name} · {row.area} · {row.year}</small>
              </article>
            ))}
          </div>
        </div>

        <section id="research-pulse" className="landing-research-feed landing-research-feed-after">
          <div className="landing-research-feed-head">
            <span>Research pulse</span>
            <b>{trText("Innovative drugs, trials and oncology reading flow", "Yenilikçi ilaçlar, klinik çalışmalar ve onkoloji okuma akışı")}</b>
          </div>

          <div className="landing-research-feed-grid">
            {researchFeed.map((item, index) => (
              <article
                className="landing-research-card"
                key={`${item.title}-${index}`}
                style={{ animationDelay: `${index * 0.07}s` }}
              >
                <div className="landing-research-card-top">
                  <span>{item.badge}</span>
                  <small>{item.type}</small>
                </div>

                <h4>{item.title}</h4>
                <p>{item.summary}</p>

                <div className="landing-research-card-bottom">
                  <b>{item.source}</b>
                  <em>{item.meta}</em>
                </div>
              </article>
            ))}
          </div>
        </section>

      </section>
    );
  };



  const EnhancedFlowSimulation = () => {
    const [scenario, setScenario] = useState("critical");
    const [activeStep, setActiveStep] = useState(0);
    const [isRunning, setIsRunning] = useState(true);
    const [eventCount, setEventCount] = useState(128);

    const scenarios = {
      stable: {
        label: "Stable patient",
        score: 18,
        status: "Stable",
        symptoms: "Fatigue 3 · Pain 2 · Mood 3",
        recommendation: "Continue tracking symptoms and prepare questions for the next visit."
      },
      review: {
        label: "Needs review",
        score: 46,
        status: "Needs review",
        symptoms: "Fatigue 6 · Pain 5 · Mood 6",
        recommendation: "Monitor symptoms closely and share the structured note with the care team."
      },
      critical: {
        label: "High support priority",
        score: 82,
        status: "Critical",
        symptoms: "Fatigue 9 · Pain 8 · Mood 7",
        recommendation: "Contact care team if symptoms are new, worsening or hard to tolerate."
      }
    };

    const current = scenarios[scenario];

    const steps = [
      {
        title: "Patient input",
        subtitle: "Role, symptoms and support need entered",
        detail: current.symptoms,
        icon: "01"
      },
      {
        title: "AI Copilot reasoning",
        subtitle: "Symptom burden is converted into a support signal",
        detail: `Support score ${current.score}/100 · ${current.status}`,
        icon: "02"
      },
      {
        title: "Doctor-ready note",
        subtitle: "Questions and next actions are generated",
        detail: current.recommendation,
        icon: "03"
      },
      {
        title: "Splunk event stream",
        subtitle: "Operational support event is prepared",
        detail: `source=oncoconnect_ai score=${current.score} status=${current.status}`,
        icon: "04"
      }
    ];

    useEffect(() => {
      if (!isRunning) return;

      const timer = setInterval(() => {
        setActiveStep((prev) => (prev + 1) % steps.length);
        setEventCount((prev) => prev + 1);
      }, 1800);

      return () => clearInterval(timer);
    }, [isRunning, scenario]);

    const resetSimulation = () => {
      setActiveStep(0);
      setEventCount(128);
      setIsRunning(true);
    };

    return (
      <EnhancedFlowSimulation />
    );
  };



  const InteractiveFlowSimulation = () => {
    const scenarios = {
      critical: {
        label: "Critical scenario",
        score: 82,
        status: "Critical",
        symptoms: "Fatigue 9 · Pain 8 · Mood 7",
        action: "Support outreach recommended",
        color: "critical"
      },
      review: {
        label: "Needs review",
        score: 46,
        status: "Needs review",
        symptoms: "Fatigue 6 · Pain 5 · Mood 6",
        action: "Monitor symptoms and prepare doctor questions",
        color: "review"
      },
      stable: {
        label: "Stable",
        score: 18,
        status: "Stable",
        symptoms: "Fatigue 3 · Pain 2 · Mood 3",
        action: "Continue tracking symptoms",
        color: "stable"
      }
    };

    const [scenario, setScenario] = useState("critical");
    const [running, setRunning] = useState(true);
    const [step, setStep] = useState(0);
    const [events, setEvents] = useState(128);

    const current = scenarios[scenario];

    const steps = [
      {
        title: "Patient input",
        subtitle: "Role and symptoms entered",
        detail: current.symptoms
      },
      {
        title: "AI Copilot reasoning",
        subtitle: "Support signal calculated",
        detail: `Risk score ${current.score}/100 · ${current.status}`
      },
      {
        title: "Doctor-ready note",
        subtitle: "Questions and next steps generated",
        detail: current.action
      },
      {
        title: "Splunk event",
        subtitle: "Monitoring event streamed",
        detail: `source=oncoconnect_ai status=${current.status}`
      }
    ];

    useEffect(() => {
      if (!running) return;

      const timer = setInterval(() => {
        setStep((prev) => (prev + 1) % steps.length);
        setEvents((prev) => prev + 1);
      }, 1600);

      return () => clearInterval(timer);
    }, [running, scenario]);

    const changeScenario = (key) => {
      setScenario(key);
      setStep(0);
      setEvents((prev) => prev + 3);
      setRunning(true);
    };

    return (
      <section className="inline-live-simulation interactive-flow-live">
        <div className="inline-sim-head">
          <div>
            <p>LIVE FLOW SIMULATION</p>
            <h2>AI support flow running in real time</h2>
            <span>
              Select a scenario and watch how symptom input becomes AI guidance,
              doctor-ready action and Splunk-ready monitoring.
            </span>
          </div>

          <div className={`inline-risk-chip ${current.color}`}>
            <small>Live risk signal</small>
            <strong>{current.score}</strong>
            <b>{current.status}</b>
          </div>
        </div>

        <div className="inline-sim-controls">
          {Object.entries(scenarios).map(([key, item]) => (
            <button
              key={key}
              type="button"
              className={scenario === key ? "active" : ""}
              onClick={() => changeScenario(key)}
            >
              {item.label}
            </button>
          ))}

          <button
            type="button"
            className={`dark ${running ? "active-running" : ""}`}
            onClick={() => setRunning((value) => !value)}
          >
            {running ? "Pause simulation" : "Auto-running"}
          </button>
        </div>

        <div className="inline-sim-canvas">
          <div className="inline-sim-grid"></div>

          <div className={`inline-sim-stream ${running ? "running" : "paused"}`}>
            <i></i>
            <i></i>
            <i></i>
            <i></i>
          </div>

          <div className="inline-sim-steps">
            {steps.map((item, index) => (
              <article
                key={item.title}
                className={step === index ? "active" : step > index ? "done" : ""}
                onClick={() => setStep(index)}
              >
                <b>{String(index + 1).padStart(2, "0")}</b>
                <h3>{item.title}</h3>
                <p>{item.detail}</p>
                <span>{item.subtitle}</span>
              </article>
            ))}
          </div>

          <div className="inline-sim-output">
            <div>
              <span>AI current recommendation</span>
              <h3>{steps[step].title}</h3>
              <p>{steps[step].detail}</p>
            </div>

            <pre>{`{
  source: "oncoconnect_ai",
  scenario: "${scenario}",
  step: "${steps[step].title}",
  risk_score: ${current.score},
  status: "${current.status}",
  event_count: ${events}
}`}</pre>
          </div>
        </div>
      </section>
    );
  };


  const scrollLandingSectionV131 = (id) => {
    setPage("landing");

    window.setTimeout(() => {
      const element = document.getElementById(id);
      if (!element) return;

      const top = element.getBoundingClientRect().top + window.scrollY - 105;
      window.scrollTo({
        top: Math.max(0, top),
        behavior: "smooth"
      });
    }, 120);
  };






  const LandingPage = () => (
    <div className="old-home-page">
      <nav className="old-home-nav">
        <div className="old-home-brand">OncoConnect AI</div>

        <div className="old-home-links">
          <button onClick={() => setPage("landing")}>{trText(trText("Home", "Ana Sayfa"), "Ana Sayfa")}</button>
          <button type="button" onClick={() => scrollLandingSectionV131("what-is-it")}>{trText(trText("What is it?", "Nedir?"), "Nedir?")}</button>
          <button type="button" onClick={() => scrollLandingSectionV131("how-it-works-anchor")}>{trText(trText("How it works", "Nasıl çalışır?"), "Nasıl çalışır?")}</button>
          <button type="button" onClick={() => scrollLandingSectionV131("cancer-burden")}>{trText(trText("Cancer Burden", "Kanser Yükü"), "Kanser Yükü")}</button>
          <button type="button" onClick={() => scrollLandingSectionV131("research-pulse")}>{trText(trText("Research", "Araştırma"), "Araştırma")}</button>
          <button type="button" onClick={() => setPage("copilot")}>{trText(trText("AI Copilot", "AI Yardımcı Pilot"), "AI Yardımcı Pilot")}</button>
          <button type="button" onClick={() => setPage("kids")}>{trText(trText("Onco Kids", "Onco Kids"), trText("Onco Kids", "Onco Kids"))}</button>
          <button onClick={() => setPage("admin")}>{trText(trText("Admin", "Admin"), trText("Admin", "Admin"))}</button>
        </div>

        <div className="old-home-lang">
          <select value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">{trText("English", "İngilizce")}</option>
            <option value="tr">Türkçe</option>
          </select>
        </div>
      </nav>

      <section className="old-portal-hero">
        <div className="old-portal-copy">
          <p className="old-eyebrow">{trText(trText("ONCOCONNECT AI PUBLIC PORTAL", "ONCOCONNECT AI KAMU PORTALI"), "ONCOCONNECT AI KAMU PORTALI")}</p>

          <h1>
            {trText(trText("Safe cancer support, research awareness and AI guidance", "Güvenli kanser desteği, araştırma farkındalığı ve AI rehberliği"), "Güvenli kanser desteği, araştırma farkındalığı ve AI rehberliği")}
          </h1>

          <p>
            {trText("A two-layer platform for patients, caregivers, clinicians, researchers and NGOs: first trusted information, then AI Copilot and Splunk-powered operational monitoring.", "Hastalar, bakım verenler, klinisyenler, araştırmacılar ve STK’lar için iki katmanlı bir platform: önce güvenilir bilgi, ardından AI Yardımcı Pilot ve Splunk destekli operasyonel izleme.")}
          </p>

          <div className="old-hero-actions">
            <button type="button" onClick={() => setPage("copilot")}>{trText(trText("Launch AI Copilot", "AI Yardımcı Pilotu Başlat"), "AI Yardımcı Pilotu Başlat")}</button>
            <button onClick={() => setPage("knowledge")}>{trText(trText("Open Knowledge Graph", "Bilgi Grafiğini Aç"), "Bilgi Grafiğini Aç")}</button>
            <button onClick={() => setPage("kids")}>{trText(trText("Onco Kids", "Onco Kids"), trText("Onco Kids", "Onco Kids"))}</button>
          </div>

          <div className="old-disclaimer">
            {trText("This platform does not provide diagnosis or treatment advice. It supports doctor-visit preparation, trusted source navigation and support coordination.", "Bu platform tanı veya tedavi önerisi sunmaz. Doktor görüşmesine hazırlığı, güvenilir kaynaklara yönlendirmeyi ve destek koordinasyonunu destekler.")}
          </div>
        </div>

        <div className="old-hero-card">
          <div className="old-orb"></div>
          <h3>{trText(trText("Calm, clear and safe guidance", "Sakin, anlaşılır ve güvenli rehberlik"), "Sakin, anlaşılır ve güvenli rehberlik")}</h3>
          <p>
            {trText("The goal is not to create fear; it is to prepare better questions, surface support needs and give care teams more structured information.", "Amaç korku oluşturmak değil; daha iyi sorular hazırlamak, destek ihtiyaçlarını görünür kılmak ve bakım ekiplerine daha yapılandırılmış bilgi sağlamaktır.")}
          </p>

          <div className="old-companion-pill">
            <span>😊</span>
            <div>
              <strong>{trText(trText("Safe companion", "Güvenli yol arkadaşı"), "Güvenli yol arkadaşı")}</strong>
              <small>{trText(trText("Guidance with warmth, not fear.", "Korkuyla değil, güven veren bir sıcaklıkla rehberlik."), "Korkuyla değil, güven veren bir sıcaklıkla rehberlik.")}</small>
            </div>
          </div>
        </div>
      </section>

      <section id="what-is-it" className="old-section">
        <div className="old-section-head">
          <h2>{trText(trText("Patient support portal + AI Copilot + operational monitoring", "Hasta destek portalı + AI Yardımcı Pilot + operasyonel izleme"), "Hasta destek portalı + AI Yardımcı Pilot + operasyonel izleme")}</h2>
          <p>
            {trText("OncoConnect AI helps cancer patients and caregivers make symptoms easier to understand, prepare for doctor visits and help support teams identify high-risk cases when needed.", "OncoConnect AI, kanser hastalarının ve bakım verenlerin semptomları daha kolay anlamasına, doktor görüşmelerine hazırlanmasına ve gerektiğinde destek ekiplerinin yüksek riskli vakaları belirlemesine yardımcı olur.")}
          </p>
        </div>

        <div className="old-grid old-grid-3">
          <div className="old-info-card">
            <h3>{trText(trText("I want to understand my symptoms", "Semptomlarımı anlamak istiyorum"), "Semptomlarımı anlamak istiyorum")}</h3>
            <p>{trText(trText("AI Copilot explains symptom burden, creates a risk signal and prepares doctor questions.", "AI Yardımcı Pilot semptom yükünü açıklar, risk sinyali oluşturur ve doktor soruları hazırlar."), "AI Yardımcı Pilot semptom yükünü açıklar, risk sinyali oluşturur ve doktor soruları hazırlar.")}</p>
          </div>
          <div className="old-info-card">
            <h3>{trText(trText("I want to prepare for a doctor visit", "Doktor görüşmesine hazırlanmak istiyorum"), "Doktor görüşmesine hazırlanmak istiyorum")}</h3>
            <p>{trText(trText("Turns symptoms into a structured conversation note.", "Semptomları yapılandırılmış bir görüşme notuna dönüştürür."), "Semptomları yapılandırılmış bir görüşme notuna dönüştürür.")}</p>
          </div>
          <div className="old-info-card">
            <h3>{trText(trText("I want simple information for my child", "Çocuğum için sade bilgi istiyorum"), "Çocuğum için sade bilgi istiyorum")}</h3>
            <p>{trText(trText("Onco Kids provides gentler, hopeful explanations for children and families.", "Onco Kids çocuklar ve aileler için daha yumuşak, umut veren açıklamalar sunar."), "Onco Kids çocuklar ve aileler için daha yumuşak, umut veren açıklamalar sunar.")}</p>
          </div>
          <div className="old-info-card">
            <h3>{trText(trText("I want to follow new cancer research", "Yeni kanser araştırmalarını takip etmek istiyorum"), "Yeni kanser araştırmalarını takip etmek istiyorum")}</h3>
            <p>{trText("A safe source-aware feed for trials, immunotherapy, early detection and patient support.", "Klinik çalışmalar, immünoterapi, erken tanı ve hasta desteği için güvenli kaynak odaklı akış.")}</p>
          </div>
          <div className="old-info-card">
            <h3>{trText(trText("I am an NGO or support team", "Bir STK veya destek ekibiyim"), "Bir STK veya destek ekibiyim")}</h3>
            <p>{trText("Prioritizes high-risk cases through Splunk dashboards and AI summaries.", "Yüksek riskli vakaları Splunk panelleri ve AI özetleriyle önceliklendirir.")}</p>
          </div>
          <div className="old-info-card">
            <h3>{trText(trText("I want to see the ecosystem", "Ekosistemi görmek istiyorum"), "Ekosistemi görmek istiyorum")}</h3>
            <p>{trText("Shows the flow between patients, clinicians, researchers, NGOs, datasets and Splunk.", "Hastalar, klinisyenler, araştırmacılar, STK’lar, veri setleri ve Splunk arasındaki akışı gösterir.")}</p>
          </div>
        </div>
      </section>

      
        <InteractiveFlowSimulation />


      <div id="how-it-works-anchor" className="landing-scroll-anchor-v131" />
      <section id="cancer-burden" className="old-section">
        <p className="old-eyebrow dark">{trText(trText("CANCER BURDEN", "KANSER YÜKÜ"), "KANSER YÜKÜ")}</p>
        <h2>{trText(trText("Data is not for fear, it is for earlier support and coordination", "Veri korku için değil, daha erken destek ve koordinasyon içindir"), "Veri korku için değil, daha erken destek ve koordinasyon içindir")}</h2>

        <div className="old-burden-grid">
          <div className="old-burden-card blue water-fill-card">
            <span>{trText(trText("Worldwide, 2022", "Dünya geneli, 2022"), "Dünya geneli, 2022")}</span>
            <strong>~20M</strong>
            <b>{trText(trText("new cancer cases", "yeni kanser vakası"), "yeni kanser vakası")}</b>
            <p>{trText(trText("GLOBOCAN 2022 estimates around 20 million new cancer cases worldwide.", "GLOBOCAN 2022 dünya genelinde yaklaşık 20 milyon yeni kanser vakası tahmin etmektedir."), "GLOBOCAN 2022 dünya genelinde yaklaşık 20 milyon yeni kanser vakası tahmin etmektedir.")}</p>
          </div>

          <div className="old-burden-card blue water-fill-card">
            <span>{trText(trText("Worldwide, 2022", "Dünya geneli, 2022"), "Dünya geneli, 2022")}</span>
            <strong>~9.7M</strong>
            <b>{trText(trText("cancer deaths", "kanser ölümü"), "kanser ölümü")}</b>
            <p>{trText(trText("This highlights the importance of support, awareness, screening and care coordination.", "Bu, destek, farkındalık, tarama ve bakım koordinasyonunun önemini gösterir."), "Bu, destek, farkındalık, tarama ve bakım koordinasyonunun önemini gösterir.")}</p>
          </div>

          <div className="old-burden-card teal water-fill-card">
            <span>{trText(trText("Türkiye context", "Türkiye bağlamı"), "Türkiye bağlamı")}</span>
            <strong>Türkiye</strong>
            <b>{trText(trText("country-level cancer statistics", "ülke düzeyinde kanser istatistikleri"), "ülke düzeyinde kanser istatistikleri")}</b>
            <p>{trText(trText("Lung, breast and colorectal cancers are among key cancer burden areas for Türkiye.", "Akciğer, meme ve kolorektal kanserler Türkiye için temel kanser yükü alanları arasındadır."), "Akciğer, meme ve kolorektal kanserler Türkiye için temel kanser yükü alanları arasındadır.")}</p>
          </div>

          <div className="old-burden-card purple water-fill-card">
            <span>{trText(trText("EU Cancer Mission", "AB Kanser Misyonu"), "AB Kanser Misyonu")}</span>
            <strong>2030</strong>
            <b>{trText(trText("quality of life and care goals", "yaşam kalitesi ve bakım hedefleri"), "yaşam kalitesi ve bakım hedefleri")}</b>
            <p>{trText(trText("The EU approach emphasizes prevention, cure, quality of life and family support.", "AB yaklaşımı önleme, tedavi, yaşam kalitesi ve aile desteğini vurgular."), "AB yaklaşımı önleme, tedavi, yaşam kalitesi ve aile desteğini vurgular.")}</p>
          </div>
        </div>
      </section>

      <section className="old-section old-research-section">
        <p className="old-eyebrow dark">{trText("RESEARCH DATA", "ARAŞTIRMA VERİSİ")}</p>
        <h2>{trText("GLOBOCAN 2022 data connected for Türkiye", "Türkiye için GLOBOCAN 2022 verisi bağlantılı")}</h2>
        <p className="old-section-desc">
          {trText("This section shows source-backed national data. The 81-city map remains a demo distribution until official province-level open data is available.", "Bu bölüm kaynak destekli ulusal verileri gösterir. 81 il haritası, resmi il düzeyinde açık veri mevcut olana kadar demo dağılım olarak kalır.")}
        </p>

        <div className="old-source-grid">
          <div>
            <strong>GLOBOCAN 2022</strong>
            <p>{trText("Türkiye total new cases, deaths and 5-year prevalence", "Türkiye toplam yeni vaka, ölüm ve 5 yıllık prevalans verileri")}</p>
          </div>
          <div>
            <strong>ECIS</strong>
            <p>{trText("Cancer burden indicators for European countries", "Avrupa ülkeleri için kanser yükü göstergeleri")}</p>
          </div>
          <div>
            <strong>HSGM</strong>
            <p>{trText("Türkiye official annual cancer statistics reports", "Türkiye resmi yıllık kanser istatistikleri raporları")}</p>
          </div>
        </div>

        <div className="old-turkiye-stats">
          <div>
            <span>Türkiye, 2022</span>
            <strong>240,013</strong>
            <b>{trText("all cancers new cases", "tüm kanserler yeni vakalar")}</b>
          </div>
          <div>
            <span>Türkiye, 2022</span>
            <strong>129,672</strong>
            <b>{trText("all cancers deaths", "tüm kanserler ölümler")}</b>
          </div>
          <div>
            <span>Türkiye, 2022</span>
            <strong>679,335</strong>
            <b>{trText("5-year prevalence", "5 yıllık prevalans")}</b>
          </div>
        </div>

        <div className="old-research-actions">
          <button onClick={() => setPage("map")}>{trText(trText("Open Interactive Cancer Map", "İnteraktif Kanser Haritasını Aç"), "İnteraktif Kanser Haritasını Aç")}</button>
          <button onClick={() => setPage("admin")}>{trText(trText("Open Admin Data Console", "Admin Veri Konsolunu Aç"), "Admin Veri Konsolunu Aç")}</button>
        </div>
      </section>
        <LandingMapPreview />
        <LandingDataDashboard />
    </div>
  );


  const CopilotPage = () => {
    // Fallback rows for CopilotPage.
    // Prevents runtime crash when landing-dashboard mergedCancerRows is out of scope.
    const mergedCancerRows = [
      {
        region: "Türkiye",
        country: "Türkiye",
        metric: trText("New cancer cases", "Yeni kanser vakaları"),
        title: trText("New cancer cases", "Yeni kanser vakaları"),
        indicator: "New cancer cases",
        value: "240,013",
        text: trText("Estimated annual new cancer cases.", "Tahmini yıllık yeni kanser vakaları."),
        source: "GLOBOCAN 2022",
        category: "cases",
        trend: "high priority"
      },
      {
        region: "Türkiye",
        country: "Türkiye",
        metric: trText("Cancer deaths", "Kanser ölümleri"),
        title: trText("Cancer deaths", "Kanser ölümleri"),
        indicator: "Cancer deaths",
        value: "129,672",
        text: trText("Estimated annual cancer mortality.", "Tahmini yıllık kanser mortalitesi."),
        source: "GLOBOCAN 2022",
        category: "mortality",
        trend: "high priority"
      },
      {
        region: "Türkiye",
        country: "Türkiye",
        metric: trText("5-year prevalence", "5 yıllık prevalans"),
        title: trText("5-year prevalence", "5 yıllık prevalans"),
        indicator: "5-year prevalence",
        value: "679,335",
        text: trText("Estimated people living within five years of diagnosis.", "Tanıdan sonraki beş yıl içinde yaşayan tahmini kişi sayısı."),
        source: "GLOBOCAN 2022",
        category: "prevalence",
        trend: "continuity of care"
      },
      {
        region: "Europe",
        country: "Europe",
        metric: trText("Regional comparison", "Bölgesel karşılaştırma"),
        title: trText("Regional comparison", "Bölgesel karşılaştırma"),
        indicator: "Regional comparison",
        value: "Context layer",
        text: trText("Used for Türkiye-Europe burden comparison inside the pilot.", "Pilot içinde Türkiye-Avrupa kanser yükü karşılaştırması için kullanılır."),
        source: trText("OncoConnect analysis layer", "OncoConnect analiz katmanı"),
        category: "comparison",
        trend: "benchmark"
      },
      {
        region: "Pilot",
        country: "Pilot",
        metric: trText("Patient navigation", "Hasta yönlendirme"),
        title: trText("Patient navigation", "Hasta yönlendirme"),
        indicator: trText("Patient navigation", "Hasta yönlendirme"),
        value: "AI-assisted",
        text: trText("Supports question preparation, visit planning and trusted information access.", "Soru hazırlığı, ziyaret planlama ve güvenilir bilgi erişimini destekler."),
        source: trText("OncoConnect AI Copilot", "OncoConnect AI Yardımcı Pilot"),
        category: "copilot",
        trend: "support"
      }
    ];


    const [role, setRole] = useState("patient");
    const [goal, setGoal] = useState("doctor");
    const [cancerType, setCancerType] = useState("all");
    const [treatmentStage, setTreatmentStage] = useState("chemotherapy");
    const [mainConcern, setMainConcern] = useState("fatigue");
    const [caseScenario, setCaseScenario] = useState("chemo_fever");
    const [feverFlag, setFeverFlag] = useState(false);
    const [breathingFlag, setBreathingFlag] = useState(false);
    const [bleedingFlag, setBleedingFlag] = useState(false);
    const [confusionFlag, setConfusionFlag] = useState(false);
    const [city, setCity] = useState("İstanbul");
    const [ageGroup, setAgeGroup] = useState("All");
    const [fatigue, setFatigue] = useState(6);
    const [pain, setPain] = useState(4);
    const [nausea, setNausea] = useState(3);
    const [mood, setMood] = useState(5);
    const [activeInsight, setActiveInsight] = useState("ai");
    const [lastCopilotAction, setLastCopilotAction] = useState(trText("AI recommendation ready", "AI önerisi hazır"));
    const [copilotActionLog, setCopilotActionLog] = useState([]);
    const [simulationRunning, setSimulationRunning] = useState(false);

  // GLOBAL_PIPELINE_IDLE_CONTROLLER_V93
  useEffect(() => {
    const forceIdle = () => {
      document.body.classList.add("pipeline-force-idle-v93");
    };

    const releaseIdle = () => {
      document.body.classList.remove("pipeline-force-idle-v93");
    };

    window.__forcePipelineIdleV93 = forceIdle;
    window.__releasePipelineIdleV93 = releaseIdle;

    forceIdle();

    return () => {
      document.body.classList.remove("pipeline-force-idle-v93");
    };
  }, []);


  const [executionStepV86, setExecutionStepV86] = useState(-1);
  const [pipelineResetModeV90, setPipelineResetModeV90] = useState(true);
  const [pipelineHardIdleV99, setPipelineHardIdleV99] = useState(true);
  const [pipelineResetKeyV100, setPipelineResetKeyV100] = useState(0);
  const isPipelineIdleV92 = pipelineResetModeV90 || lastCopilotAction === trText("Ready for new analysis.", "Yeni analiz için hazır.");
  const isPipelineIdleV95 = pipelineResetModeV90 || executionStepV86 === -1 || lastCopilotAction === trText("Ready for new analysis.", "Yeni analiz için hazır.");
  const isPipelineIdleV97 = pipelineHardIdleV99 || pipelineResetModeV90 || executionStepV86 < 0 || lastCopilotAction === trText("Ready for new analysis.", "Yeni analiz için hazır.");
  const pipelineIdleFinalV100 = pipelineHardIdleV99 || pipelineResetModeV90 || executionStepV86 < 0;
  const [shareFeedbackV86, setShareFeedbackV86] = useState("");
  const [trendRangeV119, setTrendRangeV119] = useState("30");
  const [liveTrendInputsV126, setLiveTrendInputsV126] = useState(null);

  const trendSeriesV119 = useMemo(() => {
    const ranges = {
      "7": {
        labels: ["Jun 1", "Jun 2", "Jun 3", "Jun 4", "Jun 5", "Jun 6", "Today"],
        fatigue: "62,74 150,66 238,82 326,58 414,78 502,76 590,72",
        pain: "62,108 150,106 238,112 326,94 414,108 502,106 590,104",
        nausea: "62,142 150,140 238,148 326,134 414,144 502,142 590,140",
        mood: "62,170 150,168 238,164 326,156 414,160 502,158 590,152"
      },
      "30": {
        labels: ["May 10", "May 17", "May 24", "May 31", "Jun 7", "Today"],
        fatigue: "62,70 98,52 134,58 170,50 206,78 242,70 278,52 314,72 350,96 386,94 422,108 458,70 494,90 590,88",
        pain: "62,108 98,108 134,84 170,104 206,120 242,118 278,112 314,124 350,124 386,124 422,124 458,98 494,126 590,126",
        nausea: "62,144 98,142 134,144 170,154 206,164 242,170 278,156 314,172 350,156 386,156 422,162 458,152 494,166 590,164",
        mood: "62,172 98,176 134,170 170,170 206,178 242,180 278,174 314,178 350,172 386,162 422,176 458,168 494,160 590,160"
      },
      "90": {
        labels: ["Mar", "Apr", "May", "Jun", "Last week", "Today"],
        fatigue: "62,82 120,76 178,66 236,58 294,50 352,66 410,60 468,74 526,66 590,62",
        pain: "62,112 120,108 178,104 236,98 294,94 352,100 410,96 468,102 526,98 590,94",
        nausea: "62,142 120,140 178,138 236,136 294,132 352,138 410,134 468,136 526,132 590,130",
        mood: "62,174 120,172 178,170 236,166 294,164 352,160 410,158 468,154 526,150 590,146"
      }
    };

    return ranges[trendRangeV119] || ranges["30"];
  }, [trendRangeV119]);

  const trendSeriesLiveV126 = useMemo(() => {
    if (!liveTrendInputsV126) return trendSeriesV119;

    const clamp = (value) => Math.max(0, Math.min(10, Number(value || 0)));
    const y = (value, offset = 0) => {
      const mapped = 174 - clamp(value) * 14.4 + offset;
      return Math.max(30, Math.min(174, Math.round(mapped)));
    };

    const x = [62, 170, 286, 414, 512, 590];

    const makePoints = (values, offset = 0) =>
      values.map((value, index) => `${x[index]},${y(value, offset)}`).join(" ");

    const current = {
      fatigue: clamp(liveTrendInputsV126.fatigue),
      pain: clamp(liveTrendInputsV126.pain),
      nausea: clamp(liveTrendInputsV126.nausea),
      mood: clamp(liveTrendInputsV126.mood),
    };

    const profiles = {
      "7": {
        labels: ["Day -6", "Day -4", "Day -2", "Yesterday", "Latest", "Today"],
        factors: [0.78, 0.88, 0.82, 0.92, 0.96, 1.0],
      },
      "30": {
        labels: ["May 10", "May 17", "May 24", "May 31", "Jun 7", "Today"],
        factors: [0.72, 0.82, 0.76, 0.86, 0.92, 1.0],
      },
      "90": {
        labels: ["Mar", "Apr", "May", "Jun", "Last week", "Today"],
        factors: [0.58, 0.66, 0.74, 0.82, 0.92, 1.0],
      },
    };

    const profile = profiles[trendRangeV119] || profiles["30"];
    const build = (base) => profile.factors.map((factor) => Math.max(0, Math.min(10, base * factor)));

    return {
      labels: profile.labels,
      fatigue: makePoints(build(current.fatigue), -2),
      pain: makePoints(build(current.pain), 2),
      nausea: makePoints(build(current.nausea), 6),
      mood: makePoints(build(current.mood), 10),
    };
  }, [trendRangeV119, trendSeriesV119, liveTrendInputsV126]);


  const trendDotsFromPointsV127 = (points, className) =>
    String(points || "")
      .trim()
      .split(/\s+/)
      .map((point, index) => {
        const [cx, cy] = point.split(",").map(Number);
        if (!Number.isFinite(cx) || !Number.isFinite(cy)) return null;
        return (
          <circle
            key={`${className}-${index}-${cx}-${cy}`}
            cx={cx}
            cy={cy}
            r={index === String(points || "").trim().split(/\s+/).length - 1 ? 5 : 4}
            className={className}
          />
        );
      });

  
  const [splunkLiveMetricsV140, setSplunkLiveMetricsV140] = useState(null);
  const [splunkLiveStatusV140, setSplunkLiveStatusV140] = useState("idle");

  useEffect(() => {
    let cancelled = false;

    async function loadSplunkLiveMetricsV140() {
      try {
        setSplunkLiveStatusV140("loading");
        const response = await fetch(`${API}/splunk/metrics`);
        const data = await response.json();

        if (cancelled) return;

        if (data?.success && data?.metrics) {
          setSplunkLiveMetricsV140(data);
          setSplunkLiveStatusV140("ready");
        } else {
          setSplunkLiveStatusV140("empty");
        }
      } catch {
        if (!cancelled) {
          setSplunkLiveStatusV140("error");
        }
      }
    }

    loadSplunkLiveMetricsV140();
    const timer = window.setInterval(loadSplunkLiveMetricsV140, 20000);

    return () => {
      cancelled = true;
      window.clearInterval(timer);
    };
  }, []);

const [visibleRecommendationV106, setVisibleRecommendationV106] = useState("");
const [backendRecommendationV149, setBackendRecommendationV149] = useState(null);
const [recommendationLoadingV149, setRecommendationLoadingV149] = useState(false);

  const clearExecutionTimersV86 = () => {
    if (window.__oncoExecutionTimersV86) {
      window.__oncoExecutionTimersV86.forEach((timer) => window.clearTimeout(timer));
    }
    window.__oncoExecutionTimersV86 = [];
  };

  const resetExecutionPipelineV86 = () => {
    clearExecutionTimersV86();

    if (window.__oncoExecutionTimersV80) {
      window.__oncoExecutionTimersV80.forEach((timer) => window.clearTimeout(timer));
      window.__oncoExecutionTimersV80 = [];
    }

    if (window.__oncoExecutionTimersV81) {
      window.__oncoExecutionTimersV81.forEach((timer) => window.clearTimeout(timer));
      window.__oncoExecutionTimersV81 = [];
    }

    if (window.__oncoExecutionTimersV83) {
      window.__oncoExecutionTimersV83.forEach((timer) => window.clearTimeout(timer));
      window.__oncoExecutionTimersV83 = [];
    }

    if (window.__oncoExecutionTimersV84) {
      window.__oncoExecutionTimersV84.forEach((timer) => window.clearTimeout(timer));
      window.__oncoExecutionTimersV84 = [];
    }

    setPipelineResetModeV90(true);
    setExecutionStepV86(-1);

    window.setTimeout(() => { setPipelineResetModeV90(true); setExecutionStepV86(-1); }, 50);
    window.setTimeout(() => { setPipelineResetModeV90(true); setExecutionStepV86(-1); }, 200);
    window.setTimeout(() => { setPipelineResetModeV90(true); setExecutionStepV86(-1); }, 600);
  };

  const startExecutionPipelineV86 = () => {
    setPipelineHardIdleV99(false);
    setPipelineResetModeV90(false);
    setPipelineResetModeV90(false);
    setPipelineResetModeV90(false);
    window.__releasePipelineIdleV93?.();
    clearExecutionTimersV86();
    setPipelineResetModeV90(false);
    setPipelineResetModeV90(false);
    setExecutionStepV86(0);

    window.__oncoExecutionTimersV86 = [
      window.setTimeout(() => setExecutionStepV86(1), 1300),
      window.setTimeout(() => setExecutionStepV86(2), 2600),
      window.setTimeout(() => setExecutionStepV86(3), 3900),
      window.setTimeout(() => setExecutionStepV86(4), 5200),
    ];
  };

  const handleShareV86 = async () => {
    const shareTitle = "OncoConnect AI Copilot";
    const shareText = trText(
      "OncoConnect AI Copilot care intelligence dashboard",
      "OncoConnect AI Copilot bakım zekâ paneli"
    );
    const shareUrl = window.location.href;

    try {
      if (navigator.share) {
        await navigator.share({
          title: shareTitle,
          text: shareText,
          url: shareUrl,
        });
        setShareFeedbackV86(trText("Shared", "Paylaşıldı"));
      } else if (navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(shareUrl);
        setShareFeedbackV86(trText("Link copied", "Bağlantı kopyalandı"));
      } else {
        window.prompt(trText("Copy this link", "Bu bağlantıyı kopyalayın"), shareUrl);
        setShareFeedbackV86(trText("Link ready", "Bağlantı hazır"));
      }

      window.setTimeout(() => setShareFeedbackV86(""), 2200);
    } catch (error) {
      setShareFeedbackV86(trText("Share cancelled", "Paylaşım iptal edildi"));
      window.setTimeout(() => setShareFeedbackV86(""), 2200);
    }
  };

  const runCareCockpitAnalysisV86 = () => {
    setVisibleRecommendationV106("");
    setLiveTrendInputsV126({ fatigue, pain, nausea, mood });

    setLastCopilotAction(trText("Analysis started.", "Analiz başladı."));
    startExecutionPipelineV86();
    runCareCockpitAnalysisV27();
  };

  

  // FORCE_PIPELINE_INITIAL_READY_V91
  useEffect(() => {
    setSimulationRunning(false);
    setPipelineResetModeV90?.(true);
    setExecutionStepV86?.(-1);
    window.__forcePipelineIdleV93?.();
    setLastCopilotAction(trText("Ready for new analysis.", "Yeni analiz için hazır."));
  }, []);

  const startNewSimulationV86 = () => {
    clearExecutionTimersV86();
    setVisibleRecommendationV106("");
    setPipelineHardIdleV99(true);
    setPipelineResetKeyV100((value) => value + 1);

    setPipelineResetModeV90(true);
    setExecutionStepV86(-1);
    setSimulationRunning(false);
    setLastCopilotAction(trText("Ready for new analysis.", "Yeni analiz için hazır."));

    window.setTimeout(() => {
      setVisibleRecommendationV106("");
      setPipelineHardIdleV99(true);
      setPipelineResetKeyV100((value) => value + 1);
      setPipelineResetModeV90(true);
      setExecutionStepV86(-1);
      setSimulationRunning(false);
      setLastCopilotAction(trText("Ready for new analysis.", "Yeni analiz için hazır."));
    }, 120);
  };

  // PIPELINE_INITIAL_IDLE_V87
  useEffect(() => {
    resetExecutionPipelineV86();
  }, []);


const [executionStepV80, setExecutionStepV80] = useState(-1);
const startExecutionPipelineV80 = () => {
    if (window.__oncoExecutionTimersV80) {
      window.__oncoExecutionTimersV80.forEach((timer) => window.clearTimeout(timer));
    }

    setExecutionStepV80(0);

    window.__oncoExecutionTimersV80 = [
      window.setTimeout(() => setExecutionStepV80(1), 1200),
      window.setTimeout(() => setExecutionStepV80(2), 2400),
      window.setTimeout(() => setExecutionStepV80(3), 3600),
      window.setTimeout(() => setExecutionStepV80(4), 5000),
    ];
  };

const [executionStepV75, setExecutionStepV75] = useState(-1);

  const runExecutionPipelineV78 = () => {
    setExecutionStepV75(0);

    window.setTimeout(() => setExecutionStepV75(1), 1300);
    window.setTimeout(() => setExecutionStepV75(2), 2600);
    window.setTimeout(() => setExecutionStepV75(3), 3900);
    window.setTimeout(() => setExecutionStepV75(4), 5200);
  };



const [simulationStep, setSimulationStep] = useState(0);
    const [reportGenerated, setReportGenerated] = useState(false);
    const [eventSent, setEventSent] = useState(false);
    const [mapRows, setMapRows] = useState([]);

    useEffect(() => {
      async function loadPublicRows() {
        try {
          const res = await fetch(`${API}/public/map-data`);
          const data = await res.json();

          const rows =
            Array.isArray(data) ? data :
            Array.isArray(data.rows) ? data.rows :
            Array.isArray(data.data) ? data.data :
            Array.isArray(data.records) ? data.records :
            [];

          setMapRows(rows);
        } catch {
          setMapRows([]);
        }
      }

      loadPublicRows();
    }, []);

    const roleLabels = {
      patient: trText("I am a patient", "Hastayım"),
      caregiver: trText("I am a family member / caregiver", "Aile üyesi / bakım verenim"),
      support: trText("I am a support team", "Destek ekibindeyim")
    };

    const goalLabels = {
      symptoms: trText("Understand my symptoms", "Semptomlarımı anlamak istiyorum"),
      doctor: trText("Prepare for my doctor visit", "Doktor görüşmesine hazırlanmak istiyorum"),
      urgent: trText("Know when to ask for urgent support", "Ne zaman acil destek istemeliyim?"),
      child: trText("Explain this gently to a child", "Bunu çocuğa nazikçe anlatmak istiyorum")
    };

    const cancerLabels = {
      all: trText("All cancer types", "Tüm kanser türleri"),
      breast: trText("Breast cancer", "Meme kanseri"),
      lung: trText("Lung cancer", "Akciğer kanseri"),
      colorectal: trText("Colorectal cancer", "Kolorektal kanser"),
      prostate: trText("Prostat cancer", "Prostat kanseri"),
      leukemia: trText("Leukemia / blood cancer", "Lösemi / kan kanseri"),
      other: trText("Other / not sure", "Diğer / emin değilim")
    };

    const cancerMatch = {
      all: "",
      breast: "Meme",
      lung: "Akciğer",
      colorectal: "Kolorektal",
      prostate: "Prostat",
      leukemia: "Lösemi",
      other: ""
    };

    const stageLabels = {
      diagnosis: trText("Recently diagnosed", "Yeni tanı aldı"),
      chemotherapy: trText("Receiving chemotherapy", "Kemoterapi alıyor"),
      radiotherapy: trText("Receiving radiotherapy", "Radyoterapi alıyor"),
      surgery: trText("Before / after surgery", "Ameliyat öncesi / sonrası"),
      followup: trText("Follow-up / remission", "Takip / remisyon"),
      palliative: trText("Supportive / palliative care", "Destekleyici / palyatif bakım")
    };

    const concernLabels = {
      fatigue: trText("Fatigue / weakness", "Yorgunluk / halsizlik"),
      pain: trText("Pain", "Ağrı"),
      nausea: trText("Nausea / appetite", "Bulantı / iştah"),
      anxiety: trText("Fear / anxiety", "Korku / kaygı"),
      sleep: trText("Sleep problems", "Uyku sorunları"),
      questions: trText("I do not know what to ask", "Ne soracağımı bilmiyorum")
    };

    const caseScenarioLabels = {
      chemo_fever: trText("Chemotherapy fever / infection concern", "Kemoterapi sonrası ateş / enfeksiyon endişesi"),
      appointment_prep: trText("Prepare for oncology appointment", "Onkoloji randevusuna hazırlık"),
      side_effects: trText("Side-effect tracking", "Yan etki takibi"),
      caregiver_support: trText("Caregiver support at home", "Evde bakım veren desteği"),
      child_explanation: trText("Explain cancer gently to a child", "Kanseri çocuğa nazikçe anlatma"),
      screening_awareness: trText("Screening and early diagnosis awareness", "Tarama ve erken tanı farkındalığı")
    };

    const cityOptions = Array.from(
      new Set(
        mapRows
          .map((row) => row.Ulke_Sehir || row.city || row.country)
          .filter(Boolean)
      )
    ).slice(0, 120);

    const ageOptions = [
      "All",
      ...Array.from(
        new Set(
          mapRows
            .map((row) => row.Yas_Grubu)
            .filter(Boolean)
        )
      )
    ].slice(0, 40);

    const filteredRows = mapRows.filter((row) => {
      const rowCity = row.Ulke_Sehir || row.city || row.country || "";
      const rowAge = row.Yas_Grubu || "";
      const rowCancer = row.Kanser_Turu || "";
      const cancerNeedle = cancerMatch[cancerType];

      const cityOk = !city || rowCity === city;
      const ageOk = ageGroup === "All" || rowAge === ageGroup;
      const cancerOk = !cancerNeedle || rowCancer.toLowerCase().includes(cancerNeedle.toLowerCase());

      return cityOk && ageOk && cancerOk;
    });

    const avg = (key) => {
      const nums = filteredRows
        .map((row) => safeNumber(row[key], NaN))
        .filter((n) => Number.isFinite(n));

      if (!nums.length) return null;
      return nums.reduce((a, b) => a + b, 0) / nums.length;
    };

    const incidenceAvg = avg("Yillik_Vaka_Hizi_100Bin");
    const mortalityAvg = avg("Yillik_Olum_Hizi_100Bin");
    const survivalAvg = avg("Bes_Yillik_Sagkalim_Yuzdesi");

    const symptomScore = Math.round(fatigue * 2.2 + pain * 2.4 + nausea * 1.8 + mood * 2.1);
    const dataSignal =
      incidenceAvg && mortalityAvg
        ? Math.min(30, Math.round((incidenceAvg + mortalityAvg) / 7))
        : 8;

    const supportScore = Math.min(100, symptomScore + dataSignal);

    // LIVE_SPLUNK_COHORT_CONTEXT_V151
    // Uses the same 0–40 symptom-risk formula as backend /ai-summary.
    const currentCaseRiskV151 =
      Number(fatigue) +
      Number(nausea) +
      Number(pain) +
      (10 - Number(mood));

    const cohortEventCountV151 =
      Number(splunkLiveMetricsV140?.metrics?.total_events || 0);

    const cohortAvgRiskV151 =
      Number(splunkLiveMetricsV140?.metrics?.avg_risk || 0);

    const hasLiveCohortV151 =
      splunkLiveStatusV140 === "ready" &&
      cohortEventCountV151 > 0 &&
      Number.isFinite(cohortAvgRiskV151);

    const cohortRiskDifferenceV151 = hasLiveCohortV151
      ? Number((currentCaseRiskV151 - cohortAvgRiskV151).toFixed(2))
      : 0;

    const cohortComparisonV151 = !hasLiveCohortV151
      ? "unavailable"
      : cohortRiskDifferenceV151 > 3
      ? "higher"
      : cohortRiskDifferenceV151 < -3
      ? "lower"
      : "similar";

    const cohortMarkerPositionV151 =
      cohortComparisonV151 === "lower"
        ? 22
        : cohortComparisonV151 === "higher"
        ? 78
        : 50;

    const cohortComparisonLabelV151 =
      cohortComparisonV151 === "lower"
        ? trText("Lower than live cohort", "Canlı kohorttan daha düşük")
        : cohortComparisonV151 === "higher"
        ? trText("Higher than live cohort", "Canlı kohorttan daha yüksek")
        : cohortComparisonV151 === "similar"
        ? trText("Similar to live cohort", "Canlı kohorta benzer")
        : trText("Live cohort unavailable", "Canlı kohort kullanılamıyor");

    const supportLevel =
      supportScore >= 72 ? "High support priority" :
      supportScore >= 45 ? "Needs attention" :
      "Stable today";

    const supportClass =
      supportScore >= 72 ? "high" :
      supportScore >= 45 ? "medium" :
      "low";

    const redFlags = [
      feverFlag ? trText("Fever or chills during treatment", "Tedavi sırasında ateş veya titreme") : null,
      breathingFlag ? trText("Shortness of breath or chest tightness", "Nefes darlığı veya göğüste sıkışma") : null,
      bleedingFlag ? trText("Unusual bleeding, severe vomiting or dehydration", "Olağan dışı kanama, şiddetli kusma veya susuz kalma") : null,
      confusionFlag ? trText("Confusion, fainting or sudden severe weakness", "Bilinç bulanıklığı, bayılma veya ani ciddi halsizlik") : null
    ].filter(Boolean);

    const clinicalRiskLevel =
      redFlags.length > 0 || goal === "urgent"
        ? trText("Urgent clinical safety check", "Acil klinik güvenlik kontrolü")
        : supportScore >= 72
        ? trText("High support priority", "Yüksek destek önceliği")
        : supportScore >= 45
        ? trText("Needs close monitoring", "Yakın takip gerekli")
        : trText("Stable support preparation", "Stabil destek hazırlığı");

    const safetyMessage =
      redFlags.length > 0
        ? trText(
            "One or more red flags were selected. This tool cannot evaluate emergencies. Contact your oncology team, clinic or emergency services now if symptoms are severe, new or worsening.",
            "Bir veya daha fazla kırmızı bayrak seçildi. Bu araç acil durum değerlendirmesi yapamaz. Semptomlar ciddi, yeni veya kötüleşiyorsa onkoloji ekibiniz, kliniğiniz veya acil servisle hemen iletişime geçin."
          )
        : trText(
            "No red flag was selected. Continue symptom tracking and contact the care team if symptoms worsen or become difficult to tolerate.",
            "Kırmızı bayrak seçilmedi. Semptom takibine devam edin; semptomlar kötüleşirse veya tolere edilmesi zorlaşırsa bakım ekibiyle iletişime geçin."
          );

    const selectedScenarioLabel = caseScenarioLabels[caseScenario] || caseScenarioLabels.chemo_fever;

    const scenarioPlaybooks = {
      chemo_fever: {
        urgency: trText("High safety sensitivity", "Yüksek güvenlik hassasiyeti"),
        immediate: trText("Check temperature, chills, infection signs and whether symptoms are new or worsening.", "Ateş, titreme, enfeksiyon belirtileri ve semptomların yeni ya da kötüleşen durumda olup olmadığını kontrol edin."),
        track: trText("Track temperature, fatigue, fluid intake, nausea, pain and when symptoms started.", "Ateş, yorgunluk, sıvı alımı, bulantı, ağrı ve semptomların ne zaman başladığını takip edin."),
        ask: trText("Ask the oncology team: At what temperature or symptom pattern should I call urgently?", "Onkoloji ekibine sorun: Hangi ateş veya semptom durumunda acil aramalıyım?")
      },
      appointment_prep: {
        urgency: trText("Structured visit preparation", "Yapılandırılmış görüşme hazırlığı"),
        immediate: trText("List the top three changes since the last visit and bring medication information.", "Son görüşmeden bu yana olan en önemli üç değişikliği yazın ve ilaç bilgilerini hazırlayın."),
        track: trText("Track symptoms by day, severity, triggers and what helped.", "Semptomları gün, şiddet, tetikleyici ve neyin iyi geldiğine göre takip edin."),
        ask: trText("Ask: What is expected, what is concerning, and what should be tracked before the next visit?", "Şunu sorun: Ne beklenen bir durum, ne endişe verici ve bir sonraki görüşmeye kadar ne takip edilmeli?")
      },
      side_effects: {
        urgency: trText("Treatment tolerance monitoring", "Tedavi toleransı takibi"),
        immediate: trText("Identify whether symptoms affect eating, sleeping, walking, hydration or daily functioning.", "Semptomların yemek yeme, uyku, yürüme, sıvı alımı veya günlük işlevleri etkileyip etkilemediğini belirleyin."),
        track: trText("Track fatigue, pain, nausea, appetite, bowel changes, sleep and mood daily.", "Yorgunluk, ağrı, bulantı, iştah, bağırsak değişiklikleri, uyku ve ruh halini günlük takip edin."),
        ask: trText("Ask which side effects are expected and which require same-day clinical contact.", "Hangi yan etkilerin beklenen, hangilerinin aynı gün klinik iletişim gerektirdiğini sorun.")
      },
      caregiver_support: {
        urgency: trText("Home support coordination", "Ev desteği koordinasyonu"),
        immediate: trText("Clarify who will monitor symptoms, medication timing, food, fluids and appointments.", "Semptom, ilaç zamanı, beslenme, sıvı alımı ve randevuları kimin takip edeceğini netleştirin."),
        track: trText("Track changes noticed by the patient and caregiver separately.", "Hasta ve bakım veren tarafından fark edilen değişiklikleri ayrı ayrı takip edin."),
        ask: trText("Ask the care team what caregivers should watch for at home.", "Bakım verenlerin evde nelere dikkat etmesi gerektiğini bakım ekibine sorun.")
      },
      child_explanation: {
        urgency: trText("Gentle child-safe explanation", "Çocuğa uygun nazik açıklama"),
        immediate: trText("Use short, calm and age-appropriate language. Do not overload the child with details.", "Kısa, sakin ve yaşa uygun bir dil kullanın. Çocuğu fazla ayrıntıyla yüklemeyin."),
        track: trText("Track the child’s questions, fears, sleep, appetite and school/social changes.", "Çocuğun sorularını, korkularını, uykusunu, iştahını ve okul/sosyal değişimlerini takip edin."),
        ask: trText("Ask the clinical team how to explain treatment steps to a child safely.", "Tedavi adımlarının çocuğa güvenli şekilde nasıl anlatılacağını klinik ekibe sorun.")
      },
      screening_awareness: {
        urgency: trText("Awareness and prevention pathway", "Farkındalık ve önleme yolu"),
        immediate: trText("Clarify age, sex, family history and whether organized screening applies.", "Yaş, cinsiyet, aile öyküsü ve organize taramanın uygulanıp uygulanmadığını netleştirin."),
        track: trText("Track screening eligibility, last screening date and follow-up recommendation.", "Tarama uygunluğu, son tarama tarihi ve takip önerisini not edin."),
        ask: trText("Ask which official screening program or clinic pathway is appropriate.", "Hangi resmi tarama programı veya klinik yolun uygun olduğunu sorun.")
      }
    };

    const scenarioPlan = scenarioPlaybooks[caseScenario] || scenarioPlaybooks.chemo_fever;

    const scenarioGuidanceText = `${scenarioPlan.urgency}. ${scenarioPlan.immediate} ${scenarioPlan.track} ${scenarioPlan.ask}`;

    const splunkEventPayload = {
      source: "oncoconnect_ai_copilot",
      event_type: "patient_support_case_flow",
      role,
      goal,
      scenario: caseScenario,
      scenario_label: selectedScenarioLabel,
      scenario_urgency: scenarioPlan.urgency,
      scenario_immediate_check: scenarioPlan.immediate,
      scenario_tracking: scenarioPlan.track,
      scenario_doctor_question: scenarioPlan.ask,
      city,
      age_group: ageGroup,
      cancer_type: cancerType,
      treatment_stage: treatmentStage,
      main_concern: mainConcern,
      symptom_count: [fatigue, pain, nausea, mood].filter((value) => Number(value) >= 5).length,
      red_flags: redFlags,
      risk_level: clinicalRiskLevel,
      support_score: supportScore,
      support_level: supportLevel,
      public_data_rows: filteredRows.length,
      incidence: incidenceAvg ? Number(incidenceAvg.toFixed(2)) : null,
      mortality: mortalityAvg ? Number(mortalityAvg.toFixed(2)) : null,
      survival: survivalAvg ? Number(survivalAvg.toFixed(1)) : null,
      timestamp: new Date().toISOString()
    };

    const readableTelemetryEvent = String(splunkEventPayload.event_type || "")
      .replaceAll("_", " ")
      .replace(/\s+/g, " ")
      .trim();

    // COPILOT AI POWER DASHBOARD v10 START
    const aiPowerSources = [
      {
        id: "chemotherapy_patient_data",
        name: "Chemotherapy Patient Data",
        file: "/data/chemotherapy_patient_data.csv",
        splunkSource: "chemotherapy_patient_data.csv",
        domain: trText("Chemotherapy symptom monitoring", "Kemoterapi semptom takibi"),
        status: trText("Indexed / ready", "Indexlendi / hazır"),
        signal: trText("Fatigue, nausea, pain, treatment-stage signals", "Yorgunluk, bulantı, ağrı ve tedavi aşaması sinyalleri")
      },
      {
        id: "thyrotrack_mv_processed_dataset",
        name: "ThyroTrack MV Processed Dataset",
        file: "/data/thyrotrack_mv_processed_dataset.csv",
        splunkSource: "ThyroTrack-MV Processed Dataset.csv",
        domain: trText("Thyroid monitoring intelligence", "Tiroid takip zekâsı"),
        status: trText("Indexed / ready", "Indexlendi / hazır"),
        signal: trText("Thyroid monitoring, risk-category and longitudinal pattern signals", "Tiroid takibi, risk kategorisi ve zamansal örüntü sinyalleri")
      },
      {
        id: "oncoconnect_ai_copilot_events",
        name: "OncoConnect AI Copilot Events",
        file: null,
        splunkSource: "oncoconnect_ai_copilot",
        domain: trText("AI workflow telemetry", "AI iş akışı telemetrisi"),
        status: trText("Live event preview", "Canlı olay önizlemesi"),
        signal: trText("Risk score, red flags, scenario, report and action events", "Risk skoru, kırmızı bayraklar, senaryo, rapor ve aksiyon olayları")
      }
    ];

    const aiScenarioModifier =
      caseScenario === "chemo_fever" ? 18 :
      caseScenario === "side_effects" ? 14 :
      caseScenario === "appointment_prep" ? 10 :
      caseScenario === "caregiver_support" ? 8 :
      caseScenario === "child_explanation" ? 7 :
      6;

    const aiPowerBreakdown = [
      {
        label: trText("Symptom signal", "Semptom sinyali"),
        value: symptomScore,
        max: 70,
        detail: trText("Derived from fatigue, pain, nausea and mood sliders.", "Yorgunluk, ağrı, bulantı ve ruh hali kaydırıcılarından türetilir.")
      },
      {
        label: trText("Dataset signal", "Veri seti sinyali"),
        value: dataSignal,
        max: 30,
        detail: trText("Public data and indexed dataset context used as non-diagnostic support context.", "Kamu verisi ve indexlenmiş veri seti bağlamı tanı dışı destek bağlamı olarak kullanılır.")
      },
      {
        label: trText("Red flag signal", "Kırmızı bayrak sinyali"),
        value: Math.min(100, redFlags.length * 25),
        max: 100,
        detail: trText("Safety flags increase urgency and trigger safer recommendations.", "Güvenlik bayrakları aciliyeti artırır ve daha güvenli önerileri tetikler.")
      },
      {
        label: trText("Scenario modifier", "Senaryo katsayısı"),
        value: aiScenarioModifier,
        max: 20,
        detail: selectedScenarioLabel
      }
    ];

    const aiPowerQueries = [
      {
        title: trText("Chemotherapy symptom analytics", "Kemoterapi semptom analitiği"),
        source: "chemotherapy_patient_data.csv",
        query: 'index=oncoconnect source="chemotherapy_patient_data.csv" | stats count avg(fatigue) avg(nausea) avg(pain) by treatment_stage'
      },
      {
        title: trText("ThyroTrack monitoring intelligence", "ThyroTrack takip zekâsı"),
        source: "ThyroTrack-MV Processed Dataset.csv",
        query: 'index=oncoconnect source="ThyroTrack-MV Processed Dataset.csv" | stats count avg(tsh) avg(t3) avg(t4) by risk_category'
      },
      {
        title: trText("AI Copilot workflow telemetry", "AI Copilot iş akışı telemetrisi"),
        source: "oncoconnect_ai_copilot",
        query: 'index=oncoconnect source="oncoconnect_ai_copilot" | stats count avg(support_score) by risk_level scenario'
      }
    ];

    const aiPowerEvidence = [
      trText("Current symptom sliders and red flag checklist", "Mevcut semptom kaydırıcıları ve kırmızı bayrak kontrol listesi"),
      trText("Selected role, goal, cancer type, treatment stage and scenario", "Seçilen rol, hedef, kanser türü, tedavi aşaması ve senaryo"),
      trText("Chemotherapy patient dataset indexed as Splunk source", "Splunk kaynağı olarak indexlenmiş kemoterapi hasta veri seti"),
      trText("ThyroTrack processed monitoring dataset indexed as Splunk source", "Splunk kaynağı olarak indexlenmiş işlenmiş ThyroTrack takip veri seti"),
      trText("OncoConnect AI Copilot telemetry payload", "OncoConnect AI Copilot telemetri payload’u")
    ];

    // AI POWER REAL DATA v11 START
    const [aiPowerRealData, setAiPowerRealData] = useState(null);
    const [aiPowerRealDataStatus, setAiPowerRealDataStatus] = useState("loading");

    useEffect(() => {
      let mounted = true;

      fetch("/data/ai_power_dataset_summary.json")
        .then((res) => {
          if (!res.ok) throw new Error(`AI Power summary HTTP ${res.status}`);
          return res.json();
        })
        .then((data) => {
          if (!mounted) return;
          setAiPowerRealData(data);
          setAiPowerRealDataStatus("loaded");
        })
        .catch(() => {
          if (!mounted) return;
          setAiPowerRealDataStatus("error");
        });

      return () => {
        mounted = false;
      };
    }, []);

    const aiPowerRealDatasets = aiPowerRealData?.datasets || [];

    const formatAiPowerNumber = (value) => {
      const num = Number(value || 0);
      return new Intl.NumberFormat("en-US").format(Math.round(num));
    };

    const formatAiPowerDecimal = (value) => {
      const num = Number(value || 0);
      return Number.isFinite(num) ? num.toFixed(2) : "0.00";
    };

    const aiPowerTrendPoints = (trend = []) => {
      if (!trend.length) return "";
      return trend.map((item, index) => {
        const x = trend.length === 1 ? 50 : (index / (trend.length - 1)) * 100;
        const y = 100 - Math.max(0, Math.min(100, Number(item.relative || 0)));
        return `${x},${y}`;
      }).join(" ");
    };

    // AI DATA PROVENANCE PDF v12 START
    const aiDataLineageRows = [
      {
        layer: trText("City / public cancer context", "Şehir / kamu kanser bağlamı"),
        source: "turkiye_avrupa_kanser_istatistikleri_detayli.csv",
        usedFor: trText("city dropdown, incidence, mortality, 5-year survival and map ranking", "şehir seçimi, insidans, mortalite, 5 yıllık sağkalım ve harita sıralaması"),
        columns: "Ulke_Sehir, Kanser_Turu, Yas_Grubu, Yillik_Vaka_Hizi_100Bin, Yillik_Olum_Hizi_100Bin, Bes_Yillik_Sagkalim_Yuzdesi"
      },
      {
        layer: trText("Chemotherapy analytics", "Kemoterapi analitiği"),
        source: "chemotherapy_patient_data.csv",
        usedFor: trText("symptom burden, tumor-stage distribution and treatment context", "semptom yükü, tümör evresi dağılımı ve tedavi bağlamı"),
        columns: "Nausea_Severity, Tumor_Stage, Tumor_Response, Overall_Survival_Months, Cycles_Completed"
      },
      {
        layer: trText("Thyroid monitoring analytics", "Tiroid takip analitiği"),
        source: "thyrotrack_mv_processed_dataset.csv",
        usedFor: trText("thyroid signal bars, monitoring-risk distribution and correlation preview", "tiroid sinyal barları, takip-risk dağılımı ve korelasyon önizlemesi"),
        columns: "Nodule_Size_mm, TSH_Risk_Level, Reverse_T3_Index, Recurrence_Risk, Symptom_Onset_Duration"
      },
      {
        layer: trText("AI workflow telemetry", "AI iş akışı telemetrisi"),
        source: "oncoconnect_ai_copilot",
        usedFor: trText("risk score, red flags, scenario, report and audit trail", "risk skoru, kırmızı bayraklar, senaryo, rapor ve denetim izi"),
        columns: "support_score, risk_level, red_flags, scenario, event_type, timestamp"
      }
    ];

    const publicDataHasMatch = typeof selectedPublicData !== "undefined" && Boolean(selectedPublicData);
    const publicDataNoMatchMessage = trText(
      "No matching public row was found for the selected city, cancer type and age filters. The Copilot keeps the case workflow active, but public incidence/mortality/survival context is shown as unavailable.",
      "Seçilen şehir, kanser türü ve yaş filtreleri için eşleşen kamu veri satırı bulunamadı. Copilot vaka akışını çalıştırmaya devam eder; ancak kamu insidans/mortalite/sağkalım bağlamı kullanılamıyor olarak gösterilir."
    );

    const aiPowerColumnMeaning = {
      Nausea_Severity: trText("chemotherapy symptom burden bar", "kemoterapi semptom yükü barı"),
      Tumor_Stage: trText("chemotherapy risk/prognosis distribution", "kemoterapi risk/prognoz dağılımı"),
      Tumor_Response: trText("treatment response context", "tedavi yanıtı bağlamı"),
      Overall_Survival_Months: trText("survival-context signal, not a personal prediction", "sağkalım bağlam sinyali, kişisel tahmin değildir"),
      Nodule_Size_mm: trText("thyroid nodule morphology signal", "tiroid nodül morfoloji sinyali"),
      TSH_Risk_Level: trText("thyroid monitoring risk distribution", "tiroid takip risk dağılımı"),
      Reverse_T3_Index: trText("hormone-related monitoring signal", "hormon ilişkili takip sinyali"),
      Recurrence_Risk: trText("monitoring/prognosis proxy, not a diagnosis", "takip/prognoz vekil sinyali, tanı değildir")
    };

    const getAiPowerColumnMeaning = (label) => aiPowerColumnMeaning[label] || trText("dataset-derived feature", "veri setinden türetilmiş özellik");

    const buildRealDataEvidenceHtml = () => {
      const datasets = aiPowerRealData?.datasets || [];

      if (!datasets.length) {
        return `
          <section class="report-section report-real-data-evidence">
            <h2>REAL DATA EVIDENCE</h2>
            <p class="report-muted">AI Power dataset summary was not loaded in the browser session.</p>
          </section>
        `;
      }

      const datasetCards = datasets.map((dataset) => {
        const metrics = (dataset.key_metrics || [])
          .slice(0, 5)
          .map((metric) => `
            <li>
              <b>${escapeReportHtml(metric.label)}</b>
              <span>avg ${escapeReportHtml(formatAiPowerDecimal(metric.value))} · ${escapeReportHtml(getAiPowerColumnMeaning(metric.label))}</span>
            </li>
          `)
          .join("");

        const risks = (dataset.risk_distribution || [])
          .slice(0, 4)
          .map((risk) => `
            <li>
              <b>${escapeReportHtml(risk.label)}</b>
              <span>${escapeReportHtml(risk.percent)}% · ${escapeReportHtml(String(risk.count || ""))} rows</span>
            </li>
          `)
          .join("");

        const correlations = (dataset.correlations || [])
          .slice(0, 4)
          .map((corr) => `
            <li>
              <b>${escapeReportHtml(corr.x)} ↔ ${escapeReportHtml(corr.y)}</b>
              <span>r=${escapeReportHtml(corr.r)} · ${escapeReportHtml(corr.strength)}</span>
            </li>
          `)
          .join("");

        return `
          <article class="report-real-data-card">
            <h3>${escapeReportHtml(dataset.name)}</h3>
            <div class="report-real-kpis">
              <div><small>Rows</small><b>${escapeReportHtml(formatAiPowerNumber(dataset.row_count))}</b></div>
              <div><small>Columns</small><b>${escapeReportHtml(dataset.column_count)}</b></div>
              <div><small>Numeric columns</small><b>${escapeReportHtml(dataset.numeric_columns_detected)}</b></div>
              <div><small>Checksum</small><b>${escapeReportHtml(dataset.sha256_prefix)}</b></div>
            </div>
            <p><b>Source:</b> ${escapeReportHtml(dataset.source)}</p>
            <p><b>Risk source:</b> ${escapeReportHtml(dataset.risk_source)}</p>
            <h4>Key dataset-derived features</h4>
            <ul>${metrics || "<li><span>No key metric preview available.</span></li>"}</ul>
            <h4>Risk / prognosis distribution</h4>
            <ul>${risks || "<li><span>No risk distribution preview available.</span></li>"}</ul>
            <h4>Top correlations</h4>
            <ul>${correlations || "<li><span>No strong correlation detected in preview sample.</span></li>"}</ul>
          </article>
        `;
      }).join("");

      return `
        <section class="report-section report-real-data-evidence">
          <h2>REAL DATA EVIDENCE</h2>
          <p class="report-muted">
            These analytics are generated from committed CSV dataset summaries. They support explainability and auditability, but they are not diagnostic predictions or clinical triage decisions.
          </p>
          <div class="report-lineage-table">
            ${aiDataLineageRows.map((row) => `
              <div>
                <b>${escapeReportHtml(row.layer)}</b>
                <span>${escapeReportHtml(row.source)}</span>
                <small>${escapeReportHtml(row.usedFor)}</small>
                <code>${escapeReportHtml(row.columns)}</code>
              </div>
            `).join("")}
          </div>
          ${!publicDataHasMatch ? `<div class="report-warning">${escapeReportHtml(publicDataNoMatchMessage)}</div>` : ""}
          <div class="report-real-data-grid">
            ${datasetCards}
          </div>
        </section>
      `;
    };
    // ACCESS LIFESTYLE PERFORMANCE v14 START
    const [accessLifestyleContextV14, setAccessLifestyleContextV14] = useState(null);
    const [accessLifestyleErrorV14, setAccessLifestyleErrorV14] = useState("");

    useEffect(() => {
      let cancelled = false;

      Promise.all([
        fetch("/data/ai_system_context_v14.json").then((response) => {
          if (!response.ok) throw new Error("ai_system_context_v14.json not loaded");
          return response.json();
        }),
        fetch("/data/nhs_cancer_waiting_times_summary_v14.json").then((response) => {
          if (!response.ok) throw new Error("nhs_cancer_waiting_times_summary_v14.json not loaded");
          return response.json();
        }),
        fetch("/data/cancer_treatment_performance_summary_v14.json").then((response) => {
          if (!response.ok) throw new Error("cancer_treatment_performance_summary_v14.json not loaded");
          return response.json();
        }),
        fetch("/data/colorectal_lifestyle_summary_v14.json").then((response) => {
          if (!response.ok) throw new Error("colorectal_lifestyle_summary_v14.json not loaded");
          return response.json();
        })
      ])
        .then(([system, nhs, treatment, crc]) => {
          if (!cancelled) {
            setAccessLifestyleContextV14({ system, nhs, treatment, crc });
            setAccessLifestyleErrorV14("");
          }
        })
        .catch((error) => {
          if (!cancelled) {
            setAccessLifestyleErrorV14(error.message || "v14 context could not be loaded");
          }
        });

      return () => {
        cancelled = true;
      };
    }, []);

    const v14Context = accessLifestyleContextV14;
    const v14Nhs = v14Context?.nhs;
    const v14Treatment = v14Context?.treatment;
    const v14Crc = v14Context?.crc;
    const v14System = v14Context?.system;

    const v14NhsTables = v14Nhs?.tables ? Object.entries(v14Nhs.tables).map(([id, table]) => ({ id, ...table })) : [];
    const v14NhsHighlights = v14NhsTables.slice(0, 5).map((table) => ({
      label: table.description,
      total: table.total_patients_or_pathways,
      performance: table.weighted_performance_percent,
      after: table.after_standard,
      insight: table.weighted_performance_percent < 80
        ? trText("High access-pressure context", "Yüksek erişim baskısı bağlamı")
        : trText("Treatment pathway performance context", "Tedavi yolu performans bağlamı")
    }));

    const v14TreatmentKpis = v14Treatment?.kpis || {};
    const v14CrcRiskBreakdowns = v14Crc?.risk_group_breakdowns || {};
    const v14CrcLifestyleRows = v14CrcRiskBreakdowns.Lifestyle || [];
    const v14TreatmentStages = v14Treatment?.stage_distribution || [];

    const v14IntelligenceEdges = [
      {
        layer: trText("Access pressure", "Erişim baskısı"),
        from: "NHS waiting-time pathways",
        to: trText("care escalation question", "bakım yükseltme sorusu"),
        why: trText("Waiting-time performance adds system-level pressure context to patient/caregiver actions.", "Bekleme süresi performansı hasta/bakıcı aksiyonlarına sistem düzeyi baskı bağlamı ekler."),
        action: trText("Ask when the next appointment, diagnostic result or treatment decision should happen and what to do if it is delayed.", "Sonraki randevu, tanı sonucu veya tedavi kararının ne zaman olması gerektiğini ve gecikirse ne yapılacağını sor.")
      },
      {
        layer: trText("Treatment performance", "Tedavi performansı"),
        from: "Diagnosis / stage / regimen KPIs",
        to: trText("cohort-level treatment context", "kohort düzeyi tedavi bağlamı"),
        why: trText("Treatment response, cycles and follow-up visits explain journey intensity without recommending a treatment.", "Tedavi yanıtı, döngüler ve takip ziyaretleri tedavi önermeden yolculuk yoğunluğunu açıklar."),
        action: trText("Prepare questions about expected response timing, follow-up frequency and side-effect monitoring.", "Beklenen yanıt zamanı, takip sıklığı ve yan etki izleme hakkında sorular hazırla.")
      },
      {
        layer: trText("Lifestyle / prevention", "Yaşam tarzı / önleme"),
        from: "CRC diet, BMI, family history and comorbidities",
        to: trText("screening and prevention discussion", "tarama ve önleme görüşmesi"),
        why: trText("Lifestyle and family-history fields convert raw risk factors into non-diagnostic awareness prompts.", "Yaşam tarzı ve aile öyküsü alanları ham risk faktörlerini tanısal olmayan farkındalık uyarılarına dönüştürür."),
        action: trText("Discuss screening history, family history, activity, BMI and diet pattern with a clinician.", "Tarama geçmişi, aile öyküsü, aktivite, BMI ve beslenme örüntüsünü klinisyenle konuş.")
      }
    ];

    const v14ActionPath = {
      who: String(role || "").toLowerCase().includes("caregiver")
        ? trText("Caregiver should coordinate questions, appointment timing and daily symptom/lifestyle notes.", "Bakıcı soruları, randevu zamanını ve günlük semptom/yaşam tarzı notlarını koordine etmeli.")
        : trText("Patient should use this as a structured preparation note for the care team.", "Hasta bunu bakım ekibi için yapılandırılmış hazırlık notu olarak kullanmalı."),
      where: v14Nhs
        ? trText("Access pressure is shown from NHS provider-based pathway data and should be treated as system-level context.", "Erişim baskısı NHS provider-based pathway verisinden gösterilir ve sistem düzeyi bağlam olarak ele alınmalıdır.")
        : trText("Access-pressure context is not loaded.", "Erişim baskısı bağlamı yüklenmedi."),
      why: trText("The graph now connects patient input, public burden, waiting-time access, treatment performance and lifestyle-prevention signals.", "Graf artık hasta girdisini, kamu yükünü, bekleme süresi erişimini, tedavi performansını ve yaşam tarzı/önleme sinyallerini bağlıyor."),
      what: trText("Generate a concise care conversation plan: delay questions, treatment journey questions, symptom tracking and prevention/screening prompts.", "Kısa bir bakım görüşmesi planı üret: gecikme soruları, tedavi yolculuğu soruları, semptom takibi ve önleme/tarama uyarıları."),
      safety: trText("Do not use these datasets as diagnosis, personal prognosis, treatment selection or emergency triage.", "Bu veri setlerini tanı, kişisel prognoz, tedavi seçimi veya acil triyaj olarak kullanma.")
    };

    const buildAccessLifestylePerformanceHtmlV14 = () => {
      if (!v14Context) {
        return `
          <section class="report-section report-v14-system-map">
            <h2>ACCESS, LIFESTYLE & TREATMENT PERFORMANCE INTELLIGENCE</h2>
            <p class="report-muted">v14 context was not loaded in this browser session.</p>
          </section>
        `;
      }

      const accessRows = v14NhsHighlights.map((item) => `
        <div>
          <b>${escapeReportHtml(item.label)}</b>
          <span>${escapeReportHtml(formatAiPowerNumber(item.total))} pathways · ${escapeReportHtml(item.performance)}% within standard</span>
          <small>${escapeReportHtml(item.insight)} · ${escapeReportHtml(formatAiPowerNumber(item.after))} after standard</small>
        </div>
      `).join("");

      const lifestyleRows = v14CrcLifestyleRows.slice(0, 5).map((item) => `
        <div>
          <b>${escapeReportHtml(item.label)}</b>
          <span>${escapeReportHtml(item.crc_risk_rate_percent)}% CRC risk flag rate · ${escapeReportHtml(formatAiPowerNumber(item.count))} rows</span>
        </div>
      `).join("");

      const edgeRows = v14IntelligenceEdges.map((edge) => `
        <div>
          <b>${escapeReportHtml(edge.layer)}: ${escapeReportHtml(edge.from)} → ${escapeReportHtml(edge.to)}</b>
          <span>${escapeReportHtml(edge.why)}</span>
          <small>${escapeReportHtml(edge.action)}</small>
        </div>
      `).join("");

      return `
        <section class="report-section report-v14-system-map">
          <h2>ACCESS, LIFESTYLE & TREATMENT PERFORMANCE INTELLIGENCE</h2>
          <p class="report-muted">v14 adds NHS waiting-time access pressure, cancer treatment performance KPIs and colorectal lifestyle/prevention context to the relational AI graph.</p>
          <h3>New relationship layers</h3>
          <div class="report-v14-edges">${edgeRows}</div>
          <h3>NHS access pressure</h3>
          <div class="report-v14-grid">${accessRows}</div>
          <h3>Treatment performance context</h3>
          <div class="report-v14-kpis">
            <div><small>Average response score</small><b>${escapeReportHtml(v14TreatmentKpis.avg_response_score)}</b></div>
            <div><small>Average cycles</small><b>${escapeReportHtml(v14TreatmentKpis.avg_cycles)}</b></div>
            <div><small>Avg. response days</small><b>${escapeReportHtml(v14TreatmentKpis.avg_time_to_response_days)}</b></div>
            <div><small>Avg. follow-up visits</small><b>${escapeReportHtml(v14TreatmentKpis.avg_follow_up_visits)}</b></div>
          </div>
          <h3>Colorectal lifestyle / prevention context</h3>
          <div class="report-v14-grid">${lifestyleRows}</div>
          <h3>Smart action path</h3>
          <div class="report-action-output">
            <div><b>Who</b><span>${escapeReportHtml(v14ActionPath.who)}</span></div>
            <div><b>Where</b><span>${escapeReportHtml(v14ActionPath.where)}</span></div>
            <div><b>Why</b><span>${escapeReportHtml(v14ActionPath.why)}</span></div>
            <div><b>What</b><span>${escapeReportHtml(v14ActionPath.what)}</span></div>
            <div><b>Safety</b><span>${escapeReportHtml(v14ActionPath.safety)}</span></div>
          </div>
        </section>
      `;
    };
    // ACCESS LIFESTYLE PERFORMANCE v14 END

    // AI RELATIONAL INTELLIGENCE GRAPH v13 START
    const [relationAnswers, setRelationAnswers] = useState({});

    const setRelationAnswer = (questionId, option) => {
      setRelationAnswers((prev) => ({
        ...prev,
        [questionId]: option
      }));
    };

    const relationAnswerValues = Object.values(relationAnswers || {});
    const relationUrgencyBoost = relationAnswerValues.reduce((total, item) => total + Number(item?.weight || 0), 0);
    const relationalPriorityScore = Math.min(100, Math.max(0, supportScore + relationUrgencyBoost));
    const relationalPriorityLabel =
      redFlags.length > 0 || relationalPriorityScore >= 75
        ? trText("Urgent safety conversation", "Acil güvenlik görüşmesi")
        : relationalPriorityScore >= 55
          ? trText("High monitoring priority", "Yüksek takip önceliği")
          : relationalPriorityScore >= 35
            ? trText("Structured follow-up priority", "Yapılandırılmış takip önceliği")
            : trText("Routine tracking priority", "Rutin takip önceliği");

    const aiRelationNodes = [
      {
        id: "patient",
        label: trText("Patient / caregiver input", "Hasta / bakıcı girdisi"),
        type: trText("Current case", "Mevcut vaka"),
        detail: `${city || trText("All locations", "Tüm konumlar")} · ${ageGroup}`,
        strength: Math.max(12, Math.min(100, symptomScore))
      },
      {
        id: "public",
        label: trText("Public cancer context", "Kamu kanser bağlamı"),
        type: "CSV",
        detail: trText("city, age, incidence, mortality, survival", "şehir, yaş, insidans, mortalite, sağkalım"),
        strength: Math.max(8, Math.min(100, dataSignal * 3))
      },
      {
        id: "chemo",
        label: trText("Chemotherapy cohort signal", "Kemoterapi kohort sinyali"),
        type: "CSV",
        detail: trText("stage, nausea, neutropenia, response, survival context", "evre, bulantı, nötropeni, yanıt, sağkalım bağlamı"),
        strength: cancerType ? 72 : 48
      },
      {
        id: "thyro",
        label: trText("ThyroTrack monitoring signal", "ThyroTrack takip sinyali"),
        type: "CSV",
        detail: trText("nodule size, TSH risk, recurrence risk, symptom timeline", "nodül boyutu, TSH riski, nüks riski, semptom zaman çizgisi"),
        strength: String(cancerType || "").toLowerCase().includes("thyroid") ? 88 : 54
      },
      {
        id: "safety",
        label: trText("Safety override", "Güvenlik önceliği"),
        type: trText("Red flags", "Kırmızı bayraklar"),
        detail: redFlags.length ? redFlags.join(", ") : trText("No red flag selected", "Kırmızı bayrak seçilmedi"),
        strength: redFlags.length ? 100 : 24
      },
      {
        id: "output",
        label: trText("AI support output", "AI destek çıktısı"),
        type: trText("Action", "Aksiyon"),
        detail: relationalPriorityLabel,
        strength: relationalPriorityScore
      }
    ];

    const aiRelationEdges = [
      {
        from: "Patient input",
        to: "Symptom burden",
        source: trText("Current Copilot answers", "Mevcut Copilot yanıtları"),
        relation: trText("fatigue / pain / nausea / mood increase support priority", "yorgunluk / ağrı / bulantı / ruh hali destek önceliğini artırır"),
        why: trText("Symptoms define the immediate communication need before the doctor visit.", "Semptomlar doktor görüşmesi öncesindeki acil iletişim ihtiyacını belirler."),
        action: trText("Track severity, timing and change since yesterday.", "Şiddeti, zamanlamayı ve dünden bugüne değişimi takip et.")
      },
      {
        from: "City + age group",
        to: "Public cancer context",
        source: "turkiye_avrupa_kanser_istatistikleri_detayli.csv",
        relation: trText("adds population-level incidence / mortality / survival context", "popülasyon düzeyi insidans / mortalite / sağkalım bağlamı ekler"),
        why: trText("This explains regional context but does not calculate personal medical risk.", "Bu bölgesel bağlamı açıklar; kişisel tıbbi risk hesaplamaz."),
        action: trText("Use it as awareness context, not as diagnosis.", "Bunu tanı değil farkındalık bağlamı olarak kullan.")
      },
      {
        from: "Cancer type + treatment stage",
        to: "Chemotherapy cohort signal",
        source: "chemotherapy_patient_data.csv",
        relation: trText("links tumor stage, nausea severity, neutropenia and response context", "tümör evresi, bulantı şiddeti, nötropeni ve yanıt bağlamını ilişkilendirir"),
        why: trText("Treatment-stage and side-effect patterns help prepare better questions for the care team.", "Tedavi aşaması ve yan etki örüntüleri bakım ekibi için daha iyi soru hazırlamaya yardımcı olur."),
        action: trText("Ask whether nausea, fever, low immunity or weakness should change follow-up timing.", "Bulantı, ateş, düşük bağışıklık veya halsizliğin takip zamanını değiştirip değiştirmediğini sor.")
      },
      {
        from: "Thyroid monitoring features",
        to: "Follow-up priority",
        source: "thyrotrack_mv_processed_dataset.csv",
        relation: trText("connects nodule size, TSH risk level, recurrence risk and symptom duration", "nodül boyutu, TSH risk düzeyi, nüks riski ve semptom süresini bağlar"),
        why: trText("Longitudinal monitoring signals support follow-up planning, especially for thyroid-related cases.", "Zamansal takip sinyalleri özellikle tiroid ilişkili vakalarda takip planlamasını destekler."),
        action: trText("Clarify which lab, scan or symptom change should trigger earlier review.", "Hangi laboratuvar, görüntüleme veya semptom değişiminin daha erken kontrol gerektirdiğini netleştir.")
      },
      {
        from: "Red flags",
        to: "Safety override",
        source: trText("User-selected safety checklist", "Kullanıcının seçtiği güvenlik listesi"),
        relation: trText("overrides routine guidance when severe or worsening signs are present", "şiddetli veya kötüleşen bulgular varsa rutin yönlendirmeyi geçersiz kılar"),
        why: trText("Safety signals should be escalated before any analytics interpretation.", "Güvenlik sinyalleri her türlü analitik yorumdan önce yükseltilmelidir."),
        action: trText("Contact oncology team, clinic or emergency support according to local guidance.", "Yerel yönlendirmeye göre onkoloji ekibi, klinik veya acil destek ile iletişime geç.")
      }
    ];

    const relationalQuestionFlow = [
      {
        id: "observer",
        question: trText("Who is completing this support check?", "Bu destek kontrolünü kim dolduruyor?"),
        reason: trText("The output changes depending on whether the patient or caregiver will act.", "Çıktı, aksiyonu hastanın mı bakım verenin mi alacağına göre değişir."),
        options: [
          { label: trText("Patient", "Hasta"), value: "patient", weight: 0 },
          { label: trText("Caregiver / family member", "Bakıcı / aile yakını"), value: "caregiver", weight: 4 },
          { label: trText("Clinician / navigator", "Klinisyen / hasta yönlendirici"), value: "clinician", weight: 2 }
        ]
      },
      {
        id: "change",
        question: trText("What changed most compared with yesterday or the last visit?", "Düne veya son kontrole göre en çok ne değişti?"),
        reason: trText("Change over time is often more important than a single value.", "Zaman içindeki değişim çoğu zaman tek bir değerden daha önemlidir."),
        options: [
          { label: trText("Symptoms are stable", "Semptomlar stabil"), value: "stable", weight: 0 },
          { label: trText("Symptoms are worse", "Semptomlar kötüleşti"), value: "worse", weight: 12 },
          { label: trText("New symptom appeared", "Yeni semptom çıktı"), value: "new_symptom", weight: 14 }
        ]
      },
      {
        id: "support",
        question: trText("What does the patient need most right now?", "Hastanın şu anda en çok neye ihtiyacı var?"),
        reason: trText("The system converts the answer into a concrete doctor/caregiver action.", "Sistem yanıtı somut doktor/bakıcı aksiyonuna dönüştürür."),
        options: [
          { label: trText("Prepare doctor questions", "Doktor soruları hazırlamak"), value: "questions", weight: 2 },
          { label: trText("Understand side effects", "Yan etkileri anlamak"), value: "side_effects", weight: 6 },
          { label: trText("Decide whether to seek urgent help", "Acil destek gerekip gerekmediğini anlamak"), value: "urgent_help", weight: 18 }
        ]
      },
      {
        id: "home_capacity",
        question: trText("Can the patient drink, eat, move and communicate normally?", "Hasta normal şekilde içebiliyor, yiyebiliyor, hareket ve iletişim kurabiliyor mu?"),
        reason: trText("Reduced home capacity strengthens the safety and caregiver action path.", "Evde bakım kapasitesinin düşmesi güvenlik ve bakıcı aksiyon yolunu güçlendirir."),
        options: [
          { label: trText("Yes, mostly normal", "Evet, çoğunlukla normal"), value: "normal", weight: 0 },
          { label: trText("Partly limited", "Kısmen sınırlı"), value: "limited", weight: 8 },
          { label: trText("No, clearly worse", "Hayır, belirgin kötü"), value: "worse_capacity", weight: 18 }
        ]
      }
    ];

    const observerAnswer = relationAnswers.observer?.value || role;
    const changeAnswer = relationAnswers.change?.value || "not_selected";
    const supportAnswer = relationAnswers.support?.value || "not_selected";
    const homeCapacityAnswer = relationAnswers.home_capacity?.value || "not_selected";

    const relationalActionOutput = {
      who: observerAnswer === "caregiver"
        ? trText("Caregiver / family member should help document symptoms and contact the care team if safety signs are present.", "Bakıcı / aile yakını semptomları belgelemeye yardım etmeli ve güvenlik bulguları varsa bakım ekibiyle iletişime geçmeli.")
        : observerAnswer === "clinician"
          ? trText("Clinician / navigator should review red flags, symptom trend and dataset context before advising next steps.", "Klinisyen / yönlendirici sonraki adımı önermeden önce kırmızı bayrakları, semptom trendini ve veri bağlamını gözden geçirmeli.")
          : trText("Patient should track symptoms clearly and use the prepared questions during the next care-team contact.", "Hasta semptomları net takip etmeli ve hazırlanan soruları bir sonraki bakım ekibi görüşmesinde kullanmalı."),
      where: city
        ? trText(`Use ${city} public cancer context only as population-level awareness.`, `${city} kamu kanser bağlamını sadece popülasyon düzeyi farkındalık olarak kullan.`)
        : trText("No city is selected; public context is shown at broader dataset level.", "Şehir seçilmedi; kamu bağlamı daha geniş veri seti düzeyinde gösterilir."),
      why: redFlags.length
        ? trText("Red flags are present, so safety escalation is more important than routine analytics.", "Kırmızı bayraklar mevcut; bu yüzden güvenlik yükseltmesi rutin analitikten daha önemlidir.")
        : changeAnswer === "worse" || changeAnswer === "new_symptom"
          ? trText("The patient/caregiver reported worsening or new symptoms, increasing follow-up priority.", "Hasta/bakıcı kötüleşme veya yeni semptom bildirdi; bu takip önceliğini artırır.")
          : trText("Current signals support structured tracking and better doctor-visit preparation.", "Mevcut sinyaller yapılandırılmış takip ve daha iyi doktor görüşmesi hazırlığını destekler."),
      what: supportAnswer === "urgent_help" || homeCapacityAnswer === "worse_capacity" || redFlags.length
        ? trText("Prepare a concise safety message and contact the oncology team, clinic or emergency support according to local guidance.", "Kısa bir güvenlik mesajı hazırla ve yerel yönlendirmeye göre onkoloji ekibi, klinik veya acil destekle iletişime geç.")
        : supportAnswer === "side_effects"
          ? trText("Track side-effect severity, timing, treatment cycle and medication adherence before the next call or visit.", "Bir sonraki arama/görüşmeden önce yan etki şiddetini, zamanlamayı, tedavi döngüsünü ve ilaç uyumunu takip et.")
          : trText("Use the generated doctor questions and symptom summary as a structured communication aid.", "Üretilen doktor sorularını ve semptom özetini yapılandırılmış iletişim desteği olarak kullan."),
      when: relationalPriorityScore >= 75
        ? trText("Now / same day if symptoms are severe, new or worsening.", "Semptomlar şiddetli, yeni veya kötüleşiyorsa şimdi / aynı gün.")
        : relationalPriorityScore >= 55
          ? trText("Soon; do not wait for routine follow-up if symptoms continue to worsen.", "Yakında; semptomlar kötüleşmeye devam ederse rutin kontrolü bekleme.")
          : trText("At the next planned contact, unless new safety signs appear.", "Yeni güvenlik bulguları çıkmadıkça bir sonraki planlı görüşmede.")
    };

    const buildRelationalEvidenceHtml = () => {
      const answerRows = relationalQuestionFlow.map((q) => {
        const selected = relationAnswers[q.id];
        return `
          <div>
            <b>${escapeReportHtml(q.question)}</b>
            <span>${escapeReportHtml(selected?.label || "Not selected")}</span>
            <small>${escapeReportHtml(q.reason)}</small>
          </div>
        `;
      }).join("");

      const edgeRows = aiRelationEdges.map((edge) => `
        <div>
          <b>${escapeReportHtml(edge.from)} → ${escapeReportHtml(edge.to)}</b>
          <span>${escapeReportHtml(edge.source)}</span>
          <small>${escapeReportHtml(edge.relation)}</small>
          <p>${escapeReportHtml(edge.why)}</p>
          <em>${escapeReportHtml(edge.action)}</em>
        </div>
      `).join("");

      return `
        <section class="report-section report-relational-evidence">
          <h2>RELATIONAL AI EVIDENCE MAP</h2>
          <p class="report-muted">
            This section explains how OncoConnect AI connects current case inputs, public cancer context, chemotherapy cohort signals, thyroid monitoring signals and safety rules into a non-diagnostic support graph.
          </p>

          <div class="report-relational-score">
            <div><small>Relational priority</small><b>${escapeReportHtml(relationalPriorityScore)}/100</b></div>
            <div><small>Interpretation</small><b>${escapeReportHtml(relationalPriorityLabel)}</b></div>
          </div>

          <h3>Relationship reasoning</h3>
          <div class="report-relational-edges">${edgeRows}</div>

          <h3>Patient / caregiver answers</h3>
          <div class="report-relational-answers">${answerRows}</div>

          <h3>Action output</h3>
          <div class="report-action-output">
            <div><b>Who</b><span>${escapeReportHtml(relationalActionOutput.who)}</span></div>
            <div><b>Where</b><span>${escapeReportHtml(relationalActionOutput.where)}</span></div>
            <div><b>Why</b><span>${escapeReportHtml(relationalActionOutput.why)}</span></div>
            <div><b>What</b><span>${escapeReportHtml(relationalActionOutput.what)}</span></div>
            <div><b>When</b><span>${escapeReportHtml(relationalActionOutput.when)}</span></div>
          </div>

          <p class="report-muted">
            These outputs are communication and support aids only. They are not diagnosis, treatment selection, emergency triage or personal survival prediction.
          </p>
        </section>
      `;
    };
    // DATA TO MEANING UX v15 START
    const contextModeV15 = publicDataHasMatch
      ? trText("Exact public context match", "Tam kamu veri eşleşmesi")
      : trText("Broader context mode", "Geniş bağlam modu");

    const contextModeDetailV15 = publicDataHasMatch
      ? trText(
          "The selected city, age group and cancer filters matched a public statistics row.",
          "Seçilen şehir, yaş grubu ve kanser filtreleri kamu istatistik satırıyla eşleşti."
        )
      : trText(
          "No exact public statistics row was found, so the system keeps the care workflow active and uses broader dataset, treatment and lifestyle signals instead of showing a dead end.",
          "Tam kamu istatistik satırı bulunamadı; bu yüzden sistem çıkmaz mesajı göstermek yerine bakım akışını aktif tutar ve daha geniş veri seti, tedavi ve yaşam tarzı sinyallerini kullanır."
        );

    const dataToMeaningCardsV15 = [
      {
        label: trText("Current patient signal", "Mevcut hasta sinyali"),
        raw: trText("Symptom sliders, red flags and selected scenario", "Semptom sliderları, kırmızı bayraklar ve seçilen senaryo"),
        meaning: redFlags.length
          ? trText("Safety signals override routine interpretation.", "Güvenlik sinyalleri rutin yorumu geçersiz kılar.")
          : symptomScore >= 40
            ? trText("Symptoms suggest close monitoring and structured care-team communication.", "Semptomlar yakın takip ve yapılandırılmış bakım ekibi iletişimi gerektirir.")
            : trText("Symptoms support routine tracking and better preparation.", "Semptomlar rutin takip ve daha iyi hazırlığı destekler."),
        action: redFlags.length
          ? trText("Prepare a same-day safety message for the care team.", "Bakım ekibi için aynı gün güvenlik mesajı hazırla.")
          : trText("Track timing, severity and change before the next visit.", "Bir sonraki görüşmeden önce zamanlama, şiddet ve değişimi takip et."),
        score: Math.max(8, Math.min(100, symptomScore))
      },
      {
        label: trText("Public / access context", "Kamu / erişim bağlamı"),
        raw: trText("City, age group, cancer filters and NHS waiting-time pressure", "Şehir, yaş grubu, kanser filtreleri ve NHS bekleme süresi baskısı"),
        meaning: publicDataHasMatch
          ? trText("Population-level context is available for the selected filters.", "Seçilen filtreler için popülasyon düzeyi bağlam mevcut.")
          : trText("Exact public match is missing, so the system uses broader access-pressure context.", "Tam kamu eşleşmesi yok; sistem daha geniş erişim baskısı bağlamını kullanır."),
        action: trText("Ask what happens if appointment, diagnostic result or treatment decision is delayed.", "Randevu, tanı sonucu veya tedavi kararı gecikirse ne yapılacağını sor."),
        score: Math.max(10, Math.min(100, dataSignal * 3 + 24))
      },
      {
        label: trText("Treatment evidence", "Tedavi kanıtı"),
        raw: trText("Chemotherapy regimen, stage, response and treatment-performance KPIs", "Kemoterapi rejimi, evre, yanıt ve tedavi performans KPI’ları"),
        meaning: trText("Treatment data becomes a doctor-question and monitoring-priority layer, not a treatment recommendation.", "Tedavi verisi tedavi önerisi değil, doktor sorusu ve takip önceliği katmanına dönüşür."),
        action: trText("Prepare questions about expected side effects, response timing and follow-up frequency.", "Beklenen yan etkiler, yanıt zamanı ve takip sıklığı hakkında sorular hazırla."),
        score: treatmentStage ? 72 : 48
      },
      {
        label: trText("Lifestyle / prevention context", "Yaşam tarzı / önleme bağlamı"),
        raw: trText("CRC lifestyle, BMI, diet, activity, smoking and family-history fields", "CRC yaşam tarzı, BMI, beslenme, aktivite, sigara ve aile öyküsü alanları"),
        meaning: trText("Lifestyle fields create a prevention and screening conversation, especially for colorectal awareness.", "Yaşam tarzı alanları özellikle kolorektal farkındalık için önleme ve tarama görüşmesi oluşturur."),
        action: trText("Discuss screening history, family history, activity, BMI and diet pattern with a clinician.", "Tarama geçmişi, aile öyküsü, aktivite, BMI ve beslenme düzenini klinisyenle konuş."),
        score: 64
      },
      {
        label: trText("Caregiver action path", "Bakıcı aksiyon yolu"),
        raw: trText("Patient/caregiver question engine and home-capacity answers", "Hasta/bakıcı soru motoru ve evde bakım kapasitesi yanıtları"),
        meaning: trText("Answers are converted into who should act, what to track and when to escalate.", "Yanıtlar kimin aksiyon alacağına, neyin takip edileceğine ve ne zaman yükseltileceğine çevrilir."),
        action: relationalActionOutput?.what || trText("Use generated questions and symptom summary as a care-team communication aid.", "Üretilen soruları ve semptom özetini bakım ekibi iletişim desteği olarak kullan."),
        score: relationalPriorityScore
      }
    ];

    const judgeImpactCardsV15 = [
      {
        title: trText("Technological implementation", "Teknolojik uygulama"),
        text: trText("Multiple CSV layers, derived summaries, relational graph logic, Splunk-ready telemetry and PDF evidence reporting work together.", "Çoklu CSV katmanları, türetilmiş özetler, ilişkisel graph mantığı, Splunk-ready telemetri ve PDF kanıt raporu birlikte çalışır.")
      },
      {
        title: trText("Design", "Tasarım"),
        text: trText("The UI now explains what each data signal means instead of only showing raw metrics.", "UI artık sadece ham metrik göstermek yerine her veri sinyalinin ne anlama geldiğini açıklar.")
      },
      {
        title: trText("Potential impact", "Potansiyel etki"),
        text: trText("Patients and caregivers get clearer questions, safer escalation prompts and better visit preparation.", "Hastalar ve bakıcılar daha net sorular, daha güvenli yükseltme uyarıları ve daha iyi görüşme hazırlığı alır.")
      },
      {
        title: trText("Quality of idea", "Fikir kalitesi"),
        text: trText("Disconnected cancer, treatment, access and lifestyle datasets become an explainable support intelligence graph.", "Dağınık kanser, tedavi, erişim ve yaşam tarzı veri setleri açıklanabilir destek zekâ grafına dönüşür.")
      }
    ];

    const buildDataToMeaningHtmlV15 = () => {
      const cards = dataToMeaningCardsV15.map((card) => `
        <div>
          <h3>${escapeReportHtml(card.label)}</h3>
          <small>Raw data</small>
          <p>${escapeReportHtml(card.raw)}</p>
          <small>Meaning</small>
          <p>${escapeReportHtml(card.meaning)}</p>
          <small>Suggested action</small>
          <p><b>${escapeReportHtml(card.action)}</b></p>
        </div>
      `).join("");

      return `
        <section class="report-section report-data-meaning-v15">
          <h2>DATA-TO-MEANING INTERPRETATION</h2>
          <p class="report-muted">
            This section translates raw data layers into patient-ready, caregiver-ready and judge-readable meaning.
          </p>
          <div class="report-context-mode-v15">
            <b>${escapeReportHtml(contextModeV15)}</b>
            <span>${escapeReportHtml(contextModeDetailV15)}</span>
          </div>
          <div class="report-data-meaning-grid-v15">
            ${cards}
          </div>
        </section>
      `;
    };
    // INTERACTIVE INSIGHT COCKPIT v16 START
    const [insightLensV16, setInsightLensV16] = useState("case");
    const [insightQuestionV16, setInsightQuestionV16] = useState("next_action");
    // COMMAND CENTER UX v17 START
    const [showDeepEvidenceV17, setShowDeepEvidenceV17] = useState(false);

    // COMMAND CENTER UX v17 END

    const insightLensesV16 = [
      {
        id: "case",
        label: trText("My case", "Benim vakam"),
        source: trText("Symptoms + red flags + scenario", "Semptomlar + kırmızı bayraklar + senaryo"),
        meaning: redFlags.length
          ? trText("Safety signals are present, so escalation guidance comes first.", "Güvenlik sinyalleri var; bu yüzden önce yükseltme yönlendirmesi gelir.")
          : trText("Current symptoms suggest structured tracking and visit preparation.", "Mevcut semptomlar yapılandırılmış takip ve görüşme hazırlığı gerektirir."),
        action: redFlags.length
          ? trText("Use the safety message and contact the care team according to local guidance.", "Güvenlik mesajını kullan ve yerel yönlendirmeye göre bakım ekibiyle iletişime geç.")
          : trText("Track severity, timing and change; use the generated doctor questions.", "Şiddet, zamanlama ve değişimi takip et; üretilen doktor sorularını kullan."),
        score: supportScore
      },
      {
        id: "access",
        label: trText("Access pressure", "Erişim baskısı"),
        source: trText("NHS waiting-time + public context", "NHS bekleme süresi + kamu bağlamı"),
        meaning: trText("Waiting-time and pathway pressure explain why appointment timing should be discussed.", "Bekleme süresi ve bakım yolu baskısı randevu zamanının neden konuşulması gerektiğini açıklar."),
        action: trText("Ask what happens if appointment, diagnostic result or treatment decision is delayed.", "Randevu, tanı sonucu veya tedavi kararı gecikirse ne yapılacağını sor."),
        score: 73
      },
      {
        id: "treatment",
        label: trText("Treatment journey", "Tedavi yolculuğu"),
        source: trText("Chemotherapy + treatment KPI datasets", "Kemoterapi + tedavi KPI veri setleri"),
        meaning: trText("Treatment data is used to prepare questions about side effects, response timing and follow-up intensity.", "Tedavi verisi yan etkiler, yanıt zamanı ve takip yoğunluğu hakkında soru hazırlamak için kullanılır."),
        action: trText("Ask which symptoms are expected, which should be reported, and when follow-up should change.", "Hangi semptomların beklenen, hangilerinin bildirilecek olduğunu ve takibin ne zaman değişeceğini sor."),
        score: 70
      },
      {
        id: "lifestyle",
        label: trText("Lifestyle / prevention", "Yaşam tarzı / önleme"),
        source: trText("CRC diet, BMI, family history and screening fields", "CRC beslenme, BMI, aile öyküsü ve tarama alanları"),
        meaning: trText("Lifestyle data becomes a prevention and screening conversation, not a diagnosis.", "Yaşam tarzı verisi tanı değil, önleme ve tarama konuşmasına dönüşür."),
        action: trText("Discuss screening history, family history, activity, BMI and diet pattern with a clinician.", "Tarama geçmişi, aile öyküsü, aktivite, BMI ve beslenme düzenini klinisyenle konuş."),
        score: 64
      },
      {
        id: "caregiver",
        label: trText("Caregiver plan", "Bakıcı planı"),
        source: trText("Question engine + home capacity answers", "Soru motoru + evde bakım kapasitesi yanıtları"),
        meaning: trText("Caregiver answers decide who should act, what to track and when to escalate.", "Bakıcı yanıtları kimin aksiyon alacağını, neyin takip edileceğini ve ne zaman yükseltileceğini belirler."),
        action: relationalActionOutput?.what || trText("Use the symptom summary as a care-team communication aid.", "Semptom özetini bakım ekibiyle iletişim desteği olarak kullan."),
        score: relationalPriorityScore
      }
    ];

    const insightQuestionsV16 = [
      {
        id: "next_action",
        label: trText("What should I do next?", "Sonra ne yapmalıyım?")
      },
      {
        id: "why_priority",
        label: trText("Why is this priority?", "Bu neden öncelikli?")
      },
      {
        id: "which_data",
        label: trText("Which data matters?", "Hangi veri önemli?")
      },
      {
        id: "doctor_questions",
        label: trText("What should I ask?", "Ne sormalıyım?")
      }
    ];

    const selectedInsightLensV16 =
      insightLensesV16.find((item) => item.id === insightLensV16) || insightLensesV16[0];

    const selectedInsightAnswerV16 = (() => {
      if (insightQuestionV16 === "why_priority") {
        return selectedInsightLensV16.meaning;
      }

      if (insightQuestionV16 === "which_data") {
        return trText(
          `This view uses: ${selectedInsightLensV16.source}. The system translates it into meaning before showing an action.`,
          `Bu görünüm şunu kullanır: ${selectedInsightLensV16.source}. Sistem bunu aksiyon göstermeden önce anlama çevirir.`
        );
      }

      if (insightQuestionV16 === "doctor_questions") {
        if (insightLensV16 === "access") {
          return trText(
            "Ask: If my appointment, scan, diagnostic result or treatment decision is delayed, who should I contact and when?",
            "Sor: Randevum, görüntülemem, tanı sonucum veya tedavi kararım gecikirse kiminle ve ne zaman iletişime geçmeliyim?"
          );
        }

        if (insightLensV16 === "treatment") {
          return trText(
            "Ask: Which side effects are expected for this treatment stage, and which symptoms should be reported immediately?",
            "Sor: Bu tedavi aşamasında hangi yan etkiler beklenen kabul edilir, hangi semptomlar hemen bildirilmelidir?"
          );
        }

        if (insightLensV16 === "lifestyle") {
          return trText(
            "Ask: Based on my family history, BMI, activity and diet pattern, what screening or prevention steps should I discuss?",
            "Sor: Aile öyküm, BMI, aktivite ve beslenme düzenime göre hangi tarama veya önleme adımlarını konuşmalıyım?"
          );
        }

        return trText(
          "Ask: Which symptoms should I track daily, which should I report, and what change should trigger urgent contact?",
          "Sor: Hangi semptomları günlük takip etmeliyim, hangilerini bildirmeliyim ve hangi değişim acil iletişim gerektirir?"
        );
      }

      return selectedInsightLensV16.action;
    })();

    const insightSourcePathV16 = [
      {
        label: trText("Raw data", "Ham veri"),
        value: selectedInsightLensV16.source
      },
      {
        label: trText("AI meaning", "AI anlamı"),
        value: selectedInsightLensV16.meaning
      },
      {
        label: trText("User action", "Kullanıcı aksiyonu"),
        value: selectedInsightLensV16.action
      }
    ];

    const insightDataExplorerV16 = [
      {
        label: trText("Symptoms", "Semptomlar"),
        value: `${symptomScore}/70`,
        meaning: trText("Shows current burden from fatigue, pain, nausea and mood.", "Yorgunluk, ağrı, bulantı ve ruh halinden mevcut yükü gösterir.")
      },
      {
        label: trText("Public context", "Kamu bağlamı"),
        value: publicDataHasMatch ? trText("Matched", "Eşleşti") : trText("Broader mode", "Geniş mod"),
        meaning: contextModeDetailV15
      },
      {
        label: trText("Access pressure", "Erişim baskısı"),
        value: "73.84%",
        meaning: trText("NHS pathway pressure becomes a care-access conversation.", "NHS bakım yolu baskısı bakım erişimi konuşmasına dönüşür.")
      },
      {
        label: trText("Treatment context", "Tedavi bağlamı"),
        value: "69.69",
        meaning: trText("Treatment KPI data becomes follow-up and side-effect questions.", "Tedavi KPI verisi takip ve yan etki sorularına dönüşür.")
      },
      {
        label: trText("Lifestyle context", "Yaşam tarzı bağlamı"),
        value: "1,000",
        meaning: trText("CRC lifestyle records support prevention and screening discussion prompts.", "CRC yaşam tarzı kayıtları önleme ve tarama görüşmesi ipuçlarını destekler.")
      }
    ];
    // INTERACTIVE INSIGHT COCKPIT v16 END

    // DATA TO MEANING UX v15 END

    // AI RELATIONAL INTELLIGENCE GRAPH v13 END

    // AI DATA PROVENANCE PDF v12 END
    // AI POWER REAL DATA v11 END
    // COPILOT AI POWER DASHBOARD v10 END

    const doctorQuestions = [
      "Which of my symptoms are expected, and which ones should I report immediately?",
      "At what point should I call the clinic or seek urgent support?",
      "Could fatigue, pain or nausea be related to my treatment?",
      "What should I track daily before my next visit?",
      "Is there anything my caregiver should watch for at home?"
    ];

    const actionSteps =
      supportScore >= 72
        ? [
            "Do not ignore today’s symptoms.",
            "Contact your care team or clinic if symptoms are new, worsening or hard to tolerate.",
            "Share the structured note below with a doctor, nurse or caregiver.",
            "Ask clearly: “When should I seek urgent support?”"
          ]
        : supportScore >= 45
        ? [
            "Track your symptoms today and tomorrow.",
            "Prepare the doctor questions below before your visit.",
            "Tell a trusted caregiver how you are feeling.",
            "Ask your care team which symptoms should trigger a call."
          ]
        : [
            "Continue tracking symptoms calmly.",
            "Use the questions below for your next doctor visit.",
            "Share changes early if symptoms increase.",
            "Keep this note as a simple visit-preparation summary."
          ];

    const aiRecommendation =
      supportScore >= 72
        ? "Your answers suggest that extra support may be needed today. This does not mean a diagnosis or emergency by itself, but it is strong enough to contact a care team, especially if symptoms are new, worsening, or difficult to tolerate."
        : supportScore >= 45
        ? "Your answers suggest that you should monitor symptoms closely and prepare clear questions for your doctor. A caregiver or support team can help you track changes."
        : "Your answers look relatively stable today. Keep tracking symptoms and use the doctor-visit note to communicate clearly at your next appointment.";

    const patientSummary = `ONCOCONNECT AI — Doctor Visit Note

Role: ${roleLabels[role]}
Goal: ${goalLabels[goal]}
Real-world case scenario: ${selectedScenarioLabel}
Scenario playbook: ${scenarioPlan.urgency}
Immediate check: ${scenarioPlan.immediate}
Track today: ${scenarioPlan.track}
Ask doctor: ${scenarioPlan.ask}
Clinical safety level: ${clinicalRiskLevel}
Red flags: ${redFlags.length ? redFlags.join(", ") : "None selected"}
Location / data context: ${city || "Not selected"}
Age group: ${ageGroup}
Cancer context: ${cancerLabels[cancerType]}
Treatment stage: ${stageLabels[treatmentStage]}
Main concern: ${concernLabels[mainConcern]}

Symptoms today:
- Fatigue / weakness: ${fatigue}/10
- Pain: ${pain}/10
- Nausea / appetite problem: ${nausea}/10
- Fear, worry or low mood: ${mood}/10

Data signal:
- Matching public data rows: ${filteredRows.length}
- Average annual incidence: ${incidenceAvg ? incidenceAvg.toFixed(2) : "not available"}
- Average annual mortality: ${mortalityAvg ? mortalityAvg.toFixed(2) : "not available"}
- Five-year survival: ${survivalAvg ? survivalAvg.toFixed(1) + "%" : "not available"}

Support priority:
${supportScore}/100 — ${supportLevel}

AI recommendation:
${aiRecommendation}`;

    const copilotSimulationSteps = [
      {
        title: trText("1. Case intake captured", "1. Vaka girdileri alındı"),
        detail: trText("Role, goal, scenario, city, age group, cancer type and treatment stage are read from the form.", "Rol, hedef, senaryo, şehir, yaş grubu, kanser türü ve tedavi aşaması formdan okunur.")
      },
      {
        title: trText("2. Symptom burden calculated", "2. Semptom yükü hesaplandı"),
        detail: `${trText("Fatigue", "Yorgunluk")} ${fatigue}/10 · ${trText("Pain", "Ağrı")} ${pain}/10 · ${trText("Nausea", "Bulantı")} ${nausea}/10 · ${trText("Mood", "Ruh hali")} ${mood}/10`
      },
      {
        title: trText("3. Red flag safety check applied", "3. Kırmızı bayrak güvenlik kontrolü uygulandı"),
        detail: redFlags.length
          ? redFlags.join(" · ")
          : trText("No red flag selected.", "Kırmızı bayrak seçilmedi.")
      },
      {
        title: trText("4. Public data context merged", "4. Kamu veri bağlamı birleştirildi"),
        detail: `${trText("Rows", "Satırlar")}: ${filteredRows.length} · ${trText("Incidence", "İnsidans")}: ${incidenceAvg ? incidenceAvg.toFixed(1) : "-"} · ${trText("Mortality", "Mortalite")}: ${mortalityAvg ? mortalityAvg.toFixed(1) : "-"} · ${trText("Survival", "Sağkalım")}: ${survivalAvg ? survivalAvg.toFixed(0) + "%" : "-"}`
      },
      {
        title: trText("5. Risk score generated", "5. Risk skoru üretildi"),
        detail: `${supportScore}/100 · ${clinicalRiskLevel}`
      },
      {
        title: trText("6. Doctor note and Splunk event prepared", "6. Doktor notu ve Splunk olayı hazırlandı"),
        detail: splunkEventPayload.event_type
      }
    ];

    const copilotDetailedReport = `ONCOCONNECT AI COPILOT — DETAILED CASE REPORT

1) CASE CONTEXT
Role: ${roleLabels[role]}
Goal: ${goalLabels[goal]}
Scenario: ${selectedScenarioLabel}
Scenario urgency: ${scenarioPlan.urgency}
City / data context: ${city || "All locations"}
Age group: ${ageGroup}
Cancer type: ${cancerLabels[cancerType]}
Treatment stage: ${stageLabels[treatmentStage]}
Main concern: ${concernLabels[mainConcern]}

2) SAFETY CHECK
Clinical risk level: ${clinicalRiskLevel}
Red flags: ${redFlags.length ? redFlags.join(", ") : "None selected"}
Safety message: ${safetyMessage}

3) SYMPTOM STATISTICS
Fatigue / weakness: ${fatigue}/10
Pain: ${pain}/10
Nausea / appetite: ${nausea}/10
Fear, worry or low mood: ${mood}/10
Symptom signal: ${symptomScore}/70
Dataset signal: ${dataSignal}/30
Total support score: ${supportScore}/100

4) PUBLIC DATA CONTEXT
Matching rows: ${filteredRows.length}
Average incidence: ${incidenceAvg ? incidenceAvg.toFixed(2) : "not available"}
Average mortality: ${mortalityAvg ? mortalityAvg.toFixed(2) : "not available"}
Five-year survival: ${survivalAvg ? survivalAvg.toFixed(1) + "%" : "not available"}

5) CASE FLOW PLAYBOOK
Immediate check: ${scenarioPlan.immediate}
Track today: ${scenarioPlan.track}
Ask doctor: ${scenarioPlan.ask}

6) AI RECOMMENDATION
${aiRecommendation}

7) SPLUNK EVENT PREVIEW
${JSON.stringify(splunkEventPayload, null, 2)}

Medical safety note: This report is not a diagnosis, treatment plan or emergency triage decision. It is a structured support and communication aid.`;

    const copyDetailedReport = async () => {
      try {
        await navigator.clipboard.writeText(copilotDetailedReport);
        runCopilotAction(
          "report",
          trText("Detailed report copied to clipboard.", "Detaylı rapor panoya kopyalandı."),
          "report_copied"
        );
      } catch {
        alert(copilotDetailedReport);
      }
    };

    const generateDetailedReport = () => {
      setReportGenerated(true);
      runCopilotAction(
        "report",
        trText("Detailed analytics report generated.", "Detaylı analitik rapor üretildi."),
        "detailed_report"
      );
    };

    const runWorkflowSimulation = () => {
      runExecutionPipelineV78();
                    startExecutionPipelineV80();
                    setSimulationRunning(true);
      setSimulationStep(0);
      runCopilotAction(
        "simulation",
        trText("Live Copilot workflow simulation started.", "Canlı Copilot iş akışı simülasyonu başlatıldı."),
        "workflow_simulation"
      );

      copilotSimulationSteps.forEach((_, index) => {
        window.setTimeout(() => {
          setSimulationStep(index + 1);

          if (index === copilotSimulationSteps.length - 1) {
            resetExecutionPipelineV85();
                    setSimulationRunning(false);
            setReportGenerated(true);
            setLastCopilotAction(trText("Simulation completed and report is ready.", "Simülasyon tamamlandı ve rapor hazır."));
          }
        }, 650 * (index + 1));
      });
    };

    // RUN AI ANALYSIS FIX v27 START
    const runCareCockpitAnalysisV27 = () => {
      setActiveInsight("simulation");
      setSimulationRunning(true);
      setSimulationStep(0);
      setReportGenerated(false);
      setLastCopilotAction(
        trText(
          "AI is analyzing symptoms, context, public data and care pathway.",
          "AI semptomları, bağlamı, kamu verisini ve bakım yolunu analiz ediyor."
        )
      );

      copilotSimulationSteps.forEach((_, index) => {
        window.setTimeout(() => {
          setSimulationStep(index + 1);

          if (index === 1) {
            setLastCopilotAction(
              trText(
                "Symptom burden and safety signals calculated.",
                "Semptom yükü ve güvenlik sinyalleri hesaplandı."
              )
            );
          }

          if (index === 3) {
            setLastCopilotAction(
              trText(
                "Public data and treatment context connected.",
                "Kamu verisi ve tedavi bağlamı bağlandı."
              )
            );
          }

          if (index === copilotSimulationSteps.length - 1) {
            setSimulationRunning(false);
            setReportGenerated(true);
            setActiveInsight("report");
            setLastCopilotAction(
              trText(
                "Analysis completed. Click Get Recommendation.",
                "Analiz tamamlandı. Öneriyi görmek için Get Recommendation düğmesine bas."
              )
            );
          }
        }, 520 * (index + 1));
      });
    };
    // RUN AI ANALYSIS FIX v27 END

    const escapeReportHtml = (value) =>
      String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

    const reportRiskCategory =
      redFlags.length > 0
        ? trText("Urgent safety review", "Acil güvenlik değerlendirmesi")
        : supportScore >= 72
        ? trText("High support priority", "Yüksek destek önceliği")
        : supportScore >= 45
        ? trText("Moderate monitoring priority", "Orta düzey takip önceliği")
        : trText("Stable preparation priority", "Stabil hazırlık önceliği");

    const reportCategoryRecommendations =
      redFlags.length > 0
        ? [
            trText("Do not wait for routine follow-up if symptoms are severe, new or worsening.", "Semptomlar ciddi, yeni veya kötüleşiyorsa rutin kontrolü beklemeyin."),
            trText("Contact the oncology team, clinic or emergency services according to local guidance.", "Yerel yönlendirmeye göre onkoloji ekibi, klinik veya acil servisle iletişime geçin."),
            trText("Share the red flags and symptom timeline clearly.", "Kırmızı bayrakları ve semptom zaman çizelgesini açıkça paylaşın.")
          ]
        : supportScore >= 72
        ? [
            trText("Arrange same-day communication with the care team if symptoms are difficult to tolerate.", "Semptomlar tolere edilmesi zor düzeydeyse aynı gün bakım ekibiyle iletişim kurun."),
            trText("Use the doctor note to summarize symptoms, severity and changes.", "Semptomları, şiddeti ve değişiklikleri özetlemek için doktor notunu kullanın."),
            trText("Ask which symptoms should trigger urgent contact.", "Hangi semptomların acil iletişim gerektirdiğini sorun.")
          ]
        : supportScore >= 45
        ? [
            trText("Monitor symptoms closely for the next 24–48 hours.", "Semptomları önümüzdeki 24–48 saat yakından takip edin."),
            trText("Prepare questions before the next oncology visit.", "Bir sonraki onkoloji görüşmesi öncesinde soruları hazırlayın."),
            trText("Ask a caregiver or support person to help track changes.", "Değişiklikleri takip etmek için bakım veren veya destek kişisinden yardım isteyin.")
          ]
        : [
            trText("Continue routine symptom tracking.", "Rutin semptom takibine devam edin."),
            trText("Keep the report as a visit-preparation summary.", "Raporu görüşmeye hazırlık özeti olarak saklayın."),
            trText("Contact the care team if symptoms increase or new concerns appear.", "Semptomlar artarsa veya yeni endişeler oluşursa bakım ekibiyle iletişime geçin.")
          ];

    const doctorNoteHighlights = [
      `${trText("Main scenario", "Ana senaryo")}: ${selectedScenarioLabel}`,
      `${trText("Risk category", "Risk kategorisi")}: ${reportRiskCategory}`,
      `${trText("Support score", "Destek skoru")}: ${supportScore}/100`,
      `${trText("Top symptom burden", "En yüksek semptom yükü")}: ${
        [
          [trText("Fatigue", "Yorgunluk"), fatigue],
          [trText("Pain", "Ağrı"), pain],
          [trText("Nausea", "Bulantı"), nausea],
          [trText("Mood", "Ruh hali"), mood]
        ].sort((a, b) => b[1] - a[1])[0][0]
      }`,
      `${trText("Red flags", "Kırmızı bayraklar")}: ${redFlags.length ? redFlags.join(", ") : trText("None selected", "Seçilmedi")}`
    ];

    const exportDetailedReportPdf = () => {
      setReportGenerated(true);
      setActiveInsight("report");
      setLastCopilotAction(trText("PDF report export opened.", "PDF rapor dışa aktarma açıldı."));

      const reportWindow = window.open("", "_blank", "width=980,height=1200");

      if (!reportWindow) {
        alert(trText("Popup was blocked. Please allow popups and try again.", "Açılır pencere engellendi. Lütfen popup izni verip tekrar deneyin."));
        return;
      }

      const reportHtml = `
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>OncoConnect AI Copilot Report</title>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      padding: 34px;
      font-family: Inter, Arial, sans-serif;
      background: #eef2f7;
      color: #0f172a;
    }

    .page {
      max-width: 1040px;
      margin: 0 auto;
      background: #ffffff;
      border: 1px solid #dbeafe;
      border-radius: 30px;
      overflow: hidden;
      box-shadow: 0 30px 90px rgba(15,23,42,.14);
    }

    .hero {
      padding: 34px;
      color: #ffffff;
      background:
        radial-gradient(circle at 80% 20%, rgba(34,197,94,.28), transparent 30%),
        radial-gradient(circle at 20% 0%, rgba(14,165,233,.24), transparent 32%),
        linear-gradient(135deg, #0f172a, #1e3a8a 54%, #312e81);
    }

    .kicker {
      letter-spacing: .16em;
      text-transform: uppercase;
      color: #93c5fd;
      font-weight: 950;
      font-size: 12px;
    }

    h1 {
      margin: 10px 0 10px;
      font-size: 38px;
      line-height: 1.08;
      letter-spacing: -.04em;
    }

    .sub {
      max-width: 760px;
      margin: 0;
      color: #dbeafe;
      line-height: 1.6;
      font-weight: 650;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.2fr .8fr;
      gap: 22px;
      margin-top: 26px;
      align-items: stretch;
    }

    .risk-card {
      border: 1px solid rgba(255,255,255,.18);
      border-radius: 24px;
      padding: 22px;
      background: rgba(255,255,255,.10);
      backdrop-filter: blur(10px);
    }

    .risk-card small {
      display: block;
      color: #bfdbfe;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: .12em;
    }

    .risk-score {
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-top: 10px;
    }

    .risk-score strong {
      font-size: 64px;
      line-height: 1;
      font-weight: 1000;
      letter-spacing: -.06em;
    }

    .risk-score span {
      color: #cbd5e1;
      font-weight: 900;
    }

    .risk-badge {
      display: inline-flex;
      margin-top: 12px;
      padding: 9px 13px;
      border-radius: 999px;
      background: rgba(34,197,94,.16);
      color: #bbf7d0;
      font-weight: 950;
    }

    .safety-note {
      margin-top: 14px;
      color: #e0f2fe;
      line-height: 1.55;
      font-weight: 650;
    }

    .hero-meta {
      display: grid;
      gap: 10px;
    }

    .hero-meta div {
      border: 1px solid rgba(255,255,255,.16);
      border-radius: 18px;
      padding: 14px;
      background: rgba(255,255,255,.09);
    }

    .hero-meta small {
      display: block;
      color: #bfdbfe;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: .12em;
      font-weight: 900;
      margin-bottom: 5px;
    }

    .hero-meta b {
      display: block;
      color: #ffffff;
      line-height: 1.35;
    }

    .content {
      padding: 30px 34px 34px;
    }

    .section {
      margin-top: 24px;
      padding: 22px;
      border: 1px solid #e2e8f0;
      border-radius: 24px;
      background: #ffffff;
      break-inside: avoid;
    }

    .section.soft {
      background: linear-gradient(135deg, #f8fafc, #eff6ff);
    }

    .section h2 {
      margin: 0 0 14px;
      color: #0f172a;
      font-size: 22px;
      letter-spacing: -.02em;
    }

    .section-label {
      display: inline-flex;
      margin-bottom: 8px;
      color: #2563eb;
      font-size: 11px;
      letter-spacing: .14em;
      text-transform: uppercase;
      font-weight: 950;
    }

    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }

    .kpi {
      border: 1px solid #e2e8f0;
      border-radius: 18px;
      padding: 16px;
      background: #f8fafc;
    }

    .kpi small {
      display: block;
      color: #64748b;
      font-weight: 850;
      margin-bottom: 7px;
    }

    .kpi strong {
      display: block;
      font-size: 24px;
      color: #0f172a;
      font-weight: 1000;
      letter-spacing: -.03em;
    }

    .chart-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
    }

    .bar-row {
      margin-top: 14px;
    }

    .bar-row .top {
      display: flex;
      justify-content: space-between;
      gap: 14px;
      color: #334155;
      font-weight: 850;
      margin-bottom: 7px;
    }

    .track {
      height: 13px;
      border-radius: 999px;
      background: #e2e8f0;
      overflow: hidden;
    }

    .fill {
      display: block;
      height: 100%;
      border-radius: 999px;
      background: linear-gradient(90deg, #2563eb, #22c55e);
    }

    .fill.warning {
      background: linear-gradient(90deg, #f97316, #ef4444);
    }

    .stack {
      height: 22px;
      border-radius: 999px;
      overflow: hidden;
      background: #e2e8f0;
      display: flex;
      margin-top: 10px;
    }

    .stack span,
    .stack b {
      display: grid;
      place-items: center;
      color: white;
      font-size: 11px;
      font-weight: 950;
    }

    .stack span {
      background: #2563eb;
    }

    .stack b {
      background: #059669;
    }

    .recommendations {
      display: grid;
      gap: 10px;
      margin: 0;
      padding: 0;
      list-style: none;
    }

    .recommendations li {
      position: relative;
      padding: 13px 14px 13px 42px;
      border-radius: 16px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      color: #334155;
      font-weight: 760;
      line-height: 1.45;
    }

    .recommendations li::before {
      content: "✓";
      position: absolute;
      left: 13px;
      top: 12px;
      width: 22px;
      height: 22px;
      display: grid;
      place-items: center;
      border-radius: 999px;
      background: #dcfce7;
      color: #16a34a;
      font-weight: 1000;
    }

    .doctor-note {
      display: grid;
      gap: 10px;
    }

    .doctor-note div {
      padding: 14px;
      border-radius: 16px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
    }

    .doctor-note small {
      display: block;
      color: #64748b;
      font-weight: 850;
      margin-bottom: 4px;
    }

    .doctor-note b {
      display: block;
      color: #0f172a;
      line-height: 1.45;
    }

    .questions {
      margin: 0;
      padding-left: 18px;
      color: #334155;
      line-height: 1.55;
      font-weight: 750;
    }

    .questions li {
      margin-top: 8px;
    }

    pre {
      white-space: pre-wrap;
      word-break: break-word;
      background: #0f172a;
      color: #e5e7eb;
      border-radius: 18px;
      padding: 20px;
      line-height: 1.55;
      font-size: 12.5px;
      overflow: visible;
    }

    .payload-note {
      margin-top: 10px;
      color: #64748b;
      font-size: 13px;
      font-weight: 700;
      line-height: 1.5;
    }

    .footer-note {
      margin-top: 22px;
      padding: 16px;
      border-radius: 18px;
      background: #fff7ed;
      border: 1px solid #fed7aa;
      color: #7c2d12;
      font-weight: 800;
      line-height: 1.55;
    }

    .actions {
      margin: 24px 34px 34px;
      display: flex;
      gap: 10px;
    }

    button {
      border: 0;
      border-radius: 999px;
      padding: 13px 20px;
      background: #2563eb;
      color: white;
      font-weight: 950;
      cursor: pointer;
    }

    button.secondary {
      background: #0f172a;
    }

    @media print {
      body {
        background: white;
        padding: 0;
      }

      .page {
        box-shadow: none;
        border: 0;
        border-radius: 0;
      }

      .actions {
        display: none;
      }

      .section {
        break-inside: avoid;
      }
    }
  </style>
</head>
<body>
  <main class="page">
    <section class="hero">
      <div class="kicker">OncoConnect AI Copilot</div>
      <h1>Detailed Case Intelligence Report</h1>
      <p class="sub">
        A structured support report generated from patient/caregiver inputs, symptom statistics,
        red flag screening, public cancer data context, case playbook logic and Splunk-ready telemetry.
      </p>

      <div class="hero-grid">
        <div class="risk-card">
          <small>Support priority score</small>
          <div class="risk-score">
            <strong>${supportScore}</strong>
            <span>/100</span>
          </div>
          <div class="risk-badge">${escapeReportHtml(reportRiskCategory)}</div>
          <p class="safety-note">${escapeReportHtml(safetyMessage)}</p>
        </div>

        <div class="hero-meta">
          <div><small>Scenario</small><b>${escapeReportHtml(selectedScenarioLabel)}</b></div>
          <div><small>Clinical level</small><b>${escapeReportHtml(clinicalRiskLevel)}</b></div>
          <div><small>Location / age</small><b>${escapeReportHtml(city || "All locations")} · ${escapeReportHtml(ageGroup)}</b></div>
        </div>
      </div>
    </section>

    <section class="content">
      <section class="section soft">
        <span class="section-label">Executive summary</span>
        <h2>Current case snapshot</h2>

        <div class="kpi-grid">
          <div class="kpi"><small>Support score</small><strong>${supportScore}/100</strong></div>
          <div class="kpi"><small>Symptom signal</small><strong>${symptomScore}/70</strong></div>
          <div class="kpi"><small>Dataset signal</small><strong>${dataSignal}/30</strong></div>
          <div class="kpi"><small>Red flags</small><strong>${redFlags.length}</strong></div>
        </div>
      </section>

      <section class="section">
        <span class="section-label">Statistics and charts</span>
        <h2>Symptom burden and risk composition</h2>

        <div class="chart-grid">
          <div>
            ${[
              [trText("Fatigue / weakness", "Yorgunluk / halsizlik"), fatigue],
              [trText("Pain", "Ağrı"), pain],
              [trText("Nausea / appetite", "Bulantı / iştah"), nausea],
              [trText("Fear, worry or low mood", "Korku, endişe veya düşük ruh hali"), mood]
            ].map(([label, value]) => `
              <div class="bar-row">
                <div class="top"><span>${escapeReportHtml(label)}</span><b>${value}/10</b></div>
                <div class="track"><i class="fill ${value >= 7 ? "warning" : ""}" style="width:${value * 10}%"></i></div>
              </div>
            `).join("")}
          </div>

          <div>
            <div class="bar-row">
              <div class="top"><span>Symptom signal</span><b>${symptomScore}/70</b></div>
              <div class="track"><i class="fill" style="width:${Math.min(100, Math.round((symptomScore / 70) * 100))}%"></i></div>
            </div>

            <div class="bar-row">
              <div class="top"><span>Dataset signal</span><b>${dataSignal}/30</b></div>
              <div class="track"><i class="fill" style="width:${Math.min(100, Math.round((dataSignal / 30) * 100))}%"></i></div>
            </div>

            <div class="bar-row">
              <div class="top"><span>Risk composition</span><b>${supportScore}/100</b></div>
              <div class="stack">
                <span style="width:${Math.min(100, Math.round((symptomScore / Math.max(1, supportScore)) * 100))}%">symptoms</span>
                <b style="width:${Math.min(100, Math.round((dataSignal / Math.max(1, supportScore)) * 100))}%">data</b>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section soft">
        <span class="section-label">Public data context</span>
        <h2>Selected cancer data signal</h2>

        <div class="kpi-grid">
          <div class="kpi"><small>Matching rows</small><strong>${filteredRows.length}</strong></div>
          <div class="kpi"><small>Incidence</small><strong>${incidenceAvg ? incidenceAvg.toFixed(1) : "N/A"}</strong></div>
          <div class="kpi"><small>Mortality</small><strong>${mortalityAvg ? mortalityAvg.toFixed(1) : "N/A"}</strong></div>
          <div class="kpi"><small>5-year survival</small><strong>${survivalAvg ? survivalAvg.toFixed(0) + "%" : "N/A"}</strong></div>
        </div>

        <p class="payload-note">
          Public data indicators are used as context only. They are not personal medical risk scores.
        </p>
      </section>

      <section class="section">
        <span class="section-label">Category-based recommendations</span>
        <h2>Recommended next steps</h2>

        <ul class="recommendations">
          ${reportCategoryRecommendations.map((item) => `<li>${escapeReportHtml(item)}</li>`).join("")}
        </ul>
      </section>

      <section class="section soft">
        <span class="section-label">Doctor note</span>
        <h2>Visit preparation summary</h2>

        <div class="doctor-note">
          ${doctorNoteHighlights.map((item) => {
            const [label, ...rest] = String(item).split(":");
            return `<div><small>${escapeReportHtml(label)}</small><b>${escapeReportHtml(rest.join(":").trim())}</b></div>`;
          }).join("")}
          <div><small>Immediate check</small><b>${escapeReportHtml(scenarioPlan.immediate)}</b></div>
          <div><small>Track today</small><b>${escapeReportHtml(scenarioPlan.track)}</b></div>
          <div><small>Ask doctor</small><b>${escapeReportHtml(scenarioPlan.ask)}</b></div>
        </div>
      </section>

      <section class="section">
        <span class="section-label">Questions for the care team</span>
        <h2>Suggested doctor questions</h2>

        <ol class="questions">
          ${doctorQuestions.map((question) => `<li>${escapeReportHtml(question)}</li>`).join("")}
        </ol>
      </section>

      <section class="section">
        <span class="section-label">AI recommendation</span>
        <h2>Generated support guidance</h2>
        <p style="color:#334155; font-weight:750; line-height:1.6;">${escapeReportHtml(aiRecommendation)}</p>
      </section>

                ${buildAccessLifestylePerformanceHtmlV14()}

          ${buildDataToMeaningHtmlV15()}

          ${buildRelationalEvidenceHtml()}

          ${buildRealDataEvidenceHtml()}\n\n<section class="section">
        <span class="section-label">Splunk-ready telemetry</span>
        <h2>Event payload preview</h2>
        <pre>${escapeReportHtml(JSON.stringify(splunkEventPayload, null, 2))}</pre>
        <p class="payload-note">
          This event can be used to demonstrate observability, auditability and workflow monitoring in the AI Copilot.
        </p>
      </section>

      <div class="footer-note">
        Medical safety note: This report is not a diagnosis, treatment plan or emergency triage decision.
        It is a structured support and communication aid. Medical decisions should be made with qualified healthcare professionals.
      </div>
    </section>

    <div class="actions">
      <button onclick="window.print()">Save as PDF / Print</button>
      <button class="secondary" onclick="window.close()">Close</button>
    </div>
  </main>

  <script>
    setTimeout(() => window.print(), 650);
  </script>
</body>
</html>`;

      reportWindow.document.open();
      reportWindow.document.write(reportHtml);
      reportWindow.document.close();

      setCopilotActionLog((current) => [
        {
          id: `${Date.now()}-pdf`,
          time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" }),
          type: "pdf_export",
          label: trText("PDF report export opened.", "PDF rapor dışa aktarma açıldı."),
          insight: "report"
        },
        ...current
      ].slice(0, 6));
    };

    const loadDemoCase = () => {
      setRole("patient");
      setGoal("doctor");
      setCancerType("colorectal");
      setTreatmentStage("followup");
      setMainConcern("fatigue");
      setCaseScenario("side_effects");
      setCity(cityOptions.includes("Adana") ? "Adana" : (cityOptions[0] || "İstanbul"));
      setAgeGroup(ageOptions.includes("30-49") ? "30-49" : (ageOptions[1] || "All"));
      setFatigue(6);
      setPain(4);
      setNausea(3);
      setMood(5);
      setFeverFlag(false);
      setBreathingFlag(false);
      setBleedingFlag(false);
      setConfusionFlag(false);

      runCopilotAction(
        "simulation",
        trText("Demo case loaded. Run simulation or generate report next.", "Demo vaka yüklendi. Şimdi simülasyon çalıştırın veya rapor üretin."),
        "demo_case_loaded"
      );
    };

    const runGuidedDemo = () => {
      loadDemoCase();

      window.setTimeout(() => {
        runWorkflowSimulation();
      }, 250);

      window.setTimeout(() => {
        generateDetailedReport();
      }, 4700);
    };

    const runCopilotAction = (targetInsight, message, eventType = "ui_action") => {
      setActiveInsight(targetInsight);
      setLastCopilotAction(message);

      setCopilotActionLog((current) => [
        {
          id: `${Date.now()}-${targetInsight}`,
          time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" }),
          type: eventType,
          label: message,
          insight: targetInsight
        },
        ...current
      ].slice(0, 6));

      window.setTimeout(() => {
        const outputPanel = document.querySelector(".patient-output-panel");
        if (outputPanel) {
          outputPanel.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }, 80);
    };


    const getBackendRecommendationV149 = async () => {
      setRecommendationLoadingV149(true);
      setBackendRecommendationV149(null);

      runCopilotAction(
        "ai",
        trText(
          "AI recommendation is being generated from current case inputs.",
          "Mevcut vaka girdilerinden AI önerisi oluşturuluyor."
        ),
        "ai_recommendation_requested"
      );

      try {
        const response = await fetch(`${API}/ai-summary`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            patientId: "dashboard-user",
            role,
            goal,
            cancerType,
            treatmentStage,
            city,
            ageGroup,
            mainConcern,
            scenario: caseScenario,

            fatigue,
            pain,
            nausea,
            mood,

            feverFlag,
            breathingDifficultyFlag: breathingFlag,
            severeVomitingFlag: bleedingFlag,
            confusionFlag,

            cohort_context: hasLiveCohortV151
              ? {
                  source: "splunk_live_last_24h",
                  telemetry_event_count: cohortEventCountV151,
                  cohort_avg_risk: cohortAvgRiskV151,
                  current_case_risk: currentCaseRiskV151,
                  risk_difference: cohortRiskDifferenceV151,
                  comparison: cohortComparisonV151
                }
              : null
          })
        });

        const data = await response.json();

        if (!response.ok || !data?.success || !data?.summary) {
          throw new Error(
            data?.message ||
            data?.error ||
            `Recommendation request failed with status ${response.status}`
          );
        }

        const summary = data.summary;

        setBackendRecommendationV149(summary);
        setVisibleRecommendationV106(
          summary.recommended_action ||
          summary.ai_summary ||
          aiRecommendation
        );

        setLastCopilotAction(
          summary.red_flag_detected
            ? trText(
                "Rule-based safety override applied.",
                "Kural tabanlı güvenlik geçersiz kılma kuralı uygulandı."
              )
            : trText(
                "AI recommendation ready.",
                "AI önerisi hazır."
              )
        );
      } catch (error) {
        console.error("Backend recommendation fallback:", error);

        setBackendRecommendationV149({
          fallback_used: true,
          error: error.message
        });

        setVisibleRecommendationV106(aiRecommendation);

        setLastCopilotAction(
          trText(
            "Local recommendation shown. Backend AI was unavailable.",
            "Yerel öneri gösterildi. Backend AI kullanılamadı."
          )
        );
      } finally {
        setRecommendationLoadingV149(false);
      }
    };

    const copySummary = async () => {
      try {
        await navigator.clipboard.writeText(patientSummary);
        alert("Doctor visit note copied.");
      } catch {
        alert(patientSummary);
      }
    };

    const sendEvent = () => {
      setEventSent(true);
      runCopilotAction(
        "splunk",
        trText("Splunk support event prepared and previewed.", "Splunk destek olayı hazırlandı ve önizlendi."),
        "splunk_event_preview"
      );
      setTimeout(() => setEventSent(false), 2600);
    };

    return (
      <div className="patient-copilot-page">
        <nav className="patient-copilot-nav">
          <button onClick={() => setPage("landing")}>{trText("← Home", "← Ana Sayfa")}</button>
          <button onClick={() => setPage("map")}>{trText(trText("Türkiye / Europe Map", "Türkiye / Avrupa Haritası"), "Türkiye / Avrupa Haritası")}</button>
          <button onClick={() => setPage("kids")}>Onco Kids</button>

          <div className="patient-copilot-lang">
              <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">{trText("English", "İngilizce")}</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>
        </nav>

        <section className="patient-copilot-hero">
          <div>
            <p className="patient-kicker">{trText("ONCOCONNECT AI COPILOT", "ONCOCONNECT AI YARDIMCI PİLOT")}</p>
            <h1>{trText("Simple cancer support guidance, step by step", "Adım adım sade kanser destek rehberliği")}</h1>
            <p>
              {trText("Choose your situation, select your city and age group, enter symptoms, then generate an AI recommendation, risk explanation, doctor note and Splunk support event.", "Durumunuzu seçin, şehir ve yaş grubunu belirleyin, semptomları girin; ardından AI önerisi, risk açıklaması, doktor notu ve Splunk destek olayı oluşturun.")}
            </p>

            <div className="patient-hero-actions">
              <button onClick={() => runCopilotAction("ai", trText("AI recommendation generated from hero control.", "Hero kontrolünden AI önerisi oluşturuldu."), "ai_recommendation")} className={activeInsight === "ai" ? "active" : ""}>
                {trText("AI Recommendation", "AI Önerisi")}
              </button>
              <button onClick={() => runCopilotAction("risk", trText("Risk assessment opened from hero control.", "Hero kontrolünden risk değerlendirmesi açıldı."), "risk_assessment")} className={activeInsight === "risk" ? "active" : ""}>
                {trText("Risk Assessment", "Risk Değerlendirmesi")}
              </button>
              <button onClick={() => runCopilotAction("note", trText("Doctor note opened from hero control.", "Hero kontrolünden doktor notu açıldı."), "doctor_note")} className={activeInsight === "note" ? "active" : ""}>
                {trText("Doctor Note", "Doktor Notu")}
              </button>
              <button onClick={sendEvent} className={activeInsight === "splunk" ? "active" : ""}>
                {trText("Send Splunk Event", "Splunk Olayı Gönder")}
              </button>
            </div>
          </div>

          <div className="patient-hero-card">
            <span>{trText("How to use this page", "Bu sayfa nasıl kullanılır")}</span>
            <ol>
              <li>{trText("Choose who you are.", "Kim olduğunuzu seçin.")}</li>
              <li>{trText("Select what you want to learn.", "Bugün ne öğrenmek istediğinizi seçin.")}</li>
              <li>{trText("Pick city, age group and cancer context.", "Şehir, yaş grubu ve kanser bağlamını seçin.")}</li>
              <li>{trText("Move symptom sliders.", "Semptom kaydırıcılarını hareket ettirin.")}</li>
              <li>{trText("Click AI Recommendation or Risk Assessment.", "AI Önerisi veya Risk Değerlendirmesi butonuna tıklayın.")}</li>
            </ol>
          </div>
        </section>

        <section className="patient-copilot-layout">
          <div className="care-cockpit-v42">
            <div className="cc-topbar-v42">
              <div className="cc-brand-v42">
                <span>🧠</span>
                <div>
                  <b>OncoConnect <em>AI Copilot</em></b>
                  <small>{trText("Care intelligence cockpit", "Bakım zekâ kokpiti")}</small>
                </div>
              </div>

              <div className="cc-status-pill-v42">
                <i></i>
                <span>{trText("AI analyzing your inputs", "AI girdilerini analiz ediyor")}</span>
              </div>

              <div className="cc-actions-v42">
                <button type="button" className={shareFeedbackV86 ? "is-feedback-v86" : ""} onClick={handleShareV86}>↗ {shareFeedbackV86 || trText("Share", "Paylaş")}</button>
                <button type="button" onClick={loadDemoCase}>{trText("Demo Case", "Demo Vaka")}</button>
                <button type="button" onClick={exportDetailedReportPdf}>{trText("Export PDF", "PDF Dışa Aktar")}</button>
                <button type="button" onClick={startNewSimulationV86}>{trText("New Simulation", "Yeni Simülasyon")}</button>
              </div>
            </div>

            <div className="cc-grid-v42">
              <aside className="cc-left-v42">
                <div className="cc-left-head-v42">
                  <span>1</span>
                  <div>
                    <b>{trText("Tell the AI", "AI’ya anlat")}</b>
                    <small>{trText("Your situation in a few steps", "Birkaç adımda durumunu anlat")}</small>
                  </div>
                </div>

                <div className="cc-group-v42">
                  <label>{trText("Who are you?", "Kimsiniz?")}</label>
                  <div className="cc-choice-v42 three">
                    {Object.entries(roleLabels).map(([key, label]) => (
                      <button key={key} type="button" className={role === key ? "active" : ""} onClick={() => setRole(key)}>
                        {label}
                      </button>
                    ))}
                  </div>
                </div>

                <div className="cc-group-v42">
                  <label>{trText("What do you want to learn?", "Ne öğrenmek istiyorsunuz?")}</label>
                  <div className="cc-choice-v42 two">
                    {Object.entries(goalLabels).map(([key, label]) => (
                      <button key={key} type="button" className={goal === key ? "active" : ""} onClick={() => setGoal(key)}>
                        {label}
                      </button>
                    ))}
                  </div>
                </div>

                <div className="cc-context-v42">
                  <label>
                    <span>{trText("City", "Şehir")}</span>
                    <select value={city} onChange={(e) => setCity(e.target.value)}>
                      <option value="">{trText("All locations", "Tüm konumlar")}</option>
                      {(cityOptions.length ? cityOptions : ["İstanbul", "Ankara", "İzmir", "Türkiye"]).map((item) => (
                        <option key={item} value={item}>{item}</option>
                      ))}
                    </select>
                  </label>

                  <label>
                    <span>{trText("Age group", "Yaş grubu")}</span>
                    <select value={ageGroup} onChange={(e) => setAgeGroup(e.target.value)}>
                      {ageOptions.map((item) => <option key={item} value={item}>{item}</option>)}
                    </select>
                  </label>

                  <label>
                    <span>{trText("Cancer type", "Kanser türü")}</span>
                    <select value={cancerType} onChange={(e) => setCancerType(e.target.value)}>
                      {Object.entries(cancerLabels).map(([key, label]) => (
                        <option key={key} value={key}>{label}</option>
                      ))}
                    </select>
                  </label>

                  <label>
                    <span>{trText("Treatment stage", "Tedavi aşaması")}</span>
                    <select value={treatmentStage} onChange={(e) => setTreatmentStage(e.target.value)}>
                      {Object.entries(stageLabels).map(([key, label]) => (
                        <option key={key} value={key}>{label}</option>
                      ))}
                    </select>
                  </label>

                  <label>
                    <span>{trText("Main concern", "Ana endişe")}</span>
                    <select value={mainConcern} onChange={(e) => setMainConcern(e.target.value)}>
                      {Object.entries(concernLabels).map(([key, label]) => (
                        <option key={key} value={key}>{label}</option>
                      ))}
                    </select>
                  </label>

                  <label>
                    <span>{trText("Scenario", "Senaryo")}</span>
                    <select value={caseScenario} onChange={(e) => setCaseScenario(e.target.value)}>
                      {Object.entries(caseScenarioLabels).map(([key, label]) => (
                        <option key={key} value={key}>{label}</option>
                      ))}
                    </select>
                  </label>
                </div>

                <div className="cc-symptoms-v42">
                  <div className="cc-mini-title-v42">
                    <b>{trText("How are your symptoms today?", "Bugün semptomlarınız nasıl?")}</b>
                    <small>{trText("0 none · 10 very strong", "0 yok · 10 çok güçlü")}</small>
                  </div>

                  {[
                    [trText("Fatigue / weakness", "Yorgunluk / halsizlik"), fatigue, setFatigue],
                    [trText("Pain", "Ağrı"), pain, setPain],
                    [trText("Nausea / appetite", "Bulantı / iştah"), nausea, setNausea],
                    [trText("Fear / low mood", "Kaygı / düşük ruh hali"), mood, setMood]
                  ].map(([label, value, setter]) => (
                    <label key={label}>
                      <span>{label}</span>
                      <strong>{value}/10</strong>
                      <input type="range" min="0" max="10" value={value} onChange={(e) => setter(Number(e.target.value))} />
                    </label>
                  ))}
                </div>

                <div className="cc-safety-v42">
                  <b>{trText("Safety check", "Güvenlik kontrolü")}</b>
                  <div>
                    <label className={feverFlag ? "active" : ""}>
                      <input type="checkbox" checked={feverFlag} onChange={(e) => setFeverFlag(e.target.checked)} />
                      <span>{trText("Fever / chills", "Ateş / titreme")}</span>
                    </label>
                    <label className={breathingFlag ? "active" : ""}>
                      <input type="checkbox" checked={breathingFlag} onChange={(e) => setBreathingFlag(e.target.checked)} />
                      <span>{trText("Breath tightness", "Nefes darlığı")}</span>
                    </label>
                    <label className={bleedingFlag ? "active" : ""}>
                      <input type="checkbox" checked={bleedingFlag} onChange={(e) => setBleedingFlag(e.target.checked)} />
                      <span>{trText("Severe vomiting", "Şiddetli kusma")}</span>
                    </label>
                    <label className={confusionFlag ? "active" : ""}>
                      <input type="checkbox" checked={confusionFlag} onChange={(e) => setConfusionFlag(e.target.checked)} />
                      <span>{trText("Confusion", "Bilinç bulanıklığı")}</span>
                    </label>
                  </div>
                </div>

                <div className="ai-engine-card-v141" style={{
                  display: "block",
                  visibility: "visible",
                  opacity: 1,
                  position: "relative",
                  zIndex: 10,
                  margin: "14px 0",
                  padding: "16px",
                  borderRadius: "20px",
                  background: "linear-gradient(180deg, #ffffff, #f8fbff)",
                  color: "#0f172a",
                  border: "1px solid rgba(37, 99, 235, .16)",
                  boxShadow: "0 18px 34px rgba(15, 23, 42, .07)"
                }}>
                  <span>{trText("AI Engine", "AI Motoru")}</span>
                  <b>{trText("Safety scoring + evidence layer", "Güvenlik skoru + kanıt katmanı")}</b>
                  <ul>
                    <li>{trText("Rule-based support priority engine", "Kural tabanlı destek önceliği motoru")}</li>
                    <li>{trText("v14 public-data evidence context", "v14 kamu verisi kanıt bağlamı")}</li>
                    <li>{trText("OpenRouter / 5.4 mini ready", "OpenRouter / 5.4 mini hazır")}</li>
                  </ul>
                </div>

                <div className="cc-run-v42">
                  <button type="button" className={simulationRunning ? "running" : ""} onClick={runCareCockpitAnalysisV86}>
                    ✨ {simulationRunning ? trText("AI analyzing...", "AI analiz ediyor...") : trText("Run AI Analysis", "AI Analizini Çalıştır")}
                    <small>{trText("Input → AI → Action", "Girdi → AI → Aksiyon")}</small>
                  </button>
                  <button
                    type="button"
                    onClick={getBackendRecommendationV149}
                    disabled={recommendationLoadingV149}
                  >
                    {recommendationLoadingV149
                      ? trText("Generating recommendation...", "Öneri oluşturuluyor...")
                      : trText("Get Recommendation", "Öneri Al")}
                  </button>
                </div>

              </aside>

              <main className="cc-center-v42">
                <section className={`cc-execution-v42 ${
                  lastCopilotAction === trText("Ready for new analysis.", "Yeni analiz için hazır.")
                    ? "pipeline-reset-visual-v91 ready-force-passive-v102"
                    : ""
                }`}>
                  <div className="cc-card-title-v42 dark">
                    <span>{trText("AI Execution Console", "AI Çalışma Konsolu")}</span>
                    <b>{trText("Where did the action run?", "Aksiyon nerede çalıştı?")}</b>
                  </div>

                  <div key={pipelineResetKeyV100} data-hard-idle={pipelineIdleFinalV100 ? "true" : "false"} className="cc-pipeline-v42 pipeline-v97">
                    <article className={`pipeline-card-v97 ${pipelineIdleFinalV100 ? "idle-v97" : executionStepV86 > 0 ? "done-v97" : executionStepV86 === 0 ? "active-v97" : "idle-v97"}`}>
                      <span className="plain-dot-v103" aria-hidden="true"></span>
                      <i>👤</i>
                      <small>{trText("Input capture", "Girdi alma")}</small>
                      <b>{trText("Symptoms & context received", "Semptom ve bağlam alındı")}</b>
                    </article>

                    <article className={`pipeline-card-v97 ${pipelineIdleFinalV100 ? "idle-v97" : executionStepV86 > 1 ? "done-v97" : executionStepV86 === 1 ? "active-v97" : "idle-v97"}`}>
                      <span className="plain-dot-v103" aria-hidden="true"></span>
                      <i>⚙️</i>
                      <small>{trText("Risk engine", "Risk motoru")}</small>
                      <b>{supportScore}/100</b>
                    </article>

                    <article className={`pipeline-card-v97 ${pipelineIdleFinalV100 ? "idle-v97" : executionStepV86 > 2 ? "done-v97" : executionStepV86 === 2 ? "active-v97" : "idle-v97"}`}>
                      <span className="plain-dot-v103" aria-hidden="true"></span>
                      <i>📋</i>
                      <small>{trText("Clinical note", "Klinik not")}</small>
                      <b>{trText("Care plan prepared", "Bakım planı hazır")}</b>
                    </article>

                    <article className={`pipeline-card-v97 ${pipelineIdleFinalV100 ? "idle-v97" : executionStepV86 > 3 ? "done-v97" : executionStepV86 === 3 ? "active-v97" : "idle-v97"}`}>
                      <span className="plain-dot-v103" aria-hidden="true"></span>
                      <i>〽️</i>
                      <small>{trText("Telemetry", "Telemetri")}</small>
                      <b>{readableTelemetryEvent}</b>
                    </article>
                  </div>

                  <div className="cc-statusbar-v42">
                    <span>{trText("Status", "Durum")}</span>
                    <b>{lastCopilotAction}</b>
                    <em>{trText("Simulation-ready", "Simülasyona hazır")}</em>
                  </div>

                  {visibleRecommendationV106 && lastCopilotAction !== trText("Ready for new analysis.", "Yeni analiz için hazır.") && (
                    <div
                      className="ai-recommendation-v106"
                      style={backendRecommendationV149?.red_flag_detected ? {
                        border: "1px solid rgba(239, 68, 68, 0.72)",
                        boxShadow: "0 18px 42px rgba(127, 29, 29, 0.20)",
                        background: "linear-gradient(180deg, rgba(69, 10, 10, 0.34), rgba(15, 23, 42, 0.98))"
                      } : undefined}
                    >
                      <div className="ai-recommendation-head-v106">
                        <span>
                          {backendRecommendationV149?.red_flag_detected
                            ? trText("Urgent Safety Signal", "Acil Güvenlik Sinyali")
                            : trText("AI Recommendation", "AI Önerisi")}
                        </span>
                        <b>
                          {backendRecommendationV149?.red_flag_detected
                            ? trText(
                                "Rule-based safety override applied",
                                "Kural tabanlı güvenlik kuralı uygulandı"
                              )
                            : trText(
                                "Doctor-ready next action",
                                "Doktor görüşmesine hazır sonraki aksiyon"
                              )}
                        </b>
                      </div>

                      <p>{visibleRecommendationV106}</p>

                      <div className="ai-recommendation-grid-v106">
                        <div>
                          <small>{trText("Support score", "Destek skoru")}</small>
                          <strong>{supportScore}/100</strong>
                        </div>
                        <div>
                          <small>{trText("Clinical priority", "Klinik öncelik")}</small>
                          <strong>
                            {backendRecommendationV149?.riskLevel || supportLevel}
                          </strong>
                        </div>
                        <div>
                          <small>{trText("Main concern", "Ana endişe")}</small>
                          <strong>{concernLabels[mainConcern]}</strong>
                        </div>
                      </div>

                      {backendRecommendationV149?.red_flag_detected &&
                        Array.isArray(backendRecommendationV149?.red_flags) && (
                          <div
                            style={{
                              margin: "16px 0",
                              padding: "12px 14px",
                              borderRadius: "14px",
                              background: "rgba(127, 29, 29, 0.28)",
                              border: "1px solid rgba(248, 113, 113, 0.58)"
                            }}
                          >
                            <strong
                              style={{
                                display: "block",
                                marginBottom: "6px",
                                color: "#fca5a5"
                              }}
                            >
                              {trText(
                                "Detected warning signs",
                                "Tespit edilen uyarı işaretleri"
                              )}
                            </strong>

                            <span style={{ color: "#fee2e2" }}>
                              {backendRecommendationV149.red_flags
                                .map((item) => item.label)
                                .join(" · ")}
                            </span>
                          </div>
                        )}

                      <ul>
                        <li>{trText("Prepare a short symptom summary for the next clinical contact.", "Bir sonraki klinik görüşme için kısa semptom özeti hazırla.")}</li>
                        <li>{trText("Track fatigue, pain, nausea, hydration and mood daily.", "Yorgunluk, ağrı, bulantı, sıvı alımı ve ruh halini günlük takip et.")}</li>
                        <li>{trText("Escalate immediately if fever, severe vomiting, confusion, sudden weakness or breathing difficulty appears.", "Ateş, şiddetli kusma, bilinç bulanıklığı, ani güçsüzlük veya nefes darlığı olursa hemen bakım ekibine bildir.")}</li>
                      </ul>
                    </div>
                  )}
                </section>

                <div className="cc-mid-v42">
                  <section className="cc-trend-v42 cc-trend-target-v51">
                    <div className="trend-head-v51">
                      <div>
                        <h3>What's happening (trend)</h3>
                        <p>Symptom burden over time</p>
                      </div>
                      <select
                        className="trend-range-select-v119"
                        value={trendRangeV119}
                        onChange={(event) => setTrendRangeV119(event.target.value)}
                        aria-label={trText("Trend time range", "Trend zaman aralığı")}
                      >
                        <option value="7">{trText("Last 7 days", "Son 7 gün")}</option>
                        <option value="30">{trText("Last 30 days", "Son 30 gün")}</option>
                        <option value="90">{trText("Last 90 days", "Son 90 gün")}</option>
                      </select>
                    </div>

                    <svg className="trend-chart-v51" viewBox="0 0 620 245" role="img" aria-label="Symptom trend over time">
                      <line x1="62" y1="30" x2="590" y2="30" />
                      <line x1="62" y1="78" x2="590" y2="78" />
                      <line x1="62" y1="126" x2="590" y2="126" />
                      <line x1="62" y1="174" x2="590" y2="174" />
                      <line x1="62" y1="30" x2="62" y2="174" />
                      <line x1="62" y1="174" x2="590" y2="174" />

                      <text x="22" y="35">10</text>
                      <text x="31" y="83">8</text>
                      <text x="31" y="131">6</text>
                      <text x="31" y="179">0</text>

                      <text x="62" y="215">{trendSeriesLiveV126.labels[0]}</text>
                      <text x="170" y="215">{trendSeriesLiveV126.labels[1]}</text>
                      <text x="286" y="215">{trendSeriesLiveV126.labels[2]}</text>
                      <text x="414" y="215">{trendSeriesLiveV126.labels[3]}</text>
                      <text x="512" y="215">{trendSeriesLiveV126.labels[4]}</text>
                      <text x="562" y="215">{trendSeriesLiveV126.labels[5] || "Today"}</text>

                      <polyline className="fatigue-line-v51" points={trendSeriesLiveV126.fatigue} />
                      <polyline className="pain-line-v51" points={trendSeriesLiveV126.pain} />
                      <polyline className="nausea-line-v51" points={trendSeriesLiveV126.nausea} />
                      <polyline className="mood-line-v51" points={trendSeriesLiveV126.mood} />

                      <g>
                        {trendDotsFromPointsV127(trendSeriesLiveV126.fatigue, "fatigue-dot-v51")}
                        {trendDotsFromPointsV127(trendSeriesLiveV126.pain, "pain-dot-v51")}
                        {trendDotsFromPointsV127(trendSeriesLiveV126.nausea, "nausea-dot-v51")}
                        {trendDotsFromPointsV127(trendSeriesLiveV126.mood, "mood-dot-v51")}
                      </g>                    </svg>

                    <div className="trend-legend-v51">
                      <span><i className="fatigue-dot-v51"></i> Fatigue</span>
                      <span><i className="pain-dot-v51"></i> Pain</span>
                      <span><i className="nausea-dot-v51"></i> Nausea</span>
                      <span><i className="mood-dot-v51"></i> Mood</span>
                    </div>
                  </section>

                  <section className="cc-score-v42">
                    <div className="cc-card-title-v42">
                      <span>{trText("Score calculation", "Skor hesaplama")}</span>
                      <b>{trText("How your score was calculated", "Skor nasıl hesaplandı")}</b>
                    </div>

                    <div className="cc-score-body-v42">
                      <div className="cc-donut-v42" style={{ "--score": `${supportScore}%` }}>
                        <strong>{supportScore}</strong>
                        <small>/100</small>
                      </div>

                      <ul>
                        <li><span>{trText("Symptom burden", "Semptom yükü")}</span><b>+{symptomScore}</b></li>
                        <li className="splunk-dataset-inline-v147">
                          <span>
                            {trText("Dataset signal", "Veri sinyali")}
                            <em
                              style={{
                                display: "block",
                                marginTop: "3px",
                                fontStyle: "normal",
                                fontSize: "10.5px",
                                lineHeight: 1.15,
                                fontWeight: 850,
                                color: "#059669"
                              }}
                            >
                              {splunkLiveStatusV140 === "ready"
                                ? `Splunk live: ${splunkLiveMetricsV140?.metrics?.total_events ?? "–"} events · avg ${splunkLiveMetricsV140?.metrics?.avg_risk ?? "–"}`
                                : splunkLiveStatusV140 === "loading"
                                ? trText("Splunk live: reading", "Splunk canlı: okunuyor")
                                : trText("Splunk live: waiting", "Splunk canlı: bekleniyor")}
                            </em>
                          </span>
                          <b>+{dataSignal}</b>
                        </li>
                        <li><span>{trText("Red flags", "Kırmızı bayrak")}</span><b>+{redFlags.length * 12}</b></li>
                        
</ul>
                    </div>

                    <div className="cc-score-guide-v42">
                      <span><b>0–30</b>{trText("Needs close monitoring", "Yakın takip gerekir")}</span>
                      <span><b>31–60</b>{trText("Stable support preparation", "Stabil destek hazırlığı")}</span>
                      <span><b>61–100</b>{trText("Strong condition / low concern", "Daha güçlü durum / düşük endişe")}</span>
                    </div>

                    
                  

                </section>
                </div>

                <section className="cc-network-v42 reasoning-svg-v55 reasoning-svg-v57">
                  <div className="reasoning-head-v55">
                    <div>
                      <h3>AI Reasoning Network</h3>
                      <p>How factors connect to your support priority</p>
                    </div>
                    <div className="reasoning-legend-v55">
                      <span><i className="pos-v55"></i>Positive impact</span>
                      <span><i className="neg-v55"></i>Negative impact</span>
                    </div>
                  </div>

                  <svg className="reasoning-chart-v55 reasoning-chart-v57" viewBox="0 0 940 245" role="img" aria-label="AI reasoning network">
                    <defs>
                      <filter id="softShadowV57" x="-20%" y="-20%" width="140%" height="140%">
                        <feDropShadow dx="0" dy="7" stdDeviation="7" floodColor="#0f172a" floodOpacity="0.08"/>
                      </filter>
                    </defs>

                    <path className="edge-pos-v55 edge-main-v57" d="M138 48 C215 44 250 58 320 72" />
                    <path className="edge-pos-v55 edge-main-v57" d="M138 88 C215 88 250 84 320 72" />
                    <path className="edge-neg-v55 edge-main-v57" d="M138 128 C215 122 250 112 320 112" />
                    <path className="edge-pos-v55 edge-main-v57" d="M138 168 C214 160 248 142 320 152" />

                    <path className="edge-pos-v55 edge-soft-v57" d="M138 48 C220 94 252 132 320 152" />
                    <path className="edge-pos-v55 edge-soft-v57" d="M138 88 C220 112 252 130 320 152" />
                    <path className="edge-neg-v55 edge-soft-v57" d="M138 128 C218 100 250 92 320 72" />
                    <path className="edge-pos-v55 edge-soft-v57" d="M138 168 C218 120 250 98 320 72" />

                    <path className="edge-pos-v55 edge-main-v57" d="M470 72 C520 78 548 96 585 122" />
                    <path className="edge-neg-v55 edge-main-v57" d="M470 112 C520 112 548 116 585 122" />
                    <path className="edge-pos-v55 edge-main-v57" d="M470 152 C520 148 548 134 585 122" />

                    <g className="data-packets-v125" aria-hidden="true">
                      {/* Input signals flowing into interpretation nodes */}
                      <circle className="data-packet-v125 packet-fatigue-v125" r="4.4">
                        <animateMotion dur="3.2s" repeatCount="indefinite" path="M138 48 C215 44 250 58 320 72" />
                      </circle>
                      <circle className="data-packet-v125 packet-pain-v125" r="4.1">
                        <animateMotion dur="3.4s" begin=".35s" repeatCount="indefinite" path="M138 88 C215 88 250 84 320 72" />
                      </circle>
                      <circle className="data-packet-v125 packet-negative-v125" r="4.1">
                        <animateMotion dur="3.1s" begin=".65s" repeatCount="indefinite" path="M138 128 C215 122 250 112 320 112" />
                      </circle>
                      <circle className="data-packet-v125 packet-mood-v125" r="4.2">
                        <animateMotion dur="3.5s" begin=".95s" repeatCount="indefinite" path="M138 168 C214 160 248 142 320 152" />
                      </circle>

                      {/* Interpreted factors flowing into central support priority */}
                      <circle className="data-packet-v125 packet-positive-v125" r="4.8">
                        <animateMotion dur="2.9s" begin=".9s" repeatCount="indefinite" path="M470 72 C520 78 548 96 585 122" />
                      </circle>
                      <circle className="data-packet-v125 packet-negative-v125" r="4.3">
                        <animateMotion dur="3s" begin="1.25s" repeatCount="indefinite" path="M470 112 C520 112 548 116 585 122" />
                      </circle>
                      <circle className="data-packet-v125 packet-positive-v125" r="4.5">
                        <animateMotion dur="3.2s" begin="1.55s" repeatCount="indefinite" path="M470 152 C520 148 548 134 585 122" />
                      </circle>

                      {/* Support priority flowing toward next care actions */}
                      <circle className="data-packet-v125 packet-care-v125" r="5">
                        <animateMotion dur="3.15s" begin="1.7s" repeatCount="indefinite" path="M720 122 C765 74 790 58 815 52" />
                      </circle>
                      <circle className="data-packet-v125 packet-doctor-v125" r="4.8">
                        <animateMotion dur="3.25s" begin="2.05s" repeatCount="indefinite" path="M720 122 C765 122 790 122 815 122" />
                      </circle>
                      <circle className="data-packet-v125 packet-monitor-v125" r="4.8">
                        <animateMotion dur="3.35s" begin="2.35s" repeatCount="indefinite" path="M720 122 C765 170 790 184 815 192" />
                      </circle>
                    </g>

                    <path className="edge-pos-v55 edge-soft-v57" d="M470 72 C518 100 548 116 585 122" />
                    <path className="edge-pos-v55 edge-soft-v57" d="M470 152 C518 126 548 118 585 122" />

                    <path className="edge-pos-v55 edge-main-v57" d="M655 122 C690 74 720 54 755 48" />
                    <path className="edge-pos-v55 edge-main-v57" d="M655 122 C690 122 720 119 755 112" />
                    <path className="edge-neg-v55 edge-main-v57" d="M655 122 C690 166 720 184 755 176" />

                    <path className="edge-neg-v55 edge-soft-v57" d="M655 122 C690 96 720 88 755 112" />
                    <path className="edge-pos-v55 edge-soft-v57" d="M655 122 C690 144 720 154 755 176" />

                    <g filter="url(#softShadowV57)">
                      <rect className="input-node-v55" x="20" y="30" width="128" height="32" rx="8" />
                      <circle className="blue-v55" cx="38" cy="46" r="5" />
                      <text x="55" y="50">Fatigue (6/10)</text>

                      <rect className="input-node-v55" x="20" y="70" width="128" height="32" rx="8" />
                      <circle className="purple-v55" cx="38" cy="86" r="5" />
                      <text x="55" y="90">Pain (4/10)</text>

                      <rect className="input-node-v55" x="20" y="110" width="128" height="32" rx="8" />
                      <circle className="green-v55" cx="38" cy="126" r="5" />
                      <text x="55" y="130">Nausea (3/10)</text>

                      <rect className="input-node-v55" x="20" y="150" width="128" height="32" rx="8" />
                      <circle className="orange-v55" cx="38" cy="166" r="5" />
                      <text x="55" y="170">Mood (5/10)</text>

                      <rect className="factor-node-v55" x="300" y="48" width="142" height="42" rx="13" />
                      <text x="371" y="65" textAnchor="middle">Symptom</text>
                      <text x="371" y="80" textAnchor="middle">Burden</text>

                      <rect className="factor-node-v55 purple-node-v55" x="300" y="96" width="142" height="42" rx="13" />
                      <text x="371" y="114" textAnchor="middle">Treatment</text>
                      <text x="371" y="129" textAnchor="middle">Stage</text>

                      <rect className="factor-node-v55 teal-node-v55" x="300" y="144" width="142" height="42" rx="13" />
                      <text x="371" y="162" textAnchor="middle">Public Data</text>
                      <text x="371" y="177" textAnchor="middle">Match</text>

                      <circle className="priority-halo-v55" cx="610" cy="122" r="58" />
                      <circle className="priority-node-v55" cx="610" cy="122" r="48" />
                      <text className="priority-label-v55 priority-label-top-v57" x="610" y="104">Support</text>
                      <text className="priority-label-v55 priority-label-top-v57" x="610" y="120">Priority</text>
                      <text className="priority-score-v55" x="610" y="146">{supportScore}</text>

                      <rect className="action-node-v55" x="755" y="30" width="150" height="42" rx="13" />
                      <text x="830" y="48" textAnchor="middle">Care Plan</text>
                      <text x="830" y="63" textAnchor="middle">Readiness</text>

                      <rect className="action-node-v55" x="755" y="96" width="150" height="42" rx="13" />
                      <text x="830" y="114" textAnchor="middle">Doctor Visit</text>
                      <text x="830" y="129" textAnchor="middle">Preparation</text>

                      <rect className="action-node-v55" x="755" y="162" width="150" height="42" rx="13" />
                      <text x="830" y="180" textAnchor="middle">Monitoring</text>
                      <text x="830" y="195" textAnchor="middle">Strategy</text>
                    </g>
                  </svg>
                </section>

                <section className="cc-journey-v42">
                  <h3 className="cc-journey-title-v133">{trText("Your Care Journey at a Glance", "Bakım Yolculuğunuz")}</h3>
                  {[
                    ["1", trText("You input", "Girdi"), trText("Symptoms & context", "Semptom ve bağlam")],
                    ["2", trText("AI analysis", "AI analizi"), trText("Risk & data engine", "Risk ve veri motoru")],
                    ["3", trText("Meaning", "Anlam"), trText("Clinical insight", "Klinik içgörü")],
                    ["4", trText("Action", "Aksiyon"), trText("Care recommendations", "Bakım önerileri")],
                    ["5", trText("Follow-up", "Takip"), trText("Monitoring & support", "İzlem ve destek")]
                  ].map(([num, title, desc]) => (
                    <div key={num}>
                      <b>{num}</b>
                      <span>{title}</span>
                      <small>{desc}</small>
                    </div>
                  ))}
                </section>
              </main>

              <aside className="cc-right-v42">
                <section className={`cc-priority-v42 ${supportClass}`}>
                  <span>{trText("Support Priority", "Destek Önceliği")}</span>
                  <strong>{supportScore}<small>/100</small></strong>
                  <b>{clinicalRiskLevel}</b>
                  <p>{safetyMessage}</p>
                </section>

                <section className="cc-evidence-v42 cc-evidence-expanded-v136">
                  <div className="cc-card-title-v42">
                    <span>{trText("Data & Evidence Signal", "Veri ve Kanıt Sinyali")}</span>
                    <b>{trText("Public data matched your context", "Kamu verisi bağlamla eşleşti")}</b>
                  </div>


                  <div className="cc-evidence-grid-v42 evidence-grid-v108">
                    <div>
                      <small>{trText("Treatment KPI", "Tedavi KPI")}</small>
                      <b>{trText("450 records", "450 kayıt")}</b>
                      <em>{trText("Avg response 69.69", "Ort. yanıt 69.69")}</em>
                    </div>
                    <div>
                      <small>{trText("Access pressure", "Erişim baskısı")}</small>
                      <b>{trText("6 NHS files", "6 NHS dosyası")}</b>
                      <em>{trText("28-day / 31-day pathway", "28 gün / 31 gün bakım yolu")}</em>
                    </div>
                    <div>
                      <small>{trText("Lifestyle context", "Yaşam tarzı bağlamı")}</small>
                      <b>{trText("1,000 CRC records", "1.000 CRC kaydı")}</b>
                      <em>{trText("Avg BMI 26.8 / CRC risk 0.15", "Ort. BMI 26.8 / CRC risk 0.15")}</em>
                    </div>
                    <div>
                      <small>{trText("Data quality", "Veri kalitesi")}</small>
                      <b>{trText("v14 evidence", "v14 kanıt")}</b>
                      <em>
                        {splunkLiveStatusV140 === "ready"
                          ? `Live telemetry: ${splunkLiveMetricsV140?.metrics?.total_events ?? "–"} events · avg risk ${splunkLiveMetricsV140?.metrics?.avg_risk ?? "–"}`
                          : splunkLiveStatusV140 === "loading"
                          ? trText("Live telemetry reading...", "Canlı telemetri okunuyor...")
                          : trText("summary + checksums", "özet + checksum")}
                      </em>
                    </div>
                  </div>

                  <div className={`evidence-position-v108 ${filteredRows.length ? "" : "limited-v108"}`}>
                    <div className="evidence-position-head-v108">
                      <span>{trText("Compared to similar patients", "Benzer hastalarla karşılaştırma")}</span>
                      <small>
                        {trText(
                          hasLiveCohortV151
                            ? `Live Splunk comparison uses ${cohortEventCountV151} indexed events from the last 24 hours. Current case risk: ${currentCaseRiskV151}; cohort average: ${cohortAvgRiskV151}.`
                            : "Live Splunk cohort comparison is currently unavailable. The marker remains neutral.",
                          hasLiveCohortV151
                            ? `Canlı Splunk karşılaştırması son 24 saatte indekslenen ${cohortEventCountV151} olayı kullanır. Mevcut vaka riski: ${currentCaseRiskV151}; kohort ortalaması: ${cohortAvgRiskV151}.`
                            : "Canlı Splunk kohort karşılaştırması şu anda kullanılamıyor. Gösterge nötr konumda kalır."
                        )}
                      </small>
                    </div>

                    <div className="evidence-scale-v108">
                      <div className="evidence-scale-labels-v108">
                        <b>{trText("Lower", "Daha düşük")}</b>
                        <b>{trText("Similar", "Benzer")}</b>
                        <b>{trText("Higher", "Daha yüksek")}</b>
                      </div>
                      <div className="evidence-track-v108" aria-hidden="true">
                        <i
                          style={{
                            left: hasLiveCohortV151
                              ? `${cohortMarkerPositionV151}%`
                              : "50%"
                          }}
                        ></i>
                      </div>

                      <strong
                        style={{
                          left: hasLiveCohortV151
                            ? `${cohortMarkerPositionV151}%`
                            : "50%"
                        }}
                      >
                        {hasLiveCohortV151
                          ? cohortComparisonLabelV151
                          : trText("You are here", "Buradasınız")}
                      </strong>
                    </div>
                  </div>
                </section>

                <section className="cc-next-side-v67">
                  <div className="cc-next-side-head-v67">
                    <span>Next Best Actions</span>
                    <h3>What should you do now?</h3>
                  </div>

                  <div className="cc-next-side-grid-v67">
                    <article className="cc-next-side-card-v67">
                      <div className="cc-next-side-icon-v67 blue-v67">📈</div>
                      <h4>Track</h4>
                      <p>Focus on these symptoms daily</p>
                      <ul>
                        <li>Fatigue</li>
                        <li>Pain</li>
                        <li>Nausea</li>
                        <li>Hydration</li>
                      </ul>
                    </article>

                    <article className="cc-next-side-card-v67">
                      <div className="cc-next-side-icon-v67 purple-v67">🩺</div>
                      <h4>Ask Your Doctor</h4>
                      <p>Key questions for your next visit</p>
                      <ul>
                        <li>Which symptoms should I monitor closely?</li>
                        <li>What changes should trigger urgent contact?</li>
                      </ul>
                    </article>

                    <article className="cc-next-side-card-v67">
                      <div className="cc-next-side-icon-v67 green-v67">📋</div>
                      <h4>Prepare</h4>
                      <p>Be ready for your appointment</p>
                      <ul>
                        <li>Bring this report</li>
                        <li>Track symptoms</li>
                        <li>List medications</li>
                      </ul>
                    </article>
                  </div>
                </section>

                <section className="cc-report-v42">
                  <div>
                    <b>{trText("Download your report", "Raporunu indir")}</b>
                    <p>{trText("Doctor-ready report with analysis and recommendations.", "Analiz ve öneriler içeren doktora hazır rapor.")}</p>
                    <button type="button" onClick={exportDetailedReportPdf}>{trText("Export PDF", "PDF Dışa Aktar")}</button>
                  </div>
                  <span>📄</span>
                </section>
                <div className="cc-side-mini-card-v135 cc-side-mini-card-right-v135">
                  <span>{trText("Report Readiness", "Rapor Hazırlığı")}</span>
                  <b>{trText("Doctor-ready output layer", "Doktor görüşmesine hazır çıktı katmanı")}</b>
                  <ul>
                    <li>{trText("PDF summary prepared after analysis", "Analiz sonrası PDF özeti hazırlanır")}</li>
                    <li>{trText("Reasoning network and trend signal included", "Akıl yürütme ağı ve trend sinyali dahil edilir")}</li>
                    <li>{trText("Next action notes are exportable", "Sonraki aksiyon notları dışa aktarılabilir")}</li>
                  </ul>
                </div>

              </aside>
            </div>
          </div>

          <div className="patient-input-panel">
            <div className="copilot-quickstart-v6">
              <div>
                <span>{trText("Quick start", "Hızlı başlangıç")}</span>
                <h2>{trText("How to use this Copilot", "Bu Copilot nasıl kullanılır?")}</h2>
                <p>
                  {trText(
                    "Start with a role and goal, choose the clinical context, enter symptoms, then run the risk engine, simulation and report export.",
                    "Rol ve hedef seçin, klinik bağlamı belirleyin, semptomları girin; ardından risk motorunu, simülasyonu ve rapor dışa aktarımını çalıştırın."
                  )}
                </p>
              </div>

              <ol>
                <li>{trText("Choose who you are and what you want to understand.", "Kim olduğunuzu ve neyi anlamak istediğinizi seçin.")}</li>
                <li>{trText("Select city, age group, cancer type, treatment stage and scenario.", "Şehir, yaş grubu, kanser türü, tedavi aşaması ve senaryo seçin.")}</li>
                <li>{trText("Move symptom sliders and mark red flags if present.", "Semptom kaydırıcılarını ayarlayın ve varsa kırmızı bayrakları işaretleyin.")}</li>
                <li>{trText("Run simulation, generate detailed report, then export PDF.", "Simülasyonu çalıştırın, detaylı rapor üretin ve PDF olarak dışa aktarın.")}</li>
              </ol>

              <div className="copilot-quickstart-actions-v6">
                <button type="button" onClick={loadDemoCase}>
                  {trText("Load demo case", "Demo vaka yükle")}
                </button>
                <button type="button" onClick={runGuidedDemo}>
                  {trText("Run guided demo", "Yönlendirmeli demoyu çalıştır")}
                </button>
                <button type="button" onClick={exportDetailedReportPdf}>
                  {trText("Export PDF report", "PDF raporu dışa aktar")}
                </button>



              </div>
            </div>

            <div className="copilot-ai-power-dashboard-v10">
              <div className="ai-power-hero-v10">
                <span>{trText("AI Power / Data Intelligence", "AI Gücü / Veri Zekâsı")}</span>
                <h2>{trText("CSV → Splunk → AI Plot → Report", "CSV → Splunk → AI Plot → Rapor")}</h2>
                <p>
                  {trText(
                    "This layer shows how indexed datasets and Copilot events become explainable AI signals, visual analytics and report-ready evidence.",
                    "Bu katman, indexlenmiş veri setlerinin ve Copilot olaylarının nasıl açıklanabilir AI sinyallerine, görsel analitiklere ve raporlanabilir kanıta dönüştüğünü gösterir."
                  )}
                </p>
              </div>

              <div className="ai-power-flow-v10">
                <div>
                  <b>CSV</b>
                  <small>{trText("raw datasets", "ham veri setleri")}</small>
                </div>
                <i></i>
                <div>
                  <b>Splunk</b>
                  <small>{trText("indexed events", "indexlenmiş olaylar")}</small>
                </div>
                <i></i>
                <div>
                  <b>AI</b>
                  <small>{trText("feature extraction", "özellik çıkarımı")}</small>
                </div>
                <i></i>
                <div>
                  <b>Plot</b>
                  <small>{trText("visual intelligence", "görsel zekâ")}</small>
                </div>
                <i></i>
                <div>
                  <b>Report</b>
                  <small>{trText("doctor-ready output", "doktor hazır çıktı")}</small>
                </div>
              </div>

              <div className="ai-power-real-data-v11">
                <div className="ai-power-real-head-v11">
                  <div>
                    <span>{trText("Real data verification", "Gerçek veri doğrulaması")}</span>
                    <h3>{trText("Loaded dataset analytics", "Yüklenen veri seti analitiği")}</h3>
                    <p>
                      {trText(
                        "These charts are generated from the committed CSV dataset summaries, not from static text. Row counts, checksums, distributions and correlations prove that the dashboard is connected to real data sources.",
                        "Bu grafikler statik metinden değil, commitlenmiş CSV veri seti özetlerinden üretilir. Satır sayıları, checksum değerleri, dağılımlar ve korelasyonlar panelin gerçek veri kaynaklarına bağlı olduğunu kanıtlar."
                      )}
                    </p>
                  </div>

                  <strong className={`ai-power-real-status-v11 ${aiPowerRealDataStatus}`}>
                    {aiPowerRealDataStatus === "loaded"
                      ? trText("Real data loaded", "Gerçek veri yüklendi")
                      : aiPowerRealDataStatus === "error"
                        ? trText("Summary not loaded", "Özet yüklenemedi")
                        : trText("Loading data summary", "Veri özeti yükleniyor")}
                  </strong>
                </div>

                {aiPowerRealData?.generated_at && (
                  <div className="ai-power-real-proof-v11">
                    <span>{trText("Generated from CSV", "CSV’den üretildi")}</span>
                    <code>{aiPowerRealData.generated_at}</code>
                    <small>{aiPowerRealData.proof}</small>
                  </div>
                )}

                <div className="ai-data-lineage-v12">
                  <div className="ai-data-lineage-head-v12">
                    <span>{trText("Data lineage", "Veri soy ağacı")}</span>
                    <strong>{trText("What is used, where it comes from, and how it is visualized", "Ne kullanılıyor, nereden geliyor ve nasıl görselleştiriliyor")}</strong>
                  </div>

                  <div className="ai-data-lineage-grid-v12">
                    {aiDataLineageRows.map((row) => (
                      <article key={row.layer}>
                        <b>{row.layer}</b>
                        <span>{row.source}</span>
                        <p>{row.usedFor}</p>
                        <code>{row.columns}</code>
                      </article>
                    ))}
                  </div>

                  {!publicDataHasMatch && (
                    <div className="ai-context-mode-v15">
                      <div>
                        <span>{trText("Broader context mode active", "Geniş bağlam modu aktif")}</span>
                        <b>{trText("No exact public row found — the AI keeps working with related evidence.", "Tam kamu satırı bulunamadı — AI ilişkili kanıtlarla çalışmaya devam ediyor.")}</b>
                        <p>
                          {trText(
                            "Instead of stopping, the system explains which signals are still usable: symptoms, treatment context, NHS access pressure, lifestyle/prevention data and caregiver answers.",
                            "Sistem durmak yerine hâlâ kullanılabilir sinyalleri açıklar: semptomlar, tedavi bağlamı, NHS erişim baskısı, yaşam tarzı/önleme verisi ve bakıcı yanıtları."
                          )}
                        </p>
                      </div>
                      <ul>
                        <li>{trText("Use broader access pressure", "Daha geniş erişim baskısını kullan")}</li>
                        <li>{trText("Keep treatment and symptom reasoning active", "Tedavi ve semptom akıl yürütmesini aktif tut")}</li>
                        <li>{trText("Show user-friendly next questions", "Kullanıcı dostu sonraki soruları göster")}</li>
                      </ul>
                    </div>
                  )}
                </div>

                <div className="ai-system-context-v14">
                  <div className="ai-system-context-head-v14">
                    <div>
                      <span>{trText("v14 · Access, lifestyle & treatment intelligence", "v14 · Erişim, yaşam tarzı ve tedavi zekâsı")}</span>
                      <h3>{trText("Three new evidence layers added to the relational graph", "İlişkisel grafa üç yeni kanıt katmanı eklendi")}</h3>
                      <p>
                        {trText(
                          "NHS waiting-time data adds access pressure, treatment KPIs add cohort-level care journey context, and colorectal lifestyle data adds prevention and screening-discussion prompts.",
                          "NHS bekleme süresi verisi erişim baskısı ekler, tedavi KPI verisi kohort düzeyi bakım yolculuğu bağlamı verir, colorectal yaşam tarzı verisi önleme ve tarama görüşmesi uyarıları ekler."
                        )}
                      </p>
                    </div>
                    <strong>{v14Context ? trText("Loaded", "Yüklendi") : trText("Loading", "Yükleniyor")}</strong>
                  </div>

                  {accessLifestyleErrorV14 && (
                    <div className="ai-system-error-v14">
                      <b>{trText("v14 context could not be loaded", "v14 bağlamı yüklenemedi")}</b>
                      <p>{accessLifestyleErrorV14}</p>
                    </div>
                  )}

                  {v14Context && (
                    <>
                      <div className="ai-system-layer-grid-v14">
                        {(v14System?.graph_layers || []).map((layer) => (
                          <article key={layer.layer}>
                            <span>{layer.layer}</span>
                            <b>{layer.evidence}</b>
                            <p>{layer.insight}</p>
                          </article>
                        ))}
                      </div>

                      <div className="ai-v14-kpi-grid">
                        <article>
                          <span>{trText("NHS access pressure", "NHS erişim baskısı")}</span>
                          <b>{v14NhsHighlights[0]?.performance ?? "-"}%</b>
                          <p>{v14NhsHighlights[0]?.label}</p>
                        </article>
                        <article>
                          <span>{trText("Treatment response context", "Tedavi yanıt bağlamı")}</span>
                          <b>{v14TreatmentKpis.avg_response_score ?? "-"}</b>
                          <p>{trText("Average response score across treatment KPI dataset", "Tedavi KPI veri setinde ortalama yanıt skoru")}</p>
                        </article>
                        <article>
                          <span>{trText("Treatment journey intensity", "Tedavi yolculuğu yoğunluğu")}</span>
                          <b>{v14TreatmentKpis.avg_cycles ?? "-"}</b>
                          <p>{trText("Average number of cycles", "Ortalama döngü sayısı")}</p>
                        </article>
                        <article>
                          <span>{trText("CRC lifestyle records", "CRC yaşam tarzı kayıtları")}</span>
                          <b>{formatAiPowerNumber(v14Crc?.rows || 0)}</b>
                          <p>{trText("Diet, BMI, family-history and lifestyle context", "Beslenme, BMI, aile öyküsü ve yaşam tarzı bağlamı")}</p>
                        </article>
                      </div>

                      <div className="ai-v14-relation-grid">
                        {v14IntelligenceEdges.map((edge) => (
                          <article key={edge.layer}>
                            <span>{edge.layer}</span>
                            <b>{edge.from} → {edge.to}</b>
                            <p>{edge.why}</p>
                            <strong>{edge.action}</strong>
                          </article>
                        ))}
                      </div>

                      <div className="ai-v14-evidence-columns">
                        <article>
                          <span>{trText("NHS waiting-time pathways", "NHS bekleme süresi yolları")}</span>
                          {(v14NhsHighlights || []).map((item) => (
                            <div key={item.label}>
                              <b>{item.performance ?? "-"}%</b>
                              <p>{item.label}</p>
                              <small>{formatAiPowerNumber(item.total)} {trText("pathways", "yol")} · {formatAiPowerNumber(item.after)} {trText("after standard", "standard sonrası")}</small>
                            </div>
                          ))}
                        </article>

                        <article>
                          <span>{trText("Treatment KPI distributions", "Tedavi KPI dağılımları")}</span>
                          {(v14TreatmentStages || []).slice(0, 5).map((item) => (
                            <div key={item.label}>
                              <b>{item.percent}%</b>
                              <p>{item.label}</p>
                              <small>{formatAiPowerNumber(item.count)} {trText("rows", "satır")}</small>
                            </div>
                          ))}
                        </article>

                        <article>
                          <span>{trText("CRC lifestyle risk context", "CRC yaşam tarzı risk bağlamı")}</span>
                          {(v14CrcLifestyleRows || []).slice(0, 5).map((item) => (
                            <div key={item.label}>
                              <b>{item.crc_risk_rate_percent}%</b>
                              <p>{item.label}</p>
                              <small>{formatAiPowerNumber(item.count)} {trText("rows", "satır")}</small>
                            </div>
                          ))}
                        </article>
                      </div>

                      <div className="ai-v14-action-path">
                        <span>{trText("Smart care conversation path", "Akıllı bakım görüşmesi yolu")}</span>
                        <div>
                          <article><b>{trText("Who", "Kim")}</b><p>{v14ActionPath.who}</p></article>
                          <article><b>{trText("Where", "Nerede")}</b><p>{v14ActionPath.where}</p></article>
                          <article><b>{trText("Why", "Neden")}</b><p>{v14ActionPath.why}</p></article>
                          <article><b>{trText("What", "Ne")}</b><p>{v14ActionPath.what}</p></article>
                        </div>
                        <strong>{v14ActionPath.safety}</strong>
                      </div>
                    </>
                  )}
                </div>

                <div className="ai-insight-cockpit-v16">
                  <div className="ai-cockpit-hero-v16">
                    <div>
                      <span>{trText("v16 · Interactive Insight Cockpit", "v16 · Etkileşimli İçgörü Kokpiti")}</span>
                      <h3>{trText("Choose a lens. Ask a question. See meaning, evidence and action.", "Bir lens seç. Bir soru sor. Anlamı, kanıtı ve aksiyonu gör.")}</h3>
                      <p>
                        {trText(
                          "This turns the long analytics dashboard into a guided decision experience for patients, caregivers and judges.",
                          "Bu katman uzun analitik dashboard’u hastalar, bakıcılar ve hakemler için yönlendirmeli bir karar deneyimine dönüştürür."
                        )}
                      </p>
                    </div>
                    <strong>{selectedInsightLensV16.score}/100</strong>
                  </div>

                  <div className="ai-cockpit-controls-v16">
                    <div>
                      <b>{trText("1. Choose data lens", "1. Veri lensi seç")}</b>
                      <div>
                        {insightLensesV16.map((lens) => (
                          <button
                            key={lens.id}
                            type="button"
                            className={insightLensV16 === lens.id ? "active" : ""}
                            onClick={() => setInsightLensV16(lens.id)}
                          >
                            {lens.label}
                          </button>
                        ))}
                      </div>
                    </div>

                    <div>
                      <b>{trText("2. Ask the system", "2. Sisteme sor")}</b>
                      <div>
                        {insightQuestionsV16.map((question) => (
                          <button
                            key={question.id}
                            type="button"
                            className={insightQuestionV16 === question.id ? "active" : ""}
                            onClick={() => setInsightQuestionV16(question.id)}
                          >
                            {question.label}
                          </button>
                        ))}
                      </div>
                    </div>
                  </div>

                  <div className="ai-cockpit-answer-v16">
                    <div>
                      <span>{trText("Selected lens", "Seçilen lens")}</span>
                      <b>{selectedInsightLensV16.label}</b>
                      <p>{selectedInsightLensV16.source}</p>
                    </div>
                    <div className="main-answer-v16">
                      <span>{trText("Answer", "Yanıt")}</span>
                      <b>{selectedInsightAnswerV16}</b>
                    </div>
                    <div>
                      <span>{trText("Recommended action", "Önerilen aksiyon")}</span>
                      <b>{selectedInsightLensV16.action}</b>
                    </div>
                  </div>

                  <div className="ai-pathway-v16">
                    {insightSourcePathV16.map((step, index) => (
                      <article key={step.label}>
                        <small>{index + 1}</small>
                        <span>{step.label}</span>
                        <p>{step.value}</p>
                      </article>
                    ))}
                  </div>

                  <div className="ai-data-explorer-v16">
                    <div className="ai-data-explorer-head-v16">
                      <span>{trText("Interactive data explorer", "Etkileşimli veri gezgini")}</span>
                      <b>{trText("Every metric becomes a useful explanation", "Her metrik faydalı bir açıklamaya dönüşür")}</b>
                    </div>

                    <div className="ai-data-explorer-grid-v16">
                      {insightDataExplorerV16.map((item) => (
                        <article key={item.label}>
                          <span>{item.label}</span>
                          <b>{item.value}</b>
                          <p>{item.meaning}</p>
                        </article>
                      ))}
                    </div>
                  </div>

                  <div className="ai-cockpit-note-v16">
                    {trText(
                      "Dashboard details remain below as evidence. The cockpit above is the user-friendly decision layer.",
                      "Dashboard detayları aşağıda kanıt olarak kalır. Yukarıdaki kokpit kullanıcı dostu karar katmanıdır."
                    )}
                  </div>
                </div>

                <div className="ai-command-center-v17">
                  <style>
                    {!showDeepEvidenceV17 ? `
                      .ai-data-lineage-v12,
                      .ai-power-real-grid-v11,
                      .ai-power-source-grid-v10,
                      .ai-data-meaning-v15,
                      .ai-relational-graph-v13 {
                        display: none !important;
                      }
                    ` : ""}
                  </style>

                  <div className="ai-command-hero-v17">
                    <div>
                      <span>{trText("v17 · Command Center", "v17 · Komuta Merkezi")}</span>
                      <h3>{trText("Turn data into one clear answer.", "Veriyi tek net cevaba dönüştür.")}</h3>
                      <p>
                        {trText(
                          "Choose what you want to understand. The system connects symptoms, public context, access pressure, treatment data, lifestyle signals and caregiver answers into a user-ready action.",
                          "Neyi anlamak istediğini seç. Sistem semptomları, kamu bağlamını, erişim baskısını, tedavi verisini, yaşam tarzı sinyallerini ve bakıcı yanıtlarını kullanıcıya hazır aksiyona bağlar."
                        )}
                      </p>
                    </div>

                    <div className="ai-command-score-v17">
                      <small>{trText("Current priority", "Mevcut öncelik")}</small>
                      <b>{selectedInsightLensV16.score}/100</b>
                      <span>{selectedInsightLensV16.label}</span>
                    </div>
                  </div>

                  <div className="ai-command-layout-v17">
                    <section className="ai-command-picker-v17">
                      <div className="ai-command-step-v17">
                        <span>1</span>
                        <b>{trText("Choose data lens", "Veri lensi seç")}</b>
                      </div>

                      <div className="ai-command-chip-grid-v17">
                        {insightLensesV16.map((lens) => (
                          <button
                            key={lens.id}
                            type="button"
                            className={insightLensV16 === lens.id ? "active" : ""}
                            onClick={() => setInsightLensV16(lens.id)}
                          >
                            <b>{lens.label}</b>
                            <small>{lens.source}</small>
                          </button>
                        ))}
                      </div>
                    </section>

                    <section className="ai-command-picker-v17">
                      <div className="ai-command-step-v17">
                        <span>2</span>
                        <b>{trText("Ask a question", "Bir soru sor")}</b>
                      </div>

                      <div className="ai-command-question-list-v17">
                        {insightQuestionsV16.map((question) => (
                          <button
                            key={question.id}
                            type="button"
                            className={insightQuestionV16 === question.id ? "active" : ""}
                            onClick={() => setInsightQuestionV16(question.id)}
                          >
                            {question.label}
                          </button>
                        ))}
                      </div>
                    </section>

                    <section className="ai-command-answer-v17">
                      <div className="ai-command-step-v17">
                        <span>3</span>
                        <b>{trText("Meaning and action", "Anlam ve aksiyon")}</b>
                      </div>

                      <article>
                        <small>{trText("Answer", "Yanıt")}</small>
                        <h4>{selectedInsightAnswerV16}</h4>
                      </article>

                      <article>
                        <small>{trText("What this means", "Bu ne anlama geliyor")}</small>
                        <p>{selectedInsightLensV16.meaning}</p>
                      </article>

                      <article className="action-v17">
                        <small>{trText("Recommended next step", "Önerilen sonraki adım")}</small>
                        <p>{selectedInsightLensV16.action}</p>
                      </article>
                    </section>
                  </div>

                  <div className="ai-command-path-v17">
                    <article>
                      <span>{trText("Raw evidence", "Ham kanıt")}</span>
                      <b>{selectedInsightLensV16.source}</b>
                    </article>
                    <article>
                      <span>{trText("AI interpretation", "AI yorumu")}</span>
                      <b>{selectedInsightLensV16.meaning}</b>
                    </article>
                    <article>
                      <span>{trText("User output", "Kullanıcı çıktısı")}</span>
                      <b>{selectedInsightLensV16.action}</b>
                    </article>
                  </div>

                  <div className="ai-command-footer-v17">
                    <div>
                      <b>{trText("Designed for judges and real users", "Hakemler ve gerçek kullanıcılar için tasarlandı")}</b>
                      <p>
                        {trText(
                          "The dashboard now starts with a guided decision layer. Technical dataset evidence stays available, but it no longer overwhelms the main user journey.",
                          "Dashboard artık yönlendirmeli karar katmanıyla başlar. Teknik veri kanıtları erişilebilir kalır; ancak ana kullanıcı yolculuğunu artık boğmaz."
                        )}
                      </p>
                    </div>

                    <button type="button" onClick={() => setShowDeepEvidenceV17((value) => !value)}>
                      {showDeepEvidenceV17
                        ? trText("Hide technical evidence layers", "Teknik kanıt katmanlarını gizle")
                        : trText("Show technical evidence layers", "Teknik kanıt katmanlarını göster")}
                    </button>
                  </div>
                </div>

                <div className="ai-data-meaning-v15">
                  <div className="ai-data-meaning-hero-v15">
                    <div>
                      <span>{trText("v15 · Data-to-Meaning Experience", "v15 · Veriden Anlama Deneyimi")}</span>
                      <h3>{trText("Every dataset becomes a care conversation, not just a chart.", "Her veri seti sadece grafik değil, bakım görüşmesine dönüşür.")}</h3>
                      <p>
                        {trText(
                          "OncoConnect AI translates public statistics, waiting-time pressure, treatment KPIs, lifestyle data, symptoms and caregiver answers into a clear support pathway.",
                          "OncoConnect AI kamu istatistiklerini, bekleme süresi baskısını, tedavi KPI’larını, yaşam tarzı verisini, semptomları ve bakıcı yanıtlarını net bir destek yoluna çevirir."
                        )}
                      </p>
                    </div>
                    <strong>{contextModeV15}</strong>
                  </div>

                  <div className="ai-context-mode-card-v15">
                    <span>{trText("Current interpretation mode", "Mevcut yorumlama modu")}</span>
                    <b>{contextModeV15}</b>
                    <p>{contextModeDetailV15}</p>
                  </div>

                  <div className="ai-data-meaning-grid-v15">
                    {dataToMeaningCardsV15.map((card) => (
                      <article key={card.label}>
                        <div className="ai-meaning-score-v15">
                          <span>{card.label}</span>
                          <b>{card.score}/100</b>
                        </div>
                        <em><i style={{ width: `${Math.max(5, Math.min(100, Number(card.score || 0)))}%` }}></i></em>
                        <small>{trText("Raw data", "Ham veri")}</small>
                        <p>{card.raw}</p>
                        <small>{trText("Meaning", "Anlam")}</small>
                        <p>{card.meaning}</p>
                        <strong>{card.action}</strong>
                      </article>
                    ))}
                  </div>

                  <div className="ai-judge-ready-v15">
                    <div>
                      <span>{trText("Judge-ready impact story", "Hakemlere hazır etki hikâyesi")}</span>
                      <b>{trText("Why this project matters", "Bu proje neden önemli")}</b>
                    </div>
                    <div className="ai-judge-grid-v15">
                      {judgeImpactCardsV15.map((item) => (
                        <article key={item.title}>
                          <b>{item.title}</b>
                          <p>{item.text}</p>
                        </article>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="ai-relational-graph-v13">
                  <div className="ai-relational-head-v13">
                    <div>
                      <span>{trText("AI Relational Intelligence Graph", "AI İlişkisel Zekâ Grafı")}</span>
                      <h3>{trText("From disconnected CSVs to a patient-ready action path", "Dağınık CSV’lerden hasta odaklı aksiyon yoluna")}</h3>
                      <p>
                        {trText(
                          "This graph connects public cancer context, chemotherapy cohort signals, thyroid monitoring features, red flags and patient/caregiver answers into an explainable support pathway.",
                          "Bu graf kamu kanser bağlamını, kemoterapi kohort sinyallerini, tiroid takip özelliklerini, kırmızı bayrakları ve hasta/bakıcı yanıtlarını açıklanabilir bir destek yoluna bağlar."
                        )}
                      </p>
                    </div>
                    <strong>{relationalPriorityScore}/100 · {relationalPriorityLabel}</strong>
                  </div>

                  <div className="ai-neural-map-v13">
                    {aiRelationNodes.map((node, index) => (
                      <div
                        key={node.id}
                        className={`ai-neural-node-v13 node-${node.id}`}
                        style={{ "--node-strength": `${node.strength}%`, "--node-index": index }}
                      >
                        <small>{node.type}</small>
                        <b>{node.label}</b>
                        <span>{node.detail}</span>
                        <em><i style={{ width: `${node.strength}%` }}></i></em>
                      </div>
                    ))}
                  </div>

                  <div className="ai-relation-edge-grid-v13">
                    {aiRelationEdges.map((edge) => (
                      <article key={`${edge.from}-${edge.to}`}>
                        <div>
                          <b>{edge.from} → {edge.to}</b>
                          <span>{edge.source}</span>
                        </div>
                        <p>{edge.relation}</p>
                        <small>{edge.why}</small>
                        <strong>{edge.action}</strong>
                      </article>
                    ))}
                  </div>

                  <div className="ai-caregiver-question-engine-v13">
                    <div className="ai-question-head-v13">
                      <span>{trText("Patient / caregiver question engine", "Hasta / bakıcı soru motoru")}</span>
                      <strong>{trText("Answer these to strengthen the relationship graph", "İlişki grafını güçlendirmek için yanıtlayın")}</strong>
                    </div>

                    <div className="ai-question-grid-v13">
                      {relationalQuestionFlow.map((question) => (
                        <article key={question.id}>
                          <b>{question.question}</b>
                          <p>{question.reason}</p>
                          <div>
                            {question.options.map((option) => (
                              <button
                                key={option.value}
                                type="button"
                                className={relationAnswers[question.id]?.value === option.value ? "active" : ""}
                                onClick={() => setRelationAnswer(question.id, option)}
                              >
                                {option.label}
                              </button>
                            ))}
                          </div>
                        </article>
                      ))}
                    </div>
                  </div>

                  <div className="ai-action-output-v13">
                    <div className="ai-action-output-title-v13">
                      <span>{trText("Smart action output", "Akıllı aksiyon çıktısı")}</span>
                      <strong>{trText("Who, where, why, what and when", "Kim, nerede, neden, ne yapmalı ve ne zaman")}</strong>
                    </div>

                    <div className="ai-action-output-grid-v13">
                      <article>
                        <b>{trText("Who acts?", "Kim aksiyon alır?")}</b>
                        <p>{relationalActionOutput.who}</p>
                      </article>
                      <article>
                        <b>{trText("Where is the context?", "Bağlam nerede?")}</b>
                        <p>{relationalActionOutput.where}</p>
                      </article>
                      <article>
                        <b>{trText("Why does it matter?", "Neden önemli?")}</b>
                        <p>{relationalActionOutput.why}</p>
                      </article>
                      <article>
                        <b>{trText("What should be done?", "Ne yapılmalı?")}</b>
                        <p>{relationalActionOutput.what}</p>
                      </article>
                      <article>
                        <b>{trText("When?", "Ne zaman?")}</b>
                        <p>{relationalActionOutput.when}</p>
                      </article>
                    </div>

                    <div className="ai-action-safety-note-v13">
                      {trText(
                        "This output is a structured communication aid. It is not a diagnosis, treatment decision, emergency triage or personal survival prediction.",
                        "Bu çıktı yapılandırılmış iletişim desteğidir. Tanı, tedavi kararı, acil triyaj veya kişisel sağkalım tahmini değildir."
                      )}
                    </div>
                  </div>
                </div>

                <div className="ai-power-real-grid-v11">
                  {aiPowerRealDatasets.map((dataset) => (
                    <article className="ai-power-real-card-v11" key={dataset.id}>
                      <div className="ai-power-real-title-v11">
                        <div>
                          <span>{dataset.domain}</span>
                          <h4>{dataset.name}</h4>
                        </div>
                        <b>{dataset.file_size_mb} MB</b>
                      </div>

                      <div className="ai-power-real-kpis-v11">
                        <div>
                          <strong>{formatAiPowerNumber(dataset.row_count)}</strong>
                          <small>{trText("rows", "satır")}</small>
                        </div>
                        <div>
                          <strong>{dataset.column_count}</strong>
                          <small>{trText("columns", "kolon")}</small>
                        </div>
                        <div>
                          <strong>{dataset.numeric_columns_detected}</strong>
                          <small>{trText("numeric", "sayısal")}</small>
                        </div>
                        <div>
                          <strong>{dataset.sha256_prefix}</strong>
                          <small>checksum</small>
                        </div>
                      </div>

                      <div className="ai-power-chart-block-v11">
                        <div className="ai-power-chart-head-v11">
                          <b>{trText("Key metric bars", "Ana metrik barları")}</b>
                          <small>{dataset.source}</small>
                        </div>

                        {(dataset.key_metrics || []).slice(0, 6).map((metric) => (
                          <div className="ai-power-real-bar-v11" key={`${dataset.id}-${metric.label}`}>
                            <div>
                              <span>{metric.label}</span>
                              <small>avg {formatAiPowerDecimal(metric.value)}</small>
                            </div>
                            <em>
                              <i style={{ width: `${Math.max(4, Math.min(100, Number(metric.relative || 0)))}%` }}></i>
                            </em>
                            <p>{getAiPowerColumnMeaning(metric.label)}</p>
                          </div>
                        ))}
                      </div>

                      <div className="ai-power-line-risk-v11">
                        <div>
                          <b>{trText("Trend line", "Trend çizgisi")}</b>
                          <svg viewBox="0 0 100 100" preserveAspectRatio="none">
                            <polyline points={aiPowerTrendPoints(dataset.trend)} />
                          </svg>
                          <small>{trText("10-window burden trend from dataset rows", "Veri satırlarından 10 pencereli yük trendi")}</small>
                        </div>

                        <div>
                          <b>{trText("Risk / prognosis distribution", "Risk / prognoz dağılımı")}</b>
                          <ul>
                            {(dataset.risk_distribution || []).slice(0, 4).map((risk) => (
                              <li key={`${dataset.id}-${risk.label}`}>
                                <span>{risk.label}</span>
                                <strong>{risk.percent}%</strong>
                              </li>
                            ))}
                          </ul>
                          <small>{trText("source", "kaynak")}: {dataset.risk_source}</small>
                        </div>
                      </div>

                      <div className="ai-power-correlation-v11">
                        <b>{trText("Top correlations", "En güçlü korelasyonlar")}</b>
                        {(dataset.correlations || []).length ? (
                          <ul>
                            {dataset.correlations.slice(0, 4).map((corr) => (
                              <li key={`${dataset.id}-${corr.x}-${corr.y}`}>
                                <span>{corr.x} ↔ {corr.y}</span>
                                <strong>r={corr.r}</strong>
                              </li>
                            ))}
                          </ul>
                        ) : (
                          <p>{trText("No strong numeric correlation detected in preview sample.", "Önizleme örneğinde güçlü sayısal korelasyon bulunamadı.")}</p>
                        )}
                      </div>
                    </article>
                  ))}
                </div>
              </div>

              <div className="ai-power-source-grid-v10">
                {aiPowerSources.map((source) => (
                  <article key={source.id}>
                    <div>
                      <span>{source.status}</span>
                      <strong>{source.name}</strong>
                    </div>
                    <p>{source.domain}</p>
                    <small>{source.signal}</small>
                    <code>{source.splunkSource}</code>
                  </article>
                ))}
              </div>

              <div className="ai-power-main-grid-v10">
                <section className="ai-power-breakdown-v10">
                  <div className="ai-power-section-head-v10">
                    <span>{trText("AI signal breakdown", "AI sinyal kırılımı")}</span>
                    <strong>{supportScore}/100</strong>
                  </div>

                  {aiPowerBreakdown.map((item) => (
                    <div className="ai-power-bar-v10" key={item.label}>
                      <div>
                        <b>{item.label}</b>
                        <small>{item.value}/{item.max}</small>
                      </div>
                      <em>
                        <i style={{ width: `${Math.min(100, Math.round((item.value / Math.max(1, item.max)) * 100))}%` }}></i>
                      </em>
                      <p>{item.detail}</p>
                    </div>
                  ))}
                </section>

                <section className="ai-power-query-preview-v10">
                  <div className="ai-power-section-head-v10">
                    <span>{trText("Splunk query preview", "Splunk sorgu önizlemesi")}</span>
                    <strong>SPL</strong>
                  </div>

                  {aiPowerQueries.map((item) => (
                    <details key={item.title} open={item.source === "oncoconnect_ai_copilot"}>
                      <summary>
                        <b>{item.title}</b>
                        <small>{item.source}</small>
                      </summary>
                      <pre>{item.query}</pre>
                    </details>
                  ))}
                </section>
              </div>

              <div className="ai-power-evidence-v10">
                <div>
                  <span>{trText("Evidence used by AI", "AI tarafından kullanılan kanıt")}</span>
                  <strong>{trText("Explainable decision path", "Açıklanabilir karar yolu")}</strong>
                </div>

                <ul>
                  {aiPowerEvidence.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="ai-power-actions-v10">
                <button type="button" onClick={runWorkflowSimulation}>
                  {trText("Run AI pipeline simulation", "AI pipeline simülasyonu çalıştır")}
                </button>
                <button type="button" onClick={generateDetailedReport}>
                  {trText("Generate evidence report", "Kanıt raporu üret")}
                </button>
                <button type="button" onClick={exportDetailedReportPdf}>
                  {trText("Export AI report PDF", "AI raporunu PDF dışa aktar")}
                </button>
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>1</b>
                <div>
                  <h2>{trText("Who are you?", "Kimsiniz?")}</h2>
                  <p>{trText("Choose the perspective. The explanation changes based on this.", "Bakış açısını seçin. Açıklama buna göre değişir.")}</p>
                </div>
              </div>

              <div className="patient-choice-grid">
                {Object.entries(roleLabels).map(([key, label]) => (
                  <button
                    key={key}
                    className={role === key ? "selected" : ""}
                    onClick={() => setRole(key)}
                  >
                    {label}
                  </button>
                ))}
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>2</b>
                <div>
                  <h2>{trText("What do you want to learn today?", "Bugün ne öğrenmek istiyorsunuz?")}</h2>
                  <p>{trText("Choose one simple goal.", "Basit bir hedef seçin.")}</p>
                </div>
              </div>

              <div className="patient-choice-grid two">
                {Object.entries(goalLabels).map(([key, label]) => (
                  <button
                    key={key}
                    className={goal === key ? "selected" : ""}
                    onClick={() => setGoal(key)}
                  >
                    {label}
                  </button>
                ))}
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>3</b>
                <div>
                  <h2>{trText("Select data context", "Veri bağlamını seçin")}</h2>
                  <p>{trText("City, age group and cancer type are read from the public dataset when available.", "Şehir, yaş grubu ve kanser türü mümkün olduğunda kamu veri setinden okunur.")}</p>
                </div>
              </div>

              <div className="patient-dropdown-grid">
                <label>
                  <span>{trText("City / country", "Şehir / ülke")}</span>
                  <select value={city} onChange={(e) => setCity(e.target.value)}>
                    <option value="">{trText("All locations", "Tüm konumlar")}</option>
                    {(cityOptions.length ? cityOptions : ["İstanbul", "Ankara", "İzmir", "Türkiye"]).map((item) => (
                      <option key={item} value={item}>{item}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{trText("Age group", "Yaş grubu")}</span>
                  <select value={ageGroup} onChange={(e) => setAgeGroup(e.target.value)}>
                    {ageOptions.map((item) => (
                      <option key={item} value={item}>{item}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{trText("Cancer type", "Kanser türü")}</span>
                  <select value={cancerType} onChange={(e) => setCancerType(e.target.value)}>
                    {Object.entries(cancerLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{trText("Treatment stage", "Tedavi aşaması")}</span>
                  <select value={treatmentStage} onChange={(e) => setTreatmentStage(e.target.value)}>
                    {Object.entries(stageLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{trText("Main concern today", "Bugünkü ana endişe")}</span>
                  <select value={mainConcern} onChange={(e) => setMainConcern(e.target.value)}>
                    {Object.entries(concernLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>

                <label>
                  <span>{trText("Real-world case scenario", "Gerçek dünya vaka senaryosu")}</span>
                  <select value={caseScenario} onChange={(e) => setCaseScenario(e.target.value)}>
                    {Object.entries(caseScenarioLabels).map(([key, label]) => (
                      <option key={key} value={key}>{label}</option>
                    ))}
                  </select>
                </label>
              </div>

              <div className="copilot-redflag-panel-v1">
                <div>
                  <strong>{trText("Red flag safety check", "Kırmızı bayrak güvenlik kontrolü")}</strong>
                  <p>{trText("Select any urgent warning signs. These do not diagnose; they trigger a safer support recommendation.", "Acil uyarı işaretleri varsa seçin. Bunlar tanı koymaz; daha güvenli destek önerisini tetikler.")}</p>
                </div>

                <label>
                  <input type="checkbox" checked={feverFlag} onChange={(e) => setFeverFlag(e.target.checked)} />
                  <span>{trText("Fever or chills during treatment", "Tedavi sırasında ateş veya titreme")}</span>
                </label>

                <label>
                  <input type="checkbox" checked={breathingFlag} onChange={(e) => setBreathingFlag(e.target.checked)} />
                  <span>{trText("Shortness of breath / chest tightness", "Nefes darlığı / göğüste sıkışma")}</span>
                </label>

                <label>
                  <input type="checkbox" checked={bleedingFlag} onChange={(e) => setBleedingFlag(e.target.checked)} />
                  <span>{trText("Unusual bleeding, severe vomiting or dehydration", "Olağan dışı kanama, şiddetli kusma veya susuz kalma")}</span>
                </label>

                <label>
                  <input type="checkbox" checked={confusionFlag} onChange={(e) => setConfusionFlag(e.target.checked)} />
                  <span>{trText("Confusion, fainting or sudden severe weakness", "Bilinç bulanıklığı, bayılma veya ani ciddi halsizlik")}</span>
                </label>
              </div>
            </div>

            <div className="patient-block">
              <div className="patient-block-title">
                <b>4</b>
                <div>
                  <h2>{trText("How strong are your symptoms today?", "Bugün semptomlarınız ne kadar güçlü?")}</h2>
                  <p>{trText("0 means none. 10 means very strong.", "0 yok anlamına gelir. 10 çok güçlü anlamına gelir.")}</p>
                </div>
              </div>

              <div className="patient-slider-list">
                {[
                  ["Fatigue / weakness", fatigue, setFatigue],
                  ["Pain", pain, setPain],
                  ["Nausea / appetite problem", nausea, setNausea],
                  ["Fear, worry or low mood", mood, setMood]
                ].map(([label, value, setter]) => (
                  <label key={label}>
                    <div>
                      <span>{label}</span>
                      <strong>{value}/10</strong>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="10"
                      value={value}
                      onChange={(e) => setter(Number(e.target.value))}
                    />
                  </label>
                ))}
              </div>

              <div className="patient-primary-actions copilot-primary-actions-v4">
                <button
                  type="button"
                  className={activeInsight === "ai" ? "is-running" : ""}
                  onClick={() =>
                    runCopilotAction(
                      "ai",
                      trText("AI recommendation generated from current case inputs.", "Mevcut vaka girdilerinden AI önerisi oluşturuldu."),
                      "ai_recommendation"
                    )
                  }
                >
                  <span className="copilot-action-icon-v7">✨</span>
                  <span>{trText("Generate AI recommendation", "AI önerisi oluştur")}</span>
                </button>

                <button
                  type="button"
                  className={activeInsight === "risk" ? "is-running" : ""}
                  onClick={() =>
                    runCopilotAction(
                      "risk",
                      trText("Risk assessment recalculated with symptoms, red flags and data context.", "Risk değerlendirmesi semptomlar, kırmızı bayraklar ve veri bağlamıyla yeniden hesaplandı."),
                      "risk_assessment"
                    )
                  }
                >
                  <span className="copilot-action-icon-v7">🛡️</span>
                  <span>{trText("Run risk assessment", "Risk değerlendirmesi çalıştır")}</span>
                </button>

                <button
                  type="button"
                  className={activeInsight === "note" ? "is-running" : ""}
                  onClick={() =>
                    runCopilotAction(
                      "note",
                      trText("Doctor visit note created for review and copy.", "Doktor görüşmesi notu inceleme ve kopyalama için oluşturuldu."),
                      "doctor_note"
                    )
                  }
                >
                  <span className="copilot-action-icon-v7">📝</span>
                  <span>{trText("Create doctor note", "Doktor notu oluştur")}</span>
                </button>

                <button
                  type="button"
                  className={activeInsight === "splunk" ? "is-running" : ""}
                  onClick={sendEvent}
                >
                  <span className="copilot-action-icon-v7">📡</span>
                  <span>{trText("Send to Splunk", "Splunk’a gönder")}</span>
                </button>

                <button
                  type="button"
                  className={activeInsight === "simulation" ? "is-running" : ""}
                  onClick={runWorkflowSimulation}
                >
                  <span className="copilot-action-icon-v7">▶️</span>
                  <span>{trText("Run live simulation", "Canlı simülasyon çalıştır")}</span>
                </button>

                <button
                  type="button"
                  className={activeInsight === "report" ? "is-running" : ""}
                  onClick={generateDetailedReport}
                >
                  <span className="copilot-action-icon-v7">📊</span>
                  <span>{trText("Generate detailed report", "Detaylı rapor üret")}</span>
                </button>

                <button
                  type="button"
                  onClick={exportDetailedReportPdf}
                >
                  <span className="copilot-action-icon-v7">📄</span>
                  <span>{trText("Export PDF", "PDF dışa aktar")}</span>
                </button>
              </div>
            </div>
          </div>

          <aside className="patient-output-panel">
            <div className="copilot-action-status-v4">
              <div>
                <span>{trText("Last Copilot action", "Son Copilot aksiyonu")}</span>
                <strong>{lastCopilotAction}</strong>
              </div>
              <small>{trText("Buttons update the right-side result panel and event trace.", "Butonlar sağdaki sonuç panelini ve olay izini günceller.")}</small>
            </div>

            <div className="copilot-execution-console-v5">
              <div className="copilot-console-head-v5">
                <span>{trText("Execution console", "Çalışma konsolu")}</span>
                <strong>{trText("Where did the action run?", "Aksiyon nerede çalıştı?")}</strong>
              </div>

              <div className="copilot-console-pipeline-v5">
                <div className={["ai", "risk", "note", "splunk", "simulation", "report"].includes(activeInsight) ? "active" : ""}>
                  <small>{trText("Input", "Girdi")}</small>
                  <b>{selectedScenarioLabel}</b>
                </div>

                <div className={["risk", "splunk", "simulation", "report"].includes(activeInsight) ? "active" : ""}>
                  <small>{trText("Risk engine", "Risk motoru")}</small>
                  <b>{supportScore}/100</b>
                </div>

                <div className={["note", "splunk", "simulation", "report"].includes(activeInsight) ? "active" : ""}>
                  <small>{trText("Clinical note", "Klinik not")}</small>
                  <b>{trText("Prepared", "Hazırlandı")}</b>
                </div>

                <div className={["splunk", "simulation", "report"].includes(activeInsight) ? "active" : ""}>
                  <small>{trText("Telemetry", "Telemetri")}</small>
                  <b>{readableTelemetryEvent}</b>
                </div>
              </div>

              <div className="copilot-console-status-v5">
                <b>{trText("Active output", "Aktif çıktı")}</b>
                <span>{activeInsight}</span>
                <p>{lastCopilotAction}</p>
              </div>
            </div>

            <div className={`patient-score-card ${supportClass}`}>
              <span>{trText("Support priority", "Destek önceliği")}</span>
              <strong>{supportScore}</strong>
              <b>{clinicalRiskLevel}</b>
              <p>
                {safetyMessage}
              </p>
              {redFlags.length > 0 && (
                <ul className="copilot-redflag-list-v1">
                  {redFlags.map((flag) => <li key={flag}>{flag}</li>)}
                </ul>
              )}
            </div>

            <div className="patient-data-card">
              <span>{trText("Dataset signal", "Veri seti sinyali")}</span>
              <h2>{city || "All locations"} · {ageGroup}</h2>
              <div className="patient-data-grid">
                <div>
                  <small>{trText("Rows", "Satırlar")}</small>
                  <strong>{filteredRows.length}</strong>
                </div>
                <div>
                  <small>{trText("Incidence", "İnsidans")}</small>
                  <strong>{incidenceAvg ? incidenceAvg.toFixed(1) : "-"}</strong>
                </div>
                <div>
                  <small>{trText("Mortality", "Mortalite")}</small>
                  <strong>{mortalityAvg ? mortalityAvg.toFixed(1) : "-"}</strong>
                </div>
                <div>
                  <small>{trText("5-year survival", "5 yıllık sağkalım")}</small>
                  <strong>{survivalAvg ? `${survivalAvg.toFixed(0)}%` : "-"}</strong>
                </div>
              </div>
            </div>

            <div className="copilot-analytics-card-v3">
              <div className="copilot-analytics-head-v3">
                <span>{trText("Copilot analytics", "Copilot analitikleri")}</span>
                <h2>{trText("Risk, symptoms and public data signal", "Risk, semptom ve kamu verisi sinyali")}</h2>
                <p>
                  {trText(
                    "A visual summary of the current case flow. This helps judges see how the AI Copilot converts inputs into an explainable support signal.",
                    "Mevcut vaka akışının görsel özeti. Bu bölüm, AI Yardımcı Pilot’un girdileri açıklanabilir bir destek sinyaline nasıl dönüştürdüğünü gösterir."
                  )}
                </p>
              </div>

              <div className="copilot-score-gauge-v3" style={{ "--score": `${supportScore}%` }}>
                <div>
                  <strong>{supportScore}</strong>
                  <span>/100</span>
                </div>
                <p>{clinicalRiskLevel}</p>
              </div>

              <div className="copilot-mini-kpi-grid-v3">
                <div>
                  <small>{trText("Symptom signal", "Semptom sinyali")}</small>
                  <strong>{symptomScore}</strong>
                  <span>/70</span>
                </div>

                <div>
                  <small>{trText("Dataset signal", "Veri seti sinyali")}</small>
                  <strong>{dataSignal}</strong>
                  <span>/30</span>
                </div>

                <div>
                  <small>{trText("Red flags", "Kırmızı bayraklar")}</small>
                  <strong>{redFlags.length}</strong>
                  <span>{trText("selected", "seçildi")}</span>
                </div>
              </div>

              <div className="copilot-bar-chart-v3">
                <div className="copilot-chart-title-v3">
                  {trText("Symptom burden", "Semptom yükü")}
                </div>

                {[
                  [trText("Fatigue", "Yorgunluk"), fatigue],
                  [trText("Pain", "Ağrı"), pain],
                  [trText("Nausea", "Bulantı"), nausea],
                  [trText("Mood", "Ruh hali"), mood]
                ].map(([label, value]) => (
                  <div className="copilot-bar-row-v3" key={label}>
                    <div>
                      <b>{label}</b>
                      <span>{value}/10</span>
                    </div>
                    <i style={{ width: `${value * 10}%` }}></i>
                  </div>
                ))}
              </div>

              <div className="copilot-data-viz-v3">
                <div className="copilot-chart-title-v3">
                  {trText("Public data context", "Kamu verisi bağlamı")}
                </div>

                <div className="copilot-data-pill-row-v3">
                  <div>
                    <small>{trText("Incidence", "İnsidans")}</small>
                    <strong>{incidenceAvg ? incidenceAvg.toFixed(1) : "-"}</strong>
                  </div>

                  <div>
                    <small>{trText("Mortality", "Mortalite")}</small>
                    <strong>{mortalityAvg ? mortalityAvg.toFixed(1) : "-"}</strong>
                  </div>

                  <div>
                    <small>{trText("Survival", "Sağkalım")}</small>
                    <strong>{survivalAvg ? `${survivalAvg.toFixed(0)}%` : "-"}</strong>
                  </div>
                </div>

                <div className="copilot-risk-stack-v3">
                  <span style={{ width: `${Math.min(100, Math.round((symptomScore / 70) * 100))}%` }}>
                    {trText("symptoms", "semptom")}
                  </span>
                  <b style={{ width: `${Math.min(100, Math.round((dataSignal / 30) * 100))}%` }}>
                    {trText("data", "veri")}
                  </b>
                </div>
              </div>

              <div className="copilot-event-timeline-v3">
                <div className="copilot-chart-title-v3">
                  {trText("Event trace", "Olay izi")}
                </div>

                {[
                  [trText("Case scenario selected", "Vaka senaryosu seçildi"), selectedScenarioLabel],
                  [trText("Symptoms scored", "Semptomlar skorlandı"), `${symptomScore}/70`],
                  [trText("Risk level calculated", "Risk seviyesi hesaplandı"), clinicalRiskLevel],
                  [trText("Splunk payload ready", "Splunk payload hazır"), splunkEventPayload.event_type]
                ].map(([title, detail]) => (
                  <div className="copilot-event-row-v3" key={title}>
                    <span></span>
                    <div>
                      <b>{title}</b>
                      <small>{detail}</small>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div className="copilot-playbook-card-v2">
              <span>{trText("Case flow playbook", "Vaka akış playbook’u")}</span>
              <h2>{selectedScenarioLabel}</h2>

              <div className="copilot-playbook-level-v2">
                {scenarioPlan.urgency}
              </div>

              <div className="copilot-playbook-steps-v2">
                <div>
                  <small>{trText("Immediate check", "Hemen kontrol")}</small>
                  <p>{scenarioPlan.immediate}</p>
                </div>

                <div>
                  <small>{trText("Track today", "Bugün takip et")}</small>
                  <p>{scenarioPlan.track}</p>
                </div>

                <div>
                  <small>{trText("Ask doctor", "Doktora sor")}</small>
                  <p>{scenarioPlan.ask}</p>
                </div>
              </div>
            </div>

            <div className="patient-insight-tabs">
              <button className={activeInsight === "ai" ? "active" : ""} onClick={() => setActiveInsight("ai")}>AI</button>
              <button className={activeInsight === "risk" ? "active" : ""} onClick={() => setActiveInsight("risk")}>{trText("Risk", "Risk")}</button>
              <button className={activeInsight === "actions" ? "active" : ""} onClick={() => setActiveInsight("actions")}>{trText("Actions", "Aksiyonlar")}</button>
              <button className={activeInsight === "note" ? "active" : ""} onClick={() => setActiveInsight("note")}>{trText("Note", "Not")}</button>
              <button className={activeInsight === "splunk" ? "active" : ""} onClick={() => setActiveInsight("splunk")}>{trText("Splunk", "Splunk")}</button>
              <button className={activeInsight === "simulation" ? "active" : ""} onClick={() => setActiveInsight("simulation")}>{trText("Simulation", "Simülasyon")}</button>
              <button className={activeInsight === "report" ? "active" : ""} onClick={() => setActiveInsight("report")}>{trText("Report", "Rapor")}</button>
            </div>

            {copilotActionLog.length > 0 && (
              <div className="copilot-action-log-v4">
                <span>{trText("Action trace", "Aksiyon izi")}</span>
                {copilotActionLog.map((item) => (
                  <div key={item.id}>
                    <b>{item.label}</b>
                    <small>{item.time} · {item.type}</small>
                  </div>
                ))}
              </div>
            )}

            {activeInsight === "ai" && (
              <div className="patient-result-card">
                <span>{trText("AI recommendation", "AI önerisi")}</span>
                <h2>{trText("What should I understand?", "Neyi anlamalıyım?")}</h2>
                <p>{aiRecommendation}</p>
                <div className="copilot-scenario-guidance-v2">
                  <strong>{trText("Scenario-specific guidance", "Senaryoya özel yönlendirme")}</strong>
                  <p>{scenarioGuidanceText}</p>
                </div>
              </div>
            )}

            {activeInsight === "risk" && (
              <div className="patient-result-card">
                <span>{trText("Risk assessment", "Risk değerlendirmesi")}</span>
                <h2>{trText("Why this priority?", "Bu öncelik neden?")}</h2>
                <p>
                  {trText("The score combines today’s symptom strength with the selected data context. Higher symptom values and higher public incidence/mortality signal increase the support priority.", "Skor, bugünkü semptom gücünü seçilen veri bağlamıyla birleştirir. Daha yüksek semptom değerleri ve daha yüksek kamu insidans/mortalite sinyali destek önceliğini artırır.")}
                </p>
                <ul>
                  <li>Symptom signal: {symptomScore}/70</li>
                  <li>Dataset signal: {dataSignal}/30</li>
                  <li>Total support priority: {supportScore}/100</li>
                </ul>
              </div>
            )}

            {activeInsight === "actions" && (
              <div className="patient-result-card">
                <span>{trText("Next steps", "Sonraki adımlar")}</span>
                <h2>{trText("What should I do now?", "Şimdi ne yapmalıyım?")}</h2>
                <ul>
                  {actionSteps.map((step) => <li key={step}>{step}</li>)}
                </ul>
              </div>
            )}

            {activeInsight === "note" && (
              <div className="patient-note-card">
                <span>{trText("Doctor visit note", "Doktor görüşmesi notu")}</span>
                <pre>{patientSummary}</pre>

                <div className="patient-note-actions">
                  <button onClick={copySummary}>{trText("Copy note", "Notu kopyala")}</button>
                  <button onClick={() => setActiveInsight("actions")}>{trText("Show next steps", "Sonraki adımları göster")}</button>
                </div>
              </div>
            )}

            {activeInsight === "splunk" && (
              <div className="patient-note-card">
                <span>{trText("Splunk event preview", "Splunk olay önizlemesi")}</span>
                <pre>{JSON.stringify(splunkEventPayload, null, 2)}</pre>

                <div className="patient-note-actions">
                  <button onClick={sendEvent}>{trText("Send support event", "Destek olayını gönder")}</button>
                  <button onClick={() => setActiveInsight("note")}>{trText("Create doctor note", "Doktor notu oluştur")}</button>
                </div>

                {eventSent && (
                  <div className="patient-event-success">
                    {trText("Splunk support event prepared successfully.", "Splunk destek olayı başarıyla hazırlandı.")}
                  </div>
                )}
              </div>
            )}

            {activeInsight === "simulation" && (
              <div className="patient-result-card copilot-simulation-card-v5">
                <span>{trText("Live workflow simulation", "Canlı iş akışı simülasyonu")}</span>
                <h2>{simulationRunning ? trText("Simulation running", "Simülasyon çalışıyor") : trText("Simulation result", "Simülasyon sonucu")}</h2>

                <div className="copilot-simulation-progress-v5">
                  <i style={{ width: `${Math.round((simulationStep / copilotSimulationSteps.length) * 100)}%` }}></i>
                </div>

                <div className="copilot-simulation-steps-v5">
                  {copilotSimulationSteps.map((step, index) => (
                    <div key={step.title} className={simulationStep >= index + 1 ? "done" : ""}>
                      <b>{step.title}</b>
                      <p>{step.detail}</p>
                    </div>
                  ))}
                </div>

                <div className="patient-note-actions">
                  <button type="button" onClick={runWorkflowSimulation}>
                    {trText("Run simulation again", "Simülasyonu tekrar çalıştır")}
                  </button>
                  <button type="button" onClick={generateDetailedReport}>
                    {trText("Generate report from simulation", "Simülasyondan rapor üret")}
                  </button>
                </div>
              </div>
            )}

            {activeInsight === "report" && (
              <div className="patient-note-card copilot-report-card-v5">
                <span>{trText("Detailed analytics report", "Detaylı analitik rapor")}</span>
                <h2>{reportGenerated ? trText("Report generated", "Rapor üretildi") : trText("Report preview", "Rapor önizlemesi")}</h2>

                <div className="copilot-report-kpis-v5">
                  <div>
                    <small>{trText("Support score", "Destek skoru")}</small>
                    <strong>{supportScore}/100</strong>
                  </div>
                  <div>
                    <small>{trText("Symptom signal", "Semptom sinyali")}</small>
                    <strong>{symptomScore}/70</strong>
                  </div>
                  <div>
                    <small>{trText("Dataset signal", "Veri seti sinyali")}</small>
                    <strong>{dataSignal}/30</strong>
                  </div>
                  <div>
                    <small>{trText("Red flags", "Kırmızı bayraklar")}</small>
                    <strong>{redFlags.length}</strong>
                  </div>
                </div>

                <div className="copilot-report-bars-v5">
                  {[
                    [trText("Fatigue", "Yorgunluk"), fatigue],
                    [trText("Pain", "Ağrı"), pain],
                    [trText("Nausea", "Bulantı"), nausea],
                    [trText("Mood", "Ruh hali"), mood]
                  ].map(([label, value]) => (
                    <div key={label}>
                      <span>{label}</span>
                      <i style={{ width: `${value * 10}%` }}></i>
                      <b>{value}/10</b>
                    </div>
                  ))}
                </div>

                <pre>{copilotDetailedReport}</pre>

                <div className="patient-note-actions">
                  <button type="button" onClick={copyDetailedReport}>
                    {trText("Copy detailed report", "Detaylı raporu kopyala")}
                  </button>
                  <button type="button" onClick={exportDetailedReportPdf}>
                    {trText("Export as PDF", "PDF olarak dışa aktar")}
                  </button>
                  <button type="button" onClick={runWorkflowSimulation}>
                    {trText("Run simulation", "Simülasyon çalıştır")}
                  </button>
                </div>
              </div>
            )}

            <div className="patient-result-card">
              <span>{trText("Doctor visit preparation", "Doktor görüşmesine hazırlık")}</span>
              <h2>{trText("Questions to ask", "Sorulacak sorular")}</h2>
              <ul>
                {doctorQuestions.map((question) => <li key={question}>{question}</li>)}
              </ul>
            </div>
          </aside>

        <section className="landing-data-lab">
          <div className="landing-data-head">
            <LandingMapPreviewCompact />

            <p className="csv-kicker">{trText("LIVE CANCER DATA LAB", "CANLI KANSER VERİ LABORATUVARI")}</p>
            <h2>{trText("Interactive cancer burden explorer", "İnteraktif kanser yükü keşif aracı")}</h2>
            <p>
              {trText("Explore cases, deaths and 5-year survival by cancer type, sex and age group. This turns the CSV layer into an interactive public data dashboard.", "Kanser türü, cinsiyet ve yaş grubuna göre vakaları, ölümleri ve 5 yıllık sağkalımı keşfedin. Bu, CSV katmanını interaktif bir kamu veri paneline dönüştürür.")}
            </p>

            {mergedCancerRows.length > 5 && (
              <button
                type="button"
                className="landing-header-showmore-v57"
                onClick={() => setShowAllLandingDataRows((value) => !value)}
              >
                {showAllLandingDataRows
                  ? "Show less — first 5 key indicators"
                  : `Show ${mergedCancerRows.length - 5} more indicators`}
              </button>
            )}
          </div>

          <div className="landing-data-filters">
            <label>
              <span>{trText("Metric", "Metrik")}</span>
              <select defaultValue="cases">
                <option value="cases">{trText("New cases", "Yeni vakalar")}</option>
                <option value="deaths">{trText("Deaths", "Ölümler")}</option>
                <option value="survival">{trText("5-year survival", "5 yıllık sağkalım")}</option>
              </select>
            </label>

            <label>
              <span>{trText("Sex", "Cinsiyet")}</span>
              <select defaultValue="All">
                <option>{trText("All", "Tümü")}</option>
                <option>Erkek</option>
                <option>Kadın</option>
              </select>
            </label>

            <label>
              <span>{trText("Age group", "Yaş grubu")}</span>
              <select defaultValue="All">
                <option>{trText("All", "Tümü")}</option>
                <option>0-29</option>
                <option>30-49</option>
                <option>50-69</option>
                <option>70+</option>
              </select>
            </label>

            <label>
              <span>{trText("Cancer type", "Kanser türü")}</span>
              <select defaultValue="All">
                <option>{trText("All", "Tümü")}</option>
                <option>Akciğer</option>
                <option>Meme</option>
                <option>Kolorektal</option>
                <option>Prostat</option>
                <option>Mide</option>
              </select>
            </label>
          </div>

          <div className="landing-data-grid">
            <div className="landing-data-kpi blue">
              <span>Türkiye, 2022</span>
              <strong>240,013</strong>
              <p>{trText("all cancers new cases", "tüm kanserler yeni vakalar")}</p>
            </div>

            <div className="landing-data-kpi orange">
              <span>Türkiye, 2022</span>
              <strong>129,672</strong>
              <p>{trText("all cancers deaths", "tüm kanserler ölümler")}</p>
            </div>

            <div className="landing-data-kpi green">
              <span>Türkiye, 2022</span>
              <strong>67%</strong>
              <p>{trText("estimated 5-year survival signal", "tahmini 5 yıllık sağkalım sinyali")}</p>
            </div>
          </div>

          <div className="landing-chart-area">
            <div className="landing-bars">
              {[
                ["Lung", 92],
                ["Breast", 74],
                ["Colorectum", 61],
                ["Prostate", 48],
                ["Stomach", 39]
              ].map(([name, value]) => (
                <div className="landing-bar-row" key={name}>
                  <div>
                    <b>{name}</b>
                    <span>{value} — burden index</span>
                  </div>
                  <i style={{ width: `${value}%` }}></i>
                </div>
              ))}
            </div>

            <div className="landing-data-note">
              <h3>{trText("How to read this", "Bu nasıl okunmalı")}</h3>
              <p>
                {trText("These values are not personal medical risk scores. They are public-data indicators for awareness, research prioritization and care coordination.", "Bu değerler kişisel tıbbi risk skoru değildir. Farkındalık, araştırma önceliklendirmesi ve bakım koordinasyonu için kamu verisi göstergeleridir.")}
              </p>
              <button
                type="button"
                className="landing-show-more-data-v51"
                onClick={() => setShowAllVisibleCancerRows((value) => !value)}
              >
                {showAllVisibleCancerRows ? "Show only first 5 key indicators" : "Show more indicators"}
              </button>
              <button
                type="button"
                className="landing-data-expand-control-v52"
                onClick={() => setShowAllVisibleCancerRows((value) => !value)}
              >
                {showAllVisibleCancerRows ? "Show less — keep first 5 indicators" : "Show more indicators"}
              </button>
              <button
                type="button"
                className="landing-force-showmore-v53"
                onClick={() => setShowAllVisibleCancerRows((value) => !value)}
              >
                {showAllVisibleCancerRows ? "Show less — keep first 5 indicators" : "Show more indicators"}
              </button>
              <button
              type="button"
              className="landing-final-showmore-v54"
              onClick={() => setShowAllVisibleCancerRows((value) => !value)}
            >
              {showAllVisibleCancerRows ? "Show less — first 5 key indicators" : "Show more indicators"}
            </button>

            <button onClick={() => setPage("map")}>{trText("Open full interactive map", "Tam interaktif haritayı aç")}</button>
            </div>
          </div>
        </section>

        </section>
      </div>
    );
  };







  const LandingMapPreviewCompact = () => {
    const [previewMap, setPreviewMap] = useState("turkiye");
    const [activePin, setActivePin] = useState("ankara");

    const pinData = {
      turkiye: [
        {
          id: "istanbul",
          label: "İstanbul",
          x: 30,
          y: 39,
          title: "İstanbul showcase card",
          metric: "High-population signal",
          value: "Urban monitoring layer",
          text: "Shows how a large metropolitan region can be used as a public-health intelligence point for cancer awareness, screening attention and regional comparison.",
          action: "Open the full map to explore regional indicators."
        },
        {
          id: "ankara",
          label: "Ankara",
          x: 48,
          y: 47,
          title: "Ankara showcase card",
          metric: "Central coordination point",
          value: "National comparison layer",
          text: "Represents a central Türkiye signal where public indicators can be compared with city-level and national-level cancer burden estimates.",
          action: "Use the full map for deeper Türkiye comparison."
        },
        {
          id: "izmir",
          label: "İzmir",
          x: 25,
          y: 58,
          title: "İzmir showcase card",
          metric: "Aegean regional signal",
          value: "Regional outreach layer",
          text: "Demonstrates how a local map pin can open a concise card for cancer burden, outreach planning and patient-support navigation.",
          action: "Click Open full map to inspect all pins."
        }
      ],
      europe: [
        {
          id: "germany",
          label: "Germany",
          x: 52,
          y: 45,
          title: "Germany showcase card",
          metric: "Central Europe benchmark",
          value: "Country comparison layer",
          text: "A benchmark point for comparing public cancer indicators across European countries in the full map experience.",
          action: "Open the full map to compare countries."
        },
        {
          id: "france",
          label: "France",
          x: 42,
          y: 55,
          title: "France showcase card",
          metric: "Western Europe signal",
          value: "Cross-country insight",
          text: "Shows how the same interface can switch from Türkiye city-level signals to European country-level comparison.",
          action: "Use the Europe map layer for country comparison."
        },
        {
          id: "turkiye-europe",
          label: "Türkiye",
          x: 67,
          y: 64,
          title: "Türkiye–Europe bridge",
          metric: "Bridge comparison point",
          value: "Regional context layer",
          text: "Connects the Türkiye layer with the wider European cancer burden comparison map.",
          action: "Open full map for Türkiye and Europe together."
        }
      ]
    };

    const pins = pinData[previewMap];
    const active = pins.find((pin) => pin.id === activePin) || pins[0];

    const switchPreviewMap = (nextMap) => {
      setPreviewMap(nextMap);
      setActivePin(pinData[nextMap][0].id);
    };

    return (
      <section className="landing-map-compact-v51 landing-map-showcase-v57">
        <div className="landing-map-copy-v51">
          <p>{trText("PUBLIC MAP PREVIEW", "KAMU HARİTA ÖNİZLEMESİ")}</p>
          <h2>{trText("Türkiye and Europe map intelligence", "Türkiye ve Avrupa harita zekâsı")}</h2>
          <span>
            Click a glowing pin to open a city or country showcase card. The preview explains what the full public map does before users open it.
          </span>

          <div className="landing-map-switch-v51">
            <button
              type="button"
              className={previewMap === "turkiye" ? "active" : ""}
              onClick={() => switchPreviewMap("turkiye")}
            >
              {trText("Türkiye map", "Türkiye haritası")}
            </button>
            <button
              type="button"
              className={previewMap === "europe" ? "active" : ""}
              onClick={() => switchPreviewMap("europe")}
            >
              {trText("Europe map", "Avrupa haritası")}
            </button>
            <button type="button" onClick={() => setPage("map")}>
              {trText("Open full map", "Tam haritayı aç")}
            </button>
          </div>
        </div>

        <div className="landing-map-stage-v51 landing-map-stage-showcase-v57">
          <img
            src={previewMap === "turkiye" ? "/assets/map-turkiye.png" : "/assets/map-europe.png"}
            alt={previewMap === "turkiye" ? "Türkiye cancer map preview" : "Europe cancer map preview"}
          />

          {pins.map((pin) => (
            <button
              type="button"
              key={pin.id}
              className={`landing-showcase-pin-v57 ${activePin === pin.id ? "active" : ""}`}
              style={{ left: `${pin.x}%`, top: `${pin.y}%` }}
              onClick={() => setActivePin(pin.id)}
            >
              <i></i>
              <span>{pin.label}</span>
            </button>
          ))}

          <div className="landing-map-showcase-card-v57">
            <small>{active.metric}</small>
            <h3>{active.title}</h3>
            <b>{active.value}</b>
            <p>{active.text}</p>
            <button type="button" onClick={() => setPage("map")}>
              {active.action}
            </button>
          </div>
        </div>
      </section>
    );
  };



  const KnowledgeGraphPage = () => {
    const [activeNode, setActiveNode] = useState("copilot");
    const [activeFlow, setActiveFlow] = useState("patient");

    const nodes = [
      {
        id: "patient",
        label: "Patient",
        layer: "Human layer",
        x: 12,
        y: 24,
        type: "human",
        description: "Symptoms, worries, doctor-visit questions and support needs enter the system here."
      },
      {
        id: "caregiver",
        label: "Caregiver",
        layer: "Human layer",
        x: 12,
        y: 67,
        type: "human",
        description: "Family and caregiver signals help coordinate emotional support, reminders and home observations."
      },
      {
        id: "research",
        label: "Research Pulse",
        layer: "Research layer",
        x: 50,
        y: 12,
        type: "research",
        description: "Clinical trials, innovative drugs, funding calls, research articles and care innovation flow into the intelligence layer."
      },
      {
        id: "copilot",
        label: "AI Copilot Core",
        layer: "Reasoning core",
        x: 50,
        y: 45,
        type: "core",
        description: "The central reasoning layer converts patient input, public data and research context into safe guidance and next steps."
      },
      {
        id: "clinician",
        label: "Clinician",
        layer: "Care layer",
        x: 88,
        y: 24,
        type: "care",
        description: "Doctor-ready notes, structured questions and symptom summaries support better clinical conversations."
      },
      {
        id: "ngo",
        label: "NGO / Support Team",
        layer: "Support layer",
        x: 88,
        y: 67,
        type: "care",
        description: "NGOs and support teams receive operational signals for navigation, outreach and psychosocial support."
      },
      {
        id: "dataset",
        label: "Cancer Dataset",
        layer: "Data layer",
        x: 34,
        y: 84,
        type: "data",
        description: "CSV indicators, official source-backed estimates, incidence, mortality, survival and prevalence signals live here."
      },
      {
        id: "map",
        label: "Türkiye–Europe Map",
        layer: "Visualization layer",
        x: 18,
        y: 88,
        type: "output",
        description: "The map visualizes cancer burden patterns across Türkiye and Europe with interactive data streams."
      },
      {
        id: "splunk",
        label: "Splunk Monitoring",
        layer: "Telemetry layer",
        x: 66,
        y: 84,
        type: "system",
        description: "Operational events, risk signals, support-priority changes and data quality activity are streamed for monitoring."
      }
    ];

    const edges = [
      ["patient", "copilot"],
      ["caregiver", "copilot"],
      ["research", "copilot"],
      ["dataset", "copilot"],
      ["copilot", "clinician"],
      ["copilot", "ngo"],
      ["copilot", "splunk"],
      ["copilot", "map"],
      ["dataset", "map"],
      ["research", "dataset"],
      ["splunk", "ngo"],
      ["clinician", "ngo"],
      ["patient", "caregiver"],
      ["dataset", "splunk"]
    ];

    const flows = {
      patient: {
        label: "Patient → AI → Care",
        route: ["patient", "copilot", "clinician", "splunk"],
        summary: "A patient symptom note becomes AI explanation, doctor-ready guidance and telemetry."
      },
      data: {
        label: "Dataset → Map → Monitoring",
        route: ["dataset", "copilot", "map", "splunk"],
        summary: "Cancer indicators power the map and flow into operational monitoring."
      },
      research: {
        label: "Research → AI → Support",
        route: ["research", "copilot", "dataset", "ngo"],
        summary: "Trials, papers, drugs and funding signals enrich the support ecosystem."
      },
      support: {
        label: "Caregiver → NGO → Clinician",
        route: ["caregiver", "copilot", "ngo", "clinician"],
        summary: "Caregiver observations become structured support actions."
      }
    };

    const active = nodes.find((node) => node.id === activeNode) || nodes[0];
    const currentFlow = flows[activeFlow];
    const activeRoute = currentFlow.route;

    const getNode = (id) => nodes.find((node) => node.id === id);

    const isEdgeActive = (from, to) => {
      for (let i = 0; i < activeRoute.length - 1; i++) {
        const a = activeRoute[i];
        const b = activeRoute[i + 1];

        if ((a === from && b === to) || (a === to && b === from)) {
          return true;
        }
      }

      return false;
    };

    return (
      <div className="neural-kg-page">
        <nav className="neural-kg-nav">
          <button type="button" onClick={() => setPage("landing")}>{trText("← Home", "← Ana Sayfa")}</button>
          <button type="button" onClick={() => setPage("map")}>Türkiye–Europe Map</button>
          <button type="button" onClick={() => setPage("copilot")}>{trText("AI Copilot", "AI Yardımcı Pilot")}</button>
          <button type="button" onClick={() => setPage("admin")}>{trText("Admin", "Yönetim")}</button>
        </nav>

        <section className="neural-kg-hero">
          <p>KNOWLEDGE GRAPH</p>
          <h1>Neural cancer-support intelligence network</h1>
          <span>
            A layered, learning-style graph showing how patients, caregivers, datasets,
            research pulse, map intelligence and Splunk telemetry move through OncoConnect AI.
          </span>
        </section>

        <section className="neural-flow-tabs">
          {Object.entries(flows).map(([key, item]) => (
            <button
              type="button"
              key={key}
              className={activeFlow === key ? "active" : ""}
              onClick={() => {
                setActiveFlow(key);
                setActiveNode(item.route[0]);
              }}
            >
              <strong>{item.label}</strong>
              <span>{item.summary}</span>
            </button>
          ))}
        </section>

        <section className="neural-kg-layout">
          <div className="neural-kg-canvas">
            <div className="neural-grid"></div>
            <div className="neural-core-glow"></div>
            <div className="neural-orbit one"></div>
            <div className="neural-orbit two"></div>
            <div className="neural-orbit three"></div>

            <svg className="neural-lines" viewBox="0 0 1000 680" preserveAspectRatio="none">
              {edges.map(([from, to]) => {
                const a = getNode(from);
                const b = getNode(to);

                if (!a || !b) return null;

                const x1 = a.x * 10;
                const y1 = a.y * 6.8;
                const x2 = b.x * 10;
                const y2 = b.y * 6.8;
                const activeEdge = isEdgeActive(from, to);

                return (
                  <g key={`${from}-${to}`}>
                    <line
                      x1={x1}
                      y1={y1}
                      x2={x2}
                      y2={y2}
                      className={activeEdge ? "active" : ""}
                    />
                    {activeEdge && (
                      <>
                        <circle className="neural-particle cyan" r="5">
                          <animateMotion
                            dur="2.1s"
                            repeatCount="indefinite"
                            path={`M ${x1} ${y1} L ${x2} ${y2}`}
                          />
                        </circle>
                        <circle className="neural-particle violet" r="3">
                          <animateMotion
                            dur="2.9s"
                            repeatCount="indefinite"
                            path={`M ${x1} ${y1} L ${x2} ${y2}`}
                          />
                        </circle>
                      </>
                    )}
                  </g>
                );
              })}
            </svg>

            {nodes.map((node) => (
              <button
                type="button"
                key={node.id}
                className={`neural-node ${node.type} ${activeNode === node.id ? "selected" : ""} ${activeRoute.includes(node.id) ? "route" : ""}`}
                style={{ left: `${node.x}%`, top: `${node.y}%` }}
                onMouseEnter={() => setActiveNode(node.id)}
                onFocus={() => setActiveNode(node.id)}
                onClick={() => setActiveNode(node.id)}
              >
                <i></i>
                <strong>{node.label}</strong>
                <span>{node.layer}</span>
              </button>
            ))}

            <div className="neural-flow-caption">
              <span>Active intelligence route</span>
              <strong>{activeRoute.map((id) => getNode(id)?.label || id).join(" → ")}</strong>
            </div>
          </div>

          <aside className="neural-kg-side">
            <div className={`neural-detail-card ${active.type}`}>
              <span>{active.layer}</span>
              <h2>{active.label}</h2>
              <p>{active.description}</p>

              <div className="neural-detail-metrics">
                <div>
                  <small>Node type</small>
                  <strong>{active.type}</strong>
                </div>
                <div>
                  <small>Flow status</small>
                  <strong>{activeRoute.includes(active.id) ? "Active" : "Standby"}</strong>
                </div>
              </div>
            </div>

            <div className="neural-route-card">
              <span>Information pathway</span>
              <h3>{currentFlow.label}</h3>
              <p>{currentFlow.summary}</p>

              <ol>
                {activeRoute.map((id, index) => {
                  const node = getNode(id);

                  return (
                    <li key={id}>
                      <b>{String(index + 1).padStart(2, "0")}</b>
                      <div>
                        <strong>{node?.label}</strong>
                        <small>{node?.layer}</small>
                      </div>
                    </li>
                  );
                })}
              </ol>
            </div>
          </aside>
        </section>
      </div>
    );
  };



  const MapPage = () => {
    const [rows, setRows] = useState([]);
    const [officialMapRows, setOfficialMapRows] = useState([]);
    const [status, setStatus] = useState("Loading CSV data...");
    const [view, setView] = useState("turkiye");
    const [metric, setMetric] = useState("incidence");
    const [showMode, setShowMode] = useState("top15");
    const [year, setYear] = useState(2024);
    const [selectedArea, setSelectedArea] = useState(null);
    const [hoveredArea, setHoveredArea] = useState(null);
    const [selectedCancer, setSelectedCancer] = useState("All");
    const [selectedAge, setSelectedAge] = useState("All");
    const [selectedSex, setSelectedSex] = useState("All");

    const parseCsvLine = (line) => {
      const result = [];
      let current = "";
      let insideQuotes = false;

      for (let i = 0; i < line.length; i++) {
        const char = line[i];
        const next = line[i + 1];

        if (char === '"' && insideQuotes && next === '"') {
          current += '"';
          i++;
        } else if (char === '"') {
          insideQuotes = !insideQuotes;
        } else if ((char === "," || char === ";") && !insideQuotes) {
          result.push(current.trim());
          current = "";
        } else {
          current += char;
        }
      }

      result.push(current.trim());
      return result;
    };

    const parseCsv = (text) => {
      const lines = text
        .replace(/\r/g, "")
        .split("\n")
        .filter((line) => line.trim().length > 0);

      if (lines.length < 2) return [];

      const headers = parseCsvLine(lines[0]).map((h) => h.trim());

      return lines.slice(1).map((line) => {
        const values = parseCsvLine(line);
        const row = {};
        headers.forEach((header, index) => {
          row[header] = values[index] ?? "";
        });
        return row;
      });
    };

    const toNumber = (value) => {
      const n = Number(String(value ?? "").replace(",", ".").trim());
      return Number.isFinite(n) ? n : null;
    };

    const normalizeAreaName = (name) => {
      const raw = String(name || "").trim();

      const aliases = {
        "Istanbul": "İstanbul",
        "istanbul": "İstanbul",
        "İstanbul": "İstanbul",
        "Ankara": "Ankara",
        "Izmir": "İzmir",
        "İzmir": "İzmir",
        "Almanya": "Germany",
        "Germany": "Germany",
        "Fransa": "France",
        "France": "France",
        "Italya": "Italy",
        "İtalya": "Italy",
        "Italy": "Italy",
        "Ispanya": "Spain",
        "İspanya": "Spain",
        "Spain": "Spain",
        "Polonya": "Poland",
        "Poland": "Poland",
        "Hollanda": "Netherlands",
        "Netherlands": "Netherlands",
        "Yunanistan": "Greece",
        "Greece": "Greece"
      };

      return aliases[raw] || raw;
    };

    useEffect(() => {
      async function loadCsv() {
        const csvPaths = [
          "/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv",
          "/turkiye_avrupa_kanser_istatistikleri_detayli.csv"
        ];

        for (const path of csvPaths) {
          try {
            const res = await fetch(path);
            if (!res.ok) continue;

            const text = await res.text();
            const parsed = parseCsv(text);

            if (parsed.length) {
              setRows(parsed);
              setStatus(`${parsed.length} CSV rows loaded from ${path}`);
              return;
            }
          } catch {
            // try next path
          }
        }

        try {
          const res = await fetch(`${API}/public/map-data`);
          const data = await res.json();

          const extracted =
            Array.isArray(data) ? data :
            Array.isArray(data.rows) ? data.rows :
            Array.isArray(data.data) ? data.data :
            Array.isArray(data.records) ? data.records :
            [];

          setRows(extracted);
          setStatus(`${extracted.length} rows loaded from backend public endpoint`);
        } catch {
          setRows([]);
          setStatus("No CSV/backend data found. Showing fallback simulation.");
        }
      }

      loadCsv();
    }, []);

    useEffect(() => {
      async function loadOfficialMapRows() {
        try {
          const res = await fetch("/data/official_cancer_sources.csv");
          const text = await res.text();
          const parsed = parseCsv(text);
          setOfficialMapRows(parsed);
        } catch {
          setOfficialMapRows([]);
        }
      }

      loadOfficialMapRows();
    }, []);

    const fallbackRows = [
      { Bolge: "Türkiye", Ulke_Sehir: "İstanbul", Cinsiyet: "Total", Kanser_Turu: "Meme", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 48.2, Yillik_Olum_Hizi_100Bin: 13.4, Bes_Yillik_Sagkalim_Yuzdesi: 82 },
      { Bolge: "Türkiye", Ulke_Sehir: "Ankara", Cinsiyet: "Total", Kanser_Turu: "Akciğer", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 44.8, Yillik_Olum_Hizi_100Bin: 21.1, Bes_Yillik_Sagkalim_Yuzdesi: 37 },
      { Bolge: "Türkiye", Ulke_Sehir: "İzmir", Cinsiyet: "Total", Kanser_Turu: "Kolorektal", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 39.6, Yillik_Olum_Hizi_100Bin: 14.8, Bes_Yillik_Sagkalim_Yuzdesi: 64 },
      { Bolge: "Türkiye", Ulke_Sehir: "Antalya", Cinsiyet: "Total", Kanser_Turu: "Prostat", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 36.5, Yillik_Olum_Hizi_100Bin: 9.2, Bes_Yillik_Sagkalim_Yuzdesi: 89 },
      { Bolge: "Türkiye", Ulke_Sehir: "Trabzon", Cinsiyet: "Total", Kanser_Turu: "Mide", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 31.3, Yillik_Olum_Hizi_100Bin: 15.1, Bes_Yillik_Sagkalim_Yuzdesi: 45 },
      { Bolge: "Europe", Ulke_Sehir: "Germany", Cinsiyet: "Total", Kanser_Turu: "Breast", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 61.4, Yillik_Olum_Hizi_100Bin: 15.7, Bes_Yillik_Sagkalim_Yuzdesi: 86 },
      { Bolge: "Europe", Ulke_Sehir: "France", Cinsiyet: "Total", Kanser_Turu: "Lung", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 52.1, Yillik_Olum_Hizi_100Bin: 24.2, Bes_Yillik_Sagkalim_Yuzdesi: 39 },
      { Bolge: "Europe", Ulke_Sehir: "Italy", Cinsiyet: "Total", Kanser_Turu: "Colorectal", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 47.8, Yillik_Olum_Hizi_100Bin: 16.4, Bes_Yillik_Sagkalim_Yuzdesi: 67 },
      { Bolge: "Europe", Ulke_Sehir: "Spain", Cinsiyet: "Total", Kanser_Turu: "Prostate", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 45.7, Yillik_Olum_Hizi_100Bin: 10.8, Bes_Yillik_Sagkalim_Yuzdesi: 90 },
      { Bolge: "Europe", Ulke_Sehir: "Poland", Cinsiyet: "Total", Kanser_Turu: "All", Yas_Grubu: "All", Yillik_Vaka_Hizi_100Bin: 43.2, Yillik_Olum_Hizi_100Bin: 20.4, Bes_Yillik_Sagkalim_Yuzdesi: 58 }
    ];

    const sourceRows = rows.length ? rows : fallbackRows;

    const normalizedRows = sourceRows.map((row) => ({
      region: String(row.Bolge || row.region || "").trim(),
      area: normalizeAreaName(row.Ulke_Sehir || row.city || row.country || row.area || ""),
      sex: String(row.Cinsiyet || row.sex || "All").trim(),
      cancerType: String(row.Kanser_Turu || row.cancerType || row.cancer_type || "All").trim(),
      ageGroup: String(row.Yas_Grubu || row.ageGroup || row.age_group || "All").trim(),
      incidence: toNumber(row.Yillik_Vaka_Hizi_100Bin ?? row.incidence),
      mortality: toNumber(row.Yillik_Olum_Hizi_100Bin ?? row.mortality),
      survival: toNumber(row.Bes_Yillik_Sagkalim_Yuzdesi ?? row.survival)
    })).filter((row) => row.area);

    const turkiyeCitySet = new Set([
      "adana","adiyaman","afyonkarahisar","agri","amasya","ankara","antalya","artvin","aydin","balikesir",
      "bilecik","bingol","bitlis","bolu","burdur","bursa","canakkale","cankiri","corum","denizli",
      "diyarbakir","edirne","elazig","erzincan","erzurum","eskisehir","gaziantep","giresun","gumushane",
      "hakkari","hatay","isparta","mersin","istanbul","izmir","kars","kastamonu","kayseri","kirklareli",
      "kirsehir","kocaeli","konya","kutahya","malatya","manisa","kahramanmaras","mardin","mugla","mus",
      "nevsehir","nigde","ordu","rize","sakarya","samsun","siirt","sinop","sivas","tekirdag","tokat",
      "trabzon","tunceli","sanliurfa","usak","van","yozgat","zonguldak","aksaray","bayburt","karaman",
      "kirikkale","batman","sirnak","bartin","ardahan","igdir","yalova","karabuk","kilis","osmaniye","duzce"
    ]);

    const ascii = (value) =>
      String(value || "")
        .toLowerCase()
        .replaceAll("ı", "i")
        .replaceAll("ğ", "g")
        .replaceAll("ü", "u")
        .replaceAll("ş", "s")
        .replaceAll("ö", "o")
        .replaceAll("ç", "c")
        .replaceAll("İ", "i");

    const isTurkeyRow = (row) => {
      const region = ascii(row.region);
      const area = ascii(row.area);
      return (
        region.includes("turkiye") ||
        region.includes("turkey") ||
        region.includes("tr") ||
        turkiyeCitySet.has(area)
      );
    };

    const cancerOptions = [
      "All",
      ...Array.from(new Set(normalizedRows.map((row) => row.cancerType).filter(Boolean))).sort()
    ].slice(0, 80);

    const ageOptions = [
      "All",
      ...Array.from(new Set(normalizedRows.map((row) => row.ageGroup).filter(Boolean))).sort()
    ].slice(0, 80);

    const sexOptions = [
      "All",
      ...Array.from(new Set(normalizedRows.map((row) => row.sex).filter(Boolean))).sort()
    ].slice(0, 20);

    const filteredRows = normalizedRows.filter((row) => {
      const viewOk = view === "turkiye" ? isTurkeyRow(row) : !isTurkeyRow(row);
      const cancerOk = selectedCancer === "All" || row.cancerType === selectedCancer;
      const ageOk = selectedAge === "All" || row.ageGroup === selectedAge;
      const sexOk = selectedSex === "All" || row.sex === selectedSex;
      return viewOk && cancerOk && ageOk && sexOk;
    });

    const groupedAreas = useMemo(() => {
      const map = new Map();

      filteredRows.forEach((row) => {
        const current = map.get(row.area) || {
          name: row.area,
          rows: 0,
          incidenceValues: [],
          mortalityValues: [],
          survivalValues: [],
          cancerTypes: new Set(),
          sexValues: new Set(),
          ageGroups: new Set()
        };

        current.rows += 1;
        if (Number.isFinite(row.incidence)) current.incidenceValues.push(row.incidence);
        if (Number.isFinite(row.mortality)) current.mortalityValues.push(row.mortality);
        if (Number.isFinite(row.survival)) current.survivalValues.push(row.survival);
        if (row.cancerType) current.cancerTypes.add(row.cancerType);
        if (row.sex) current.sexValues.add(row.sex);
        if (row.ageGroup) current.ageGroups.add(row.ageGroup);

        map.set(row.area, current);
      });

      const avg = (values) => {
        if (!values.length) return null;
        return values.reduce((a, b) => a + b, 0) / values.length;
      };

      return Array.from(map.values()).map((area) => {
        const simulationMultiplier = 1 + ((year - 2024) * 0.018);

        const incidenceBase = avg(area.incidenceValues);
        const mortalityBase = avg(area.mortalityValues);
        const survivalBase = avg(area.survivalValues);

        return {
          ...area,
          incidence: incidenceBase == null ? null : incidenceBase * simulationMultiplier,
          mortality: mortalityBase == null ? null : mortalityBase * simulationMultiplier,
          survival: survivalBase == null ? null : Math.max(5, Math.min(98, survivalBase - ((year - 2024) * 0.25))),
          cancerTypes: Array.from(area.cancerTypes),
          sexValues: Array.from(area.sexValues),
          ageGroups: Array.from(area.ageGroups)
        };
      });
    }, [filteredRows, year]);

    const metricConfig = {
      incidence: {
        label: trText("New cases", "Yeni vakalar"),
        short: "Vaka",
        field: "incidence",
        suffix: " / 100K",
        explanation: "Annual case-rate signal. Higher values indicate higher observed burden in the selected dataset."
      },
      mortality: {
        label: trText("Deaths", "Ölümler"),
        short: "Ölüm",
        field: "mortality",
        suffix: " / 100K",
        explanation: "Annual mortality-rate signal. It helps identify where care coordination and earlier support matter most."
      },
      survival: {
        label: trText("5-year survival", "5 yıllık sağkalım"),
        short: "Sağkalım",
        field: "survival",
        suffix: "%",
        explanation: "Five-year survival percentage when available. Lower values can guide support and awareness planning."
      }
    };

    const currentMetric = metricConfig[metric];

    const sortedAreas = [...groupedAreas].sort((a, b) => {
      const av = a[metric] ?? -Infinity;
      const bv = b[metric] ?? -Infinity;
      return metric === "survival" ? av - bv : bv - av;
    });

    const visibleAreas = showMode === "top15" ? sortedAreas.slice(0, 15) : sortedAreas;

    const selected =
      selectedArea
        ? groupedAreas.find((area) => area.name === selectedArea) || sortedAreas[0]
        : sortedAreas[0];

    const activeArea = hoveredArea
      ? groupedAreas.find((area) => area.name === hoveredArea) || selected
      : selectedArea
        ? selected
        : null;

    const totalSignal = groupedAreas.reduce((sum, area) => {
      const value = area[metric];
      return sum + (Number.isFinite(value) ? value : 0);
    }, 0);

    const formatMetric = (area, key = metric) => {
      const value = area?.[key];
      if (!Number.isFinite(value)) return "-";
      if (key === "survival") return `${value.toFixed(0)}%`;
      return value.toFixed(1);
    };

    const coordinateSeed = (name) => {
      let hash = 0;
      for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
      return Math.abs(hash);
    };

    const fixedTurkeyCoords = {
      "İstanbul": [25, 50],
      "Istanbul": [25, 50],
      "Ankara": [47, 47],
      "İzmir": [20, 62],
      "Izmir": [20, 62],
      "Bursa": [28, 48],
      "Antalya": [36, 70],
      "Adana": [53, 64],
      "Samsun": [55, 37],
      "Trabzon": [76, 40],
      "Erzurum": [78, 47],
      "Diyarbakır": [72, 61],
      "Diyarbakir": [72, 61],
      "Mersin": [51, 68],
      "Konya": [44, 60],
      "Kayseri": [57, 55],
      "Gaziantep": [65, 64],
      "Aydın": [24, 65],
      "Aydin": [24, 65],
      "Muğla": [26, 72],
      "Mugla": [26, 72],
      "Manisa": [23, 58],
      "Kocaeli": [29, 48],
      "Sakarya": [32, 47],
      "Edirne": [18, 44],
      "Van": [80, 56]
    };

    const fixedEuropeCoords = {
      "Germany": [50, 42],
      "France": [39, 52],
      "Italy": [50, 65],
      "Spain": [28, 67],
      "Poland": [59, 39],
      "Netherlands": [43, 38],
      "Greece": [58, 74],
      "Sweden": [54, 22],
      "Norway": [46, 18],
      "Denmark": [48, 32],
      "Belgium": [42, 43],
      "Austria": [55, 52],
      "Portugal": [22, 68],
      "Ireland": [27, 39],
      "United Kingdom": [32, 36],
      "Türkiye": [70, 75],
      "Turkiye": [70, 75],
      "Turkey": [70, 75]
    };

    const turkeyAutoCoords = [
      [24, 52], [27, 57], [31, 49], [34, 60], [38, 54], [41, 47], [44, 61],
      [48, 53], [51, 46], [54, 58], [58, 51], [61, 62], [64, 55], [67, 46],
      [70, 56], [73, 50], [76, 59], [79, 52], [81, 46], [82, 56],
      [33, 66], [43, 66], [53, 66], [63, 64], [73, 64],
      [36, 40], [46, 39], [56, 38], [66, 39], [76, 40]
    ];

    const europeAutoCoords = [
      [34, 40], [39, 48], [45, 37], [50, 51], [56, 42], [61, 55], [67, 45],
      [43, 62], [52, 67], [31, 58], [58, 30], [48, 27], [70, 61], [38, 32],
      [63, 35], [73, 52], [28, 46], [46, 72], [57, 73], [68, 70]
    ];

    const getCoords = (areaName, index) => {
      const fixed = view === "turkiye" ? fixedTurkeyCoords[areaName] : fixedEuropeCoords[areaName];
      if (fixed) return fixed;

      const list = view === "turkiye" ? turkeyAutoCoords : europeAutoCoords;
      return list[index % list.length];
    };

    return (
      <div className="csv-map-page">
        <nav className="csv-map-nav">
          <button onClick={() => setPage("landing")}>{trText("← Home", "← Ana Sayfa")}</button>
          <button onClick={() => setPage("knowledge")}>{trText("Knowledge Graph", "Bilgi Grafiği")}</button>
          <button onClick={() => setPage("copilot")}>{trText("AI Copilot", "AI Yardımcı Pilot")}</button>
          <button onClick={() => setPage("admin")}>{trText("Admin", "Yönetim")}</button>

          
          <div className="csv-map-lang-select-v106">
            <label>{trText("Language", "Dil")}</label>
            <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">{trText("English", "İngilizce")}</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>

          <div className="csv-map-status">
            <span></span>
            {status}
          </div>
        </nav>

        <section className="csv-map-hero">
          <div>
            <p className="csv-kicker">{trText("INTERACTIVE CANCER MAP", "İNTERAKTİF KANSER HARİTASI")}</p>
            <h1>{trText("Türkiye–Europe cancer burden simulation", "Türkiye–Avrupa kanser yükü simülasyonu")}</h1>
            <p>
              {trText("CSV-powered cancer indicators with interactive pins, metric switching, year simulation, Top 15 / All view and futuristic area cards.", "CSV destekli kanser göstergeleri; interaktif işaretler, metrik değiştirme, yıl simülasyonu, İlk 15 / Tümü görünümü ve futuristik bölge kartları.")}
            </p>
          </div>

          <div className="csv-hero-data">
            <span>{trText("CSV / Public data rows", "CSV / Kamu veri satırları")}</span>
            <strong>{normalizedRows.length}</strong>
            <small>{filteredRows.length} rows after current filters</small>
          </div>
        </section>

        <section className="csv-map-controls">
          <div className="csv-control-row">
            <div className="csv-segment">
              <button className={view === "turkiye" ? "active" : ""} onClick={() => { setView("turkiye"); setSelectedArea(null); }}>
                {trText("Türkiye — 81 cities", "Türkiye — 81 il")}
              </button>
              <button className={view === "europe" ? "active" : ""} onClick={() => { setView("europe"); setSelectedArea(null); }}>
                {trText("Europe", "Avrupa")}
              </button>
              <button className={showMode === "top15" ? "active dark" : ""} onClick={() => setShowMode("top15")}>
                {trText("Show Top 15", "İlk 15’i göster")}
              </button>
              <button className={showMode === "all" ? "active dark" : ""} onClick={() => setShowMode("all")}>
                {trText("Show All", "Tümünü göster")}
              </button>
            </div>

            <div className="csv-year-control">
              <span>{trText("Simulation year", "Simülasyon yılı")}</span>
              <strong>{year}</strong>
              <input min="2024" max="2030" type="range" value={year} onChange={(e) => setYear(Number(e.target.value))} />
            </div>
          </div>

          <div className="csv-metric-row">
            {Object.entries(metricConfig).map(([key, item]) => (
              <button key={key} className={metric === key ? "active" : ""} onClick={() => setMetric(key)}>
                <small>{item.short}</small>
                <strong>{item.label}</strong>
              </button>
            ))}
          </div>

          <div className="csv-filter-row">
            <label>
              <span>{trText("Cancer type", "Kanser türü")}</span>
              <select value={selectedCancer} onChange={(e) => { setSelectedCancer(e.target.value); setSelectedArea(null); }}>
                {cancerOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </label>

            <label>
              <span>{trText("Age group", "Yaş grubu")}</span>
              <select value={selectedAge} onChange={(e) => { setSelectedAge(e.target.value); setSelectedArea(null); }}>
                {ageOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </label>

            <label>
              <span>{trText("Sex", "Cinsiyet")}</span>
              <select value={selectedSex} onChange={(e) => { setSelectedSex(e.target.value); setSelectedArea(null); }}>
                {sexOptions.map((item) => <option key={item} value={item}>{item}</option>)}
              </select>
            </label>
          </div>
        </section>

        <section className="csv-map-layout">
          <div className="csv-map-card">
            <div className="csv-map-summary">
              <div><span>{trText("View", "Görünüm")}</span><strong>{view === "turkiye" ? "Türkiye" : "Europe"}</strong></div>
              <div><span>{trText("Metric", "Metrik")}</span><strong>{currentMetric.label}</strong></div>
              <div><span>{trText("Areas", "Alanlar")}</span><strong>{groupedAreas.length}</strong></div>
              <div><span>{trText("Total signal", "Toplam sinyal")}</span><strong>{totalSignal.toFixed(1)}</strong></div>
            </div>

            <div className={`csv-real-map ${view}`}>
              <div className="csv-map-grid"></div>
              <img
                src={view === "turkiye" ? "/assets/map-turkiye.png" : "/assets/map-europe.png"}
                alt={view === "turkiye" ? trText("Türkiye map", "Türkiye haritası") : trText("Europe map", "Avrupa haritası")}
                onError={(e) => { e.currentTarget.style.display = "none"; }}
              />

              <div className="csv-map-overlay-panel">
                <span>{showMode === "top15" ? "Top 15 mode" : "All areas mode"}</span>
                <strong>{currentMetric.label}</strong>
                <small>{metric === "survival" ? "Lower survival appears first" : "Higher burden appears first"}</small>
              </div>

              <div className="csv-map-year-inline">
                <span>{trText("Simulation year", "Simülasyon yılı")}</span>
                <strong>{year}</strong>
                <input min="2024" max="2030" type="range" value={year} onChange={(e) => setYear(Number(e.target.value))} />
              </div>

              <div className="csv-map-data-stream">
                <span>{trText("CSV + official source stream", "CSV + resmî kaynak akışı")}</span>
                <b>{normalizedRows.length} CSV rows</b>
                <b>{officialMapRows.length} verified rows</b>
                <i></i>
              </div>

              {visibleAreas.map((area, index) => {
                const [x, y] = getCoords(area.name, index);
                const value = area[metric];
                const scale = Math.max(
                  0.82,
                  Math.min(1.65, Number.isFinite(value) ? value / (metric === "survival" ? 55 : 32) : 1)
                );

                return (
                  <button
                    key={`${area.name}-${index}`}
                    className={`csv-map-pin ${activeArea?.name === area.name ? "selected" : ""}`}
                    style={{ left: `${x}%`, top: `${y}%`, "--pin-scale": scale }}
                    onMouseEnter={() => setHoveredArea(area.name)}
                    onMouseLeave={() => {
                      setHoveredArea(null);
                      setSelectedArea(null);
                    }}
                    onFocus={() => setHoveredArea(area.name)}
                    onBlur={() => setHoveredArea(null)}
                    onClick={() => setSelectedArea((prev) => prev === area.name ? null : area.name)}
                  >
                    <i></i>
                    <span>{area.name}</span>
                    <b>{formatMetric(area)}</b>
                  </button>
                );
              })}

              {activeArea && (
                <div className="csv-floating-card">
                  <span>{trText("Selected area", "Seçili alan")}</span>
                  <h3>{activeArea.name}</h3>
                  <div><small>{trText("New cases", "Yeni vakalar")}</small><strong>{formatMetric(activeArea, "incidence")}</strong></div>
                  <div><small>{trText("Deaths", "Ölümler")}</small><strong>{formatMetric(activeArea, "mortality")}</strong></div>
                  <div><small>{trText("5-year survival", "5 yıllık sağkalım")}</small><strong>{formatMetric(activeArea, "survival")}</strong></div>
                  
                </div>
              )}
            </div>
          </div>

          <aside className="csv-map-side">
            <div className="csv-selected-card">
              <span>{trText("Selected area", "Seçili alan")}</span>
              <h2>{selected?.name || "Select a pin"}</h2>
              <p>{currentMetric.explanation}</p>

              <div className="csv-selected-metrics">
                <button className={metric === "incidence" ? "active" : ""} onClick={() => setMetric("incidence")}>
                  <small>{trText("Annual cases", "Yıllık vakalar")}</small>
                  <strong>{formatMetric(selected, "incidence")}</strong>
                </button>
                <button className={metric === "mortality" ? "active" : ""} onClick={() => setMetric("mortality")}>
                  <small>{trText("Annual deaths", "Yıllık ölümler")}</small>
                  <strong>{formatMetric(selected, "mortality")}</strong>
                </button>
                <button className={metric === "survival" ? "active" : ""} onClick={() => setMetric("survival")}>
                  <small>{trText("5-year survival", "5 yıllık sağkalım")}</small>
                  <strong>{formatMetric(selected, "survival")}</strong>
                </button>
              </div>

              <div className="csv-source-note">
                <strong>{filteredRows.length}</strong>
                <span>{trText("filtered rows from CSV/backend", "CSV/backend’den filtrelenmiş satırlar")}</span>
              </div>
            </div>

            <div className="csv-rank-card">
              <span>{trText("Ranked areas", "Sıralanmış alanlar")}</span>
              <h3>{currentMetric.label}</h3>

              <div className="csv-rank-list">
                {sortedAreas.slice(0, 12).map((area, index) => (
                  <button key={area.name} className={selected?.name === area.name ? "active" : ""} onClick={() => setSelectedArea(area.name)}>
                    <b>{index + 1}</b>
                    <span>
                      <strong>{area.name}</strong>
                      <small>{area.rows} rows · {area.cancerTypes.slice(0, 2).join(", ") || "mixed"}</small>
                    </span>
                    <em>{formatMetric(area)}</em>
                  </button>
                ))}
              </div>
            </div>
          </aside>
        </section>
      </div>
    );
  };



  const AdminPanel = () => {
    const ADMIN_DATASETS_KEY = "oncoconnect_admin_datasets_v2";
    const ADMIN_PASSWORD_KEY = "oncoconnect_admin_password_v1";
    const PUBLISHED_ROWS_KEY = "oncoconnect_published_cancer_rows_v1";

    const [datasets, setDatasets] = useState(() => {
      try {
        return JSON.parse(localStorage.getItem(ADMIN_DATASETS_KEY) || "[]");
      } catch {
        return [];
      }
    });

    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("");
    const [loading, setLoading] = useState(false);
    const [tab, setTab] = useState("datasets");
    const [previewDataset, setPreviewDataset] = useState(null);
    const [oldPassword, setOldPassword] = useState("");
    const [newPassword, setNewPassword] = useState("");
    const [loginPassword, setLoginPassword] = useState("");
    const [isAdminAuthenticated, setIsAdminAuthenticated] = useState(false);
    const [officialDataUrl, setOfficialDataUrl] = useState("https://ghoapi.azureedge.net/api/NCDMORT3070?$filter=SpatialDimType%20eq%20%27COUNTRY%27%20and%20TimeDim%20ge%202015");
    const [officialDataName, setOfficialDataName] = useState("WHO GHO NCD Mortality Risk Dataset");
    const [officialSourceName, setOfficialSourceName] = useState("WHO_Global_Health_Observatory_OData_API");

    const saveDatasets = (next) => {
      setDatasets(next);
      localStorage.setItem(ADMIN_DATASETS_KEY, JSON.stringify(next));

      const publishedRows = next
        .filter((dataset) => dataset.published)
        .flatMap((dataset) =>
          (dataset.rows || []).map((row) => ({
            ...row,
            _datasetId: dataset.id,
            _datasetName: dataset.name,
            _qualityFlag: dataset.qualityFlag,
            _sourceName: dataset.sourceName,
            _sourceUrl: dataset.sourceUrl
          }))
        );

      localStorage.setItem(PUBLISHED_ROWS_KEY, JSON.stringify(publishedRows));
      window.dispatchEvent(new Event("oncoconnect-admin-data-updated"));
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
      const lines = text
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

    const createDatasetFromCsv = ({ text, name, sourceName = "manual_csv_upload", sourceUrl = "" }) => {
      const parsed = parseCsvText(text);

      if (!parsed.rows.length) {
        throw new Error("CSV has no data rows.");
      }

      return {
        id: `ds_${Date.now()}`,
        name: name || "Manual CSV Dataset",
        originalName: name || "manual_upload.csv",
        uploadedAt: new Date().toISOString(),
        rowCount: parsed.rows.length,
        columns: parsed.columns,
        rows: parsed.rows,
        previewRows: parsed.rows.slice(0, 25),
        qualityFlag: "needs_verification",
        sourceName,
        sourceUrl,
        published: false
      };
    };

    const loadDatasets = () => {
      try {
        const stored = JSON.parse(localStorage.getItem(ADMIN_DATASETS_KEY) || "[]");
        setDatasets(stored);
        setStatus(`Reloaded ${stored.length} dataset(s) from local admin storage.`);
      } catch {
        setStatus("Could not reload local datasets.");
      }
    };

    const uploadDataset = async () => {
      if (!file) {
        setStatus("Please select a CSV file first.");
        return;
      }

      setLoading(true);
      setStatus("Reading CSV locally...");

      try {
        const text = await file.text();
        const dataset = createDatasetFromCsv({
          text,
          name: file.name,
          sourceName: "manual_csv_upload",
          sourceUrl: ""
        });

        const next = [dataset, ...datasets];
        saveDatasets(next);
        setFile(null);
        setStatus(`Uploaded locally: ${dataset.name} (${dataset.rowCount} rows). Review and publish when ready.`);
      } catch (err) {
        setStatus(err.message || "Upload failed.");
      } finally {
        setLoading(false);
      }
    };

    const loadCurrentSiteCsv = async () => {
      setLoading(true);
      setStatus("Loading current map/landing CSV...");

      try {
        const res = await fetch("/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv");

        if (!res.ok) {
          throw new Error("Current CSV file could not be loaded.");
        }

        const text = await res.text();
        const dataset = createDatasetFromCsv({
          text,
          name: "Current Türkiye–Europe Cancer Dataset",
          sourceName: "site_public_csv",
          sourceUrl: "/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv"
        });

        dataset.qualityFlag = "verified_demo";
        dataset.published = true;

        const next = [
          dataset,
          ...datasets.filter((item) => item.sourceUrl !== dataset.sourceUrl)
        ];

        saveDatasets(next);
        setStatus(`Current site CSV loaded and published: ${dataset.rowCount} rows.`);
      } catch (err) {
        setStatus(err.message || "Current CSV load failed.");
      } finally {
        setLoading(false);
      }
    };

    const updateDataset = (id, patch) => {
      const next = datasets.map((dataset) =>
        dataset.id === id ? { ...dataset, ...patch } : dataset
      );

      saveDatasets(next);
      setStatus(patch.published === true ? "Dataset published." : patch.published === false ? "Dataset unpublished." : "Dataset updated.");
    };

    const deleteDataset = (id) => {
      if (!confirm("Delete this dataset from Admin?")) return;

      const next = datasets.filter((dataset) => dataset.id !== id);
      saveDatasets(next);
      setStatus("Dataset deleted.");
    };


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

    const cleanOfficialRows = (rows) => {
      const numericColumns = [
        "Yillik_Vaka_Hizi_100Bin",
        "Yillik_Olum_Hizi_100Bin",
        "Bes_Yillik_Sagkalim_Yuzdesi",
        "incidence",
        "mortality",
        "survival"
      ];

      const requiredAnyColumns = [
        "Bolge",
        "Ulke_Sehir",
        "region",
        "location",
        "Kanser_Turu",
        "cancerType"
      ];

      return rows
        .map((row) => {
          const cleaned = {};

          Object.entries(row || {}).forEach(([key, value]) => {
            if (key.startsWith("_")) return;

            if (numericColumns.includes(key)) {
              cleaned[key] = normalizeNumericCell(value);
              return;
            }

            cleaned[key] = isEmptyCell(value) ? "" : String(value).trim();
          });

          return cleaned;
        })
        .filter((row) => {
          const hasAnyContent = Object.values(row).some((value) => !isEmptyCell(value));
          const hasRequiredSignal = requiredAnyColumns.some((column) => !isEmptyCell(row[column]));

          return hasAnyContent && hasRequiredSignal;
        });
    };

    const prepareOfficialCleanDraft = async () => {
      setLoading(true);
      setStatus("Automation is reading official demo CSV, cleaning empty/NaN values and preparing a publish-ready draft...");

      try {
        const res = await fetch("/data/turkiye_avrupa_kanser_istatistikleri_detayli.csv");

        if (!res.ok) {
          throw new Error("Official demo CSV could not be loaded.");
        }

        const text = await res.text();
        const parsed = parseCsvText(text);
        const cleanedRows = cleanOfficialRows(parsed.rows);

        if (!cleanedRows.length) {
          throw new Error("No valid rows after cleaning. Draft was not created.");
        }

        const removedRows = parsed.rows.length - cleanedRows.length;
        const columns = Array.from(
          cleanedRows.reduce((set, row) => {
            Object.keys(row).forEach((key) => set.add(key));
            return set;
          }, new Set())
        );

        const draft = {
          id: `official_clean_draft_${Date.now()}`,
          name: "Official Clean Cancer Dataset Draft",
          originalName: "official_clean_cancer_dataset_draft.csv",
          uploadedAt: new Date().toISOString(),
          rowCount: cleanedRows.length,
          columns,
          rows: cleanedRows,
          previewRows: cleanedRows.slice(0, 25),
          qualityFlag: removedRows > 0 ? `cleaned_${removedRows}_invalid_rows_removed` : "clean_validated",
          sourceName: "IARC_GLOBOCAN_ECIS_ready_draft",
          sourceUrl: "GLOBOCAN / ECIS / local official demo CSV",
          published: false,
          automationMeta: {
            cleanedAt: new Date().toISOString(),
            inputRows: parsed.rows.length,
            outputRows: cleanedRows.length,
            removedRows,
            emptyValuesBlocked: true,
            nanValuesBlocked: true,
            publishReady: true
          }
        };

        saveDatasets([draft, ...datasets]);
        setTab("datasets");
        setPreviewDataset(draft);
        setStatus(`Clean draft ready: ${cleanedRows.length} valid rows. Removed ${removedRows} invalid/empty rows. Review before publishing.`);
      } catch (err) {
        setStatus(err.message || "Automation clean draft failed.");
      } finally {
        setLoading(false);
      }
    };


    const searchOfficialSourcesAndCreateDraft = async () => {
      setLoading(true);
      setStatus("Searching official sources, validating availability and creating a clean draft...");

      try {
        if (!officialDataUrl.trim()) {
          setStatus("Paste a verified downloadable official CSV/API URL first. No dataset was created.");
          setLoading(false);
          return;
        }

        const response = await fetch(`${API}/admin/official-search`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            officialDataUrl: officialDataUrl.trim(),
            officialDataName: officialDataName.trim() || "Official Cancer Dataset Draft",
            officialSourceName: officialSourceName.trim() || "verified_official_cancer_source"
          })
        });

        const data = await response.json();

        if (!data.success) {
          throw new Error(data.error || "Official source search failed.");
        }

        const dataset = {
          ...data.dataset,
          id: data.dataset?.id || `official_source_draft_${Date.now()}`,
          published: false
        };

        saveDatasets([dataset, ...datasets]);
        setPreviewDataset(dataset);
        setTab("datasets");

        setStatus(
          `${data.message} Source checks: ${(data.sources || [])
            .map((source) => `${source.name}: ${source.reachable ? "reachable" : "not reachable"}`)
            .join(" | ")}`
        );
      } catch (error) {
        setStatus(error.message || "Official source search failed.");
      } finally {
        setLoading(false);
      }
    };

    const runAutoResearch = () => {
      const draft = {
        id: `research_${Date.now()}`,
        name: "Research Pulse Draft Dataset",
        originalName: "research_pulse_draft.json",
        uploadedAt: new Date().toISOString(),
        rowCount: 5,
        columns: ["category", "topic", "priority", "status", "source"],
        rows: [
          { category: "Clinical trials", topic: "Oncology trial monitoring", priority: "High", status: "candidate", source: "admin_generated" },
          { category: "Innovative drugs", topic: "Emerging oncology therapies", priority: "High", status: "candidate", source: "admin_generated" },
          { category: trText("Funding", "Fonlama"), topic: "Cancer research grants", priority: "Medium", status: "candidate", source: "admin_generated" },
          { category: "Papers", topic: "Cancer support AI literature", priority: "Medium", status: "candidate", source: "admin_generated" },
          { category: "Care innovation", topic: "Patient navigation systems", priority: "High", status: "candidate", source: "admin_generated" }
        ],
        previewRows: [],
        qualityFlag: "draft_research",
        sourceName: "admin_research_agent_demo",
        sourceUrl: "",
        published: false
      };

      draft.previewRows = draft.rows;

      saveDatasets([draft, ...datasets]);
      setTab("datasets");
      setStatus("Research draft generated. Review it, then publish if suitable.");
    };

    const runOfficialIngest = () => {
      loadCurrentSiteCsv();
    };

    const clearAllDatasets = () => {
      if (!confirm("Clear all local admin datasets?")) return;

      saveDatasets([]);
      setPreviewDataset(null);
      setStatus("All local admin datasets cleared.");
    };

    const changePassword = () => {
      const current = localStorage.getItem(ADMIN_PASSWORD_KEY) || "admin123";

      if (oldPassword !== current) {
        setStatus("Old password is incorrect. Default is admin123 if you never changed it.");
        return;
      }

      if (!newPassword || newPassword.length < 6) {
        setStatus("New password must be at least 6 characters.");
        return;
      }

      localStorage.setItem(ADMIN_PASSWORD_KEY, newPassword);
      setOldPassword("");
      setNewPassword("");
      setStatus("Admin password changed locally.");
    };


    const handleAdminLogin = () => {
      const currentPassword = localStorage.getItem(ADMIN_PASSWORD_KEY) || "admin123";

      if (loginPassword !== currentPassword) {
        setStatus("Wrong admin password. Default password is admin123 if you never changed it.");
        return;
      }

      setIsAdminAuthenticated(true);
      setLoginPassword("");
      setStatus("");
    };

    const totalRows = datasets.reduce((sum, dataset) => {
      return sum + safeNumber(dataset.rowCount || dataset.rows?.length || 0);
    }, 0);

    const publishedCount = datasets.filter((dataset) => dataset.published).length;
    const publishedRows = datasets
      .filter((dataset) => dataset.published)
      .reduce((sum, dataset) => sum + safeNumber(dataset.rowCount || dataset.rows?.length || 0), 0);

    if (!isAdminAuthenticated) {
      return (
        <div className="admin-login-page-v36 admin-login-command-fix">
          <button
            type="button"
            className="admin-back-home-v36"
            onClick={() => setPage("landing")}
          >
            {trText("← Home", "← Ana Sayfa")}
          </button>

          <div className="admin-login-card-v36">
            <small>ADMIN ACCESS</small>
            <h1>OncoConnect Command Center</h1>
            <p>
              Enter the admin password to control datasets, publishing, sources and demo settings.
            </p>

            <input
              type="password"
              placeholder="Admin password"
              value={loginPassword}
              onChange={(event) => setLoginPassword(event.target.value)}
              onKeyDown={(event) => {
                if (event.key === "Enter") handleAdminLogin();
              }}
            />

            <button type="button" onClick={handleAdminLogin}>
              Login to Admin
            </button>

            {status && <div className="admin-status-v35">{status}</div>}

            <p className="admin-login-hint-v36">
              Default password: <b>admin123</b>
            </p>
          </div>
        </div>
      );
    }

    return (
      <div className="admin-page-v35">
        <header className="admin-topbar-v35">
          <button type="button" onClick={() => setPage("landing")}>
            {lang === "tr" ? "← Ana Sayfa" : "← Home"}
          </button>
          <strong>OncoConnect Admin Command Center</strong>
          <div className="admin-topbar-actions-v40">
            <button type="button" onClick={loadDatasets}>Refresh</button>
            <button
              type="button"
              onClick={() => {
                setIsAdminAuthenticated(false);
                setStatus("");
              }}
            >
              Logout
            </button>
          </div>
        </header>

        <section className="admin-hero-v35">
          <div>
            <p className="eyebrow">DATA OPERATIONS</p>
            <h1>Dataset Governance Console</h1>
            <p>
              Upload, preview, publish, unpublish and control the datasets powering the demo intelligence layer.
            </p>
          </div>
        </section>

        <section className="admin-kpi-grid-v35">
          <div><strong>{datasets.length}</strong><span>Total datasets</span></div>
          <div><strong>{publishedCount}</strong><span>Published</span></div>
          <div><strong>{totalRows}</strong><span>Total rows</span></div>
          <div><strong>{publishedRows}</strong><span>Published rows</span></div>
        </section>

        <section className="admin-tabs-v38">
          {["datasets", "automation", "sources", "settings"].map((item) => (
            <button
              type="button"
              key={item}
              className={tab === item ? "active" : ""}
              onClick={() => setTab(item)}
            >
              {item}
            </button>
          ))}
        </section>

        {status && <section className="admin-status-v35">{status}</section>}

        {tab === "datasets" && (
          <section className="admin-card-v35">
            <h2>Datasets</h2>

            <div className="admin-upload-row-v35">
              <input
                type="file"
                accept=".csv"
                onChange={(event) => setFile(event.target.files?.[0] || null)}
              />
              <button type="button" onClick={uploadDataset} disabled={loading}>
                Upload CSV
              </button>
              <button type="button" onClick={loadCurrentSiteCsv} disabled={loading}>
                Load current map/landing CSV
              </button>
            </div>

            <div className="admin-table-wrap-v35">
              <table>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>{trText("Rows", "Satırlar")}</th>
                    <th>Quality</th>
                    <th>Source</th>
                    <th>Published</th>
                    <th>{trText("Actions", "Aksiyonlar")}</th>
                  </tr>
                </thead>
                <tbody>
                  {datasets.length === 0 && (
                    <tr>
                      <td colSpan="6">No datasets yet. Upload CSV or load current site CSV.</td>
                    </tr>
                  )}

                  {datasets.map((dataset) => (
                    <tr key={dataset.id}>
                      <td>{dataset.name || dataset.originalName}</td>
                      <td>{dataset.rowCount || dataset.rows?.length || 0}</td>
                      <td>{dataset.qualityFlag || "-"}</td>
                      <td>{dataset.sourceName || "-"}</td>
                      <td>{dataset.published ? "Yes" : "No"}</td>
                      <td>
                        <button
                          type="button"
                          onClick={() => setPreviewDataset(dataset)}
                          disabled={loading}
                        >
                          Preview
                        </button>
                        <button
                          type="button"
                          onClick={() => updateDataset(dataset.id, { published: !dataset.published })}
                          disabled={loading}
                        >
                          {dataset.published ? "Unpublish" : "Publish"}
                        </button>
                        <button
                          type="button"
                          onClick={() => deleteDataset(dataset.id)}
                          disabled={loading}
                        >
                          Delete
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {previewDataset && (
              <div className="admin-preview-overlay-v37">
                <div className="admin-preview-modal-v37">
                  <div className="admin-preview-head-v37">
                    <div>
                      <small>Dataset Preview</small>
                      <h2>{previewDataset.name}</h2>
                      <p>
                        Showing first {Math.min(25, previewDataset.rows?.length || 0)} rows from {previewDataset.rowCount || 0} total rows.
                      </p>
                    </div>
                    <button type="button" onClick={() => setPreviewDataset(null)}>Close</button>
                  </div>

                  <div className="admin-preview-table-wrap-v37">
                    <table className="admin-preview-table-v37">
                      <thead>
                        <tr>
                          {(previewDataset.columns || []).map((column) => (
                            <th key={column}>{column}</th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {(previewDataset.previewRows || previewDataset.rows || []).slice(0, 25).map((row, index) => (
                          <tr key={index}>
                            {(previewDataset.columns || []).map((column) => (
                              <td key={column}>{row[column]}</td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            )}
          </section>
        )}

        {tab === "automation" && (
          <section className="admin-card-v35">
            <h2>Automation</h2>
            <p>
              Generate reviewable research drafts or reload the current official demo CSV into Admin control.
            </p>

            <div className="admin-official-url-panel-v40">
              <label>
                <span>Verified downloadable CSV/API URL</span>
                <input
                  type="url"
                  placeholder="https://.../official-cancer-data.csv"
                  value={officialDataUrl}
                  onChange={(event) => setOfficialDataUrl(event.target.value)}
                />
              </label>

              <label>
                <span>Dataset name</span>
                <input
                  type="text"
                  value={officialDataName}
                  onChange={(event) => setOfficialDataName(event.target.value)}
                />
              </label>

              <label>
                <span>Source label</span>
                <input
                  type="text"
                  value={officialSourceName}
                  onChange={(event) => setOfficialSourceName(event.target.value)}
                />
              </label>
            </div>

            <div className="admin-tab-actions-v39">
              <button type="button" onClick={searchOfficialSourcesAndCreateDraft} disabled={loading}>
                Import Official URL & Create Draft
              </button>
              <button type="button" onClick={runAutoResearch} disabled={loading}>
                Generate Research Draft
              </button>
              <button type="button" onClick={prepareOfficialCleanDraft} disabled={loading}>
                Prepare Official Clean Draft
              </button>
              <button type="button" onClick={runOfficialIngest} disabled={loading}>
                Fetch Current Official Demo CSV
              </button>
              <button type="button" onClick={() => setStatus("Published rows are stored locally for map/landing integration.")}>
                Check Published Layer
              </button>
            </div>
          </section>
        )}

        {tab === "sources" && (
          <section className="admin-card-v35">
            <h2>Official Sources</h2>
            <p>Manage source labels for datasets before publishing.</p>

            <div className="admin-tab-actions-v39">
              <button type="button" onClick={loadCurrentSiteCsv} disabled={loading}>
                Register Current CSV Source
              </button>
              <button type="button" onClick={() => setStatus("Source registry is controlled locally in this demo build.")}>
                Validate Source Registry
              </button>
            </div>
          </section>
        )}

        {tab === "settings" && (
          <section className="admin-card-v35">
            <h2>Settings</h2>
            <p>Control local admin password and reset demo data.</p>

            <div className="admin-upload-row-v35">
              <input
                type="password"
                placeholder="Old password"
                value={oldPassword}
                onChange={(event) => setOldPassword(event.target.value)}
              />
              <input
                type="password"
                placeholder="New password"
                value={newPassword}
                onChange={(event) => setNewPassword(event.target.value)}
              />
              <button type="button" onClick={changePassword}>
                Change Password
              </button>
            </div>

            <div className="admin-tab-actions-v39">
              <button type="button" onClick={loadDatasets}>Reload Local Datasets</button>
              <button type="button" onClick={clearAllDatasets}>Clear All Admin Data</button>
              <button type="button" onClick={() => setPage("landing")}>Back Home</button>
            </div>
          </section>
        )}
      </div>
    );
  };



  


const SeasonPocketV105 = ({ kind = "sun" }) => {
  const data = {
    sun: {
      eyebrow: "SUMMER POCKET",
      title: "Sea breeze",
      text: "Tiny sea friends drift through warm summer light.",
      badge: "🌊",
      toys: [
        { label: "Sea", icon: "🌊", scene: "🐠" },
        { label: "Shell", icon: "🐚", scene: "🐚" },
        { label: "Sun", icon: "☀️", scene: "☀️" },
      ],
      minis: ["✨", "🌼", "🐟", "○", "🌿"],
    },
    spring: {
      eyebrow: "SPRING POCKET",
      title: "Blossom breeze",
      text: "Flowers, butterflies and soft hopeful energy.",
      badge: "🌸",
      toys: [
        { label: "Blossom", icon: "🌸", scene: "🌸" },
        { label: "Butterfly", icon: "🦋", scene: "🦋" },
        { label: "Bird", icon: "🐦", scene: "🐦" },
      ],
      minis: ["🌿", "🌼", "🦋", "○", "🌸"],
    },
    rain: {
      eyebrow: "RAIN POCKET",
      title: "Calm rain",
      text: "Soft drops, slow breathing and a quiet sky.",
      badge: "🌧️",
      toys: [
        { label: "Drop", icon: "💧", scene: "💧" },
        { label: "Cloud", icon: "☁️", scene: "☁️" },
        { label: "Umbrella", icon: "☂️", scene: "☂️" },
      ],
      minis: ["💧", "☁️", "○", "🌧️", "🫧"],
    },
    snow: {
      eyebrow: "SNOW POCKET",
      title: "Snow sparkle",
      text: "Quiet snowflakes and a safe winter glow.",
      badge: "❄️",
      toys: [
        { label: "Snow", icon: "❄️", scene: "❄️" },
        { label: "Star", icon: "✦", scene: "✦" },
        { label: "Warm", icon: "🧣", scene: "🧣" },
      ],
      minis: ["❄️", "✦", "○", "☃️", "✨"],
    },
  };

  const content = data[kind] || data.sun;

  return (
    <aside className={`kids-season-pocket-v105 is-${kind}`} aria-label={content.eyebrow}>
      <div className="season-pocket-glow-v105" />

      <div className="season-pocket-eyebrow-v105">{content.eyebrow}</div>

      <div className="season-pocket-head-v105">
        <div className="season-pocket-badge-v105">{content.badge}</div>
        <div>
          <h3>{content.title}</h3>
          <p>{content.text}</p>
        </div>
      </div>

      <div className="season-pocket-scene-v105">
        {content.toys.map((toy, index) => (
          <button
            key={toy.label}
            type="button"
            className={`season-pocket-orb-v105 orb-${index + 1}`}
            aria-label={toy.label}
          >
            {toy.scene}
          </button>
        ))}

        <span className="season-pocket-mini-v105 one">{content.minis[0]}</span>
        <span className="season-pocket-mini-v105 two">{content.minis[1]}</span>
        <span className="season-pocket-mini-v105 three">{content.minis[2]}</span>
        <span className="season-pocket-mini-v105 four">{content.minis[3]}</span>
        <span className="season-pocket-mini-v105 five">{content.minis[4]}</span>
      </div>

      <div className="season-pocket-actions-v105">
        {content.toys.map((toy, index) => (
          <button
            key={toy.label}
            type="button"
            className={index === 0 ? "is-active" : ""}
            aria-label={toy.label}
          >
            {toy.icon} {toy.label}
          </button>
        ))}
      </div>
    </aside>
  );
};


const OncoKidsPage = () => {
    const [activeAge, setActiveAge] = useState("7-10");
    const [activeGuide, setActiveGuide] = useState("hospital");
    const [activeFeeling, setActiveFeeling] = useState(lang === "tr" ? "Meraklı" : "Curious");
    const [checkedQuestions, setCheckedQuestions] = useState([]);
    const [activeStory, setActiveStory] = useState("helpers");
    const [completedMissions, setCompletedMissions] = useState([]);
    const [activeReward, setActiveReward] = useState("calm");
    const [activeSeason, setActiveSeason] = useState("spring");
    const [seasonTaps, setSeasonTaps] = useState([]);
    const [poppedCells, setPoppedCells] = useState([]);
    const [activeCellLesson, setActiveCellLesson] = useState("growth");

    const copy = {
      tr: {
        home: "← Ana Sayfa",
        eyebrow: "ONCO KIDS",
        title: "Çocuklar ve aileler için sakin, umutlu ve güvenli bir alan",
        subtitle: "Tedavi tavsiyesi vermez. Çocukların duygularını konuşmasına, ailelerin açıklama yapmasına ve doktor görüşmesine hazırlanmasına yardımcı olur.",
        parentGuide: "Çocuğuma nasıl anlatırım?",
        parentGuideText: "Yaşa uygun, kısa ve korkutmayan açıklamalarla başlayın. Önce güven verin, sonra sorulara yer açın.",
        storyTitle: "Hikaye diliyle anlat",
        hospitalTitle: "Hastanede bir gün",
        siblingTitle: "Kardeş desteği",
        doctorTitle: "Doktora sorulacak sorular",
        hopeTitle: "Umut Duvarı",
        safety: "Bu sayfa tanı, tedavi veya acil tıbbi yönlendirme sağlamaz. Tıbbi kararlar için çocuk onkolojisi ekibine başvurulmalıdır.",
        checklistDone: "Hazırlandı"
      },
      en: {
        home: "← Home",
        eyebrow: "ONCO KIDS",
        title: "A calm, hopeful and safe space for children and families",
        subtitle: "This space does not give treatment advice. It helps children talk about feelings, helps families explain difficult moments, and prepares questions for doctor visits.",
        parentGuide: "How do I explain this to my child?",
        parentGuideText: "Start with short, calm and age-appropriate words. Give safety first, then leave room for questions.",
        storyTitle: "Explain with story language",
        hospitalTitle: "A day at the hospital",
        siblingTitle: "Sibling support",
        doctorTitle: "Questions for the doctor",
        hopeTitle: "Wall of Hope",
        safety: "This page does not provide diagnosis, treatment or emergency medical guidance. Medical decisions should be discussed with the pediatric oncology team.",
        checklistDone: "Prepared"
      }
    }[lang];

    const ageGuides = {
      "3-6": {
        title: lang === "tr" ? "3–6 yaş" : "Ages 3–6",
        text: lang === "tr"
          ? "Kısa cümleler kullanın: Doktorlar vücudunun daha iyi hissetmesine yardım ediyor. Yanında olacağım."
          : "Use very short sentences: The doctors are helping your body feel better. I will stay with you.",
        tone: lang === "tr" ? "Somut, sakin, tekrar edilebilir." : "Concrete, calm, repeatable."
      },
      "7-10": {
        title: lang === "tr" ? "7–10 yaş" : "Ages 7–10",
        text: lang === "tr"
          ? "Vücudunda iyi çalışmayan bazı hücreler var. Tedavi ekibi onları kontrol altına almaya çalışıyor."
          : "Some cells in the body are not working the way they should. The care team is helping control them.",
        tone: lang === "tr" ? "Basit neden-sonuç, güvenli sorular." : "Simple cause-effect, safe questions."
      },
      "11-14": {
        title: lang === "tr" ? "11–14 yaş" : "Ages 11–14",
        text: lang === "tr"
          ? "Daha dürüst ve açık olun. Bilinmeyen şeyleri saklamak yerine birlikte doktora soracağınızı söyleyin."
          : "Be more honest and clear. Instead of hiding unknowns, say that you will ask the doctor together.",
        tone: lang === "tr" ? "Saygılı, açık, duyguları kabul eden." : "Respectful, clear, validating feelings."
      },
      "15+": {
        title: lang === "tr" ? "15+ yaş" : "Ages 15+",
        text: lang === "tr"
          ? "Kontrol hissini artırın. Randevu sorularını birlikte yazın, seçenekleri ekipten birlikte öğrenin."
          : "Support agency. Write visit questions together and learn options from the care team together.",
        tone: lang === "tr" ? "Katılımcı, mahremiyete saygılı." : "Collaborative, respectful of privacy."
      }
    };

    const storyCards = {
      helpers: {
        icon: "🛡️",
        title: lang === "tr" ? "İlaç yardımcıları" : "Medicine helpers",
        text: lang === "tr"
          ? "Bazı ilaçlar vücuttaki karışık hücrelerle ilgilenmek için çalışan küçük yardımcılar gibi düşünülebilir."
          : "Some medicines can be imagined as small helpers that work with the body when some cells are causing trouble."
      },
      spaceship: {
        icon: "🚀",
        title: lang === "tr" ? "Tarama uzay gemisi" : "The scan spaceship",
        text: lang === "tr"
          ? "Bazı makineler vücudun içinden resim çekmeye yarar. Uzay gemisi gibi ses çıkarabilir ama ekip yanında olur."
          : "Some machines take pictures inside the body. They may sound like a spaceship, but the care team stays nearby."
      },
      brave: {
        icon: "🌈",
        title: lang === "tr" ? "Cesur beden takımı" : "The brave body team",
        text: lang === "tr"
          ? "Cesur olmak hiç korkmamak değildir. Korkunca söylemek de cesur bir davranıştır."
          : "Being brave does not mean never feeling scared. Telling someone when you are scared is brave too."
      }
    };

    const hospitalSteps = [
      {
        key: "hospital",
        icon: "🏥",
        title: lang === "tr" ? "Hastaneye gelmek" : "Arriving at hospital",
        text: lang === "tr" ? "Bugün neler olacağını ekipten öğrenebiliriz." : "We can ask the team what will happen today."
      },
      {
        key: "blood",
        icon: "🩸",
        title: lang === "tr" ? "Kan testi" : "Blood test",
        text: lang === "tr" ? "Kısa sürebilir. Derin nefes almak ve el tutmak yardımcı olabilir." : "It may be quick. Breathing slowly and holding a hand can help."
      },
      {
        key: "scan",
        icon: "🛰️",
        title: lang === "tr" ? "Görüntüleme" : "Scan",
        text: lang === "tr" ? "Makine resim çeker. Hareket etmemek gerekebilir." : "The machine takes pictures. Staying still may be needed."
      },
      {
        key: "rest",
        icon: "☁️",
        title: lang === "tr" ? "Dinlenme" : "Rest",
        text: lang === "tr" ? "Yorgun hissetmek normal olabilir. Bunu söylemek önemlidir." : "Feeling tired can happen. It is important to say it."
      }
    ];

    const siblingCards = [
      {
        icon: "💛",
        title: lang === "tr" ? "Dışlanmış hissetmek normal olabilir" : "Feeling left out can happen",
        text: lang === "tr" ? "Kardeşler de ilgiye, açıklamaya ve özel zamana ihtiyaç duyar." : "Siblings also need attention, explanations and special time."
      },
      {
        icon: "🗣️",
        title: lang === "tr" ? "Suçluluk duygusu konuşulmalı" : "Guilt should be talked about",
        text: lang === "tr" ? "Hiçbir çocuk hastalıktan sorumlu değildir. Bunu açıkça söylemek gerekir." : "No child is responsible for the illness. It helps to say this clearly."
      },
      {
        icon: "🤝",
        title: lang === "tr" ? "Küçük görevler iyi gelebilir" : "Small roles can help",
        text: lang === "tr" ? "Kart çizmek, çanta hazırlamak veya kısa mesaj yazmak kardeşi dahil edebilir." : "Drawing a card, packing a small bag or writing a note can include siblings."
      }
    ];

    const doctorQuestions = lang === "tr"
      ? [
          "Bugünkü tedavi veya kontrolün amacı nedir?",
          "Evde hangi belirtilerde sizi aramalıyız?",
          "Beslenme, okul ve oyun için nelere dikkat etmeliyiz?",
          "Enfeksiyondan korunmak için en önemli 3 şey nedir?",
          "Kardeşlere bu süreci nasıl açıklamalıyız?"
        ]
      : [
          "What is the goal of today’s treatment or check-up?",
          "Which symptoms should make us call the care team at home?",
          "What should we know about food, school and play?",
          "What are the top 3 infection-prevention steps?",
          "How should we explain this process to siblings?"
        ];

    const hopeNotes = lang === "tr"
      ? [
          "Bugün bir soru sormak da cesarettir.",
          "Korkunca söylemek güvenli bir adımdır.",
          "Aileler her şeyi tek başına taşımak zorunda değildir.",
          "Küçük rutinler çocuklara güven hissi verir."
        ]
      : [
          "Asking one question today is brave.",
          "Saying I feel scared is a safe step.",
          "Families do not have to carry everything alone.",
          "Small routines can help children feel safe."
        ];

    const seasonOptions = [
      {
        id: "spring",
        icon: "🌸",
        label: lang === "tr" ? "İlkbahar" : "Spring",
        text: lang === "tr" ? "Çiçekler, umut ve yumuşak başlangıç." : "Flowers, hope and a soft beginning."
      },
      {
        id: "rain",
        icon: "🌧️",
        label: lang === "tr" ? "Yağmur" : "Rain",
        text: lang === "tr" ? "Sakin damlalar ve yavaş nefes." : "Calm drops and slow breathing."
      },
      {
        id: "snow",
        icon: "❄️",
        label: lang === "tr" ? "Kış" : "Snow",
        text: lang === "tr" ? "Sessiz kar ve güvenli alan." : "Quiet snow and a safe space."
      },
      {
        id: "sun",
        icon: "☀️",
        label: lang === "tr" ? "Güneş" : "Sunshine",
        text: lang === "tr" ? "Sıcak ışık ve cesaret." : "Warm light and courage."
      }
    ];

    const selectedSeason = seasonOptions.find((item) => item.id === activeSeason) || seasonOptions[0];

    const seasonPlayItems = {
      spring: [
        { id: "sakura", icon: "🌸", label: lang === "tr" ? "Kiraz çiçeği" : "Cherry blossom" },
        { id: "butterfly", icon: "🦋", label: lang === "tr" ? "Kelebek" : "Butterfly" },
        { id: "bird", icon: "🐦", label: lang === "tr" ? "Kuş" : "Bird" }
      ],
      rain: [
        { id: "drop", icon: "💧", label: lang === "tr" ? "Damla yakala" : "Catch a drop" },
        { id: "cloud", icon: "☁️", label: lang === "tr" ? "Bulutu izle" : "Follow cloud" },
        { id: "breath", icon: "🌬️", label: lang === "tr" ? "Nefes al" : "Breathe" }
      ],
      snow: [
        { id: "flake", icon: "❄️", label: lang === "tr" ? "Kar tanesi" : "Snowflake" },
        { id: "star", icon: "✦", label: lang === "tr" ? "Buz yıldızı" : "Ice star" },
        { id: "warm", icon: "🧣", label: lang === "tr" ? "Sıcak kal" : "Stay warm" }
      ],
      sun: [
        { id: "wave", icon: "🌊", label: lang === "tr" ? "Dalgayı izle" : "Watch wave" },
        { id: "shell", icon: "🐚", label: lang === "tr" ? "Deniz kabuğu" : "Shell" },
        { id: "sunray", icon: "☀️", label: lang === "tr" ? "Güneş ışığı" : "Sun ray" }
      ]
    };

    const tapSeasonItem = (item) => {
      const key = `${activeSeason}-${item.id}`;
      setSeasonTaps((current) => current.includes(key) ? current : [...current, key]);
      setActiveReward("hope");
    };

    const missionCards = [
      {
        id: "breath",
        icon: "☁️",
        title: lang === "tr" ? "3 sakin nefes" : "3 calm breaths",
        text: lang === "tr" ? "Bulutu izle ve yavaşça nefes al." : "Follow the cloud and take slow breaths.",
        reward: "calm"
      },
      {
        id: "question",
        icon: "❓",
        title: lang === "tr" ? "Bir soru seç" : "Pick one question",
        text: lang === "tr" ? "Doktora sorabileceğin bir şeyi seç." : "Choose one thing you can ask the doctor.",
        reward: "ask"
      },
      {
        id: "feeling",
        icon: "💛",
        title: lang === "tr" ? "Duygunu adlandır" : "Name a feeling",
        text: lang === "tr" ? "Korku, merak veya yorgunluk söylemek güvenlidir." : "It is safe to say scared, curious or tired.",
        reward: "feel"
      },
      {
        id: "bag",
        icon: "🎒",
        title: lang === "tr" ? "Konfor çantası" : "Comfort bag",
        text: lang === "tr" ? "Su, oyuncak, kulaklık veya not defteri düşün." : "Think of water, a toy, headphones or a notebook.",
        reward: "bag"
      },
      {
        id: "hope",
        icon: "🌈",
        title: lang === "tr" ? "Umut notu" : "Hope note",
        text: lang === "tr" ? "Bugün için küçük ve cesur bir cümle seç." : "Choose one small brave sentence for today.",
        reward: "hope"
      }
    ];

    const rewardCopy = {
      calm: {
        icon: "☁️",
        title: lang === "tr" ? "Sakinlik rozeti" : "Calm badge",
        text: lang === "tr" ? "Yavaş nefes almak bedene güven sinyali verir." : "Slow breathing gives the body a safety signal."
      },
      ask: {
        icon: "❓",
        title: lang === "tr" ? "Soru kahramanı" : "Question hero",
        text: lang === "tr" ? "Soru sormak kontrol hissini güçlendirir." : "Asking questions can build a sense of control."
      },
      feel: {
        icon: "💛",
        title: lang === "tr" ? "Duygu pusulası" : "Feeling compass",
        text: lang === "tr" ? "Duyguyu adlandırmak onu taşımayı kolaylaştırır." : "Naming a feeling can make it easier to carry."
      },
      bag: {
        icon: "🎒",
        title: lang === "tr" ? "Hazırlık çantası" : "Ready bag",
        text: lang === "tr" ? "Küçük rutinler hastane gününü daha tanıdık yapar." : "Small routines can make hospital days feel more familiar."
      },
      hope: {
        icon: "🌈",
        title: lang === "tr" ? "Umut izi" : "Hope trail",
        text: lang === "tr" ? "Küçük umut cümleleri aileye güç verebilir." : "Small hopeful words can support the whole family."
      }
    };

    const toggleMission = (mission) => {
      setActiveReward(mission.reward);
      setCompletedMissions((current) =>
        current.includes(mission.id)
          ? current.filter((item) => item !== mission.id)
          : [...current, mission.id]
      );
    };

    const missionProgress = Math.round((completedMissions.length / missionCards.length) * 100);
    const currentReward = rewardCopy[activeReward] || rewardCopy.calm;

    const cellLessons = [
      {
        id: "growth",
        icon: "🟣",
        title: lang === "tr" ? "Karışık hücre" : "Confused cell",
        text: lang === "tr"
          ? "Bazı hücreler vücudun kurallarını unutmuş gibi davranabilir. Doktorlar bu durumu anlamak için testler kullanır."
          : "Some cells may act as if they forgot the body’s rules. Doctors use tests to understand what is happening."
      },
      {
        id: "divide",
        icon: "🔴",
        title: lang === "tr" ? "Hızlı çoğalma" : "Fast growing cell",
        text: lang === "tr"
          ? "Bazı hücreler gereğinden hızlı çoğalabilir. Tedavi ekibi bu büyümeyi kontrol etmeye çalışır."
          : "Some cells may grow faster than they should. The care team works to help control that growth."
      },
      {
        id: "signal",
        icon: "🟡",
        title: lang === "tr" ? "Sinyal arama" : "Looking for signals",
        text: lang === "tr"
          ? "Kan testleri, görüntüleme ve muayene doktorlara vücuttan gelen işaretleri anlamada yardım eder."
          : "Blood tests, scans and check-ups help doctors understand signals from the body."
      },
      {
        id: "care",
        icon: "🟢",
        title: lang === "tr" ? "Bakım yardımcıları" : "Care helpers",
        text: lang === "tr"
          ? "İlaçlar, hemşireler, doktorlar ve aile birlikte çocuğun daha güvende hissetmesine yardım eder."
          : "Medicines, nurses, doctors and family work together to help the child feel safer."
      }
    ];

    const popCell = (cell) => {
      setActiveCellLesson(cell.id);
      setPoppedCells((current) =>
        current.includes(cell.id)
          ? current
          : [...current, cell.id]
      );
    };

    const activeCell = cellLessons.find((cell) => cell.id === activeCellLesson) || cellLessons[0];

    const toggleQuestion = (item) => {
      setCheckedQuestions((current) =>
        current.includes(item)
          ? current.filter((entry) => entry !== item)
          : [...current, item]
      );
    };

    const selectedAge = ageGuides[activeAge];
    const selectedStory = storyCards[activeStory];
    const selectedHospital = hospitalSteps.find((item) => item.key === activeGuide) || hospitalSteps[0];

    return (
      <div className={`onco-kids-sanctuary-v70 onco-kids-season-${activeSeason}`}>
        <header className="kids-sanctuary-nav-v70">
          <button type="button" onClick={() => setPage("landing")}>{copy.home}</button>

          <div>
            <strong>Onco Kids</strong>
            <span>{lang === "tr" ? "Aile ve çocuk destek alanı" : "Family and child support space"}</span>
          </div>

          <div className="kids-lang-mini-v70">
              <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">{trText("English", "İngilizce")}</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>
        </header>

        <section className="kids-sanctuary-hero-v70">
          <SeasonPocketV105 kind="sun" />
          <SeasonPocketV105 kind="spring" />
          <SeasonPocketV105 kind="rain" />
          <SeasonPocketV105 kind="snow" />



<div className="kids-safe-smiling-sun-v103" aria-hidden="true"><span>😊</span></div>
<div className="kids-sun-sea-real-final" aria-hidden="true">
            <span className="fish one">🐠</span>
            <span className="fish two">🐟</span>
            <span className="shell one">🐚</span>
            <span className="bubble one">🫧</span>
            <span className="bubble two">🫧</span>
            <span className="sun one">☀️</span>
          </div>
          <div className="kids-season-effects-v80" aria-hidden="true">
            {Array.from({ length: 140 }).map((_, index) => {
              const x = (index * 37) % 100;
              const delay = -((index * 17) % 90) / 10;
              const dur = 3.8 + ((index * 11) % 70) / 10;
              const size = 14 + ((index * 7) % 28);
              const drift = -90 + ((index * 19) % 180);
              const rot = (index * 29) % 360;

              return (
                <span
                  key={index}
                  style={{
                    "--i": index,
                    "--x": `${x}%`,
                    "--delay": `${delay}s`,
                    "--dur": `${dur}s`,
                    "--size": `${size}px`,
                    "--drift": `${drift}px`,
                    "--rot": `${rot}deg`
                  }}
                />
              );
            })}
          </div>
          <div className="kids-floating-cloud one"></div>
          <div className="kids-floating-cloud two"></div>
          <div className="kids-floating-star">✨</div>

          <div className="kids-hero-copy-v70">
            <p>{copy.eyebrow}</p>
            <h1>{copy.title}</h1>
            <span>{copy.subtitle}</span>

            <div className="kids-hero-actions-v70">
              <button
                type="button"
                onClick={() => {
                  setActiveGuide("hospital");
                  setTimeout(() => {
                    document.querySelector(".kids-hospital-guide-v70")?.scrollIntoView({
                      behavior: "smooth",
                      block: "start"
                    });
                  }, 80);
                }}
              >
                {lang === "tr" ? "Hastane Gününü Aç" : "Open Hospital Day"}
              </button>
              <button
                type="button"
                onClick={() => {
                  setActiveStory("helpers");
                  setTimeout(() => {
                    document.querySelector(".kids-module-grid-v70")?.scrollIntoView({
                      behavior: "smooth",
                      block: "start"
                    });
                  }, 80);
                }}
              >
                {lang === "tr" ? "Hikaye Dilini Gör" : "View Story Mode"}
              </button>
            </div>

            <div className="kids-season-switch-v78">
              <div className="kids-season-current-v78">
                <span>{selectedSeason.icon}</span>
                <strong>{selectedSeason.label}</strong>
                <small>{selectedSeason.text}</small>
              </div>

              <div className="kids-season-buttons-v78">
                {seasonOptions.map((season) => (
                  <button
                    key={season.id}
                    type="button"
                    className={activeSeason === season.id ? "active" : ""}
                    onClick={() => setActiveSeason(season.id)}
                  >
                    <span>{season.icon}</span>
                    {season.label}
                  </button>
                ))}
              </div>
            </div>
          </div>

          
            <div className={`kids-season-play-v82 ${activeSeason}`}>
              {(seasonPlayItems[activeSeason] || []).map((item, index) => {
                const key = `${activeSeason}-${item.id}`;
                return (
                  <button
                    key={item.id}
                    type="button"
                    className={seasonTaps.includes(key) ? "collected" : ""}
                    onClick={() => tapSeasonItem(item)}
                    style={{ "--n": index }}
                  >
                    <span>{item.icon}</span>
                    <small>{item.label}</small>
                    <b>{seasonTaps.includes(key) ? "✓" : "+"}</b>
                  </button>
                );
              })}
            </div>
<button
            type="button"
            className="lumi-safe-card-v70 lumi-clickable-v74"
            onClick={() => {
              setActiveReward("calm");
              setCompletedMissions((current) =>
                current.includes("breath") ? current : [...current, "breath"]
              );
            }}
            aria-label={lang === "tr" ? "Lumi sakin nefes görevini tamamla" : "Complete Lumi calm breathing mission"}
          >
            <div className="lumi-big-face-v70">😊</div>
            <strong>{lang === "tr" ? "Lumi burada" : "Lumi is here"}</strong>
            <span>
              {lang === "tr"
                ? "Bana tıkla: sakin nefes görevini tamamla ve rozet kazan."
                : "Click me: complete the calm breathing quest and unlock a badge."}
            </span>

            <div className="lumi-mini-actions-v74">
              <i>☁️ {lang === "tr" ? "Nefes" : "Breathe"}</i>
              <i>❓ {lang === "tr" ? "Soru" : "Ask"}</i>
              <i>💛 {lang === "tr" ? "Duygu" : "Feel"}</i>
            </div>
          </button>
        </section>

        <section className="kids-mission-board-v73">
          <div className="kids-mission-copy-v73">
            <small>{lang === "tr" ? "OYUNLAŞTIRILMIŞ ÖĞRENME" : "GAMIFIED LEARNING"}</small>
            <h2>{lang === "tr" ? "Bugünün küçük görevleri" : "Today’s small quests"}</h2>
            <p>
              {lang === "tr"
                ? "Çocuklar küçük, güvenli ve tamamlanabilir görevlerle öğrenir. Her görev bir rozet ve sakinlik adımı kazandırır."
                : "Children learn through small, safe and achievable quests. Each quest unlocks a badge and a calm step."}
            </p>

            <div className="kids-progress-wrap-v73">
              <div>
                <strong>{lang === "tr" ? "Görev ilerlemesi" : "Quest progress"}</strong>
                <span>{completedMissions.length}/{missionCards.length}</span>
              </div>
              <i style={{ width: `${missionProgress}%` }}></i>
            </div>
          </div>

          <div className="kids-mission-grid-v73">
            {missionCards.map((mission) => (
              <button
                key={mission.id}
                type="button"
                className={completedMissions.includes(mission.id) ? "complete" : ""}
                onClick={() => toggleMission(mission)}
              >
                <span>{mission.icon}</span>
                <strong>{mission.title}</strong>
                <small>{mission.text}</small>
                <b>{completedMissions.includes(mission.id) ? "✓" : "+"}</b>
              </button>
            ))}
          </div>

          <div className="kids-reward-card-v73">
            <div>{currentReward.icon}</div>
            <small>{lang === "tr" ? "AÇILAN ROZET" : "UNLOCKED BADGE"}</small>
            <h3>{currentReward.title}</h3>
            <p>{currentReward.text}</p>
          </div>
        </section>

        <section className="kids-cell-lab-v79">
          <div className="kids-cell-copy-v79">
            <small>{lang === "tr" ? "OYUNLA ÖĞRENME" : "LEARN THROUGH PLAY"}</small>
            <h2>{lang === "tr" ? "Hücreleri oyunla keşfet" : "Explore cells through play"}</h2>
            <p>
              {lang === "tr"
                ? "Bu alan basitleştirilmiş bir eğitim simülasyonudur. Gerçek tedavi anlatmaz; çocukların vücutta neler konuşulduğunu daha az korkutucu şekilde anlamasına yardım eder."
                : "This is a simplified learning simulation. It does not explain real treatment; it helps children understand body conversations in a less frightening way."}
            </p>

            <div className="kids-cell-progress-v79">
              <span>{lang === "tr" ? "Keşfedilen hücreler" : "Cells explored"}</span>
              <strong>{poppedCells.length}/{cellLessons.length}</strong>
              <i style={{ width: `${Math.round((poppedCells.length / cellLessons.length) * 100)}%` }}></i>
            </div>
          </div>

          <div className="kids-cell-playground-v79">
            {cellLessons.map((cell, index) => (
              <button
                key={cell.id}
                type="button"
                className={`kids-cell-v79 cell-${index + 1} ${poppedCells.includes(cell.id) ? "popped" : ""} ${activeCellLesson === cell.id ? "active" : ""}`}
                onClick={() => popCell(cell)}
              >
                <span>{cell.icon}</span>
                <b>{poppedCells.includes(cell.id) ? "✨" : "tap"}</b>
              </button>
            ))}

            <div className="kids-cell-orbit-v79"></div>
            <div className="kids-cell-helper-v79">🛡️</div>
          </div>

          <div className="kids-cell-lesson-v79">
            <span>{activeCell.icon}</span>
            <small>{lang === "tr" ? "AKTİF DERS" : "ACTIVE LESSON"}</small>
            <h3>{activeCell.title}</h3>
            <p>{activeCell.text}</p>
            <button type="button" onClick={() => setPoppedCells(cellLessons.map((cell) => cell.id))}>
              {lang === "tr" ? "Tüm hücreleri keşfet" : "Explore all cells"}
            </button>
          </div>

          <div className="kids-video-card-v79">
            <small>{lang === "tr" ? "EĞİTİM VİDEOSU" : "LEARNING VIDEO"}</small>
            <h3>{lang === "tr" ? "Hücreleri daha iyi anlamak" : "Understanding cells better"}</h3>
            <div className="kids-video-frame-v79">
              <iframe
                width="560"
                height="315"
                src="https://www.youtube.com/embed/VEJ6zYD01pM?si=raMxAb8Gkwwo6O-K"
                title="YouTube video player"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerPolicy="strict-origin-when-cross-origin"
                allowFullScreen
              ></iframe>
            </div>
          </div>
        </section>

        <section className="kids-module-grid-v70">
          <div className="kids-module-card-v70 parent-guide">
            <small>{lang === "tr" ? "EBEVEYN REHBERİ" : "PARENT GUIDE"}</small>
            <h2>{copy.parentGuide}</h2>
            <p>{copy.parentGuideText}</p>

            <div className="age-tabs-v70">
              {Object.keys(ageGuides).map((age) => (
                <button
                  key={age}
                  type="button"
                  className={activeAge === age ? "active" : ""}
                  onClick={() => setActiveAge(age)}
                >
                  {age}
                </button>
              ))}
            </div>

            <div className="age-output-v70">
              <strong>{selectedAge.title}</strong>
              <p>{selectedAge.text}</p>
              <span>{selectedAge.tone}</span>
            </div>
          </div>

          <div className="kids-module-card-v70 story-mode">
            <small>{lang === "tr" ? "METAFOR KÜTÜPHANESİ" : "METAPHOR LIBRARY"}</small>
            <h2>{copy.storyTitle}</h2>

            <div className="story-tabs-v70">
              {Object.entries(storyCards).map(([key, item]) => (
                <button
                  key={key}
                  type="button"
                  className={activeStory === key ? "active" : ""}
                  onClick={() => setActiveStory(key)}
                >
                  {item.icon}
                </button>
              ))}
            </div>

            <div className="story-output-v70">
              <div>{selectedStory.icon}</div>
              <strong>{selectedStory.title}</strong>
              <p>{selectedStory.text}</p>
            </div>
          </div>
        </section>

        <section className="kids-hospital-guide-v70">
          <div className="kids-section-title-v70">
            <small>{lang === "tr" ? "İNTERAKTİF AKIŞ" : "INTERACTIVE FLOW"}</small>
            <h2>{copy.hospitalTitle}</h2>
            <p>
              {lang === "tr"
                ? "Çocukların hastane adımlarını daha az korkutucu ve daha anlaşılır görmesine yardımcı olur."
                : "Helps children see hospital steps as less frightening and more understandable."}
            </p>
          </div>

          <div className="hospital-flow-v70">
            <div className="hospital-step-buttons-v70">
              {hospitalSteps.map((item) => (
                <button
                  key={item.key}
                  type="button"
                  className={activeGuide === item.key ? "active" : ""}
                  onClick={() => setActiveGuide(item.key)}
                >
                  <span>{item.icon}</span>
                  {item.title}
                </button>
              ))}
            </div>

            <div className="hospital-stage-v70">
              <div className="hospital-stage-icon-v70">{selectedHospital.icon}</div>
              <h3>{selectedHospital.title}</h3>
              <p>{selectedHospital.text}</p>
              <div className="calm-breath-v70">
                <i></i>
                <span>{lang === "tr" ? "Yavaş nefes al · 1 · 2 · 3" : "Slow breath · 1 · 2 · 3"}</span>
              </div>
            </div>
          </div>
        </section>

        <section className="kids-module-grid-v70 lower">
          <div className="kids-module-card-v70 sibling-support">
            <small>{lang === "tr" ? "KARDEŞ DESTEĞİ" : "SIBLING SUPPORT"}</small>
            <h2>{copy.siblingTitle}</h2>

            <div className="sibling-list-v70">
              {siblingCards.map((item) => (
                <div key={item.title}>
                  <span>{item.icon}</span>
                  <strong>{item.title}</strong>
                  <p>{item.text}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="kids-module-card-v70 doctor-checklist">
            <small>{lang === "tr" ? "RANDEVU HAZIRLIĞI" : "VISIT PREP"}</small>
            <h2>{copy.doctorTitle}</h2>

            <div className="doctor-question-list-v70">
              {doctorQuestions.map((item) => (
                <button
                  key={item}
                  type="button"
                  className={checkedQuestions.includes(item) ? "checked" : ""}
                  onClick={() => toggleQuestion(item)}
                >
                  <span>{checkedQuestions.includes(item) ? "✓" : "+"}</span>
                  {item}
                </button>
              ))}
            </div>

            <div className="prepared-count-v70">
              {copy.checklistDone}: <strong>{checkedQuestions.length}/{doctorQuestions.length}</strong>
            </div>
          </div>
        </section>

        <section className="wall-of-hope-v70">
          <div className="kids-section-title-v70">
            <small>{lang === "tr" ? "UMUT DUVARI" : "WALL OF HOPE"}</small>
            <h2>{copy.hopeTitle}</h2>
          </div>

          <div className="hope-note-grid-v70">
            {hopeNotes.map((note, index) => (
              <div key={note} className={`hope-note-v70 note-${index + 1}`}>
                <span>{["🌈", "☀️", "💛", "🧸"][index]}</span>
                <p>{note}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="kids-safety-note-v70">
          {copy.safety}
        </section>
      </div>
    );
  };



  if (page === "landing") return <LandingPage />;
  if (page === "copilot") return <CopilotPage />;
  if (page === "knowledge") return <KnowledgeGraphPage />;
  if (page === "graph") return <KnowledgeGraphPage />;
  if (page === "map") return <MapPage />;
  if (page === "admin") return <AdminPanel />;
  if (page === "kids") return <OncoKidsPage />;

  return <LandingPage />;
}

export default App;

// FINAL_JOURNEY_TIGHT_OVERRIDE_V135
const ONCOCONNECT_FINAL_JOURNEY_TIGHT_OVERRIDE_V135 = `
html body section.cc-journey-v42 {
  height: auto !important;
  min-height: 132px !important;
  max-height: 150px !important;
  padding: 18px 30px 16px 30px !important;
  margin-top: 14px !important;
  display: grid !important;
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  grid-template-rows: auto auto !important;
  column-gap: 22px !important;
  row-gap: 10px !important;
  align-items: start !important;
  overflow: hidden !important;
}

html body section.cc-journey-v42::before {
  content: none !important;
  display: none !important;
}

html body section.cc-journey-v42 > h3.cc-journey-title-v133 {
  grid-column: 1 / -1 !important;
  grid-row: 1 !important;
  margin: 0 !important;
  padding: 0 !important;
  font-size: 18px !important;
  line-height: 1.05 !important;
  font-weight: 900 !important;
  color: #0f172a !important;
}

html body section.cc-journey-v42 > div {
  grid-row: 2 !important;
  min-width: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  gap: 2px !important;
  margin: 0 !important;
  padding: 0 !important;
}

html body section.cc-journey-v42 > div > b {
  width: 42px !important;
  height: 42px !important;
  min-width: 42px !important;
  min-height: 42px !important;
  margin: 0 0 6px 0 !important;
  padding: 0 !important;
  font-size: 17px !important;
  line-height: 1 !important;
}

html body section.cc-journey-v42 > div > span {
  font-size: 14px !important;
  line-height: 1.02 !important;
  font-weight: 900 !important;
  margin: 0 !important;
}

html body section.cc-journey-v42 > div > small {
  font-size: 10.5px !important;
  line-height: 1.05 !important;
  font-weight: 750 !important;
  margin: 0 !important;
}
`;

if (typeof document !== "undefined") {
  const old = document.getElementById("onco-final-journey-tight-override-v135");
  if (old) old.remove();

  const style = document.createElement("style");
  style.id = "onco-final-journey-tight-override-v135";
  style.textContent = ONCOCONNECT_FINAL_JOURNEY_TIGHT_OVERRIDE_V135;
  document.head.appendChild(style);
}

// JOURNEY_FULL_WIDTH_BALANCE_V136
const ONCOCONNECT_JOURNEY_FULL_WIDTH_BALANCE_V136 = `
html body section.cc-journey-v42 {
  width: 100% !important;
  max-width: none !important;
  box-sizing: border-box !important;
  margin: 14px 0 0 0 !important;
  padding: 18px 28px 18px 28px !important;
  min-height: 132px !important;
  max-height: 150px !important;
  display: grid !important;
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  grid-template-rows: auto auto !important;
  column-gap: 12px !important;
  row-gap: 10px !important;
  align-items: start !important;
  justify-items: stretch !important;
  overflow: hidden !important;
}

html body section.cc-journey-v42::before {
  content: none !important;
  display: none !important;
}

html body section.cc-journey-v42 > h3.cc-journey-title-v133 {
  grid-column: 1 / -1 !important;
  grid-row: 1 !important;
  margin: 0 !important;
  padding: 0 !important;
  font-size: 18px !important;
  line-height: 1.08 !important;
  font-weight: 900 !important;
  color: #0f172a !important;
}

html body section.cc-journey-v42 > div {
  grid-row: 2 !important;
  width: 100% !important;
  min-width: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  gap: 2px !important;
  margin: 0 !important;
  padding: 0 !important;
}

html body section.cc-journey-v42 > div > b {
  width: 44px !important;
  height: 44px !important;
  min-width: 44px !important;
  min-height: 44px !important;
  margin: 0 0 6px 0 !important;
  padding: 0 !important;
  font-size: 18px !important;
  line-height: 1 !important;
}

html body section.cc-journey-v42 > div > span {
  display: block !important;
  font-size: 14.5px !important;
  line-height: 1.04 !important;
  font-weight: 900 !important;
  color: #0f172a !important;
  margin: 0 !important;
  max-width: 100% !important;
}

html body section.cc-journey-v42 > div > small {
  display: block !important;
  font-size: 10.5px !important;
  line-height: 1.08 !important;
  font-weight: 750 !important;
  color: #64748b !important;
  margin: 0 !important;
  max-width: 100% !important;
}
`;

if (typeof document !== "undefined") {
  const old = document.getElementById("onco-journey-full-width-balance-v136");
  if (old) old.remove();

  const style = document.createElement("style");
  style.id = "onco-journey-full-width-balance-v136";
  style.textContent = ONCOCONNECT_JOURNEY_FULL_WIDTH_BALANCE_V136;
  document.head.appendChild(style);
}

// JOURNEY_WORKFLOW_BAND_V137
const ONCOCONNECT_JOURNEY_WORKFLOW_BAND_V137 = `
html body section.cc-journey-v42 {
  width: 100% !important;
  max-width: none !important;
  box-sizing: border-box !important;
  margin: 12px 0 0 0 !important;
  padding: 18px 26px !important;
  min-height: 104px !important;
  max-height: 118px !important;
  display: grid !important;
  grid-template-columns: 250px repeat(5, minmax(0, 1fr)) !important;
  grid-template-rows: 1fr !important;
  column-gap: 18px !important;
  row-gap: 0 !important;
  align-items: center !important;
  justify-items: stretch !important;
  overflow: hidden !important;
}

html body section.cc-journey-v42::before {
  content: none !important;
  display: none !important;
}

html body section.cc-journey-v42 > h3.cc-journey-title-v133 {
  grid-column: 1 !important;
  grid-row: 1 !important;
  margin: 0 !important;
  padding: 0 !important;
  max-width: 230px !important;
  font-size: 19px !important;
  line-height: 1.08 !important;
  font-weight: 950 !important;
  color: #0f172a !important;
}

html body section.cc-journey-v42 > div {
  grid-row: 1 !important;
  min-width: 0 !important;
  width: 100% !important;
  height: 100% !important;
  display: grid !important;
  grid-template-columns: 52px 1fr !important;
  grid-template-rows: auto auto !important;
  column-gap: 10px !important;
  row-gap: 2px !important;
  align-items: center !important;
  justify-content: start !important;
  margin: 0 !important;
  padding: 0 !important;
}

html body section.cc-journey-v42 > div > b {
  grid-column: 1 !important;
  grid-row: 1 / 3 !important;
  width: 46px !important;
  height: 46px !important;
  min-width: 46px !important;
  min-height: 46px !important;
  margin: 0 !important;
  padding: 0 !important;
  font-size: 18px !important;
  line-height: 1 !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}

html body section.cc-journey-v42 > div > span {
  grid-column: 2 !important;
  grid-row: 1 !important;
  display: block !important;
  font-size: 13.8px !important;
  line-height: 1.02 !important;
  font-weight: 950 !important;
  color: #0f172a !important;
  margin: 0 !important;
  white-space: normal !important;
}

html body section.cc-journey-v42 > div > small {
  grid-column: 2 !important;
  grid-row: 2 !important;
  display: block !important;
  font-size: 10px !important;
  line-height: 1.08 !important;
  font-weight: 760 !important;
  color: #64748b !important;
  margin: 0 !important;
  white-space: normal !important;
}

@media (max-width: 1300px) {
  html body section.cc-journey-v42 {
    grid-template-columns: 210px repeat(5, minmax(0, 1fr)) !important;
    column-gap: 12px !important;
    padding-left: 22px !important;
    padding-right: 22px !important;
  }

  html body section.cc-journey-v42 > h3.cc-journey-title-v133 {
    font-size: 17px !important;
  }

  html body section.cc-journey-v42 > div {
    grid-template-columns: 44px 1fr !important;
    column-gap: 8px !important;
  }

  html body section.cc-journey-v42 > div > b {
    width: 40px !important;
    height: 40px !important;
    min-width: 40px !important;
    min-height: 40px !important;
  }
}
`;

if (typeof document !== "undefined") {
  const old = document.getElementById("onco-journey-workflow-band-v137");
  if (old) old.remove();

  const style = document.createElement("style");
  style.id = "onco-journey-workflow-band-v137";
  style.textContent = ONCOCONNECT_JOURNEY_WORKFLOW_BAND_V137;
  document.head.appendChild(style);
}

// JOURNEY_GRID_FIX_AFTER_BAND_V138
const ONCOCONNECT_JOURNEY_GRID_FIX_AFTER_BAND_V138 = `
html body section.cc-journey-v42 {
  width: 100% !important;
  max-width: none !important;
  box-sizing: border-box !important;
  margin: 12px 0 0 0 !important;
  padding: 18px 30px 20px 30px !important;
  min-height: 150px !important;
  max-height: 170px !important;
  display: grid !important;
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  grid-template-rows: auto 1fr !important;
  column-gap: 22px !important;
  row-gap: 14px !important;
  align-items: start !important;
  justify-items: stretch !important;
  overflow: hidden !important;
}

html body section.cc-journey-v42::before {
  content: none !important;
  display: none !important;
}

html body section.cc-journey-v42 > h3.cc-journey-title-v133 {
  grid-column: 1 / -1 !important;
  grid-row: 1 !important;
  margin: 0 !important;
  padding: 0 !important;
  max-width: none !important;
  font-size: 19px !important;
  line-height: 1.08 !important;
  font-weight: 950 !important;
  color: #0f172a !important;
  white-space: nowrap !important;
}

html body section.cc-journey-v42 > div {
  grid-row: 2 !important;
  min-width: 0 !important;
  width: 100% !important;
  height: auto !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  gap: 3px !important;
  margin: 0 !important;
  padding: 0 !important;
}

html body section.cc-journey-v42 > div > b {
  width: 48px !important;
  height: 48px !important;
  min-width: 48px !important;
  min-height: 48px !important;
  margin: 0 0 8px 0 !important;
  padding: 0 !important;
  font-size: 18px !important;
  line-height: 1 !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 999px !important;
}

html body section.cc-journey-v42 > div > span {
  display: block !important;
  font-size: 15px !important;
  line-height: 1.05 !important;
  font-weight: 950 !important;
  color: #0f172a !important;
  margin: 0 !important;
  white-space: normal !important;
  word-break: normal !important;
}

html body section.cc-journey-v42 > div > small {
  display: block !important;
  font-size: 10.8px !important;
  line-height: 1.08 !important;
  font-weight: 760 !important;
  color: #64748b !important;
  margin: 0 !important;
  white-space: normal !important;
  word-break: normal !important;
}
`;

if (typeof document !== "undefined") {
  const ids = [
    "onco-journey-workflow-band-v137",
    "onco-journey-full-width-balance-v136",
    "onco-final-journey-tight-override-v135",
    "onco-journey-grid-fix-after-band-v138"
  ];

  ids.forEach((id) => {
    const old = document.getElementById(id);
    if (old) old.remove();
  });

  const style = document.createElement("style");
  style.id = "onco-journey-grid-fix-after-band-v138";
  style.textContent = ONCOCONNECT_JOURNEY_GRID_FIX_AFTER_BAND_V138;
  document.head.appendChild(style);
}

// JOURNEY_FINAL_COMPACT_V139
const ONCOCONNECT_JOURNEY_FINAL_COMPACT_V139 = `
html body section.cc-journey-v42 {
  margin: 10px 0 0 0 !important;
  padding: 14px 30px 14px 30px !important;
  min-height: 128px !important;
  max-height: 138px !important;
  grid-template-rows: auto auto !important;
  row-gap: 10px !important;
  column-gap: 22px !important;
  align-items: start !important;
  overflow: hidden !important;
}

html body section.cc-journey-v42 > h3.cc-journey-title-v133 {
  margin: 0 !important;
  padding: 0 !important;
  font-size: 18px !important;
  line-height: 1.04 !important;
}

html body section.cc-journey-v42 > div {
  gap: 2px !important;
  margin: 0 !important;
  padding: 0 !important;
}

html body section.cc-journey-v42 > div > b {
  width: 42px !important;
  height: 42px !important;
  min-width: 42px !important;
  min-height: 42px !important;
  margin: 0 0 6px 0 !important;
  font-size: 17px !important;
}

html body section.cc-journey-v42 > div > span {
  font-size: 14px !important;
  line-height: 1.02 !important;
  margin: 0 !important;
}

html body section.cc-journey-v42 > div > small {
  font-size: 10.2px !important;
  line-height: 1.05 !important;
  margin: 0 !important;
}
`;

if (typeof document !== "undefined") {
  const old = document.getElementById("onco-journey-final-compact-v139");
  if (old) old.remove();

  const style = document.createElement("style");
  style.id = "onco-journey-final-compact-v139";
  style.textContent = ONCOCONNECT_JOURNEY_FINAL_COMPACT_V139;
  document.head.appendChild(style);
}

// SPLUNK_LIVE_BADGE_V140
const ONCOCONNECT_SPLUNK_LIVE_BADGE_V140 = `
html body .splunk-live-badge-v140 {
  margin: 10px 0 12px 0 !important;
  padding: 8px 10px !important;
  border-radius: 14px !important;
  border: 1px solid rgba(37, 99, 235, 0.16) !important;
  background: linear-gradient(135deg, rgba(239, 246, 255, 0.95), rgba(248, 250, 252, 0.98)) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 10px !important;
  box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04) !important;
}

html body .splunk-live-badge-v140 span {
  flex: 0 0 auto !important;
  font-size: 10.5px !important;
  line-height: 1 !important;
  font-weight: 900 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: #2563eb !important;
}

html body .splunk-live-badge-v140 b {
  flex: 1 !important;
  min-width: 0 !important;
  text-align: right !important;
  font-size: 11px !important;
  line-height: 1.15 !important;
  font-weight: 850 !important;
  color: #334155 !important;
}

html body .splunk-live-badge-v140.ready {
  border-color: rgba(16, 185, 129, 0.28) !important;
  background: linear-gradient(135deg, rgba(236, 253, 245, 0.92), rgba(248, 250, 252, 0.98)) !important;
}

html body .splunk-live-badge-v140.ready span {
  color: #059669 !important;
}
`;

if (typeof document !== "undefined") {
  const old = document.getElementById("onco-splunk-live-badge-v140");
  if (old) old.remove();

  const style = document.createElement("style");
  style.id = "onco-splunk-live-badge-v140";
  style.textContent = ONCOCONNECT_SPLUNK_LIVE_BADGE_V140;
  document.head.appendChild(style);
}

// FORCE_VISIBLE_SPLUNK_BADGE_V142
const ONCOCONNECT_FORCE_VISIBLE_SPLUNK_BADGE_V142 = `
html body section.cc-evidence-v42.cc-evidence-expanded-v136 {
  overflow: visible !important;
  height: auto !important;
  max-height: none !important;
}

html body section.cc-evidence-v42.cc-evidence-expanded-v136 .splunk-live-badge-v140 {
  display: flex !important;
  visibility: visible !important;
  opacity: 1 !important;
  position: relative !important;
  z-index: 50 !important;
  width: 100% !important;
  box-sizing: border-box !important;
  margin: 10px 0 14px 0 !important;
  padding: 8px 10px !important;
  min-height: 34px !important;
  border-radius: 14px !important;
  border: 1px solid rgba(16, 185, 129, 0.38) !important;
  background: linear-gradient(135deg, rgba(236, 253, 245, 0.98), rgba(240, 253, 250, 0.95)) !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 8px !important;
  box-shadow: 0 8px 18px rgba(15, 23, 42, 0.06) !important;
}

html body section.cc-evidence-v42.cc-evidence-expanded-v136 .splunk-live-badge-v140 span {
  display: inline-block !important;
  visibility: visible !important;
  opacity: 1 !important;
  flex: 0 0 auto !important;
  font-size: 10.5px !important;
  line-height: 1 !important;
  font-weight: 950 !important;
  letter-spacing: 0.10em !important;
  text-transform: uppercase !important;
  color: #059669 !important;
  white-space: nowrap !important;
}

html body section.cc-evidence-v42.cc-evidence-expanded-v136 .splunk-live-badge-v140 b {
  display: inline-block !important;
  visibility: visible !important;
  opacity: 1 !important;
  flex: 1 1 auto !important;
  min-width: 0 !important;
  text-align: right !important;
  font-size: 10.8px !important;
  line-height: 1.12 !important;
  font-weight: 850 !important;
  color: #334155 !important;
  white-space: normal !important;
}
`;

if (typeof document !== "undefined") {
  const old = document.getElementById("onco-force-visible-splunk-badge-v142");
  if (old) old.remove();

  const style = document.createElement("style");
  style.id = "onco-force-visible-splunk-badge-v142";
  style.textContent = ONCOCONNECT_FORCE_VISIBLE_SPLUNK_BADGE_V142;
  document.head.appendChild(style);
}

// DOWNLOAD_REPORT_COMPACT_V148
const ONCOCONNECT_DOWNLOAD_REPORT_COMPACT_V148 = `
html body .onco-download-report-compact-v148 {
  min-height: auto !important;
  height: auto !important;
  padding: 24px 26px !important;
  display: grid !important;
  grid-template-columns: 1fr 108px !important;
  grid-template-rows: auto auto !important;
  column-gap: 18px !important;
  row-gap: 14px !important;
  align-items: start !important;
  overflow: hidden !important;
}

html body .onco-download-report-compact-v148 h1,
html body .onco-download-report-compact-v148 h2,
html body .onco-download-report-compact-v148 h3 {
  margin-top: 0 !important;
  margin-bottom: 10px !important;
  line-height: 1.08 !important;
}

html body .onco-download-report-compact-v148 p {
  margin: 0 0 16px 0 !important;
  line-height: 1.32 !important;
}

html body .onco-download-report-compact-v148 button {
  margin-top: 0 !important;
  margin-bottom: 8px !important;
}

html body .onco-download-report-compact-v148 img,
html body .onco-download-report-compact-v148 svg {
  max-width: 54px !important;
  max-height: 54px !important;
}

html body .onco-download-report-compact-v148 > div,
html body .onco-download-report-compact-v148 > section,
html body .onco-download-report-compact-v148 > article {
  min-height: auto !important;
}

html body .onco-download-report-compact-v148 [class*="include"],
html body .onco-download-report-compact-v148 [class*="report-includes"],
html body .onco-download-report-compact-v148 [class*="includes"] {
  grid-column: 1 / -1 !important;
  margin-top: 6px !important;
  padding: 16px 18px !important;
  min-height: auto !important;
}

html body .onco-download-report-compact-v148 [class*="include"] ul,
html body .onco-download-report-compact-v148 [class*="report-includes"] ul,
html body .onco-download-report-compact-v148 [class*="includes"] ul {
  margin: 8px 0 0 0 !important;
  padding-left: 0 !important;
}

html body .onco-download-report-compact-v148 [class*="include"] li,
html body .onco-download-report-compact-v148 [class*="report-includes"] li,
html body .onco-download-report-compact-v148 [class*="includes"] li {
  margin: 4px 0 !important;
  line-height: 1.15 !important;
}

/* Sağ üstteki gri placeholder fazla büyükse küçült */
html body .onco-download-report-compact-v148 div:empty {
  width: 82px !important;
  height: 82px !important;
  min-width: 82px !important;
  min-height: 82px !important;
  border-radius: 16px !important;
}
`;

function applyDownloadReportCompactV148() {
  if (typeof document === "undefined") return;

  if (!document.getElementById("onco-download-report-compact-style-v148")) {
    const style = document.createElement("style");
    style.id = "onco-download-report-compact-style-v148";
    style.textContent = ONCOCONNECT_DOWNLOAD_REPORT_COMPACT_V148;
    document.head.appendChild(style);
  }

  const nodes = Array.from(document.querySelectorAll("h1,h2,h3,b,strong,span,div"));
  const title = nodes.find((el) => (el.textContent || "").trim() === "Download your report");

  if (!title) return;

  const card =
    title.closest("section") ||
    title.closest("article") ||
    title.parentElement?.parentElement ||
    title.parentElement;

  if (card) {
    card.classList.add("onco-download-report-compact-v148");
  }
}

if (typeof window !== "undefined") {
  window.setTimeout(applyDownloadReportCompactV148, 50);
  window.setTimeout(applyDownloadReportCompactV148, 300);
  window.setTimeout(applyDownloadReportCompactV148, 900);
  window.addEventListener("load", applyDownloadReportCompactV148);
}

