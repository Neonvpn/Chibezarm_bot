import telebot

# توکن رباتتو بذار اینجا 👇
TOKEN = "8198029652:AAGJpwrNW3cZPM0slOg2JRytw3MWrux165U"
bot = telebot.TeleBot(TOKEN)

# وقتی کاربر /start فرستاد
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! 🎶 به ربات چی بزارم خوش اومدی 😊")

# حالت پیش‌فرض که هر پیامی داد
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "در حال حاضر فقط دستور /start فعاله 😉")

# اجرای ربات
bot.infinity_polling()
