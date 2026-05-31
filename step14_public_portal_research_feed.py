from pathlib import Path
import re

path = Path("frontend/src/App.jsx")
css_path = Path("frontend/src/App.css")

app = path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

new_landing = r'''  const LandingPage = () => (
    <div className="landing-page portal-page">
      <section className="portal-hero">
        <div className="language-control landing-lang">
          <label>{t.langLabel}</label>
          <select value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">English</option>
            <option value="tr">Türkçe</option>
          </select>
        </div>

        <div className="portal-copy">
          <p className="eyebrow">ONCOCONNECT AI PUBLIC PORTAL</p>
          <h1>
            {lang === "tr"
              ? "Kanser yolculuğunda güvenli bilgi, destek ve AI rehberliği"
              : "Safe cancer support, research awareness and AI guidance"}
          </h1>

          <p className="portal-subtitle">
            {lang === "tr"
              ? "Hastalar, hasta yakınları, doktorlar, araştırmacılar, STK’lar ve destek ekipleri için iki katmanlı bir platform: önce güvenilir bilgi ve araştırma farkındalığı, sonra AI Copilot ve Splunk destekli operasyonel izleme."
              : "A two-layer platform for patients, caregivers, clinicians, researchers, NGOs and support teams: first trusted information and research awareness, then AI Copilot and Splunk-powered operational monitoring."}
          </p>

          <div className="portal-actions">
            <button onClick={() => setPage("copilot")}>
              {lang === "tr" ? "AI Copilot’u Başlat" : "Launch AI Copilot"}
            </button>
            <button className="secondary" onClick={() => setPage("graph")}>
              {lang === "tr" ? "Knowledge Graph’i Aç" : "Open Knowledge Graph"}
            </button>
            <a className="soft-link" href="#research-feed">
              {lang === "tr" ? "Araştırma Akışını Gör" : "View Research Feed"}
            </a>
          </div>

          <div className="portal-note">
            {lang === "tr"
              ? "Bu platform tanı veya tedavi önerisi vermez. Bilgileri doktor görüşmesine hazırlık, güvenilir kaynaklara yönlendirme ve destek koordinasyonu için sunar."
              : "This platform does not provide diagnosis or treatment advice. It supports doctor-visit preparation, trusted source navigation and support coordination."}
          </div>
        </div>

        <div className="calm-visual">
          <div className="glow-circle main">
            <span>OncoConnect<br />AI</span>
          </div>
          <div className="soft-bubble b1">{lang === "tr" ? "Hasta" : "Patient"}</div>
          <div className="soft-bubble b2">{lang === "tr" ? "Aile" : "Family"}</div>
          <div className="soft-bubble b3">{lang === "tr" ? "Doktor" : "Doctor"}</div>
          <div className="soft-bubble b4">{lang === "tr" ? "Araştırma" : "Research"}</div>
          <div className="soft-bubble b5">Splunk</div>
          <div className="calm-line l1"></div>
          <div className="calm-line l2"></div>
          <div className="calm-line l3"></div>
        </div>
      </section>

      <section className="need-section">
        <div className="section-intro">
          <p className="eyebrow dark">{lang === "tr" ? "BUGÜN NEYE İHTİYACINIZ VAR?" : "WHAT DO YOU NEED TODAY?"}</p>
          <h2>{lang === "tr" ? "Kullanıcıyı doğru kapıya yönlendiren karşılama alanı" : "A welcome layer that routes users to the right support path"}</h2>
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
              lang === "tr" ? "Yeni araştırmaları takip etmek istiyorum" : "I want to follow new cancer research",
              lang === "tr" ? "Klinik çalışmalar, immünoterapi, erken tanı ve hasta destek kaynakları için güvenli kaynak akışı." : "A safe source-aware feed for trials, immunotherapy, early detection and patient support.",
              "feed"
            ],
            [
              lang === "tr" ? "Çocuklar ve aileler için daha yumuşak bilgi istiyorum" : "I want softer information for children and families",
              lang === "tr" ? "Onco Kids alanı korkutmadan, sade ve umut veren açıklamalar sunar." : "Onco Kids gives gentle, simple and hopeful explanations.",
              "kids"
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
                if (target === "feed") document.getElementById("research-feed")?.scrollIntoView({ behavior: "smooth" });
                if (target === "kids") document.getElementById("onco-kids")?.scrollIntoView({ behavior: "smooth" });
              }}
            >
              <strong>{title}</strong>
              <span>{body}</span>
            </button>
          ))}
        </div>
      </section>

      <section className="statistics-section">
        <div className="section-intro">
          <p className="eyebrow dark">{lang === "tr" ? "KANSER YÜKÜ" : "CANCER BURDEN"}</p>
          <h2>{lang === "tr" ? "Veri, korkutmak için değil; erken destek ve koordinasyon için" : "Data is not for fear; it is for earlier support and coordination"}</h2>
        </div>

        <div className="stat-world-grid">
          <div className="stat-panel global">
            <small>{lang === "tr" ? "Dünya geneli, 2022" : "Worldwide, 2022"}</small>
            <strong>~20M</strong>
            <span>{lang === "tr" ? "yeni kanser vakası" : "new cancer cases"}</span>
            <p>{lang === "tr" ? "GLOBOCAN 2022 tahminleri dünya genelinde yaklaşık 20 milyon yeni vaka ve 9,7 milyon ölüm bildiriyor." : "GLOBOCAN 2022 estimates around 20 million new cases and 9.7 million deaths worldwide."}</p>
          </div>

          <div className="stat-panel global">
            <small>{lang === "tr" ? "Dünya geneli, 2022" : "Worldwide, 2022"}</small>
            <strong>~9.7M</strong>
            <span>{lang === "tr" ? "kanser ölümü" : "cancer deaths"}</span>
            <p>{lang === "tr" ? "Bu sayı destek, erken farkındalık, tarama ve bakım koordinasyonunun önemini gösterir." : "This highlights the importance of support, awareness, screening and care coordination."}</p>
          </div>

          <div className="stat-panel turkiye">
            <small>{lang === "tr" ? "Türkiye bağlamı" : "Türkiye context"}</small>
            <strong>GLOBOCAN</strong>
            <span>{lang === "tr" ? "ülke bazlı kanser istatistikleri" : "country-level cancer statistics"}</span>
            <p>{lang === "tr" ? "Türkiye için akciğer, meme ve kolorektal kanserler öne çıkan başlıklar arasındadır." : "For Türkiye, lung, breast and colorectal cancers are among the key cancer burden areas."}</p>
          </div>

          <div className="stat-panel mission">
            <small>EU Cancer Mission</small>
            <strong>2030</strong>
            <span>{lang === "tr" ? "yaşam kalitesi ve bakım hedefleri" : "quality of life and care goals"}</span>
            <p>{lang === "tr" ? "AB Kanser Misyonu; önleme, tedavi, yaşam kalitesi ve kanserden etkilenen aileleri kapsayan hedeflerle ilerler." : "The EU Cancer Mission focuses on prevention, cure, quality of life and people affected by cancer including families."}</p>
          </div>
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
            },
            {
              category: lang === "tr" ? "Hasta ve aile desteği" : "Patient and family support",
              title: lang === "tr" ? "Güvenilir hasta bilgi kaynakları" : "Trusted patient information sources",
              body: lang === "tr" ? "Tedavi, yan etkiler, yaşam kalitesi ve pratik destek konularında kaynaklar hasta-hekim iletişimini güçlendirebilir." : "Resources on treatment, side effects, quality of life and practical support can strengthen patient-clinician communication.",
              source: "Cancer Council Australia / MSK",
              url: "https://www.cancer.org.au/",
              ask: lang === "tr" ? "Bu semptomlar için hangi güvenilir hasta bilgi kaynaklarını okuyabilirim?" : "Which reliable patient information resources can I read about these symptoms?"
            },
            {
              category: lang === "tr" ? "Avrupa kanser politikası" : "European cancer policy",
              title: lang === "tr" ? "Bakım kalitesi, multidisipliner yaklaşım ve hasta savunuculuğu" : "Care quality, multidisciplinary care and patient advocacy",
              body: lang === "tr" ? "Avrupa kanser ekosistemi kalite, erişim, hasta savunuculuğu ve multidisipliner bakım konularını vurgular." : "The European cancer ecosystem emphasizes quality, access, patient advocacy and multidisciplinary care.",
              source: "European Cancer Organisation / UICC",
              url: "https://www.europeancancer.org/",
              ask: lang === "tr" ? "Bu alanda hasta savunuculuğu veya STK desteği nasıl bulunabilir?" : "How can patient advocacy or NGO support be found in this area?"
            },
            {
              category: lang === "tr" ? "Farkındalık kampanyaları" : "Awareness campaigns",
              title: "United by Unique",
              body: lang === "tr" ? "World Cancer Day 2025–2027 teması, bakımın merkezine insan hikâyelerini ve kişiye özgü ihtiyaçları koyar." : "The World Cancer Day 2025–2027 theme places people and unique stories at the center of care.",
              source: "World Cancer Day / UICC",
              url: "https://www.worldcancerday.org/",
              ask: lang === "tr" ? "Kendi hikâyemi ve ihtiyaçlarımı bakım ekibime nasıl daha iyi anlatabilirim?" : "How can I communicate my story and needs more clearly to my care team?"
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
                <a href={item.url} target="_blank" rel="noreferrer">
                  {lang === "tr" ? "Kaynağı aç" : "Open source"}
                </a>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section id="onco-kids" className="kids-section">
        <div className="kids-copy">
          <p className="eyebrow dark">ONCO KIDS</p>
          <h2>{lang === "tr" ? "Çocuklar ve aileler için yumuşak, umut veren açıklamalar" : "Gentle, hopeful explanations for children and families"}</h2>
          <p>
            {lang === "tr"
              ? "Onco Kids alanı çocukları korkutmadan, aile içi konuşmayı kolaylaştıran sade açıklamalar sunmak için tasarlanır. Tıbbi karar vermez; anlamayı, duygusal hazırlığı ve doğru uzmanla konuşmayı destekler."
              : "Onco Kids is designed to support simple, non-frightening explanations that help families talk. It does not make medical decisions; it supports understanding, emotional preparation and conversations with the right professionals."}
          </p>

          <div className="kids-actions">
            <a href="https://www.activeoncokids.org/en/" target="_blank" rel="noreferrer">
              Active Onco Kids
            </a>
            <button onClick={() => setPage("copilot")}>
              {lang === "tr" ? "Aile modu ile Copilot’u aç" : "Open Copilot in family mode"}
            </button>
          </div>
        </div>

        <div className="kids-card-stack">
          <div className="kids-card peach">
            <strong>{lang === "tr" ? "Korkutmadan anlat" : "Explain gently"}</strong>
            <span>{lang === "tr" ? "Kısa, sade, umut veren dil" : "Short, simple, hopeful language"}</span>
          </div>
          <div className="kids-card mint">
            <strong>{lang === "tr" ? "Aileyi güçlendir" : "Empower families"}</strong>
            <span>{lang === "tr" ? "Doktora sorulacak sorular" : "Questions for care teams"}</span>
          </div>
          <div className="kids-card lavender">
            <strong>{lang === "tr" ? "Duyguyu unutma" : "Include emotions"}</strong>
            <span>{lang === "tr" ? "Kaygı, umut, destek" : "Anxiety, hope, support"}</span>
          </div>
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
          <button onClick={() => setPage("copilot")}>
            {lang === "tr" ? "AI Copilot" : "AI Copilot"}
          </button>
          <button className="secondary" onClick={() => setPage("graph")}>
            Knowledge Graph
          </button>
        </div>
      </section>
    </div>
  );
'''

pattern = r"  const LandingPage = \(\) => \([\s\S]*?\n  const KnowledgeGraph = \(\) => \("
replacement = new_landing + "\n\n  const KnowledgeGraph = () => ("

app, count = re.subn(pattern, replacement, app)

if count != 1:
    raise RuntimeError("LandingPage block could not be replaced. Make sure step13 was applied first.")

css += r'''

/* Step 14: Public Portal, Research Feed, Onco Kids */

.portal-page {
  background:
    radial-gradient(circle at top left, rgba(59, 130, 246, 0.16), transparent 28%),
    radial-gradient(circle at bottom right, rgba(20, 184, 166, 0.14), transparent 30%),
    #f7fbff;
}

.portal-hero {
  position: relative;
  min-height: 86vh;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 46px;
  align-items: center;
  padding: 78px 64px 115px;
  color: white;
  overflow: hidden;
  background:
    linear-gradient(135deg, rgba(6, 24, 47, 0.92), rgba(30, 58, 138, 0.84)),
    radial-gradient(circle at 80% 20%, rgba(216, 180, 254, 0.48), transparent 34%),
    radial-gradient(circle at 20% 85%, rgba(45, 212, 191, 0.32), transparent 34%),
    linear-gradient(135deg, #06182f, #1e3a8a 52%, #7c3aed);
}

.portal-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.055) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.055) 1px, transparent 1px);
  background-size: 46px 46px;
  mask-image: linear-gradient(to bottom, black, transparent 88%);
}

.portal-copy,
.calm-visual,
.portal-hero .language-control {
  position: relative;
  z-index: 2;
}

.portal-copy h1 {
  font-size: 64px;
  line-height: 0.98;
  max-width: 920px;
}

.portal-subtitle {
  font-size: 21px;
  line-height: 1.65;
  color: rgba(255,255,255,0.92);
  max-width: 900px;
}

.portal-actions {
  display: flex;
  gap: 13px;
  flex-wrap: wrap;
  margin-top: 26px;
}

.portal-actions button,
.platform-entry-actions button,
.kids-actions button {
  border: none;
  border-radius: 999px;
  padding: 14px 20px;
  font-weight: 950;
  cursor: pointer;
  background: white;
  color: #1d4ed8;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.18);
}

.portal-actions button.secondary,
.platform-entry-actions button.secondary {
  background: rgba(255,255,255,0.14);
  color: white;
  border: 1px solid rgba(255,255,255,0.28);
}

.soft-link,
.kids-actions a {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 13px 18px;
  font-weight: 900;
  text-decoration: none;
  color: white;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.22);
}

.portal-note {
  margin-top: 22px;
  padding: 15px 18px;
  border-radius: 20px;
  max-width: 820px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.22);
  color: rgba(255,255,255,0.88);
  line-height: 1.55;
}

.calm-visual {
  min-height: 500px;
  border-radius: 42px;
  background:
    radial-gradient(circle at center, rgba(255,255,255,0.2), transparent 26%),
    rgba(255,255,255,0.09);
  border: 1px solid rgba(255,255,255,0.18);
  backdrop-filter: blur(20px);
  overflow: hidden;
  box-shadow: inset 0 0 90px rgba(255,255,255,0.05), 0 30px 90px rgba(15,23,42,0.24);
}

.glow-circle.main {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 190px;
  height: 190px;
  transform: translate(-50%, -50%);
  border-radius: 999px;
  display: grid;
  place-items: center;
  text-align: center;
  font-size: 25px;
  font-weight: 950;
  color: #1e3a8a;
  background: linear-gradient(135deg, #ffffff, #dbeafe);
  box-shadow: 0 0 70px rgba(255,255,255,0.55);
  animation: pulseSoft 4s ease-in-out infinite;
}

.soft-bubble {
  position: absolute;
  padding: 11px 16px;
  border-radius: 999px;
  font-weight: 900;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.28);
  animation: floatNode 5.5s ease-in-out infinite;
}

.b1 { left: 9%; top: 18%; }
.b2 { right: 10%; top: 17%; animation-delay: .5s; }
.b3 { right: 8%; bottom: 18%; animation-delay: 1s; }
.b4 { left: 10%; bottom: 18%; animation-delay: 1.4s; }
.b5 { left: 50%; top: 8%; transform: translateX(-50%); animation-delay: 1.8s; }

.calm-line {
  position: absolute;
  left: 16%;
  top: 50%;
  width: 68%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.55), transparent);
  opacity: .7;
}

.calm-line.l2 { transform: rotate(55deg); }
.calm-line.l3 { transform: rotate(-55deg); }

@keyframes pulseSoft {
  0%, 100% { box-shadow: 0 0 52px rgba(255,255,255,0.45); }
  50% { box-shadow: 0 0 86px rgba(45,212,191,0.55); }
}

.need-section,
.statistics-section,
.research-feed-section,
.kids-section,
.source-section,
.platform-entry-section {
  max-width: 1180px;
  margin: 42px auto;
  padding: 0 24px;
}

.need-section {
  margin-top: -66px;
  position: relative;
  z-index: 4;
}

.section-intro {
  margin-bottom: 18px;
}

.section-intro h2 {
  font-size: 36px;
  margin: 6px 0;
  color: #0f172a;
}

.section-intro p {
  color: #475569;
  line-height: 1.65;
  max-width: 860px;
}

.need-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.need-card {
  text-align: left;
  background: rgba(255,255,255,0.94);
  border: 1px solid #e2e8f0;
  border-radius: 24px;
  padding: 22px;
  min-height: 168px;
  cursor: pointer;
  box-shadow: 0 24px 70px rgba(15,23,42,0.12);
  transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
}

.need-card:hover {
  transform: translateY(-5px);
  border-color: #93c5fd;
  box-shadow: 0 30px 90px rgba(15,23,42,0.18);
}

.need-card strong,
.need-card span {
  display: block;
}

.need-card strong {
  font-size: 18px;
  color: #0f172a;
}

.need-card span {
  margin-top: 10px;
  color: #475569;
  line-height: 1.5;
}

.stat-world-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.stat-panel {
  border-radius: 26px;
  padding: 24px;
  color: white;
  min-height: 255px;
  box-shadow: 0 24px 70px rgba(15,23,42,0.14);
  position: relative;
  overflow: hidden;
}

.stat-panel::after {
  content: "";
  position: absolute;
  width: 180px;
  height: 180px;
  right: -60px;
  bottom: -70px;
  border-radius: 999px;
  background: rgba(255,255,255,0.15);
}

.stat-panel.global { background: linear-gradient(135deg, #1e3a8a, #2563eb); }
.stat-panel.turkiye { background: linear-gradient(135deg, #0f766e, #14b8a6); }
.stat-panel.mission { background: linear-gradient(135deg, #6d28d9, #a855f7); }

.stat-panel small,
.stat-panel strong,
.stat-panel span,
.stat-panel p {
  position: relative;
  z-index: 1;
}

.stat-panel small,
.stat-panel span {
  display: block;
  opacity: .9;
  font-weight: 800;
}

.stat-panel strong {
  display: block;
  font-size: 44px;
  margin: 12px 0 4px;
}

.stat-panel p {
  line-height: 1.55;
  color: rgba(255,255,255,0.88);
}

.feed-intro {
  display: grid;
  grid-template-columns: 0.9fr 1.1fr;
  gap: 24px;
  align-items: end;
}

.feed-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.feed-card {
  background: white;
  border-radius: 26px;
  border: 1px solid #e2e8f0;
  padding: 22px;
  box-shadow: 0 24px 70px rgba(15,23,42,0.10);
  display: flex;
  flex-direction: column;
  min-height: 390px;
}

.feed-category {
  align-self: flex-start;
  border-radius: 999px;
  padding: 7px 11px;
  font-size: 12px;
  font-weight: 950;
  color: #3730a3;
  background: #eef2ff;
}

.feed-card h3 {
  margin: 14px 0 8px;
  font-size: 21px;
  color: #0f172a;
}

.feed-card p {
  color: #475569;
  line-height: 1.58;
}

.doctor-question {
  margin-top: auto;
  background: #f8fafc;
  border-radius: 18px;
  padding: 14px;
  border: 1px solid #e2e8f0;
}

.doctor-question strong,
.doctor-question span {
  display: block;
}

.doctor-question strong {
  color: #1d4ed8;
  font-size: 13px;
}

.doctor-question span {
  margin-top: 6px;
  color: #334155;
  line-height: 1.45;
}

.feed-footer {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid #e2e8f0;
}

.feed-footer span {
  font-weight: 850;
  color: #64748b;
}

.feed-footer a {
  color: #1d4ed8;
  font-weight: 900;
  text-decoration: none;
}

.kids-section {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 28px;
  align-items: center;
  border-radius: 34px;
  padding: 34px;
  background:
    radial-gradient(circle at top right, rgba(253, 186, 116, 0.30), transparent 36%),
    radial-gradient(circle at bottom left, rgba(125, 211, 252, 0.30), transparent 36%),
    #fff7ed;
  border: 1px solid #fed7aa;
  box-shadow: 0 24px 70px rgba(15,23,42,0.10);
}

.kids-copy h2 {
  font-size: 38px;
  margin: 8px 0;
  color: #7c2d12;
}

.kids-copy p {
  color: #7c2d12;
  line-height: 1.7;
}

.kids-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 18px;
}

.kids-actions a {
  background: white;
  color: #c2410c;
  border-color: #fed7aa;
}

.kids-actions button {
  background: #fb923c;
  color: white;
}

.kids-card-stack {
  display: grid;
  gap: 14px;
}

.kids-card {
  border-radius: 24px;
  padding: 22px;
  color: #0f172a;
  box-shadow: 0 18px 50px rgba(15,23,42,0.10);
}

.kids-card strong,
.kids-card span {
  display: block;
}

.kids-card strong {
  font-size: 21px;
}

.kids-card span {
  margin-top: 6px;
  color: #475569;
}

.kids-card.peach { background: #ffedd5; }
.kids-card.mint { background: #ccfbf1; }
.kids-card.lavender { background: #ede9fe; }

.source-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.source-card {
  display: block;
  text-decoration: none;
  color: #0f172a;
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 22px;
  padding: 20px;
  box-shadow: 0 18px 50px rgba(15,23,42,0.08);
  transition: transform .2s ease, border-color .2s ease;
}

.source-card:hover {
  transform: translateY(-4px);
  border-color: #93c5fd;
}

.source-card strong,
.source-card span {
  display: block;
}

.source-card span {
  margin-top: 6px;
  color: #64748b;
  line-height: 1.45;
}

.platform-entry-section {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 24px;
  align-items: center;
  background: linear-gradient(135deg, #0f172a, #1e3a8a);
  color: white;
  border-radius: 32px;
  padding: 32px;
  box-shadow: 0 24px 70px rgba(15,23,42,0.18);
}

.platform-entry-section h2 {
  margin: 0 0 8px;
  font-size: 34px;
}

.platform-entry-section p {
  color: rgba(255,255,255,0.86);
  line-height: 1.65;
}

.platform-entry-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

@media (max-width: 1100px) {
  .need-grid,
  .feed-grid,
  .source-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .stat-world-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .portal-copy h1 {
    font-size: 52px;
  }
}

@media (max-width: 900px) {
  .portal-hero,
  .feed-intro,
  .kids-section,
  .platform-entry-section {
    grid-template-columns: 1fr;
  }

  .portal-hero {
    padding: 88px 24px 100px;
  }

  .portal-copy h1 {
    font-size: 42px;
  }

  .calm-visual {
    min-height: 420px;
  }

  .need-grid,
  .feed-grid,
  .source-grid,
  .stat-world-grid {
    grid-template-columns: 1fr;
  }

  .platform-entry-actions {
    justify-content: flex-start;
  }
}
'''

path.write_text(app, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

print("✅ Public portal, research feed, statistics, Onco Kids, and trusted sources added.")
