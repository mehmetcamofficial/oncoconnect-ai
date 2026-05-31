from pathlib import Path

app = r'''
import { useMemo, useState } from "react";
import "./App.css";

const API_URL = "http://localhost:5050";

const patientPresets = {
  P999: {
    patientId: "P999",
    scenarioEN: "Critical symptoms after chemotherapy",
    scenarioTR: "Kemoterapi sonrası kritik semptom artışı",
    cancerType: "Breast Cancer",
    cancerTypeTR: "Meme Kanseri",
    treatmentStage: "Chemotherapy",
    treatmentStageTR: "Kemoterapi",
    city: "Istanbul",
    fatigue: 10,
    nausea: 9,
    pain: 9,
    mood: 1,
    noteEN: "Critical symptom escalation detected during demo.",
    noteTR: "Demo sırasında kritik semptom artışı tespit edildi."
  },
  P001: {
    patientId: "P001",
    scenarioEN: "High fatigue and nausea after chemotherapy",
    scenarioTR: "Kemoterapi sonrası yüksek halsizlik ve bulantı",
    cancerType: "Breast Cancer",
    cancerTypeTR: "Meme Kanseri",
    treatmentStage: "Chemotherapy",
    treatmentStageTR: "Kemoterapi",
    city: "Izmir",
    fatigue: 8,
    nausea: 7,
    pain: 3,
    mood: 2,
    noteEN: "Fatigue and nausea increased after chemotherapy.",
    noteTR: "Kemoterapi sonrası halsizlik ve bulantı arttı."
  },
  P002: {
    patientId: "P002",
    scenarioEN: "Radiotherapy follow-up with continuing fatigue",
    scenarioTR: "Radyoterapi sonrası devam eden yorgunluk",
    cancerType: "Lung Cancer",
    cancerTypeTR: "Akciğer Kanseri",
    treatmentStage: "Radiotherapy",
    treatmentStageTR: "Radyoterapi",
    city: "Ankara",
    fatigue: 6,
    nausea: 4,
    pain: 5,
    mood: 5,
    noteEN: "Fatigue continues after radiotherapy.",
    noteTR: "Radyoterapi sonrası yorgunluk devam ediyor."
  },
  P012: {
    patientId: "P012",
    scenarioEN: "Stable follow-up visit",
    scenarioTR: "Stabil takip görüşmesi",
    cancerType: "Colon Cancer",
    cancerTypeTR: "Kolon Kanseri",
    treatmentStage: "Follow-up",
    treatmentStageTR: "Takip",
    city: "Izmir",
    fatigue: 4,
    nausea: 3,
    pain: 2,
    mood: 7,
    noteEN: "Stable follow-up condition.",
    noteTR: "Takip sürecinde genel durum stabil."
  },
  P013: {
    patientId: "P013",
    scenarioEN: "Improving condition during immunotherapy",
    scenarioTR: "İmmünoterapi sürecinde iyileşen durum",
    cancerType: "Lymphoma",
    cancerTypeTR: "Lenfoma",
    treatmentStage: "Immunotherapy",
    treatmentStageTR: "İmmünoterapi",
    city: "Bursa",
    fatigue: 5,
    nausea: 3,
    pain: 2,
    mood: 6,
    noteEN: "Feeling better today.",
    noteTR: "Bugün daha iyi hissediyor."
  }
};

const text = {
  en: {
    langLabel: "Language",
    title: "OncoConnect AI Copilot",
    subtitle:
      "A patient support copilot that helps cancer patients, caregivers, and support teams turn symptom updates into care-ready guidance and Splunk-powered operational intelligence.",
    valueTitle: "What value does it provide?",
    valueText:
      "A user can select their situation, enter symptoms, receive a clear explanation, get doctor-visit questions, and send the event to Splunk so support teams can monitor high-risk cases.",
    points: ["Patient guidance", "Doctor visit preparation", "Risk prioritization", "Splunk monitoring"],
    metrics: ["Operational events in Splunk", "Chemotherapy records", "Monitoring follow-ups", "Live HEC event streaming"],
    who: "Who are you?",
    whoDesc: "Select the user perspective for the guidance.",
    help: "What do you need help with?",
    helpDesc: "The output adapts to your selected goal.",
    scenario: "Select patient scenario",
    scenarioDesc: "These are demo scenarios. Population-scale datasets are analyzed in Splunk dashboards.",
    symptoms: "Enter symptoms",
    symptomsDesc: "Risk model: fatigue + nausea + pain + (10 - mood)",
    send: "Send check-in to Splunk",
    generate: "Generate AI care guidance",
    copilotResult: "AI Copilot Result",
    whatMeans: "What this means",
    questions: "Questions to ask your doctor",
    copyQuestions: "Copy doctor questions",
    copied: "Copied",
    nextStep: "Suggested next step",
    splunkStatus: "Splunk pipeline status",
    safety:
      "Safety note: This tool does not provide diagnosis, treatment, or medication advice. It supports symptom tracking, doctor-visit preparation, and care coordination.",
    footerTitle: "Where the 15K+ records are used",
    footerText:
      "The frontend creates live check-in and AI summary events. Splunk dashboards analyze both these live events and the imported historical chemotherapy and monitoring datasets.",
    roles: {
      patient: ["I am a patient", "I want to understand my symptoms and prepare for my doctor visit."],
      caregiver: ["I am a caregiver", "I want to understand whether my loved one may need extra support."],
      support: ["I am a support organization", "I want to prioritize high-risk patients for outreach."]
    },
    goals: {
      symptoms: "Understand today’s symptoms",
      doctor: "Prepare questions for doctor visit",
      support: "Check whether extra support is needed"
    },
    cards: [
      ["Frontend", "Patient support experience"],
      ["Backend", "Risk score + AI summary event"],
      ["Splunk", "Monitoring, prioritization, dashboards"],
      ["Support team", "High-risk outreach queue"]
    ],
    notePlaceholder: "Describe what changed today...",
    ready: "No event sent yet.",
    loaded: "Scenario loaded. Send check-in to Splunk when ready.",
    changed: "Changes not sent yet.",
    sending: "Sending symptom check-in to Splunk HEC...",
    aiSending: "Generating AI support summary and sending it to Splunk...",
    backendFailed: "Backend connection failed. Start backend with: node server.js",
    aiFailed: "AI endpoint failed. Check backend server.",
    checkinFailed: "Check-in failed.",
    aiSummaryTitle: "AI Summary Event"
  },
  tr: {
    langLabel: "Dil",
    title: "OncoConnect AI Copilot",
    subtitle:
      "Kanser hastaları, hasta yakınları ve destek ekipleri için semptom güncellemelerini bakım hazırlığına, risk önceliklendirmesine ve Splunk destekli operasyonel içgörülere dönüştüren yapay zekâ destekli yardımcı.",
    valueTitle: "Bu araç ne işe yarar?",
    valueText:
      "Kullanıcı kendi durumunu seçer, semptomlarını girer, anlaşılır bir açıklama alır, doktora sorulacak soruları hazırlar ve olayı Splunk’a göndererek destek ekiplerinin yüksek riskli vakaları izlemesini sağlar.",
    points: ["Hasta rehberliği", "Doktor görüşmesi hazırlığı", "Risk önceliklendirme", "Splunk izleme"],
    metrics: ["Splunk operasyonel olayı", "Kemoterapi kaydı", "Takip/izlem kaydı", "Canlı HEC veri akışı"],
    who: "Kimsiniz?",
    whoDesc: "Çıktının hangi kullanıcı bakış açısına göre hazırlanacağını seçin.",
    help: "Ne konuda yardım istiyorsunuz?",
    helpDesc: "Copilot çıktısı seçtiğiniz amaca göre uyarlanır.",
    scenario: "Hasta senaryosu seçin",
    scenarioDesc: "Bunlar demo senaryolarıdır. Büyük ölçekli veri setleri Splunk dashboardlarında analiz edilir.",
    symptoms: "Semptomları girin",
    symptomsDesc: "Risk modeli: halsizlik + bulantı + ağrı + (10 - moral)",
    send: "Kontrolü Splunk’a gönder",
    generate: "AI bakım rehberi oluştur",
    copilotResult: "AI Copilot Sonucu",
    whatMeans: "Bu ne anlama geliyor?",
    questions: "Doktora sorulabilecek sorular",
    copyQuestions: "Doktor sorularını kopyala",
    copied: "Kopyalandı",
    nextStep: "Önerilen sonraki adım",
    splunkStatus: "Splunk veri akışı durumu",
    safety:
      "Güvenlik notu: Bu araç tanı, tedavi veya ilaç önerisi sunmaz. Semptom takibi, doktor görüşmesine hazırlık ve bakım koordinasyonu için destek sağlar.",
    footerTitle: "15K+ kayıt nerede kullanılıyor?",
    footerText:
      "Frontend canlı check-in ve AI summary olayları üretir. Splunk dashboardları bu canlı olayları ve içe aktarılan geçmiş kemoterapi/izlem veri setlerini birlikte analiz eder.",
    roles: {
      patient: ["Hastayım", "Semptomlarımı anlamak ve doktor görüşmesine hazırlanmak istiyorum."],
      caregiver: ["Hasta yakınıyım", "Yakınımın ekstra desteğe ihtiyacı olup olmadığını anlamak istiyorum."],
      support: ["Destek ekibiyim", "Yüksek riskli hastaları önceliklendirmek istiyorum."]
    },
    goals: {
      symptoms: "Bugünkü semptomları anlamak",
      doctor: "Doktor görüşmesine hazırlanmak",
      support: "Ek destek ihtiyacını kontrol etmek"
    },
    cards: [
      ["Frontend", "Hasta destek deneyimi"],
      ["Backend", "Risk skoru + AI özet olayı"],
      ["Splunk", "İzleme, önceliklendirme, dashboardlar"],
      ["Destek ekibi", "Yüksek riskli hasta kuyruğu"]
    ],
    notePlaceholder: "Bugün ne değiştiğini açıklayın...",
    ready: "Henüz olay gönderilmedi.",
    loaded: "Senaryo yüklendi. Hazır olduğunuzda kontrolü Splunk’a gönderin.",
    changed: "Değişiklikler henüz gönderilmedi.",
    sending: "Semptom kontrolü Splunk HEC’e gönderiliyor...",
    aiSending: "AI destek özeti oluşturuluyor ve Splunk’a gönderiliyor...",
    backendFailed: "Backend bağlantısı başarısız. Backend’i başlatın: node server.js",
    aiFailed: "AI endpoint başarısız. Backend’i kontrol edin.",
    checkinFailed: "Check-in gönderimi başarısız.",
    aiSummaryTitle: "AI Özet Olayı"
  }
};

function App() {
  const [lang, setLang] = useState("en");
  const t = text[lang];

  const [role, setRole] = useState("patient");
  const [goal, setGoal] = useState("doctor");
  const [form, setForm] = useState(patientPresets.P999);
  const [result, setResult] = useState(null);
  const [aiSummary, setAiSummary] = useState(null);
  const [splunkStatus, setSplunkStatus] = useState(text.en.ready);
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const riskScore = useMemo(() => {
    return Number(form.fatigue) + Number(form.nausea) + Number(form.pain) + (10 - Number(form.mood));
  }, [form]);

  const riskLevel = useMemo(() => {
    if (riskScore >= 25) return lang === "tr" ? "Kritik" : "Critical";
    if (riskScore >= 20) return lang === "tr" ? "Yüksek" : "High";
    if (riskScore >= 12) return lang === "tr" ? "Orta" : "Medium";
    return lang === "tr" ? "Düşük" : "Low";
  }, [riskScore, lang]);

  const riskClass = useMemo(() => {
    if (riskScore >= 25) return "critical";
    if (riskScore >= 20) return "high";
    if (riskScore >= 12) return "medium";
    return "low";
  }, [riskScore]);

  const symptomLabels = lang === "tr"
    ? { fatigue: "Halsizlik", nausea: "Bulantı", pain: "Ağrı", mood: "Moral" }
    : { fatigue: "Fatigue", nausea: "Nausea", pain: "Pain", mood: "Mood" };

  const update = (key, value) => {
    setForm({ ...form, [key]: value });
    setResult(null);
    setAiSummary(null);
    setCopied(false);
    setSplunkStatus(t.changed);
  };

  const selectPatient = (patientId) => {
    setForm(patientPresets[patientId]);
    setResult(null);
    setAiSummary(null);
    setCopied(false);
    setSplunkStatus(t.loaded);
  };

  const scenarioLabel = (p) => {
    return lang === "tr" ? p.scenarioTR : p.scenarioEN;
  };

  const visibleCancerType = (p = form) => {
    return lang === "tr" ? p.cancerTypeTR : p.cancerType;
  };

  const visibleTreatment = (p = form) => {
    return lang === "tr" ? p.treatmentStageTR : p.treatmentStage;
  };

  const visibleNote = () => {
    return lang === "tr" ? form.noteTR || form.noteEN : form.noteEN || form.noteTR;
  };

  const buildDoctorQuestions = () => {
    const questions = [];

    if (lang === "tr") {
      if (form.fatigue >= 7) questions.push("Halsizliğim yüksek. Bu tedavi aşamasında beklenen bir durum mu?");
      if (form.nausea >= 7) questions.push("Bulantım arttı. Bir sonraki randevudan önce neyi takip etmeliyim veya bildirmeliyim?");
      if (form.pain >= 7) questions.push("Ağrı seviyem yükseldi. Hangi durumda bakım ekibiyle acil iletişime geçmeliyim?");
      if (form.mood <= 3) questions.push("Moral puanım düşük. Duygusal destek için hangi seçenekler mevcut?");
      if (questions.length === 0) {
        questions.push("Mevcut semptomlarım tedavi aşamamla uyumlu mu?");
        questions.push("Bir sonraki randevuya kadar hangi belirtileri takip etmeliyim?");
      }
      questions.push("Hangi semptomlar acil iletişim gerektirir?");
      return questions;
    }

    if (form.fatigue >= 7) questions.push("My fatigue is high. Is this expected at this stage of treatment?");
    if (form.nausea >= 7) questions.push("My nausea has increased. What should I monitor or report before the next appointment?");
    if (form.pain >= 7) questions.push("My pain level is elevated. When should I contact the care team urgently?");
    if (form.mood <= 3) questions.push("My mood score is low. What support options are available for emotional wellbeing?");
    if (questions.length === 0) {
      questions.push("Are my current symptoms consistent with my treatment stage?");
      questions.push("What signs should I monitor before my next appointment?");
    }
    questions.push("Which symptoms should trigger immediate contact with the care team?");
    return questions;
  };

  const buildUserExplanation = () => {
    if (lang === "tr") {
      if (riskScore >= 25) return "Girdiğiniz değerlere göre semptom yükü belirgin şekilde yüksek görünüyor. Bu durum bakım ekibi değerlendirmesi veya destek ekibi takibi için önceliklendirilebilir.";
      if (riskScore >= 20) return "Semptomlarınız yüksek destek ihtiyacına işaret ediyor. Bakım ekibi veya hasta destek organizasyonu ile iletişime geçmek faydalı olabilir.";
      if (riskScore >= 12) return "Semptomlar orta düzeyde destek ihtiyacına işaret ediyor. Değişiklikleri takip etmek ve doktor görüşmesine sorularla hazırlanmak faydalı olabilir.";
      return "Bu destek modeline göre semptomlar daha düşük riskli görünüyor. Rutin takibe devam edin ve değişiklikleri bakım ekibinizle paylaşın.";
    }

    if (riskScore >= 25) return "Your symptom burden appears significantly elevated based on the values entered. This should be prioritized for care team review or support outreach.";
    if (riskScore >= 20) return "Your symptoms suggest a high support need. It may be useful to contact your care team or support organization for follow-up.";
    if (riskScore >= 12) return "Your symptoms show a moderate support need. Continue tracking changes and prepare key questions for your next appointment.";
    return "Your symptoms appear lower risk based on this support model. Continue routine tracking and raise any changes with your care team.";
  };

  const buildRecommendedAction = () => {
    if (lang === "tr") {
      if (role === "support") {
        if (riskScore >= 20) return "Bu hastayı erişim/arama kuyruğunda önceliklendirin ve son semptom artışını inceleyin.";
        return "Bu hastayı rutin izlemde tutun.";
      }

      if (role === "caregiver") {
        if (riskScore >= 20) return "Hastanın semptomlarını not etmesine yardımcı olun ve bakım ekibiyle iletişime geçmesini teşvik edin.";
        return "Semptomları gözlemlemeye devam edin ve bir sonraki görüşme için soruları birlikte hazırlayın.";
      }

      if (riskScore >= 20) return "Bakım ekibiniz veya hasta destek organizasyonunuzla takip için iletişime geçmeyi değerlendirin.";
      return "Rutin semptom takibine devam edin ve bu özeti bir sonraki doktor görüşmenize götürün.";
    }

    if (role === "support") {
      if (riskScore >= 20) return "Prioritize this patient in the outreach queue and review recent symptom escalation.";
      return "Keep this patient in routine monitoring.";
    }

    if (role === "caregiver") {
      if (riskScore >= 20) return "Encourage the patient to contact their care team or support organization and help document symptoms.";
      return "Continue observing symptoms and help the patient prepare questions for the next visit.";
    }

    if (riskScore >= 20) return "Consider contacting your care team or patient support organization for follow-up.";
    return "Continue routine symptom tracking and bring this summary to your next doctor visit.";
  };

  const guidance = {
    explanation: buildUserExplanation(),
    questions: buildDoctorQuestions(),
    action: buildRecommendedAction()
  };

  const sendCheckin = async () => {
    setLoading(true);
    setSplunkStatus(t.sending);

    const payload = {
      ...form,
      note: visibleNote()
    };

    try {
      const res = await fetch(`${API_URL}/checkin`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();
      setResult(data);

      if (data.success) {
        setSplunkStatus(
          lang === "tr"
            ? `Başarılı: Semptom olayı Splunk’a oncoconnect:symptom olarak gönderildi. Risk skoru: ${data.risk_score}.`
            : `Success: symptom event sent to Splunk as oncoconnect:symptom. Risk score: ${data.risk_score}.`
        );
      } else {
        setSplunkStatus(t.checkinFailed);
      }
    } catch (error) {
      setSplunkStatus(t.backendFailed);
    }

    setLoading(false);
  };

  const generateAISummary = async () => {
    setLoading(true);
    setSplunkStatus(t.aiSending);

    try {
      const res = await fetch(`${API_URL}/ai-summary`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      const data = await res.json();
      setAiSummary(data.summary);

      if (data.success) {
        setSplunkStatus(
          lang === "tr"
            ? "Başarılı: AI özet olayı Splunk’a oncoconnect:ai_summary olarak gönderildi."
            : "Success: AI summary event sent to Splunk as oncoconnect:ai_summary."
        );
      } else {
        setSplunkStatus(t.aiFailed);
      }
    } catch (error) {
      setSplunkStatus(t.aiFailed);
    }

    setLoading(false);
  };

  const copyQuestions = async () => {
    const body = guidance.questions.map((q, i) => `${i + 1}. ${q}`).join("\n");
    await navigator.clipboard.writeText(body);
    setCopied(true);
    setTimeout(() => setCopied(false), 1600);
  };

  return (
    <div className="page">
      <section className="hero">
        <div className="language-control">
          <label>{t.langLabel}</label>
          <select value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">English</option>
            <option value="tr">Türkçe</option>
          </select>
        </div>

        <div>
          <p className="eyebrow">SPLUNK AI HACKATHON PROJECT</p>
          <h1>{t.title}</h1>
          <p className="subtitle">{t.subtitle}</p>

          <div className="hero-points">
            {t.points.map((item) => (
              <span key={item}>{item}</span>
            ))}
          </div>
        </div>

        <div className="hero-card">
          <h3>{t.valueTitle}</h3>
          <p>{t.valueText}</p>
        </div>
      </section>

      <section className="metrics">
        <div><strong>15K+</strong><span>{t.metrics[0]}</span></div>
        <div><strong>10K</strong><span>{t.metrics[1]}</span></div>
        <div><strong>5.2K</strong><span>{t.metrics[2]}</span></div>
        <div><strong>Live</strong><span>{t.metrics[3]}</span></div>
      </section>

      <main className="workspace">
        <section className="panel">
          <div className="step-header">
            <div className="step-number">1</div>
            <div>
              <h2>{t.who}</h2>
              <p>{t.whoDesc}</p>
            </div>
          </div>

          <div className="role-grid">
            {Object.entries(t.roles).map(([key, item]) => (
              <button
                key={key}
                className={`role-card ${role === key ? "active" : ""}`}
                onClick={() => setRole(key)}
              >
                <strong>{item[0]}</strong>
                <span>{item[1]}</span>
              </button>
            ))}
          </div>

          <div className="step-header compact">
            <div className="step-number">2</div>
            <div>
              <h2>{t.help}</h2>
              <p>{t.helpDesc}</p>
            </div>
          </div>

          <div className="goal-grid">
            {Object.entries(t.goals).map(([key, label]) => (
              <button
                key={key}
                className={`goal-card ${goal === key ? "active" : ""}`}
                onClick={() => setGoal(key)}
              >
                {label}
              </button>
            ))}
          </div>

          <div className="step-header compact">
            <div className="step-number">3</div>
            <div>
              <h2>{t.scenario}</h2>
              <p>{t.scenarioDesc}</p>
            </div>
          </div>

          <select className="wide-select" value={form.patientId} onChange={(e) => selectPatient(e.target.value)}>
            {Object.values(patientPresets).map((p) => (
              <option key={p.patientId} value={p.patientId}>
                {scenarioLabel(p)} — {visibleCancerType(p)} / {p.city}
              </option>
            ))}
          </select>

          <div className="scenario-summary">
            <strong>{form.patientId}</strong>
            <span>{visibleCancerType()} • {visibleTreatment()} • {form.city}</span>
            <p>{visibleNote()}</p>
          </div>

          <div className="info-grid">
            <select value={form.cancerType} onChange={(e) => update("cancerType", e.target.value)}>
              <option>Breast Cancer</option>
              <option>Lung Cancer</option>
              <option>Colon Cancer</option>
              <option>Lymphoma</option>
              <option>Leukemia</option>
            </select>

            <select value={form.treatmentStage} onChange={(e) => update("treatmentStage", e.target.value)}>
              <option>Chemotherapy</option>
              <option>Radiotherapy</option>
              <option>Immunotherapy</option>
              <option>Follow-up</option>
              <option>Post-surgery follow-up</option>
            </select>

            <select value={form.city} onChange={(e) => update("city", e.target.value)}>
              <option>Istanbul</option>
              <option>Izmir</option>
              <option>Ankara</option>
              <option>Bursa</option>
            </select>

            <div className={`risk-pill ${riskClass}`}>
              <small>{lang === "tr" ? "Tahmini destek riski" : "Predicted support risk"}</small>
              <strong>{riskScore}</strong>
              <span>{riskLevel}</span>
            </div>
          </div>

          <div className="step-header compact">
            <div className="step-number">4</div>
            <div>
              <h2>{t.symptoms}</h2>
              <p>{t.symptomsDesc}</p>
            </div>
          </div>

          <div className="sliders">
            {[
              ["fatigue", symptomLabels.fatigue],
              ["nausea", symptomLabels.nausea],
              ["pain", symptomLabels.pain],
              ["mood", symptomLabels.mood]
            ].map(([key, label]) => (
              <div className="slider-row" key={key}>
                <label>{label}: <b>{form[key]}</b></label>
                <input
                  type="range"
                  min="0"
                  max="10"
                  value={form[key]}
                  onChange={(e) => update(key, Number(e.target.value))}
                />
              </div>
            ))}
          </div>

          <textarea value={visibleNote()} onChange={(e) => update(lang === "tr" ? "noteTR" : "noteEN", e.target.value)} placeholder={t.notePlaceholder} />

          <div className="actions">
            <button onClick={sendCheckin} disabled={loading}>{t.send}</button>
            <button className="secondary" onClick={generateAISummary} disabled={loading}>{t.generate}</button>
          </div>
        </section>

        <section className="panel output-panel">
          <div className="copilot-header">
            <div>
              <p className="eyebrow dark">{t.copilotResult}</p>
              <h2>{t.roles[role][0]}</h2>
              <p>{t.goals[goal]}</p>
            </div>
            <div className={`risk-score ${riskClass}`}>
              <strong>{riskScore}</strong>
              <span>{riskLevel}</span>
            </div>
          </div>

          <div className="answer-card">
            <h3>{t.whatMeans}</h3>
            <p>{guidance.explanation}</p>
          </div>

          <div className="answer-card">
            <div className="card-head">
              <h3>{t.questions}</h3>
              <button className="copy-btn" onClick={copyQuestions}>
                {copied ? t.copied : t.copyQuestions}
              </button>
            </div>
            <ol>
              {guidance.questions.map((q, i) => (
                <li key={i}>{q}</li>
              ))}
            </ol>
          </div>

          <div className="answer-card highlight">
            <h3>{t.nextStep}</h3>
            <p>{guidance.action}</p>
          </div>

          {aiSummary && (
            <div className="answer-card ai">
              <h3>{t.aiSummaryTitle}</h3>
              <p>{aiSummary.ai_summary}</p>
              <strong>{t.nextStep}</strong>
              <p>{aiSummary.recommended_action}</p>
            </div>
          )}

          <div className="splunk-status">
            <strong>{t.splunkStatus}</strong>
            <p>{splunkStatus}</p>
          </div>

          <small className="safety">{t.safety}</small>
        </section>
      </main>

      <section className="explain">
        <div>
          <h2>{t.footerTitle}</h2>
          <p>{t.footerText}</p>
        </div>

        <div className="cards">
          {t.cards.map(([title, body]) => (
            <div key={title}>
              <strong>{title}</strong>
              <span>{body}</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default App;
'''

css = r'''
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  background: #f4f7fb;
  color: #111827;
}

.page {
  min-height: 100vh;
}

.hero {
  position: relative;
  min-height: 46vh;
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  align-items: center;
  gap: 34px;
  padding: 48px 56px 105px;
  color: white;
  background:
    radial-gradient(circle at top right, rgba(168, 85, 247, 0.55), transparent 35%),
    linear-gradient(135deg, #06182f, #1e3a8a 52%, #6d28d9);
}

.language-control {
  position: absolute;
  right: 56px;
  top: 22px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.language-control label {
  font-weight: 800;
  color: rgba(255,255,255,0.85);
}

.language-control select {
  width: auto;
  padding: 9px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,0.16);
  color: white;
  border: 1px solid rgba(255,255,255,0.3);
}

.language-control option {
  color: #111827;
}

.eyebrow {
  letter-spacing: 3px;
  font-size: 12px;
  font-weight: 900;
  opacity: 0.85;
}

.eyebrow.dark {
  color: #64748b;
}

h1 {
  font-size: 56px;
  margin: 10px 0;
  line-height: 1;
}

.subtitle {
  font-size: 18px;
  line-height: 1.55;
  max-width: 900px;
  color: rgba(255,255,255,0.92);
}

.hero-points {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 24px;
}

.hero-points span {
  background: rgba(255,255,255,0.13);
  border: 1px solid rgba(255,255,255,0.24);
  padding: 9px 13px;
  border-radius: 999px;
  font-weight: 800;
  font-size: 14px;
}

.hero-card {
  padding: 22px;
  border-radius: 24px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.18);
  backdrop-filter: blur(14px);
}

.hero-card h3 {
  margin-top: 0;
  font-size: 28px;
}

.hero-card p {
  line-height: 1.65;
  color: rgba(255,255,255,0.9);
}

.metrics {
  max-width: 1180px;
  margin: -72px auto 24px;
  padding: 0 24px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  position: relative;
  z-index: 2;
}

.metrics div {
  background: white;
  border-radius: 20px;
  padding: 18px 20px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 18px 50px rgba(15, 23, 42, 0.12);
}

.metrics strong {
  display: block;
  font-size: 28px;
}

.metrics span {
  color: #64748b;
  font-weight: 700;
}

.workspace {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 24px;
  max-width: 1180px;
  margin: 0 auto 38px;
  padding: 0 24px;
}

.panel {
  background: white;
  border-radius: 26px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 28px 70px rgba(15, 23, 42, 0.14);
  padding: 24px;
}

.step-header {
  display: grid;
  grid-template-columns: 38px 1fr;
  gap: 12px;
  align-items: start;
  margin-bottom: 14px;
}

.step-header.compact {
  margin-top: 24px;
}

.step-number {
  width: 34px;
  height: 34px;
  border-radius: 999px;
  background: #1d4ed8;
  color: white;
  display: grid;
  place-items: center;
  font-weight: 950;
}

.step-header h2 {
  margin: 0;
  font-size: 22px;
}

.step-header p {
  margin: 4px 0 0;
  color: #64748b;
}

.role-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.role-card,
.goal-card {
  text-align: left;
  border: 1px solid #cbd5e1;
  border-radius: 16px;
  background: white;
  color: #111827;
  padding: 14px;
  cursor: pointer;
}

.role-card strong,
.role-card span {
  display: block;
}

.role-card span {
  margin-top: 6px;
  color: #64748b;
  font-size: 13px;
  line-height: 1.35;
}

.role-card.active,
.goal-card.active {
  border-color: #1d4ed8;
  background: #eef2ff;
  box-shadow: 0 0 0 2px rgba(29,78,216,0.12);
}

.goal-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.goal-card {
  font-weight: 850;
}

input,
select,
textarea {
  width: 100%;
  border: 1px solid #cbd5e1;
  border-radius: 14px;
  padding: 13px;
  font-size: 15px;
  background: white;
}

select {
  cursor: pointer;
}

.wide-select {
  font-weight: 800;
  margin-bottom: 12px;
}

.scenario-summary {
  border: 1px solid #dbeafe;
  background: #eff6ff;
  border-radius: 16px;
  padding: 14px;
  margin-bottom: 12px;
}

.scenario-summary strong {
  display: block;
  font-size: 18px;
}

.scenario-summary span {
  display: block;
  color: #1d4ed8;
  font-weight: 850;
  margin-top: 4px;
}

.scenario-summary p {
  margin: 8px 0 0;
  color: #334155;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.risk-pill {
  border-radius: 16px;
  padding: 12px 14px;
  color: white;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
}

.risk-pill small {
  opacity: 0.9;
}

.risk-pill strong {
  font-size: 32px;
}

.risk-pill span {
  grid-column: 1 / 3;
  font-weight: 900;
}

.critical {
  background: #dc2626;
}

.high {
  background: #ea580c;
}

.medium {
  background: #ca8a04;
}

.low {
  background: #16a34a;
}

.sliders {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.slider-row label {
  display: block;
  font-weight: 850;
  margin-bottom: 8px;
}

textarea {
  min-height: 94px;
  margin-top: 18px;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 16px;
}

button {
  font-family: inherit;
}

.actions button {
  border: none;
  background: #1d4ed8;
  color: white;
  padding: 14px 17px;
  border-radius: 14px;
  font-weight: 950;
  cursor: pointer;
}

.actions button.secondary {
  background: #7c3aed;
}

button:disabled {
  opacity: 0.55;
}

.output-panel {
  align-self: start;
}

.copilot-header {
  display: grid;
  grid-template-columns: 1fr 120px;
  gap: 16px;
  align-items: start;
  margin-bottom: 16px;
}

.copilot-header h2 {
  margin: 4px 0;
}

.copilot-header p {
  color: #64748b;
  margin: 0;
}

.risk-score {
  color: white;
  border-radius: 20px;
  padding: 16px;
  text-align: center;
}

.risk-score strong,
.risk-score span {
  display: block;
}

.risk-score strong {
  font-size: 42px;
}

.risk-score span {
  font-weight: 950;
}

.answer-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 16px;
  margin-top: 12px;
}

.answer-card h3 {
  margin: 0 0 8px;
}

.answer-card p,
.answer-card li {
  line-height: 1.55;
  color: #334155;
}

.answer-card.highlight {
  background: #ecfdf5;
  border-color: #bbf7d0;
}

.answer-card.ai {
  background: #eef2ff;
  border-color: #c7d2fe;
}

.card-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.copy-btn {
  border: 1px solid #cbd5e1;
  background: white;
  color: #1d4ed8;
  border-radius: 999px;
  padding: 8px 12px;
  font-weight: 850;
  cursor: pointer;
}

.splunk-status {
  margin-top: 12px;
  background: #111827;
  color: white;
  border-radius: 18px;
  padding: 16px;
}

.splunk-status p {
  margin-bottom: 0;
  color: #d1d5db;
}

.safety {
  display: block;
  margin-top: 12px;
  color: #64748b;
  line-height: 1.5;
}

.explain {
  max-width: 1180px;
  margin: 0 auto 70px;
  padding: 0 24px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.explain h2 {
  font-size: 34px;
  margin-bottom: 8px;
}

.explain p {
  line-height: 1.7;
  color: #475569;
}

.cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}

.cards div {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 12px 34px rgba(15, 23, 42, 0.08);
}

.cards strong,
.cards span {
  display: block;
}

.cards span {
  color: #64748b;
  margin-top: 4px;
}

@media (max-width: 900px) {
  .hero,
  .workspace,
  .explain,
  .metrics,
  .role-grid,
  .goal-grid {
    grid-template-columns: 1fr;
  }

  .hero {
    padding: 32px 24px 90px;
  }

  h1 {
    font-size: 44px;
  }

  .info-grid,
  .sliders,
  .cards {
    grid-template-columns: 1fr;
  }

  .language-control {
    position: static;
    margin-bottom: 18px;
  }
}
'''

Path("frontend/src/App.jsx").write_text(app, encoding="utf-8")
Path("frontend/src/App.css").write_text(css, encoding="utf-8")

print("✅ Language toggle, improved scenario UX, and copy doctor questions added.")
