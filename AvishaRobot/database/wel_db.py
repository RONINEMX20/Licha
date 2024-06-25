import os
import logging
from pymongo import MongoClient
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['telegram_bot_db']
welcome_collection = db['welcome_messages']

# Command handler for /setwelcome
def set_welcome(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = ' '.join(context.args)

    welcome_collection.update_one(
        {'chat_id': chat_id},
        {'$set': {'message': message}},
        upsert=True
    )
    update.message.reply_text(f"Welcome message set for this chat.")

# Command handler for /getwelcome
def get_welcome(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id

    welcome_message = welcome_collection.find_one({'chat_id': chat_id})
    if welcome_message and 'message' in welcome_message:
        update.message.reply_text(f"Current welcome message:\n{welcome_message['message']}")
    else:
        update.message.reply_text("No welcome message set for this chat.")

# Command handler for /clearwelcome
def clear_welcome(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id

    result = welcome_collection.delete_one({'chat_id': chat_id})
    if result.deleted_count > 0:
        update.message.reply_text("Welcome message cleared for this chat.")
    else:
        update.message.reply_text("No welcome message found to clear for this chat.")

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('setwelcome', set_welcome))
dispatcher.add_handler(CommandHandler('getwelcome', get_welcome))
dispatcher.add_handler(CommandHandler('clearwelcome', clear_welcome))

# Main function
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()