from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /time
def time(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        update.message.reply_text("Please provide the number of seconds to convert.")
        return
    
    try:
        seconds = int(args[0])
        if seconds < 0:
            update.message.reply_text("Please provide a positive number of seconds.")
            return
        
        days, remainder = divmod(seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        response = f"{args[0]} seconds is approximately:\n"
        if days > 0:
            response += f"{days} days, "
        if hours > 0:
            response += f"{hours} hours, "
        if minutes > 0:
            response += f"{minutes} minutes, "
        response += f"{seconds} seconds."
        
        update.message.reply_text(response)
        
    except ValueError:
        update.message.reply_text("Invalid input. Please provide a valid number of seconds.")

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('time', time))

# Main function
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()