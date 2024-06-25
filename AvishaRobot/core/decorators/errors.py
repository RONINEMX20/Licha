import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token and owner ID
TOKEN = 'YOUR_BOT_TOKEN'
OWNER_ID = 'OWNER_ID'

# Example command handler that raises an error
def error_example(update: Update, context: CallbackContext):
    raise Exception("An error occurred in the bot!")

# Error handler function
def error_handler(update: Update, context: CallbackContext):
    """Log the error and send a message to the owner."""
    logging.error(msg="Exception occurred", exc_info=context.error)

    # Notify the owner about the error
    context.bot.send_message(chat_id=OWNER_ID, text=f"Error occurred in the bot:\n{context.error}")

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handler
dispatcher.add_handler(CommandHandler('error_example', error_example))

# Register error handler
dispatcher.add_error_handler(error_handler)

# Main function
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()