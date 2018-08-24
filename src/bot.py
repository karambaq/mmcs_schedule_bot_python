import os

from telegram.ext import Updater
from telegram.ext import CommandHandler

TOKEN = os.environ.get('TOKEN')

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="wow")

def polling():
    updater = Updater(token=TOKEN)
    start_handler = CommandHandler('start', start) 
    updater.dispatcher.add_handler(start_handler) 
    updater.start_polling() 
