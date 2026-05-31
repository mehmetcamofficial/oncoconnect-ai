# step39_oncokids_system_core.py
# ONCOCONNECT AI - STEP 39: ONCO KIDS CORE SYSTEM BACKEND

import os
import time
import json
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")
SPLUNK_HEC_URL = os.getenv("SPLUNK_HEC_URL", "http://localhost:8088/services/collector/event")
SPLUNK_TOKEN = os.getenv("SPLUNK_TOKEN", "YOUR_SPLUNK_HEC_TOKEN_HERE")

ONCO_KIDS_SYSTEM_PROMPT = """
Sen OncoConnect AI platformunun çocuk dostu, şefkatli ve güven veren yapay zeka asistanı 'Lumi'sin.
Karşındaki kullanıcılar kanser teşhisi almış çocuklar (6-12 yaş) veya onların çok endişeli ebeveynleridir.

Uyman Gereken Katı Kurallar:
1. Kesinlikle tıbbi teşhis koyma, ilaç dozu önerme veya tedavi süresi verme. Tıbbi tavsiye istendiğinde "Bunu hemen pediatrik onkoloğumuza sormalıyız!" de.
2. Çocukların sorduğu zor sorulara (Örn: "Saçlarım dökülecek mi?", "Canım acıyacak mı?") korkutmadan, onları birer "Süper Kahraman Yolculuğu" içinde hissettirecek tatlı metaforlarla cevap ver.
3. Kemoterapiyi "vücuttaki zararlı mikropları kovalayan süper temizlik ekibi", hastaneyi "kahramanların güç topladığı parlak bir istasyon" olarak tanımla.
4. Yanıtların kısa, net, umut dolu ve sevgi dolu olsun. Tıbbi jargon (metastaz, tümör vb.) asla kullanma.
"""

def log_event_to_splunk(activity_type, payload_data):
    if not SPLUNK_TOKEN or "YOUR_SPLUNK" in SPLUNK_TOKEN:
        print(f"[SPLUNK SIMULATION] Event: {activity_type} | Data: {json.dumps(payload_data)}")
        return True
    headers = {"Authorization": f"Splunk {SPLUNK_TOKEN}"}
    splunk_payload = {
        "time": time.time(),
        "host": "oncoconnect-root-core",
        "source": "onco_kids_subsystem",
        "sourcetype": "_json",
        "event": {
            "sub_module": "onco_kids",
            "action": activity_type,
            "metrics": payload_data,
            "system_time": time.strftime('%Y-%m-%d %H:%M:%S')
        }
    }
    try:
        response = requests.post(SPLUNK_HEC_URL, data=json.dumps(splunk_payload), headers=headers, timeout=1.0)
        return response.status_code == 200
    except Exception as e:
        print(f"[SPLUNK ERROR] Bağlantı başarısız: {e}")
        return False

def fetch_lumi_response(message, role):
    if not GROQ_API_KEY or "YOUR_GROQ" in GROQ_API_KEY:
        return "Merhaba! Ben Lumi. Şu an bulutların arkasında süper güçlerimi topluyorum ama unutma: Sen harika bir süper kahramansın! ✨"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": ONCO_KIDS_SYSTEM_PROMPT},
            {"role": "user", "content": f"Kullanıcı Rolü: {role}\nKullanıcı Mesajı: {message}"}
        ],
        "temperature": 0.5,
        "max_tokens": 300
    }
    try:
        res = requests.post(url, json=data, headers=headers, timeout=5.0)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        return "Lumi şu an biraz dinleniyor ama kalbi her zaman seninle! 🧸"
    except Exception:
        return "Küçük bir bulut bağlantıyı engelledi, ama Lumi her an senin yanında!"

@app.route('/api/kids/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "subsystem": "onco_kids_core", "port": 5055})

@app.route('/api/kids/feeling', methods=['POST'])
def handle_feeling():
    req_data = request.json or {}
    selected_feeling = req_data.get("feeling", "neutral")
    log_event_to_splunk("ui_feeling_click", {"feeling": selected_feeling})
    reactions = {
        "happy": "Harika! Enerjin etrafa neşe saçıyor, gökkuşağı bugün senin için parlıyor! 🌈",
        "worried": "Bazen endişeli hissetmek çok normal. Süper kahramanlar da büyük görevlerden önce derin bir nefes alır. Gel beraber 'Breathe' sekmesine geçelim. 🌬️",
        "tired": "Yorulmak çok doğal, vücudun şu an süper güçlerini yeniliyor. Biraz dinlenmek sana çok iyi gelecek. 🧸",
        "brave": "İşte benim cesur kahramanım! Bugün seninle gurur duyuyorum! 🏆"
    }
    reply = reactions.get(selected_feeling, "Her duygu bizim bir parçamız. Lumi her zaman seninle!")
    return jsonify({"status": "success", "lumi_reaction": reply})

@app.route('/api/kids/chat', methods=['POST'])
def handle_chat():
    req_data = request.json or {}
    user_message = req_data.get("message", "")
    user_role = req_data.get("role", "child")
    if not user_message:
        return jsonify({"status": "error", "message": "Mesaj içeriği boş olamaz."}), 400
    ai_response = fetch_lumi_response(user_message, user_role)
    log_event_to_splunk("ai_copilot_request", {
        "role": user_role,
        "input_length": len(user_message),
        "contains_anxiety_keywords": any(word in user_message.lower() for word in ["korku", "acı", "iğne", "kanser"])
    })
    return jsonify({"status": "success", "sender": "Lumi", "message": ai_response})

if __name__ == '__main__':
    print("=" * 60)
    print("  ONCOCONNECT AI - ONCO KIDS SUBSYSTEM CORE IS RUNNING")
    print("  -> Base Port: 5055 (No conflict with port 5050)")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5055, debug=True)
