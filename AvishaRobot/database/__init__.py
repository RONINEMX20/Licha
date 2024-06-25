import logging
from telegram.ext import Updater

# Import command handlers from separate modules
from . import misc, permissions, sections

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Main function to start the bot
def main():
    logging.info("Bot started.")

    # Add command handlers from imported modules
    # Make sure to replace 'updater' with 'dispatcher' if using add_handler from dispatcher
    updater.dispatcher.add_handler(misc.dispatcher)
    updater.dispatcher.add_handler(permissions.dispatcher)
    updater.dispatcher.add_handler(sections.dispatcher)

    # Start the Bot
    updater.start_polling()

    # Run the bot until Ctrl+C is pressed or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()