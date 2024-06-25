import os
import logging
from pymongo import MongoClient
from telegram.ext import Updater

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['telegram_bot_db']

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Import command handlers from separate modules
from . import misc, permissions, sections, wel_db

# Register command handlers from imported modules
dispatcher.add_handler(misc.dispatcher)
dispatcher.add_handler(permissions.dispatcher)
dispatcher.add_handler(sections.dispatcher)
dispatcher.add_handler(wel_db.dispatcher)

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()