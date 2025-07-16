import os
import telebot

# توکن را از متغیر محیطی بگیر (در Railway: BOT_TOKEN را ست کن)
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("No BOT_TOKEN environment variable set!")

bot = telebot.TeleBot(TOKEN, parse_mode=None)  # می‌تونی HTML هم بذاری

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "سلام! 🎶 به ربات چی بزارم خوش اومدی 😊\n"
        "فعلاً /start و پیام تست رو جواب میدم."
    )

@bot.message_handler(func=lambda m: True, content_types=['text'])
def echo_all(message):
    bot.reply_to(message, "در حال حاضر فقط دستور /start فعاله 😉")

# اجرای پایدار
bot.infinity_polling(skip_pending=True, timeout=60)
