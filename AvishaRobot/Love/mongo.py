from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from pymongo import MongoClient
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client.telegram_bot_db
collection = db.afk_statuses

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /afk
def afk(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_name = update.effective_user.username
    args = context.args
    reason = ' '.join(args) if args else None
    
    # Check if user is already AFK
    if collection.find_one({'user_id': user_id}):
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are already AFK.")
        return
    
    # Store AFK status in MongoDB
    afk_data = {'user_id': user_id, 'user_name': user_name, 'reason': reason}
    collection.insert_one(afk_data)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user_name} is now AFK.")

# Command handler for /back
def back(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_name = update.effective_user.username
    
    # Check if user is AFK
    afk_data = collection.find_one({'user_id': user_id})
    if afk_data:
        collection.delete_one({'user_id': user_id})
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user_name} is back.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are not AFK.")

# Command handler for /list_afk
def list_afk(update: Update, context: CallbackContext):
    afk_users = collection.find()
    if afk_users.count() > 0:
        afk_list = "\n".join([f"{user['user_name']} - Reason: {user['reason'] or 'Not provided'}" for user in afk_users])
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Users AFK:\n{afk_list}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No users are currently AFK.")

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('afk', afk))
dispatcher.add_handler(CommandHandler('back', back))
dispatcher.add_handler(CommandHandler('list_afk', list_afk))

# Main function
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()