# - *- coding: utf- 8 - *-
""" Bot to suggest music from Spotify based on your mood.
"""
import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from access_token import AUTH_TOKEN, CLIENT_ID, CLIENT_SECRET

# Intialise spotipy
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define command handlers. They usually take two arguments bot and update
# In case of error handler they recieve TelegramError object in error
def start(bot, update):
    update.message.reply_text("I'm Sarika and music is my life😉")

def help(bot, update):
    update.message.reply_text("I am Sarika and I'll help you find the right music based on your mood\n\nYou can control me by sending these commands:\n\n/start - start a conversation with bot\n/help - get help from bot")

def new(bot, update):
    response = []
    results = sp.new_releases(country='US',limit=10)
    for i, album in enumerate(results['albums']['items'],1):
        response.append(' ' + str(i) + ' ' + album['name'] + ' - ' + album['artists'][0]['name'])
    update.message.reply_text('\n\n'.join(response))

def echo(bot, update):
    update.message.reply_text(update.message.text)

def main():
    """Start the bot"""
    # Create event handler and pass it your bot's token
    updater = Updater(AUTH_TOKEN)

    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher
    print("Bot started!")

    # On different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('new', new))

    # On non-command i.e message - echo the message in telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
