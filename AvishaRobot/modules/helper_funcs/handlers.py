import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your bot. Send me a message or use /help to see available commands.')

# Command handler for /help
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Available commands:\n/start - Start the bot\n/help - Show this help message')

# Message handler for text messages
def text_message(update: Update, context: CallbackContext):
    update.message.reply_text(f'You said: {update.message.text}')

# Message handler for photo messages
def photo_message(update: Update, context: CallbackContext):
    update.message.reply_text('Nice photo!')

# Message handler for document messages
def document_message(update: Update, context: CallbackContext):
    update.message.reply_text('Thanks for the document!')

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_command))

# Register message handlers
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))
dispatcher.add_handler(MessageHandler(Filters.photo, photo_message))
dispatcher.add_handler(MessageHandler(Filters.document, document_message))

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()