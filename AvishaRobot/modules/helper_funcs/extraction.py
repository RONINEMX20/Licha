import logging
import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Send me a message with URLs and hashtags to extract.')

# Message handler for extracting URLs and hashtags
def extract_info(update: Update, context: CallbackContext):
    message = update.message.text
    
    # Extract URLs using regex
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    
    # Extract hashtags using regex
    hashtags = re.findall(r'#(\w+)', message)

    # Prepare response message
    response = ""
    if urls:
        response += f"URLs found:\n"
        for url in urls:
            response += f"{url}\n"
    if hashtags:
        response += f"Hashtags found:\n"
        for tag in hashtags:
            response += f"#{tag}\n"
    
    # If no URLs or hashtags found
    if not urls and not hashtags:
        response = "No URLs or hashtags found in the message."

    update.message.reply_text(response)

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handler
dispatcher.add_handler(CommandHandler('start', start))

# Register message handler for all text messages
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, extract_info))

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()