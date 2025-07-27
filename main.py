import requests
import time
from telegram import Bot
from apscheduler.schedulers.background import BackgroundScheduler

# Telegram config
TOKEN = "8272069185:AAE_7oA_wregGCCq60LgZpClC_UImGSS4kk"
CHAT_ID = "7817169469"

# Bot Telegram
bot = Bot(token=TOKEN)

# Fungsi untuk klaim faucet
def claim_faucet():
    wallet_address = "2aGv8XGXqtuJFiRzMaULmcZ6juaDpDfFPRS6t6YpZP7F"
    url = f"https://faucet.fogo.io/api/faucet?address={wallet_address}"
    response = requests.get(url)

    if response.status_code == 200:
        bot.send_message(chat_id=CHAT_ID, text="✅ Berhasil klaim dari Fogo Faucet!")
    else:
        bot.send_message(chat_id=CHAT_ID, text=f"❌ Gagal klaim: {response.status_code}\n{response.text}")

# Jadwal tiap 1 menit
scheduler = BackgroundScheduler()
scheduler.add_job(claim_faucet, 'interval', minutes=1)
scheduler.start()

print("Bot sedang berjalan dan akan klaim faucet setiap 1 menit...")
while True:
    time.sleep(60)
