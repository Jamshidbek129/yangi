# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:28:41 2023

@author: shoki
"""

from transliterate import to_cyrillic,to_latin
import telebot
bot=telebot.TeleBot("6417591547:AAEedG-pDRCLjrMSK8ExMWKV-Kn5cLpDCGk",parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
   # bot.reply_to(message, "Assalomu aleykum. Xush kelibsiz! Mening ismim Jamshidbek.\n\
#")
    javob="Assalomu aleykum. Xush kelibsiz! Mening ismim Jamshidbek.\n\
Sizga bu bot orqali lotinni kirilga kirilni lotinga aylantirib beraman"
    bot.reply_to(message,javob)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    x=message.text
    if x.isascii():
        javob=to_cyrillic(x)
    else:
        javob=to_latin(x)
    bot.reply_to(message, javob)
bot.polling()




        
#




