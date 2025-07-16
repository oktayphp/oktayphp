#!/usr/bin/env python2
# -*- coding: utf-8 -*-from telegram.ext import Updater, CommandHandler

from telegram.ext import Updater, CommandHandler
updater = Updater('7266501628:AAH1g11eufhijE6allGLSVUTPzKxjiliduE')

def start_method(bot, update):
    bot.sendMessage(update.message.chat_id, "سلام")
start_command = CommandHandler('start', start_method)
updater.dispatcher.add_handler(start_command)

updater.start_polling()

# for exit
updater.idle()
