from pathlib import Path

path = Path("backend/server.js")
content = path.read_text(encoding="utf-8")

insert = r'''
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
'''

if 'app.post("/ai-summary"' not in content:
    content = content.replace('app.listen(5050, () => {', insert + '\n\napp.listen(5050, () => {')
    path.write_text(content, encoding="utf-8")
    print("✅ /ai-summary endpoint added.")
else:
    print("ℹ️ /ai-summary already exists.")
