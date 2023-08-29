 
# telegram.py
import requests

def send_telegram_message(chat_id, message, token):
    """
    Send a message to a specific Telegram chat.
    """
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()
