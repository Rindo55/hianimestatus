import asyncio
import requests
from pyrogram import Client
from datetime import datetime

api_id = "10247139"
api_hash = '96b46175824223a33737657ab943fd6a'
bot_token = '7083780360:AAHOyNXyzQN1vODhvsfBBYjD-mRSc1ydVEg'

channel_id = -1001950011842

website_status = 'up'

def timee(message):
    current_time = datetime.now().strftime("<code>%Y-%m-%d</code> at <code>%H:%M:%S</code>")
    return f"{message}\n\n{current_time}"

async def check_website_status():
    global website_status
    while True:
        try:
            response = requests.get('https://hianime.to')
            if response.status_code != 200:
                if website_status == 'up':
                    error_message = f"<b><u>HiAnime is reporting error</u></b>[.](https://i.ibb.co/ZmJj811/DOWN-Telegram.jpg)\n#website #status\n\n🚫 <code>HTTP ERROR {response.status_code}</code>"
                    formatted_message = timee(error_message)
                    await bot.send_message(channel_id, formatted_message, disable_web_page_preview=False)
                    website_status = 'down'
            else:
                if website_status == 'down':
                    success_message = "<b><u>HiAnime is Available</u></b>[!](https://i.ibb.co/fHMgDVf/UP-Telegram.jpg)\n#website #status\n\n✅ <code>Available</code>"
                    msg = timee(success_message)
                    await bot.send_message(channel_id, msg, disable_web_page_preview=False)
                    website_status = 'up'

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            msg = timee(error_message)
            print(error_message)
            await bot.send_message(channel_id, msg)
        await asyncio.sleep(60)

bot = Client("statusbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def main():
    await bot.start()
    print("Powered by HiAnime.to")
    await check_website_status()

if __name__ == '__main__':
    asyncio.run(main())
