import os
import logging
import threading
import telebot
from flask import Flask

# --- Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Token from environment ---
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set! Please add it in Render > Environment.")

# --- Telegram Bot ---
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "سلام! 🎶 به ربات چی بزارم خوش اومدی 😊\n"
        "فعلاً فقط /start و پیام تست جواب می‌دم."
    )

@bot.message_handler(func=lambda m: True, content_types=['text'])
def echo_all(message):
    bot.reply_to(message, "در حال حاضر فقط دستور /start فعاله 😉")

def run_bot():
    """Run Telegram polling in a background thread."""
    logger.info("Starting Telegram bot polling...")
    # skip_pending=True تا پیام‌های قدیمی رو نریزه بیرون
    bot.infinity_polling(skip_pending=True, timeout=60)

# --- Flask keepalive app for Render ---
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅", 200

def main():
    # Start bot thread
    t = threading.Thread(target=run_bot, daemon=True)
    t.start()

    # Start Flask (keeps Render Web Service alive)
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"Starting Flask keepalive server on port {port}...")
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
