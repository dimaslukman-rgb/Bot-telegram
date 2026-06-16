import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

bot.send_message(
    chat_id=CHAT_ID,
    text="Telegram Reporting Bot is running successfully."
)

print("Message sent successfully.")
