import os

from telegram.ext import Updater
from telegram.ext import CommandHandler

TOKEN = "687954179:AAHiQy0nBRvkmrGA1Gk1rH8ZA7b3FsNcS68"

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="wow")

def polling():
    updater = Updater(token=TOKEN)
    print('here')
    start_handler = CommandHandler('start', start) 
    updater.dispatcher.add_handler(start_handler) 
    updater.start_polling() 
