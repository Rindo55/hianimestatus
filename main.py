import asyncio
import requests
from pyrogram import Client
from datetime import datetime

# Your bot's API credentials
api_id = "10247139"
api_hash = '96b46175824223a33737657ab943fd6a'
bot_token = '7083780360:AAHOyNXyzQN1vODhvsfBBYjD-mRSc1ydVEg'

# The channel ID where the bot will send messages
channel_id = -1001950011842

# Variable to track website status (initially set to 'up')
website_status = 'up'

# Function to format the message with date and time
def format_message(message):
    current_time = datetime.now().strftime("<code>%Y-%m-%d</code> at <code>%H:%M:%S</code>")
    return f"{message}\n\n{current_time}"
# Function to check website status
async def check_website_status():
    global website_status
    while True:
        try:
            # Replace 'https://ddl.animxt.fun' with the URL you want to monitor
            response = requests.get('https://hianime.to')
            if response.status_code != 200:
                if website_status == 'up':
                    error_message = f"<b><u>HiAnime is reporting error</u></b>[.](https://da.gd/B5OP3c)\n#website #status\n\n🚫 <code>HTTP ERROR {response.status_code}</code>"
                    formatted_message = format_message(error_message)
                    await bot.send_message(channel_id, formatted_message, disable_web_page_preview=False)
                    website_status = 'down'
            else:
                if website_status == 'down':
                    success_message = "<b><u>HiAnime is Available</u></b>[!](https://da.gd/B5OP3c)\n#website #status\n\n✅ <code>Available</code>"
                    formatted_message = format_message(success_message)
                    await bot.send_message(channel_id, formatted_message)
                    website_status = 'up'

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            formatted_message = format_message(error_message)
            await bot.send_message(channel_id, formatted_message)

        # Check every 5 minutes (adjust the sleep duration as needed)
        await asyncio.sleep(30)

# Create the bot client
bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Start the bot
async def main():
    await bot.start()
    print("Powered by HiAnime.to")
    await check_website_status()

if __name__ == '__main__':
    asyncio.run(main())
