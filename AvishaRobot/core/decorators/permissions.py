import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /grant
def grant_permission(update: Update, context: CallbackContext):
    if context.args:
        user_id = context.args[0]
        context.bot.promote_chat_member(chat_id=update.effective_chat.id, user_id=user_id, can_manage_chat=True)

# Command handler for /revoke
def revoke_permission(update: Update, context: CallbackContext):
    if context.args:
        user_id = context.args[0]
        context.bot.promote_chat_member(chat_id=update.effective_chat.id, user_id=user_id, can_manage_chat=False)

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('grant', grant_permission))
dispatcher.add_handler(CommandHandler('revoke', revoke_permission))

# Main function
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()