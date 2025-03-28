from flask import Flask, request
import requests
from flask_cors import CORS  # 👈 добавили

app = Flask(__name__)
CORS(app)  # 👈 разрешить кросс-доменные запросы

# === CONFIG ===
BOT_TOKEN = '7857665629:AAHNhtGs5DmlUEXcfVWVps2U-w4eIQQScF0'
CHAT_USERNAME = '@Michael_BLACKSIDE'

def send_telegram_message(fullname, date):
    message = f"🗓 Новая бронь!\n👤 ФИО: {fullname}\n📅 Дата: {date}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_USERNAME,
        "text": message
    }
    requests.post(url, data=payload)

@app.route('/book', methods=['POST'])
def book():
    fullname = request.form.get('fullname')
    date = request.form.get('date')
    if fullname and date:
        send_telegram_message(fullname, date)
        return "Бронирование успешно!", 200
    return "Ошибка в данных", 400

@app.route('/')
def ping():
    return "Booking API работает!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
