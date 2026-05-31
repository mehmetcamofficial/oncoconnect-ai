from pathlib import Path
import csv
import json

ROOT = Path(".")
DATA_DIR = ROOT / "frontend/public/data"
APP = ROOT / "frontend/src/App.jsx"
CSS = ROOT / "frontend/src/App.css"

DATA_DIR.mkdir(parents=True, exist_ok=True)

official_csv = DATA_DIR / "official_cancer_sources.csv"
registry_json = DATA_DIR / "official_cancer_source_registry.json"

rows = [
    {
        "source_id": "globocan_2022_turkiye_factsheet",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "publisher": "IARC / Global Cancer Observatory",
        "year": "2022",
        "region": "Türkiye",
        "area": "Türkiye",
        "sex": "All",
        "age_group": "All ages",
        "cancer_type": "All cancers",
        "indicator": "new_cases_count",
        "value": "240013",
        "unit": "count",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "evidence_note": "Türkiye all cancers new cases, 2022",
        "data_quality": "official_source_backed"
    },
    {
        "source_id": "globocan_2022_turkiye_factsheet",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "publisher": "IARC / Global Cancer Observatory",
        "year": "2022",
        "region": "Türkiye",
        "area": "Türkiye",
        "sex": "All",
        "age_group": "All ages",
        "cancer_type": "All cancers",
        "indicator": "deaths_count",
        "value": "129672",
        "unit": "count",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "evidence_note": "Türkiye all cancers deaths, 2022",
        "data_quality": "official_source_backed"
    },
    {
        "source_id": "globocan_2022_turkiye_factsheet",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "publisher": "IARC / Global Cancer Observatory",
        "year": "2022",
        "region": "Türkiye",
        "area": "Türkiye",
        "sex": "All",
        "age_group": "All ages",
        "cancer_type": "All cancers",
        "indicator": "five_year_prevalence_count",
        "value": "679335",
        "unit": "count",
        "source_url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "evidence_note": "Türkiye all cancers 5-year prevalent cases, 2022",
        "data_quality": "official_source_backed"
    },
    {
        "source_id": "canscreen5_turkiye_country_factsheet",
        "source_name": "CanScreen5 Türkiye Country Fact Sheet",
        "publisher": "IARC / CanScreen5",
        "year": "latest_available",
        "region": "Türkiye",
        "area": "Türkiye",
        "sex": "All",
        "age_group": "All ages",
        "cancer_type": "All cancers",
        "indicator": "overall_incidence_rate",
        "value": "225.9",
        "unit": "rate_per_100000",
        "source_url": "https://canscreen5.iarc.fr/?page=countryfactsheet&q=TUR",
        "evidence_note": "Overall cancer incidence rate per 100,000 persons per year",
        "data_quality": "official_source_backed"
    },
    {
        "source_id": "canscreen5_turkiye_country_factsheet",
        "source_name": "CanScreen5 Türkiye Country Fact Sheet",
        "publisher": "IARC / CanScreen5",
        "year": "latest_available",
        "region": "Türkiye",
        "area": "Türkiye",
        "sex": "All",
        "age_group": "All ages",
        "cancer_type": "All cancers",
        "indicator": "overall_mortality_rate",
        "value": "116.1",
        "unit": "rate_per_100000",
        "source_url": "https://canscreen5.iarc.fr/?page=countryfactsheet&q=TUR",
        "evidence_note": "Overall cancer mortality rate per 100,000 persons per year",
        "data_quality": "official_source_backed"
    },
    {
        "source_id": "canscreen5_turkiye_country_factsheet",
        "source_name": "CanScreen5 Türkiye Country Fact Sheet",
        "publisher": "IARC / CanScreen5",
        "year": "latest_available",
        "region": "Türkiye",
        "area": "Türkiye",
        "sex": "Female",
        "age_group": "All ages",
        "cancer_type": "Breast",
        "indicator": "female_breast_incidence_rate",
        "value": "46.8",
        "unit": "rate_per_100000",
        "source_url": "https://canscreen5.iarc.fr/?page=countryfactsheet&q=TUR",
        "evidence_note": "Most common cancer site by incidence for females: Breast",
        "data_quality": "official_source_backed"
    },
    {
        "source_id": "canscreen5_turkiye_country_factsheet",
        "source_name": "CanScreen5 Türkiye Country Fact Sheet",
        "publisher": "IARC / CanScreen5",
        "year": "latest_available",
        "region": "Türkiye",
        "area": "Türkiye",
        "sex": "Female",
        "age_group": "All ages",
        "cancer_type": "Breast",
        "indicator": "female_breast_mortality_rate",
        "value": "12.5",
        "unit": "rate_per_100000",
        "source_url": "https://canscreen5.iarc.fr/?page=countryfactsheet&q=TUR",
        "evidence_note": "Most common cancer site by mortality for females: Breast",
        "data_quality": "official_source_backed"
    },
    {
        "source_id": "canscreen5_turkiye_country_factsheet",
        "source_name": "CanScreen5 Türkiye Country Fact Sheet",
        "publisher": "IARC / CanScreen5",
        "year": "latest_available",
        "region": "Türkiye",
        "area": "Türkiye",
        "sex": "Male",
        "age_group": "All ages",
        "cancer_type": "Lung",
        "indicator": "male_lung_incidence_rate",
        "value": "68.0",
        "unit": "rate_per_100000",
        "source_url": "https://canscreen5.iarc.fr/?page=countryfactsheet&q=TUR",
        "evidence_note": "Most common cancer site by incidence for males: Lung",
        "data_quality": "official_source_backed"
    }
]

registry = [
    {
        "source_id": "globocan_2022_turkiye_factsheet",
        "source_name": "GLOBOCAN 2022 Türkiye Fact Sheet",
        "publisher": "IARC / Global Cancer Observatory",
        "type": "official_country_fact_sheet",
        "url": "https://gco.iarc.who.int/media/globocan/factsheets/populations/792-turkiye-fact-sheet.pdf",
        "status": "seeded",
        "notes": "Use only rows manually verified from official fact sheet."
    },
    {
        "source_id": "gco_cancer_today",
        "source_name": "GLOBOCAN Cancer Today",
        "publisher": "IARC / Global Cancer Observatory",
        "type": "official_global_data_explorer",
        "url": "https://gco.iarc.who.int/today/",
        "status": "source_registry_only",
        "notes": "Use exported tables from the official explorer; do not fabricate country rows."
    },
    {
        "source_id": "ecis_data_explorer",
        "source_name": "European Cancer Information System Data Explorer",
        "publisher": "European Commission / JRC",
        "type": "official_european_data_explorer",
        "url": "https://ecis.jrc.ec.europa.eu/explorer.php",
        "status": "source_registry_only",
        "notes": "Use exported ECIS tables for Europe incidence, mortality, prevalence and survival."
    },
    {
        "source_id": "canscreen5_turkiye_country_factsheet",
        "source_name": "CanScreen5 Türkiye Country Fact Sheet",
        "publisher": "IARC / CanScreen5",
        "type": "official_country_screening_factsheet",
        "url": "https://canscreen5.iarc.fr/?page=countryfactsheet&q=TUR",
        "status": "seeded",
        "notes": "Seeded rate rows from the public country factsheet."
    }
]

with official_csv.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

registry_json.write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"✅ Created: {official_csv}")
print(f"✅ Created: {registry_json}")
print(f"✅ Official source-backed rows: {len(rows)}")
print("ℹ️ Registry includes GLOBOCAN Cancer Today and ECIS as sources for future exported-table imports.")
