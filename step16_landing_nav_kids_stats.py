from pathlib import Path
import re
import shutil

app_path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

uploaded_bg = Path("/mnt/data/ChatGPT Image May 30, 2026, 04_24_36 PM.png")
public_dir = Path("frontend/public")
public_dir.mkdir(parents=True, exist_ok=True)

bg_target = public_dir / "onco-sea-hero.png"

if uploaded_bg.exists():
    shutil.copyfile(uploaded_bg, bg_target)
else:
    print("⚠️ Uploaded background image not found. CSS will still be updated.")

app = app_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# Page state already exists from previous steps. We add kids page handling later.

new_landing = r'''  const LandingPage = () => {
    const scrollToSection = (id) => {
      document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" });
    };

    return (
      <div className="landing-page portal-page">
        <header className="portal-topnav">
          <div className="portal-brand" onClick={() => scrollToSection("home")}>
            OncoConnect AI
          </div>

          <nav className="portal-tabs">
            <button onClick={() => scrollToSection("home")}>{lang === "tr" ? "Ana Sayfa" : "Home"}</button>
            <button onClick={() => scrollToSection("what-is")}>{lang === "tr" ? "Nedir?" : "What is it?"}</button>
            <button onClick={() => scrollToSection("how-it-works")}>{lang === "tr" ? "Nasıl çalışır?" : "How it works"}</button>
            <button onClick={() => scrollToSection("cancer-burden")}>{lang === "tr" ? "İstatistikler" : "Cancer Burden"}</button>
            <button onClick={() => scrollToSection("research-feed")}>{lang === "tr" ? "Araştırma" : "Research"}</button>
            <button onClick={() => setPage("kids")}>Onco Kids</button>
            <button onClick={() => setPage("copilot")}>{lang === "tr" ? "Platform" : "Platform"}</button>
          </nav>

          <div className="language-control nav-lang">
            <label>{t.langLabel}</label>
            <select value={lang} onChange={(e) => setLang(e.target.value)}>
              <option value="en">English</option>
              <option value="tr">Türkçe</option>
            </select>
          </div>
        </header>

        <section id="home" className="portal-hero calm-sea-hero">
          <div className="portal-copy">
            <p className="eyebrow">ONCOCONNECT AI PUBLIC PORTAL</p>
            <h1>
              {lang === "tr"
                ? "Kanser yolculuğunda güvenli bilgi, destek ve AI rehberliği"
                : "Safe cancer support, research awareness and AI guidance"}
            </h1>

            <p className="portal-subtitle">
              {lang === "tr"
                ? "Hastalar, hasta yakınları, doktorlar, araştırmacılar ve STK’lar için iki katmanlı bir platform: önce güvenilir bilgi, sonra AI Copilot ve Splunk destekli operasyonel izleme."
                : "A two-layer platform for patients, caregivers, clinicians, researchers and NGOs: first trusted information, then AI Copilot and Splunk-powered operational monitoring."}
            </p>

            <div className="portal-actions">
              <button onClick={() => setPage("copilot")}>
                {lang === "tr" ? "AI Copilot’u Başlat" : "Launch AI Copilot"}
              </button>
              <button className="secondary" onClick={() => setPage("graph")}>
                {lang === "tr" ? "Knowledge Graph’i Aç" : "Open Knowledge Graph"}
              </button>
              <button className="secondary" onClick={() => setPage("kids")}>
                Onco Kids
              </button>
            </div>

            <div className="portal-note">
              {lang === "tr"
                ? "Bu platform tanı veya tedavi önerisi vermez. Bilgileri doktor görüşmesine hazırlık, güvenilir kaynaklara yönlendirme ve destek koordinasyonu için sunar."
                : "This platform does not provide diagnosis or treatment advice. It supports doctor-visit preparation, trusted source navigation and support coordination."}
            </div>
          </div>

          <div className="hero-glass-panel">
            <div className="breathing-orb"></div>
            <h3>{lang === "tr" ? "Daha sakin, daha anlaşılır, daha güvenli" : "Calm, clear and safe guidance"}</h3>
            <p>
              {lang === "tr"
                ? "Amaç hastayı korkutmak değil; doğru soruları hazırlamak, destek ihtiyacını görünür kılmak ve bakım ekibine daha yapılandırılmış bilgi sunmaktır."
                : "The goal is not to create fear; it is to prepare better questions, surface support needs and give care teams more structured information."}
            </p>
          </div>
        </section>

        <section id="what-is" className="portal-section what-section">
          <div className="section-intro">
            <p className="eyebrow dark">{lang === "tr" ? "NEDİR?" : "WHAT IS IT?"}</p>
            <h2>{lang === "tr" ? "Hasta destek portalı + AI Copilot + operasyonel izleme" : "Patient support portal + AI Copilot + operational monitoring"}</h2>
            <p>
              {lang === "tr"
                ? "OncoConnect AI; kanser hastalarının ve hasta yakınlarının semptomları daha anlaşılır hale getirmesine, doktor görüşmesine hazırlanmasına ve gerektiğinde destek ekiplerinin yüksek riskli vakaları görmesine yardımcı olur."
                : "OncoConnect AI helps cancer patients and caregivers make symptoms easier to understand, prepare for doctor visits and help support teams identify high-risk cases when needed."}
            </p>
          </div>

          <div className="need-grid">
            {[
              [
                lang === "tr" ? "Semptomlarımı anlamak istiyorum" : "I want to understand my symptoms",
                lang === "tr" ? "AI Copilot semptom yükünü açıklar, risk sinyali üretir ve doktora sorulacak soruları hazırlar." : "AI Copilot explains symptom burden, creates a risk signal and prepares doctor questions.",
                "copilot"
              ],
              [
                lang === "tr" ? "Doktor görüşmesine hazırlanmak istiyorum" : "I want to prepare for a doctor visit",
                lang === "tr" ? "Şikâyetleri yapılandırılmış bir konuşma notuna dönüştürür." : "Turns symptoms into a structured conversation note.",
                "copilot"
              ],
              [
                lang === "tr" ? "Çocuğum için sade bilgi istiyorum" : "I want simple information for my child",
                lang === "tr" ? "Onco Kids çocuklara ve ailelere daha yumuşak, umut veren açıklamalar sunar." : "Onco Kids provides gentler, hopeful explanations for children and families.",
                "kids"
              ],
              [
                lang === "tr" ? "Yeni araştırmaları takip etmek istiyorum" : "I want to follow new cancer research",
                lang === "tr" ? "Klinik çalışmalar, immünoterapi, erken tanı ve hasta destek kaynakları için güvenli kaynak akışı." : "A safe source-aware feed for trials, immunotherapy, early detection and patient support.",
                "feed"
              ],
              [
                lang === "tr" ? "STK veya destek ekibiyim" : "I am an NGO or support team",
                lang === "tr" ? "Yüksek riskli vakaları Splunk dashboardları ve AI özetleriyle önceliklendirir." : "Prioritizes high-risk cases through Splunk dashboards and AI summaries.",
                "graph"
              ],
              [
                lang === "tr" ? "Ekosistemi görmek istiyorum" : "I want to see the ecosystem",
                lang === "tr" ? "Hasta, doktor, araştırmacı, STK, veri setleri ve Splunk arasındaki bilgi akışını gösterir." : "Shows the flow between patients, clinicians, researchers, NGOs, datasets and Splunk.",
                "graph"
              ]
            ].map(([title, body, target]) => (
              <button
                key={title}
                className="need-card"
                onClick={() => {
                  if (target === "copilot") setPage("copilot");
                  if (target === "graph") setPage("graph");
                  if (target === "kids") setPage("kids");
                  if (target === "feed") scrollToSection("research-feed");
                }}
              >
                <strong>{title}</strong>
                <span>{body}</span>
              </button>
            ))}
          </div>
        </section>

        <section id="how-it-works" className="portal-section how-section">
          <div className="section-intro">
            <p className="eyebrow dark">{lang === "tr" ? "NASIL ÇALIŞIR?" : "HOW IT WORKS"}</p>
            <h2>{lang === "tr" ? "Bilgiden aksiyona giden güvenli akış" : "A safe path from information to action"}</h2>
          </div>

          <div className="flow-steps">
            {[
              [1, lang === "tr" ? "Kullanıcı rolünü seçer" : "User selects role", lang === "tr" ? "Hasta, hasta yakını, destek ekibi veya araştırmacı bakış açısı." : "Patient, caregiver, support team or researcher perspective."],
              [2, lang === "tr" ? "Semptom veya ihtiyaç girilir" : "Symptoms or needs are entered", lang === "tr" ? "Halsizlik, bulantı, ağrı, moral ve kısa not." : "Fatigue, nausea, pain, mood and short notes."],
              [3, lang === "tr" ? "AI Copilot açıklar" : "AI Copilot explains", lang === "tr" ? "Risk düzeyi, anlamı, doktora sorular ve sonraki adım." : "Risk level, meaning, doctor questions and next step."],
              [4, lang === "tr" ? "Splunk’a olay akar" : "Event streams to Splunk", lang === "tr" ? "Destek ekipleri yüksek riskli vakaları dashboard’da izler." : "Support teams monitor high-risk cases in dashboards."]
            ].map(([num, title, body]) => (
              <div className="flow-card" key={num}>
                <div>{num}</div>
                <strong>{title}</strong>
                <span>{body}</span>
              </div>
            ))}
          </div>
        </section>

        <section id="cancer-burden" className="statistics-section animated-burden">
          <div className="section-intro">
            <p className="eyebrow dark">{lang === "tr" ? "KANSER YÜKÜ" : "CANCER BURDEN"}</p>
            <h2>{lang === "tr" ? "Veri korkutmak için değil; erken destek ve koordinasyon için" : "Data is not for fear; it is for earlier support and coordination"}</h2>
          </div>

          <div className="stat-world-grid improved-stats">
            <div className="stat-panel global animated-stat">
              <small>{lang === "tr" ? "Dünya geneli, 2022" : "Worldwide, 2022"}</small>
              <strong className="stat-number">~20M</strong>
              <span>{lang === "tr" ? "yeni kanser vakası" : "new cancer cases"}</span>
              <p>{lang === "tr" ? "GLOBOCAN 2022 tahminleri dünya genelinde yaklaşık 20 milyon yeni vaka bildiriyor." : "GLOBOCAN 2022 estimates around 20 million new cancer cases worldwide."}</p>
              <div className="stat-progress"><i style={{ width: "82%" }}></i></div>
            </div>

            <div className="stat-panel global animated-stat">
              <small>{lang === "tr" ? "Dünya geneli, 2022" : "Worldwide, 2022"}</small>
              <strong className="stat-number">~9.7M</strong>
              <span>{lang === "tr" ? "kanser ölümü" : "cancer deaths"}</span>
              <p>{lang === "tr" ? "Bu tablo destek, farkındalık, tarama ve bakım koordinasyonunun önemini gösterir." : "This highlights the importance of support, awareness, screening and care coordination."}</p>
              <div className="stat-progress"><i style={{ width: "62%" }}></i></div>
            </div>

            <div className="stat-panel turkiye animated-stat compact-stat">
              <small>{lang === "tr" ? "Türkiye bağlamı" : "Türkiye context"}</small>
              <strong className="stat-number smaller">Türkiye</strong>
              <span>{lang === "tr" ? "ülke bazlı kanser istatistikleri" : "country-level cancer statistics"}</span>
              <p>{lang === "tr" ? "Akciğer, meme ve kolorektal kanserler Türkiye için öne çıkan başlıklar arasındadır." : "Lung, breast and colorectal cancers are among the key cancer burden areas for Türkiye."}</p>
              <div className="stat-progress"><i style={{ width: "70%" }}></i></div>
            </div>

            <div className="stat-panel mission animated-stat">
              <small>EU Cancer Mission</small>
              <strong className="stat-number">2030</strong>
              <span>{lang === "tr" ? "yaşam kalitesi ve bakım hedefleri" : "quality of life and care goals"}</span>
              <p>{lang === "tr" ? "AB yaklaşımı; önleme, tedavi, yaşam kalitesi ve aileleri kapsayan destek hedeflerini vurgular." : "The EU approach emphasizes prevention, cure, quality of life and support for people and families affected by cancer."}</p>
              <div className="stat-progress"><i style={{ width: "88%" }}></i></div>
            </div>
          </div>
        </section>

        <section className="prevention-simulator-section">
          <div className="simulator-copy">
            <p className="eyebrow dark">{lang === "tr" ? "ÖNLEME FARKINDALIĞI SİMÜLATÖRÜ" : "PREVENTION AWARENESS SIMULATOR"}</p>
            <h2>
              {lang === "tr"
                ? "Küçük davranış değişiklikleri, büyük farkındalık yaratabilir"
                : "Small behavior changes can create meaningful awareness"}
            </h2>
            <p>
              {lang === "tr"
                ? "Bu araç kişisel kanser riskinizi hesaplamaz. Tütün, alkol, hareket ve tarama farkındalığı gibi değiştirilebilir faktörlerin önemini görselleştiren eğitim amaçlı bir simülasyondur."
                : "This tool does not calculate your personal cancer risk. It is an educational simulation that visualizes the importance of modifiable factors such as tobacco, alcohol, movement and screening awareness."}
            </p>

            <div className="evidence-note">
              {lang === "tr"
                ? "Farkındalık, sağlıklı yaşam davranışları ve tarama programları kanser kontrolünde önemli destek alanlarıdır."
                : "Awareness, healthy behaviors and screening programs are important support areas in cancer control."}
            </div>
          </div>

          <div className="simulator-card">
            <div className="simulator-score">
              <div className="score-ring" style={{ "--score": `${preventionScore}%` }}>
                <span>{preventionScore}</span>
              </div>
              <div>
                <strong>{preventionLevel}</strong>
                <p>
                  {lang === "tr"
                    ? "Bu skor kişisel tıbbi risk değildir; eğitim ve farkındalık göstergesidir."
                    : "This score is not a personal medical risk; it is an education and awareness indicator."}
                </p>
              </div>
            </div>

            <div className="simulator-sliders">
              {[
                [
                  "tobaccoFree",
                  lang === "tr" ? "Tütünsüz yaşam farkındalığı" : "Tobacco-free awareness",
                  lang === "tr" ? "Tütün kullanmamak kanserden korunmada en güçlü adımlardan biridir." : "Avoiding tobacco is one of the strongest steps for cancer prevention."
                ],
                [
                  "alcoholReduction",
                  lang === "tr" ? "Alkol azaltma farkındalığı" : "Alcohol reduction awareness",
                  lang === "tr" ? "Alkol tüketimini azaltmak bazı kanser türleri için risk azaltma stratejilerinde yer alır." : "Reducing alcohol is part of cancer risk reduction strategies for several cancer types."
                ],
                [
                  "movement",
                  lang === "tr" ? "Fiziksel aktivite" : "Physical activity",
                  lang === "tr" ? "Düzenli hareket, sağlıklı kilo ve genel iyilik hali için destekleyicidir." : "Regular movement supports healthy weight and overall wellbeing."
                ],
                [
                  "screeningAwareness",
                  lang === "tr" ? "Tarama ve erken farkındalık" : "Screening and early awareness",
                  lang === "tr" ? "Yaşa ve risk durumuna uygun taramalar için doktorla görüşmek önemlidir." : "Discussing age- and risk-appropriate screening with clinicians is important."
                ]
              ].map(([key, label, desc]) => (
                <div className="prevention-slider" key={key}>
                  <div className="slider-meta">
                    <strong>{label}</strong>
                    <span>{prevention[key]}%</span>
                  </div>
                  <input type="range" min="0" max="100" value={prevention[key]} onChange={(e) => updatePrevention(key, e.target.value)} />
                  <small>{desc}</small>
                </div>
              ))}
            </div>
          </div>

          <div className="simulator-visual">
            <div className="floating-stat s1"><strong>30–50%</strong><span>{lang === "tr" ? "önlenebilir vaka potansiyeli" : "preventable case potential"}</span></div>
            <div className="floating-stat s2"><strong>{lang === "tr" ? "Tarama" : "Screening"}</strong><span>{lang === "tr" ? "erken farkındalık" : "early awareness"}</span></div>
            <div className="floating-stat s3"><strong>{lang === "tr" ? "Destek" : "Support"}</strong><span>{lang === "tr" ? "bakım koordinasyonu" : "care coordination"}</span></div>
            <div className="visual-orb"></div>
          </div>
        </section>

        <section id="research-feed" className="research-feed-section">
          <div className="section-intro feed-intro">
            <p className="eyebrow dark">{lang === "tr" ? "ARAŞTIRMA & İNOVASYON AKIŞI" : "RESEARCH & INNOVATION FEED"}</p>
            <h2>{lang === "tr" ? "Klinik çalışmalar, yeni buluşlar, hasta destek kaynakları" : "Clinical trials, breakthroughs and patient support sources"}</h2>
            <p>
              {lang === "tr"
                ? "Bu alan canlı tedavi önerisi değildir. Güvenilir kaynaklardan gelen başlıkları doktorla konuşmaya hazırlık ve araştırma farkındalığı için kategorize eder."
                : "This is not live treatment advice. It categorizes trusted-source topics for doctor-visit preparation and research awareness."}
            </p>
          </div>

          <div className="feed-grid">
            {[
              {
                category: lang === "tr" ? "Klinik çalışma farkındalığı" : "Clinical trial awareness",
                title: lang === "tr" ? "Klinik araştırmaları güvenli şekilde nasıl ararım?" : "How can I search clinical trials safely?",
                body: lang === "tr" ? "Kanser türü, evre, tedavi geçmişi ve ülke filtresiyle arama yapılabilir; uygunluk mutlaka doktorla değerlendirilmelidir." : "Search by cancer type, stage, treatment history and country; eligibility must be discussed with a clinician.",
                source: "ClinicalTrials.gov / EU Clinical Trials",
                url: "https://clinicaltrials.gov/",
                ask: lang === "tr" ? "Benim kanser türüm ve tedavi aşamam için uygun klinik çalışma var mı?" : "Are there clinical trials appropriate for my cancer type and treatment stage?"
              },
              {
                category: lang === "tr" ? "İmmünoterapi araştırmaları" : "Immunotherapy research",
                title: lang === "tr" ? "Bağışıklık sistemini hedefleyen tedavi araştırmaları" : "Research into treatments that use the immune system",
                body: lang === "tr" ? "İmmünoterapi, bazı kanserlerde bağışıklık sisteminin kanseri tanıma ve hedefleme kapasitesinden yararlanır." : "Immunotherapy uses the immune system’s ability to recognize and target cancer in some cancer types.",
                source: "Cancer Research Institute",
                url: "https://www.cancerresearch.org/",
                ask: lang === "tr" ? "Benim kanser türümde immünoterapi veya immüno-onkoloji çalışmaları var mı?" : "Are immunotherapy or immuno-oncology studies relevant to my cancer type?"
              },
              {
                category: lang === "tr" ? "Onkoloji haberleri" : "Oncology news",
                title: lang === "tr" ? "Yeni klinik gelişmeleri takip etmek" : "Tracking new clinical developments",
                body: lang === "tr" ? "Yeni ilaç, kombinasyon tedavisi, erken tanı ve konferans haberleri uzman değerlendirmesiyle okunmalıdır." : "New drug, combination therapy, early detection and conference updates should be interpreted with expert guidance.",
                source: "CancerNetwork / ecancer",
                url: "https://www.cancernetwork.com/",
                ask: lang === "tr" ? "Bu haber benim tedavi planımla ilişkili mi, yoksa araştırma aşamasında mı?" : "Is this relevant to my care plan, or is it still investigational?"
              }
            ].map((item) => (
              <article key={item.title} className="feed-card">
                <div className="feed-category">{item.category}</div>
                <h3>{item.title}</h3>
                <p>{item.body}</p>
                <div className="doctor-question">
                  <strong>{lang === "tr" ? "Doktorla konuşulacak soru" : "Question for your doctor"}</strong>
                  <span>{item.ask}</span>
                </div>
                <div className="feed-footer">
                  <span>{item.source}</span>
                  <a href={item.url} target="_blank" rel="noreferrer">{lang === "tr" ? "Kaynağı aç" : "Open source"}</a>
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="source-section">
          <div className="section-intro">
            <p className="eyebrow dark">{lang === "tr" ? "GÜVENİLİR KAYNAK HARİTASI" : "TRUSTED SOURCE MAP"}</p>
            <h2>{lang === "tr" ? "Platformun besleneceği kaynak ekosistemi" : "The source ecosystem behind the platform"}</h2>
          </div>

          <div className="source-grid">
            {[
              ["Active Onco Kids", "https://www.activeoncokids.org/en/", lang === "tr" ? "Çocuk ve aile odaklı destek ilhamı" : "Child and family support inspiration"],
              ["ecancer", "https://ecancer.org/en/", lang === "tr" ? "Onkoloji eğitimi, haberler ve araştırma içeriği" : "Oncology education, news and research content"],
              ["European Cancer Organisation", "https://www.europeancancer.org/", lang === "tr" ? "Avrupa kanser politikası ve hasta savunuculuğu" : "European cancer policy and advocacy"],
              ["Cancer Research Institute", "https://www.cancerresearch.org/", lang === "tr" ? "İmmünoterapi araştırma farkındalığı" : "Immunotherapy research awareness"],
              ["CancerNetwork", "https://www.cancernetwork.com/", lang === "tr" ? "Klinik onkoloji haberleri" : "Clinical oncology news"],
              ["MSK", "https://www.mskcc.org/", lang === "tr" ? "Klinik bakım ve araştırma referansı" : "Clinical care and research reference"],
              ["Cancer Council Australia", "https://www.cancer.org.au/", lang === "tr" ? "Kanıta dayalı hasta bilgisi ve destek" : "Evidence-based patient information and support"],
              ["World Cancer Day", "https://www.worldcancerday.org/", lang === "tr" ? "Farkındalık ve insan odaklı kampanya" : "Awareness and people-centered campaigns"],
              ["UICC", "https://www.uicc.org/", lang === "tr" ? "Küresel kanser kontrol ağı" : "Global cancer control network"]
            ].map(([name, url, desc]) => (
              <a key={name} className="source-card" href={url} target="_blank" rel="noreferrer">
                <strong>{name}</strong>
                <span>{desc}</span>
              </a>
            ))}
          </div>
        </section>

        <section className="platform-entry-section">
          <div>
            <h2>{lang === "tr" ? "Platforma geç" : "Enter the platform"}</h2>
            <p>
              {lang === "tr"
                ? "Karşılama portalı bilgilendirir. Platform katmanı ise AI Copilot, Knowledge Graph ve Splunk operasyonel izleme ile aksiyona dönüştürür."
                : "The welcome portal informs. The platform layer turns it into action through AI Copilot, Knowledge Graph and Splunk operational monitoring."}
            </p>
          </div>

          <div className="platform-entry-actions">
            <button onClick={() => setPage("copilot")}>AI Copilot</button>
            <button className="secondary" onClick={() => setPage("graph")}>Knowledge Graph</button>
          </div>
        </section>
      </div>
    );
  };
'''

kids_component = r'''
  const OncoKidsPage = () => (
    <div className="kids-page">
      <header className="kids-topbar">
        <button className="ghost-btn" onClick={() => setPage("landing")}>
          {lang === "tr" ? "← Ana Sayfa" : "← Home"}
        </button>

        <div className="language-control kids-lang">
          <label>{t.langLabel}</label>
          <select value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">English</option>
            <option value="tr">Türkçe</option>
          </select>
        </div>
      </header>

      <section className="kids-hero">
        <div>
          <p className="eyebrow dark">ONCO KIDS</p>
          <h1>{lang === "tr" ? "Çocuklar ve aileler için yumuşak kanser açıklamaları" : "Gentle cancer explanations for children and families"}</h1>
          <p>
            {lang === "tr"
              ? "Bu alan çocukları korkutmadan, sade ve umut veren bir dille konuşmayı kolaylaştırır. Tanı veya tedavi önerisi vermez; aile içi iletişimi ve doktorla konuşmayı destekler."
              : "This space helps families talk with children using gentle, simple and hopeful language. It does not provide diagnosis or treatment advice; it supports family communication and conversations with clinicians."}
          </p>

          <div className="kids-hero-actions">
            <button onClick={() => setPage("copilot")}>
              {lang === "tr" ? "Aile modu ile Copilot’u aç" : "Open Copilot in family mode"}
            </button>
          </div>
        </div>

        <div className="kids-sun-card">
          <div className="kids-sun"></div>
          <strong>{lang === "tr" ? "Amaç: korkutmak değil, anlatmayı kolaylaştırmak" : "Goal: not to frighten, but to make explaining easier"}</strong>
        </div>
      </section>

      <section className="kids-learning-grid">
        {[
          [
            lang === "tr" ? "Kanser nedir?" : "What is cancer?",
            lang === "tr" ? "Vücudumuz çok küçük yapı taşlarından oluşur. Bazen bazı hücreler olması gerektiğinden farklı davranabilir. Doktorlar bunu anlamak ve yardımcı olmak için çalışır." : "Our body is made of tiny building blocks. Sometimes some cells behave differently than they should. Doctors work to understand this and help."
          ],
          [
            lang === "tr" ? "Tedavi neden olur?" : "Why does treatment happen?",
            lang === "tr" ? "Tedavi, doktorların hastalığı kontrol etmeye veya azaltmaya çalıştığı bir süreçtir. Her kişinin tedavi yolu farklı olabilir." : "Treatment is how doctors try to control or reduce illness. Each person’s treatment journey can be different."
          ],
          [
            lang === "tr" ? "Çocuk ne yapabilir?" : "What can a child do?",
            lang === "tr" ? "Soru sormak, duygularını söylemek, resim çizmek, dinlenmek ve güvendiği yetişkinlerle konuşmak yardımcı olabilir." : "Asking questions, sharing feelings, drawing, resting and talking with trusted adults can help."
          ],
          [
            lang === "tr" ? "Aile nasıl destek olur?" : "How can family help?",
            lang === "tr" ? "Kısa ve dürüst cümleler kurmak, umut veren ama gerçekçi olmak, çocuğun duygularına alan açmak önemlidir." : "Use short and honest sentences, stay hopeful but realistic, and make space for the child’s feelings."
          ]
        ].map(([title, body]) => (
          <div className="kids-learn-card" key={title}>
            <strong>{title}</strong>
            <p>{body}</p>
          </div>
        ))}
      </section>

      <section className="kids-feeling-section">
        <div>
          <h2>{lang === "tr" ? "Bugün nasıl hissediyorsun?" : "How do you feel today?"}</h2>
          <p>{lang === "tr" ? "Bu küçük alan çocukların duygularını konuşmaya başlaması için tasarlanmıştır." : "This small area helps children start talking about feelings."}</p>
        </div>

        <div className="feeling-grid">
          {[
            lang === "tr" ? "Korkmuş" : "Scared",
            lang === "tr" ? "Meraklı" : "Curious",
            lang === "tr" ? "Üzgün" : "Sad",
            lang === "tr" ? "Umutlu" : "Hopeful"
          ].map((item) => (
            <button key={item}>{item}</button>
          ))}
        </div>
      </section>
    </div>
  );

'''

# Replace LandingPage block
# More flexible replacement: works whether LandingPage is written as () => ( or () => {
start = app.find("const LandingPage")
end = app.find("const KnowledgeGraph")

if start == -1 or end == -1 or end <= start:
    raise RuntimeError("Could not find LandingPage or KnowledgeGraph in App.jsx.")

# Keep indentation consistent
app = app[:start] + new_landing.lstrip() + "\n\n" + kids_component + "\n  " + app[end:]

# Add kids page route
app = app.replace(
'''  if (page === "landing") return <LandingPage />;
  if (page === "graph") return <KnowledgeGraph />;''',
'''  if (page === "landing") return <LandingPage />;
  if (page === "kids") return <OncoKidsPage />;
  if (page === "graph") return <KnowledgeGraph />;'''
)

app_path.write_text(app, encoding="utf-8")

css += r'''

/* Step 16: sea background, aligned navigation, Onco Kids internal page, animated stats */

.portal-topnav {
  position: fixed;
  left: 24px;
  right: 24px;
  top: 18px;
  z-index: 30;
  height: 58px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 18px;
  padding: 8px 12px 8px 18px;
  border-radius: 999px;
  background: rgba(8, 22, 48, 0.56);
  border: 1px solid rgba(255,255,255,0.22);
  backdrop-filter: blur(18px);
  box-shadow: 0 18px 60px rgba(15,23,42,0.18);
}

.portal-brand {
  color: white;
  font-weight: 950;
  letter-spacing: -0.02em;
  cursor: pointer;
  white-space: nowrap;
}

.portal-tabs {
  display: flex;
  justify-content: center;
  gap: 4px;
  overflow-x: auto;
  scrollbar-width: none;
}

.portal-tabs::-webkit-scrollbar {
  display: none;
}

.portal-tabs button {
  border: none;
  background: transparent;
  color: rgba(255,255,255,0.86);
  font-weight: 850;
  padding: 9px 12px;
  border-radius: 999px;
  cursor: pointer;
  white-space: nowrap;
}

.portal-tabs button:hover {
  background: rgba(255,255,255,0.14);
  color: white;
}

.nav-lang {
  position: static !important;
  display: flex !important;
  align-items: center;
  gap: 10px;
}

.nav-lang label {
  color: white;
  font-weight: 850;
}

.nav-lang select {
  width: auto;
  min-width: 128px;
  color: white;
  background: rgba(255,255,255,0.16);
  border-color: rgba(255,255,255,0.28);
  border-radius: 999px;
  padding: 8px 12px;
}

.nav-lang option {
  color: #111827;
}

.calm-sea-hero {
  min-height: 780px !important;
  padding: 150px 64px 120px !important;
  grid-template-columns: minmax(0, 1.05fr) minmax(360px, 0.75fr) !important;
  background:
    linear-gradient(90deg, rgba(4, 16, 38, 0.72), rgba(4, 16, 38, 0.38), rgba(4, 16, 38, 0.20)),
    linear-gradient(180deg, rgba(4, 16, 38, 0.30), rgba(248,251,255,0.08)),
    url("/onco-sea-hero.png") center / cover no-repeat !important;
}

.calm-sea-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 18% 25%, rgba(255,255,255,0.26), transparent 22%),
    radial-gradient(circle at 80% 22%, rgba(255,224,180,0.22), transparent 28%);
  pointer-events: none;
}

.hero-glass-panel {
  position: relative;
  z-index: 2;
  padding: 28px;
  border-radius: 32px;
  background: rgba(255,255,255,0.18);
  border: 1px solid rgba(255,255,255,0.34);
  backdrop-filter: blur(18px);
  color: white;
  box-shadow: 0 26px 80px rgba(15,23,42,0.22);
}

.hero-glass-panel h3 {
  font-size: 28px;
  margin: 18px 0 8px;
}

.hero-glass-panel p {
  color: rgba(255,255,255,0.9);
  line-height: 1.65;
}

.breathing-orb {
  width: 120px;
  height: 120px;
  border-radius: 999px;
  background:
    radial-gradient(circle at 35% 30%, #ffffff, #bae6fd 38%, #2dd4bf 80%);
  box-shadow: 0 0 70px rgba(186,230,253,0.72);
  animation: breathe 4.5s ease-in-out infinite;
}

@keyframes breathe {
  0%, 100% { transform: scale(1); opacity: .88; }
  50% { transform: scale(1.08); opacity: 1; }
}

.portal-section {
  max-width: 1180px;
  margin: 66px auto;
  padding: 0 24px;
  scroll-margin-top: 90px;
}

.flow-steps {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.flow-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 24px;
  padding: 22px;
  box-shadow: 0 20px 60px rgba(15,23,42,0.10);
  position: relative;
  overflow: hidden;
}

.flow-card::after {
  content: "";
  position: absolute;
  width: 120px;
  height: 120px;
  right: -50px;
  bottom: -50px;
  border-radius: 999px;
  background: rgba(59,130,246,0.10);
}

.flow-card div {
  width: 38px;
  height: 38px;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: #1d4ed8;
  color: white;
  font-weight: 950;
  margin-bottom: 16px;
}

.flow-card strong,
.flow-card span {
  display: block;
}

.flow-card strong {
  font-size: 18px;
  color: #0f172a;
}

.flow-card span {
  margin-top: 8px;
  color: #475569;
  line-height: 1.5;
}

/* Animated cancer burden */

.animated-burden {
  scroll-margin-top: 90px;
}

.improved-stats .stat-panel {
  min-height: 310px !important;
  transform: translateY(0);
  animation: statFloat 6s ease-in-out infinite;
}

.improved-stats .stat-panel:nth-child(2) {
  animation-delay: .5s;
}

.improved-stats .stat-panel:nth-child(3) {
  animation-delay: 1s;
}

.improved-stats .stat-panel:nth-child(4) {
  animation-delay: 1.5s;
}

@keyframes statFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-7px); }
}

.stat-number {
  font-size: clamp(34px, 4vw, 56px) !important;
  letter-spacing: -0.06em;
  line-height: 1;
  white-space: normal;
  overflow-wrap: anywhere;
}

.stat-number.smaller {
  font-size: clamp(30px, 3.4vw, 44px) !important;
  letter-spacing: -0.03em;
}

.compact-stat strong {
  word-break: normal;
}

.stat-progress {
  position: relative;
  height: 8px;
  border-radius: 999px;
  background: rgba(255,255,255,0.22);
  overflow: hidden;
  margin-top: 18px;
}

.stat-progress i {
  position: absolute;
  inset: 0 auto 0 0;
  display: block;
  border-radius: 999px;
  background: rgba(255,255,255,0.75);
  animation: progressGrow 2.4s ease both;
}

@keyframes progressGrow {
  from { width: 0; }
}

.stat-panel p {
  font-size: 16px;
  line-height: 1.45 !important;
}

/* Onco Kids internal page */

.kids-page {
  min-height: 100vh;
  background:
    radial-gradient(circle at 20% 20%, rgba(253, 186, 116, 0.24), transparent 28%),
    radial-gradient(circle at 80% 10%, rgba(125, 211, 252, 0.28), transparent 30%),
    linear-gradient(180deg, #fff7ed, #eff6ff);
  color: #0f172a;
}

.kids-topbar {
  max-width: 1180px;
  margin: 0 auto;
  padding: 24px;
  display: flex;
  justify-content: space-between;
  gap: 18px;
  align-items: center;
}

.kids-lang {
  position: static !important;
  color: #0f172a;
}

.kids-lang label {
  color: #0f172a;
}

.kids-lang select {
  color: #0f172a;
  background: white;
  border-color: #e2e8f0;
}

.kids-hero {
  max-width: 1180px;
  margin: 0 auto;
  padding: 34px 24px 40px;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 28px;
  align-items: center;
}

.kids-hero h1 {
  font-size: clamp(42px, 5vw, 68px);
  line-height: 0.98;
  letter-spacing: -0.05em;
  color: #7c2d12;
}

.kids-hero p {
  font-size: 19px;
  color: #7c2d12;
  line-height: 1.7;
}

.kids-hero-actions button {
  border: none;
  border-radius: 999px;
  padding: 14px 20px;
  background: #fb923c;
  color: white;
  font-weight: 950;
  cursor: pointer;
}

.kids-sun-card {
  min-height: 360px;
  border-radius: 38px;
  display: grid;
  place-items: center;
  text-align: center;
  padding: 32px;
  background:
    radial-gradient(circle at center, rgba(255,255,255,0.8), transparent 34%),
    linear-gradient(135deg, #ffedd5, #ccfbf1);
  border: 1px solid rgba(251,146,60,0.25);
  box-shadow: 0 26px 80px rgba(15,23,42,0.12);
}

.kids-sun {
  width: 150px;
  height: 150px;
  border-radius: 999px;
  background: radial-gradient(circle at 35% 30%, #fff, #fde68a 45%, #fb923c);
  box-shadow: 0 0 70px rgba(251,146,60,0.36);
  animation: breathe 4s ease-in-out infinite;
}

.kids-sun-card strong {
  display: block;
  max-width: 360px;
  font-size: 24px;
  color: #7c2d12;
}

.kids-learning-grid {
  max-width: 1180px;
  margin: 0 auto;
  padding: 24px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.kids-learn-card {
  background: rgba(255,255,255,0.86);
  border: 1px solid rgba(251,146,60,0.22);
  border-radius: 26px;
  padding: 22px;
  box-shadow: 0 20px 60px rgba(15,23,42,0.09);
}

.kids-learn-card strong {
  display: block;
  color: #9a3412;
  font-size: 20px;
}

.kids-learn-card p {
  color: #7c2d12;
  line-height: 1.6;
}

.kids-feeling-section {
  max-width: 1180px;
  margin: 20px auto 70px;
  padding: 28px;
  border-radius: 32px;
  background: white;
  border: 1px solid #fed7aa;
  box-shadow: 0 20px 60px rgba(15,23,42,0.09);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  align-items: center;
}

.kids-feeling-section h2 {
  font-size: 34px;
  margin: 0 0 8px;
  color: #7c2d12;
}

.kids-feeling-section p {
  color: #7c2d12;
}

.feeling-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.feeling-grid button {
  border: none;
  border-radius: 20px;
  background: #ffedd5;
  color: #9a3412;
  padding: 18px;
  font-weight: 950;
  cursor: pointer;
}

/* Responsive navigation */

@media (max-width: 1100px) {
  .portal-topnav {
    grid-template-columns: 1fr auto;
    height: auto;
    border-radius: 28px;
  }

  .portal-brand {
    grid-column: 1;
  }

  .nav-lang {
    grid-column: 2;
  }

  .portal-tabs {
    grid-column: 1 / 3;
    justify-content: flex-start;
  }

  .flow-steps,
  .kids-learning-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .calm-sea-hero {
    grid-template-columns: 1fr !important;
  }
}

@media (max-width: 700px) {
  .portal-topnav {
    left: 12px;
    right: 12px;
    top: 10px;
  }

  .portal-brand {
    font-size: 14px;
  }

  .portal-tabs button {
    font-size: 13px;
    padding: 8px 9px;
  }

  .nav-lang label {
    display: none;
  }

  .nav-lang select {
    min-width: 100px;
  }

  .calm-sea-hero {
    padding: 170px 24px 80px !important;
  }

  .hero-glass-panel {
    padding: 20px;
  }

  .flow-steps,
  .kids-learning-grid,
  .kids-hero,
  .kids-feeling-section {
    grid-template-columns: 1fr;
  }

  .kids-topbar {
    flex-direction: column;
    align-items: stretch;
  }
}
'''

css_path.write_text(css, encoding="utf-8")

print("✅ Step 16 applied: sea background, top navigation, internal Onco Kids page, animated stats, and overflow fixes.")

