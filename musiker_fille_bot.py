# - *- coding: utf- 8 - *-
""" Bot to suggest music from Spotify based on your mood.
"""
import spotipy, os
from spotipy.oauth2 import SpotifyClientCredentials
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#from access_token import AUTH_TOKEN, CLIENT_ID, CLIENT_SECRET

# Intialise spotipy
client_credentials_manager = SpotifyClientCredentials(client_id=os.environ['CLIENT_ID'], client_secret=os.environ['CLIENT_SECRET'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define command handlers. They usually take two arguments bot and update
# In case of error handler they recieve TelegramError object in error
def start(bot, update):
    update.message.reply_text("I can help you find the best music from Spotify 😉")

def help(bot, update):
    update.message.reply_text("You can control me by sending these commands:\n\n/start - start a conversation with bot\n/new - get new releases from Spotify\n/help - get help from bot")

def new(bot, update):
    response = []
    results = sp.new_releases(country='US',limit=10)
    for i, album in enumerate(results['albums']['items'],1):
        response.append(' ' + str(i) + ' ' + album['name'] + ' - ' + album['artists'][0]['name'])
    update.message.reply_text('\n\n'.join(response))

def sorry(bot, update):
    update.message.reply_text("Sorry, I didn't get you. Type /help to get the list of available commands.")

def main():
    """Start the bot"""
    # Create event handler and pass it your bot's token
    updater = Updater(os.environ['AUTH_TOKEN'])

    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher
    print("Bot started!")

    # On different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('new', new))
    # dispatcher.add_handler(CommandHandler(''))

    # On non-command i.e message - echo the message in telegram
    dispatcher.add_handler(MessageHandler(Filters.text, sorry))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
