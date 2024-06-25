import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /alternate
def alternate(update: Update, context: CallbackContext):
    # List of messages to alternate
    messages = ["Message 1", "Message 2"]

    # Get current index from user_data or initialize it
    user_data = context.user_data
    current_index = user_data.get('index', 0)

    # Send the next message
    update.message.reply_text(messages[current_index])

    # Update the index for the next iteration
    user_data['index'] = (current_index + 1) % len(messages)

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handler
dispatcher.add_handler(CommandHandler('alternate', alternate))

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()