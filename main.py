import os
import telebot
import random

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

hazillar = [
    "Kompyuter nega sovqotadi? Windows ochiq edi 😂",
    "Dangasa odam yugurishni tushida qiladi 🤣",
    "Telefon nega xafa? Zaryadi tugagan 😅",
    "Matematika kitobi nega xafa? Muammolari ko‘p 😂",
    "Wi-Fi nega xafa? Hech kim unga ulanmayapti 😂",
    "Baliq nega internetga kirmaydi? Tarmoqda suv bor 🤣"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men Uzbek Hazilkash botman 😂")

@bot.message_handler(commands=['hazil'])
def hazil(message):
    bot.reply_to(message, random.choice(hazillar))

@bot.message_handler(func=lambda message: True)
def javob(message):
    bot.reply_to(message, "Hazil eshitish uchun /hazil yoz 😂")

print("BOT ISHGA TUSHDI!")
bot.infinity_polling()
