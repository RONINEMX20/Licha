import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Send me a message or a file to see different filters in action.')

# Message handler for text messages
def text_message(update: Update, context: CallbackContext):
    update.message.reply_text('You sent a text message!')

# Message handler for photo messages
def photo_message(update: Update, context: CallbackContext):
    update.message.reply_text('You sent a photo!')

# Message handler for document messages
def document_message(update: Update, context: CallbackContext):
    update.message.reply_text('You sent a document!')

# Message handler for replies
def reply_message(update: Update, context: CallbackContext):
    update.message.reply_text('You replied or mentioned me!')

# Message handler for unknown messages
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, I didn't understand that message.")

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handler
dispatcher.add_handler(CommandHandler('start', start))

# Register message handlers with filters
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))
dispatcher.add_handler(MessageHandler(Filters.photo, photo_message))
dispatcher.add_handler(MessageHandler(Filters.document, document_message))
dispatcher.add_handler(MessageHandler(Filters.reply, reply_message))

# Fallback handler for unknown messages
dispatcher.add_handler(MessageHandler(Filters.all, unknown))

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()