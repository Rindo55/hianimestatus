import asyncio
import requests
from pyrogram import Client
from pyrogram.types import Message

# Your bot's API credentials
api_id = "10247139"
api_hash = '96b46175824223a33737657ab943fd6a'
bot_token = '6461840799:AAG5Ve1YeSkR1fEQfsI3plN51_oqCm25G9U'

# The channel ID where the bot will send messages
channel_id = -1002022217944

# Function to check website status
async def check_website_status():
    while True:
        try:
            # Replace 'https://hianime.to' with the URL you want to monitor
            response = requests.get('https://ddl.animxt.fun')
            if response.status_code != 200:
                error_message = f"Website is down! Error code: {response.status_code}"
                await bot.send_message(channel_id, error_message)
            else:
                await bot.send_message(channel_id, "Website is back up!")

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            await bot.send_message(channel_id, error_message)

        # Check every 5 minutes (adjust the sleep duration as needed)
        await asyncio.sleep(300)

# Create the bot client
bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Start the bot
async def main():
    await bot.start()
    await check_website_status()

if __name__ == '__main__':
    asyncio.run(main())


