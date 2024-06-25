import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Decorator to log information about incoming messages
def log_message(func):
    def wrapper(update: Update, context: CallbackContext):
        user = update.effective_user
        if user:
            username = user.username
            user_id = user.id
            logging.info(f"Received message from {username} (ID: {user_id}): {update.message.text}")
        else:
            logging.info(f"Received message from unknown user: {update.message.text}")
        return func(update, context)
    return wrapper

# Command handler for /start
@log_message
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! This is the start command.')

# Message handler with the decorator
@log_message
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handler
dispatcher.add_handler(CommandHandler('start', start))

# Register message handler for all text messages
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()