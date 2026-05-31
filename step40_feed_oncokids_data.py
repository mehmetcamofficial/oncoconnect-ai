# step40_feed_oncokids_data.py
# ONCOCONNECT AI - STEP 40: ONCO KIDS DATA INJECTOR & SIMULATOR

import requests
import time
import random

BACKEND_URL = "http://localhost:5055"
FEELINGS = ["worried", "happy", "brave", "tired", "worried", "brave"]
KIDS_QUESTIONS = [
    "Hastaneye gitmekten çok korkuyorum, canım acır mı?",
    "Süper kahramanlar da bazen kendilerini yorgun hisseder mi?",
    "Saçlarım döküldüğünde pelerin takarsam yine de güçlü görünür müyüm?"
]
PARENT_QUESTIONS = [
    "Çocuğuma saçlarının döküleceğini pedagojik olarak nasıl açıklayabilirim?",
    "Kanser teşhisini 7 yaşındaki bir çocuğa anlatmanın en doğru yolu nedir?"
]

def run_simulation():
    print("=" * 60)
    print("🚀 ONCO KIDS CANLI VERİ ENJEKSİYONU VE TEST SİMÜLASYONU BAŞLADI")
    print("=" * 60)

    try:
        health = requests.get(f"{BACKEND_URL}/api/kids/health", timeout=2.0)
        if health.status_code != 200:
            print("❌ Backend yanıt verdi ama durum kodu hatalı.")
            return
    except Exception:
        print("❌ Port 5055 üzerindeki backend sunucusuna bağlanılamadı!")
        print("Lütfen önce diğer terminalde 'python step39_oncokids_system_core.py' çalıştırın.")
        return

    print("\n--- [AŞAMA 1] Çocuk Duygu Tıklamaları Gönderiliyor ---")
    for f in random.sample(FEELINGS, 3):
        res = requests.post(f"{BACKEND_URL}/api/kids/feeling", json={"feeling": f})
        if res.status_code == 200:
            print(f"👉 Çocuk '{f.upper()}' duygusunu seçti.")
            print(f"   Lumi Yanıtı: {res.json().get('lumi_reaction')}")
        time.sleep(0.5)

    print("\n--- [AŞAMA 2] Çocuk AI Chat Soruları Gönderiliyor ---")
    for msg in random.sample(KIDS_QUESTIONS, 1):
        print(f"❓ Soru: '{msg}'")
        res = requests.post(f"{BACKEND_URL}/api/kids/chat", json={"message": msg, "role": "child"})
        if res.status_code == 200:
            print(f"🤖 Lumi: {res.json().get('message')}\n")

    print("\n--- [AŞAMA 3] Ebeveyn AI Chat Soruları Gönderiliyor ---")
    for msg in random.sample(PARENT_QUESTIONS, 1):
        print(f"❓ Soru: '{msg}'")
        res = requests.post(f"{BACKEND_URL}/api/kids/chat", json={"message": msg, "role": "parent"})
        if res.status_code == 200:
            print(f"🤖 Lumi (Pedagojik Mod): {res.json().get('message')}\n")

    print("=" * 60)
    print("🎉 SİMÜLASYON BAŞARIYLA TAMAMLANDI!")
    print("=" * 60)

if __name__ == "__main__":
    run_simulation()
