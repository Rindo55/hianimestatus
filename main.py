import requests
import time
import json

# Your Telegram Bot Token and Channel ID
bot_token = "6461840799:AAG5Ve1YeSkR1fEQfsI3plN51_oqCm25G9U"
channel_id = -1002022217944

# Function to send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": channel_id, "text": message}
    requests.post(url, data=data)

# Function to check website status
def check_website_status():
    url = "https://ddl.animxt.fun"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True, None
        else:
            return False, response.status_code
    except requests.exceptions.RequestException as e:
        return False, str(e)

# Track website status changes
website_down = False

# Main loop to check website status periodically
while True:
    is_down, error = check_website_status()
    
    if is_down and not website_down:
        website_down = True
        if isinstance(error, int):
            send_telegram_message(f"HiAnime is Down\nError Code: {error}")
        else:
            send_telegram_message(f"HiAnime is Down\nError: {error}")
    
    if not is_down and website_down:
        website_down = False
        send_telegram_message("HiAnime is Up")

    # Check every 5 minutes
    time.sleep(300)
