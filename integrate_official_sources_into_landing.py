from pathlib import Path

app = Path("frontend/src/App.jsx")
css = Path("frontend/src/App.css")

s = app.read_text(encoding="utf-8")

# LandingDataDashboard içinde state ekle
s = s.replace(
'''    const [landingRows, setLandingRows] = useState([]);''',
'''    const [landingRows, setLandingRows] = useState([]);
    const [officialRows, setOfficialRows] = useState([]);''',
1
)

# CSV load useEffect içine official source load ekle
s = s.replace(
'''          setLandingRows([]);
        }
      }

      loadLandingCsv();
    }, []);''',
'''          setLandingRows([]);
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
    }, []);''',
1
)

# Side panelde official source sayısını göster
s = s.replace(
'''            <div>
              <strong>{normalized.length}</strong>
              <small>CSV rows loaded</small>
            </div>''',
'''            <div>
              <strong>{normalized.length}</strong>
              <small>CSV rows loaded</small>
            </div>

            <div>
              <strong>{officialRows.length}</strong>
              <small>official source-backed rows</small>
            </div>''',
1
)

# Source-backed mini panel ekle
s = s.replace(
'''          <aside className="landing-live-side">
            <span>Current view</span>''',
'''          <aside className="landing-live-side">
            <span>Current view</span>''',
1
)

# Chart grid sonrasına official source table ekle
s = s.replace(
'''        </div>
      </section>
    );
  };''',
'''        </div>

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
      </section>
    );
  };''',
1
)

app.write_text(s, encoding="utf-8")

css_patch = r'''

/* Official source-backed layer */

.landing-official-source-strip {
  position: relative;
  z-index: 2;
  margin-top: 24px;
  padding: 24px;
  border-radius: 30px;
  background: rgba(15, 23, 42, 0.94);
  color: white;
  box-shadow: 0 24px 80px rgba(15,23,42,0.18);
  overflow: hidden;
}

.landing-official-source-strip::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(120deg, transparent, rgba(34,211,238,0.12), transparent);
  animation: officialSourceScan 4.8s linear infinite;
  pointer-events: none;
}

@keyframes officialSourceScan {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}

.landing-official-source-strip > span {
  position: relative;
  z-index: 2;
  display: block;
  color: #a5f3fc;
  font-size: 12px;
  font-weight: 950;
  letter-spacing: 0.18em;
  margin-bottom: 16px;
}

.landing-official-source-strip > div {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}

.landing-official-source-strip article {
  padding: 16px;
  border-radius: 20px;
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(125,211,252,0.18);
}

.landing-official-source-strip b,
.landing-official-source-strip strong,
.landing-official-source-strip small {
  display: block;
}

.landing-official-source-strip b {
  color: rgba(255,255,255,0.72);
  font-size: 12px;
}

.landing-official-source-strip strong {
  margin: 8px 0;
  color: white;
  font-size: 24px;
}

.landing-official-source-strip small {
  color: rgba(226,232,240,0.72);
  line-height: 1.45;
}

@media (max-width: 1050px) {
  .landing-official-source-strip > div {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 650px) {
  .landing-official-source-strip > div {
    grid-template-columns: 1fr;
  }
}

'''

css.write_text(css.read_text(encoding="utf-8") + css_patch, encoding="utf-8")
print("✅ Landing dashboard now imports official_cancer_sources.csv.")
