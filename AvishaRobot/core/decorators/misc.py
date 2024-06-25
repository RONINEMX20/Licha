import logging
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /echo
def echo(update: Update, context: CallbackContext):
    text = ' '.join(context.args)
    update.message.reply_text(text)

# Command handler for /random
def random_number(update: Update, context: CallbackContext):
    args = context.args
    if len(args) != 2:
        update.message.reply_text("Please provide two integers: /random <min> <max>")
        return
    
    try:
        min_value = int(args[0])
        max_value = int(args[1])
        random_num = random.randint(min_value, max_value)
        update.message.reply_text(f"Random number between {min_value} and {max_value}: {random_num}")
    except ValueError:
        update.message.reply_text("Invalid input. Please provide two integers.")

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('echo', echo))
dispatcher.add_handler(CommandHandler('random', random_number))

# Main function
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()