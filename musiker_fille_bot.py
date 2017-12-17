""" Bot to suggest music from Spotify based on your mood.
"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from access_token import TOKEN

# Define command handlers. They usually take two arguments bot and update
# In case of error handler they recieve TelegramError object in error
def start(bot, update):
    update.message.reply_text("I'm Sarika and music is my life 😉")

def echo(bot, update):
    update.message.reply_text(update.message.text)

def main():
    """Start the bot"""
    # Create event handler and pass it your bot's token
    updater = Updater(TOKEN)

    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher

    # On different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler('start', start))

    # On non-command i.e message - echo the message in telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
