from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /afk
def afk(update: Update, context: CallbackContext):
    user = update.effective_user
    args = context.args
    reason = ' '.join(args)
    
    if not reason:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name} is now AFK.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name} is now AFK with reason: {reason}.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Register command handlers
    dispatcher.add_handler(CommandHandler('afk', afk))
    
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()