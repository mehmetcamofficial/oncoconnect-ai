from pathlib import Path
import csv

root = Path(".")
public_data = root / "frontend" / "public" / "data"
public_data.mkdir(parents=True, exist_ok=True)

csv_path = public_data / "cancer_registry_template.csv"

rows = [
    {
        "record_id": "TR-2022-ALL",
        "data_status": "official",
        "data_type": "country_level_globocan",
        "geography_level": "country",
        "country": "Türkiye",
        "iso3": "TUR",
        "region_code": "TR",
        "region_name": "Türkiye",
        "year": "2022",
        "sex": "total",
        "age_group": "all",
        "cancer_site": "All cancers",
        "icd10_code": "C00-C97",
        "metric": "new_cases",
        "value": "240013",
        "rate_per_100k": "",
        "population": "",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "quality_flag": "official_country_level",
        "notes": "Country-level official estimate. Not province-level."
    },
    {
        "record_id": "TR-2022-DEATHS",
        "data_status": "official",
        "data_type": "country_level_globocan",
        "geography_level": "country",
        "country": "Türkiye",
        "iso3": "TUR",
        "region_code": "TR",
        "region_name": "Türkiye",
        "year": "2022",
        "sex": "total",
        "age_group": "all",
        "cancer_site": "All cancers",
        "icd10_code": "C00-C97",
        "metric": "deaths",
        "value": "129672",
        "rate_per_100k": "",
        "population": "",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "quality_flag": "official_country_level",
        "notes": "Country-level official estimate. Not province-level."
    },
    {
        "record_id": "TR-2022-PREV5Y",
        "data_status": "official",
        "data_type": "country_level_globocan",
        "geography_level": "country",
        "country": "Türkiye",
        "iso3": "TUR",
        "region_code": "TR",
        "region_name": "Türkiye",
        "year": "2022",
        "sex": "total",
        "age_group": "all",
        "cancer_site": "All cancers",
        "icd10_code": "C00-C97",
        "metric": "5y_prevalence",
        "value": "679335",
        "rate_per_100k": "",
        "population": "",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "quality_flag": "official_country_level",
        "notes": "Country-level official estimate. Not province-level."
    },
    {
        "record_id": "TR-2022-LUNG",
        "data_status": "official",
        "data_type": "country_level_globocan",
        "geography_level": "country",
        "country": "Türkiye",
        "iso3": "TUR",
        "region_code": "TR",
        "region_name": "Türkiye",
        "year": "2022",
        "sex": "total",
        "age_group": "all",
        "cancer_site": "Lung",
        "icd10_code": "C33-C34",
        "metric": "new_cases",
        "value": "41032",
        "rate_per_100k": "",
        "population": "",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "quality_flag": "official_country_level",
        "notes": "Country-level official estimate."
    },
    {
        "record_id": "TR-2022-BREAST",
        "data_status": "official",
        "data_type": "country_level_globocan",
        "geography_level": "country",
        "country": "Türkiye",
        "iso3": "TUR",
        "region_code": "TR",
        "region_name": "Türkiye",
        "year": "2022",
        "sex": "total",
        "age_group": "all",
        "cancer_site": "Breast",
        "icd10_code": "C50",
        "metric": "new_cases",
        "value": "25249",
        "rate_per_100k": "",
        "population": "",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "quality_flag": "official_country_level",
        "notes": "Country-level official estimate."
    },
    {
        "record_id": "TR-2022-COLORECTAL",
        "data_status": "official",
        "data_type": "country_level_globocan",
        "geography_level": "country",
        "country": "Türkiye",
        "iso3": "TUR",
        "region_code": "TR",
        "region_name": "Türkiye",
        "year": "2022",
        "sex": "total",
        "age_group": "all",
        "cancer_site": "Colorectum",
        "icd10_code": "C18-C20",
        "metric": "new_cases",
        "value": "21718",
        "rate_per_100k": "",
        "population": "",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "quality_flag": "official_country_level",
        "notes": "Country-level official estimate."
    },
]

fieldnames = list(rows[0].keys())

with csv_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

css_path = root / "frontend" / "src" / "App.css"
css = css_path.read_text(encoding="utf-8")

css += r'''

/* Step 20: Türkiye map visual fix + real data folder indicator */

.turkiye-pin-map {
  display: block !important;
  position: relative !important;
  min-height: 560px !important;
  padding: 0 !important;
  overflow: hidden !important;
  border-radius: 30px !important;
  background:
    radial-gradient(circle at 20% 20%, rgba(56,189,248,0.22), transparent 28%),
    radial-gradient(circle at 75% 65%, rgba(20,184,166,0.18), transparent 32%),
    linear-gradient(135deg, #06182f, #1e3a8a) !important;
}

.turkiye-pin-map::before {
  content: "";
  position: absolute;
  left: 6%;
  right: 6%;
  top: 23%;
  height: 48%;
  background:
    linear-gradient(135deg, rgba(255,255,255,0.18), rgba(255,255,255,0.07));
  border: 1px solid rgba(255,255,255,0.24);
  clip-path: polygon(
    3% 55%, 8% 44%, 15% 41%, 22% 36%, 31% 32%,
    43% 28%, 55% 30%, 66% 34%, 78% 31%, 90% 38%,
    96% 49%, 92% 61%, 80% 64%, 66% 70%, 52% 68%,
    38% 73%, 25% 68%, 13% 66%, 6% 61%
  );
  filter: drop-shadow(0 18px 40px rgba(0,0,0,0.22));
}

.turkiye-pin-map::after {
  content: "Türkiye cancer burden map — demo province distribution";
  position: absolute;
  left: 24px;
  bottom: 20px;
  color: rgba(255,255,255,0.78);
  font-weight: 850;
  letter-spacing: 0.02em;
}

.turkiye-pin-map .map-pin {
  position: absolute !important;
  width: var(--size) !important;
  height: var(--size) !important;
  min-width: 14px !important;
  min-height: 14px !important;
  padding: 0 !important;
  border-radius: 999px !important;
  background: #38bdf8 !important;
  border: 2px solid rgba(255,255,255,0.88) !important;
  box-shadow:
    0 0 0 7px rgba(56,189,248,0.13),
    0 0 28px rgba(56,189,248,0.72) !important;
  animation: provincePulse 3.2s ease-in-out infinite !important;
  animation-delay: var(--delay) !important;
  z-index: 3;
}

.turkiye-pin-map .map-pin::before {
  display: none !important;
}

.turkiye-pin-map .map-pin span,
.turkiye-pin-map .map-pin b {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  padding-left: 0 !important;
  text-align: center !important;
  opacity: 0;
  pointer-events: none;
  white-space: nowrap;
  background: rgba(15,23,42,0.92);
  color: white;
  border-radius: 12px;
  padding: 5px 8px !important;
  transition: opacity .2s ease, transform .2s ease;
}

.turkiye-pin-map .map-pin span {
  bottom: calc(100% + 7px);
  font-size: 12px !important;
  font-weight: 950 !important;
}

.turkiye-pin-map .map-pin b {
  top: calc(100% + 7px);
  font-size: 11px !important;
}

.turkiye-pin-map .map-pin:hover {
  transform: scale(1.9) !important;
  z-index: 20;
  background: #fbbf24 !important;
  box-shadow:
    0 0 0 9px rgba(251,191,36,0.16),
    0 0 36px rgba(251,191,36,0.8) !important;
}

.turkiye-pin-map .map-pin:hover span,
.turkiye-pin-map .map-pin:hover b {
  opacity: 1;
}

@keyframes provincePulse {
  0%, 100% {
    opacity: .82;
    box-shadow:
      0 0 0 5px rgba(56,189,248,0.10),
      0 0 22px rgba(56,189,248,0.55);
  }
  50% {
    opacity: 1;
    box-shadow:
      0 0 0 11px rgba(56,189,248,0.18),
      0 0 36px rgba(56,189,248,0.78);
  }
}

/* Approximate 81 province coordinates arranged on Türkiye silhouette */

.turkiye-pin-map .map-pin:nth-child(1) { left: 20%; top: 54%; }
.turkiye-pin-map .map-pin:nth-child(2) { left: 66%; top: 55%; }
.turkiye-pin-map .map-pin:nth-child(3) { left: 29%; top: 51%; }
.turkiye-pin-map .map-pin:nth-child(4) { left: 86%; top: 43%; }
.turkiye-pin-map .map-pin:nth-child(5) { left: 48%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(6) { left: 43%; top: 48%; }
.turkiye-pin-map .map-pin:nth-child(7) { left: 30%; top: 61%; }
.turkiye-pin-map .map-pin:nth-child(8) { left: 85%; top: 33%; }
.turkiye-pin-map .map-pin:nth-child(9) { left: 22%; top: 61%; }
.turkiye-pin-map .map-pin:nth-child(10) { left: 19%; top: 48%; }
.turkiye-pin-map .map-pin:nth-child(11) { left: 28%; top: 45%; }
.turkiye-pin-map .map-pin:nth-child(12) { left: 77%; top: 47%; }
.turkiye-pin-map .map-pin:nth-child(13) { left: 81%; top: 53%; }
.turkiye-pin-map .map-pin:nth-child(14) { left: 39%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(15) { left: 31%; top: 57%; }
.turkiye-pin-map .map-pin:nth-child(16) { left: 25%; top: 43%; }
.turkiye-pin-map .map-pin:nth-child(17) { left: 16%; top: 44%; }
.turkiye-pin-map .map-pin:nth-child(18) { left: 46%; top: 40%; }
.turkiye-pin-map .map-pin:nth-child(19) { left: 50%; top: 43%; }
.turkiye-pin-map .map-pin:nth-child(20) { left: 26%; top: 59%; }
.turkiye-pin-map .map-pin:nth-child(21) { left: 72%; top: 58%; }
.turkiye-pin-map .map-pin:nth-child(22) { left: 9%; top: 36%; }
.turkiye-pin-map .map-pin:nth-child(23) { left: 66%; top: 49%; }
.turkiye-pin-map .map-pin:nth-child(24) { left: 73%; top: 43%; }
.turkiye-pin-map .map-pin:nth-child(25) { left: 79%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(26) { left: 35%; top: 45%; }
.turkiye-pin-map .map-pin:nth-child(27) { left: 61%; top: 62%; }
.turkiye-pin-map .map-pin:nth-child(28) { left: 61%; top: 35%; }
.turkiye-pin-map .map-pin:nth-child(29) { left: 67%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(30) { left: 88%; top: 57%; }
.turkiye-pin-map .map-pin:nth-child(31) { left: 55%; top: 63%; }
.turkiye-pin-map .map-pin:nth-child(32) { left: 32%; top: 56%; }
.turkiye-pin-map .map-pin:nth-child(33) { left: 46%; top: 64%; }
.turkiye-pin-map .map-pin:nth-child(34) { left: 11%; top: 32%; }
.turkiye-pin-map .map-pin:nth-child(35) { left: 18%; top: 58%; }
.turkiye-pin-map .map-pin:nth-child(36) { left: 88%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(37) { left: 41%; top: 35%; }
.turkiye-pin-map .map-pin:nth-child(38) { left: 51%; top: 50%; }
.turkiye-pin-map .map-pin:nth-child(39) { left: 8%; top: 34%; }
.turkiye-pin-map .map-pin:nth-child(40) { left: 48%; top: 48%; }
.turkiye-pin-map .map-pin:nth-child(41) { left: 20%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(42) { left: 43%; top: 55%; }
.turkiye-pin-map .map-pin:nth-child(43) { left: 31%; top: 47%; }
.turkiye-pin-map .map-pin:nth-child(44) { left: 59%; top: 52%; }
.turkiye-pin-map .map-pin:nth-child(45) { left: 22%; top: 54%; }
.turkiye-pin-map .map-pin:nth-child(46) { left: 58%; top: 59%; }
.turkiye-pin-map .map-pin:nth-child(47) { left: 74%; top: 60%; }
.turkiye-pin-map .map-pin:nth-child(48) { left: 22%; top: 66%; }
.turkiye-pin-map .map-pin:nth-child(49) { left: 82%; top: 49%; }
.turkiye-pin-map .map-pin:nth-child(50) { left: 50%; top: 53%; }
.turkiye-pin-map .map-pin:nth-child(51) { left: 48%; top: 57%; }
.turkiye-pin-map .map-pin:nth-child(52) { left: 58%; top: 34%; }
.turkiye-pin-map .map-pin:nth-child(53) { left: 67%; top: 32%; }
.turkiye-pin-map .map-pin:nth-child(54) { left: 18%; top: 39%; }
.turkiye-pin-map .map-pin:nth-child(55) { left: 55%; top: 36%; }
.turkiye-pin-map .map-pin:nth-child(56) { left: 80%; top: 57%; }
.turkiye-pin-map .map-pin:nth-child(57) { left: 47%; top: 32%; }
.turkiye-pin-map .map-pin:nth-child(58) { left: 57%; top: 46%; }
.turkiye-pin-map .map-pin:nth-child(59) { left: 10%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(60) { left: 54%; top: 40%; }
.turkiye-pin-map .map-pin:nth-child(61) { left: 64%; top: 34%; }
.turkiye-pin-map .map-pin:nth-child(62) { left: 70%; top: 46%; }
.turkiye-pin-map .map-pin:nth-child(63) { left: 68%; top: 64%; }
.turkiye-pin-map .map-pin:nth-child(64) { left: 28%; top: 54%; }
.turkiye-pin-map .map-pin:nth-child(65) { left: 88%; top: 52%; }
.turkiye-pin-map .map-pin:nth-child(66) { left: 51%; top: 45%; }
.turkiye-pin-map .map-pin:nth-child(67) { left: 35%; top: 32%; }
.turkiye-pin-map .map-pin:nth-child(68) { left: 47%; top: 55%; }
.turkiye-pin-map .map-pin:nth-child(69) { left: 73%; top: 37%; }
.turkiye-pin-map .map-pin:nth-child(70) { left: 45%; top: 60%; }
.turkiye-pin-map .map-pin:nth-child(71) { left: 46%; top: 46%; }
.turkiye-pin-map .map-pin:nth-child(72) { left: 78%; top: 55%; }
.turkiye-pin-map .map-pin:nth-child(73) { left: 84%; top: 59%; }
.turkiye-pin-map .map-pin:nth-child(74) { left: 33%; top: 32%; }
.turkiye-pin-map .map-pin:nth-child(75) { left: 86%; top: 35%; }
.turkiye-pin-map .map-pin:nth-child(76) { left: 91%; top: 42%; }
.turkiye-pin-map .map-pin:nth-child(77) { left: 17%; top: 36%; }
.turkiye-pin-map .map-pin:nth-child(78) { left: 36%; top: 35%; }
.turkiye-pin-map .map-pin:nth-child(79) { left: 62%; top: 65%; }
.turkiye-pin-map .map-pin:nth-child(80) { left: 57%; top: 65%; }
.turkiye-pin-map .map-pin:nth-child(81) { left: 24%; top: 38%; }

@media (max-width: 900px) {
  .turkiye-pin-map {
    min-height: 430px !important;
  }

  .turkiye-pin-map::after {
    font-size: 12px;
    right: 20px;
  }

  .turkiye-pin-map .map-pin {
    width: 13px !important;
    height: 13px !important;
    min-width: 13px !important;
    min-height: 13px !important;
  }
}
'''

css_path.write_text(css, encoding="utf-8")

print("✅ public/data created.")
print("✅ cancer_registry_template.csv created.")
print("✅ Türkiye map visual upgraded from grid to animated pin map.")
