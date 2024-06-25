import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /promote
def promote(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.message.reply_to_message.from_user.id

    context.bot.promote_chat_member(
        chat_id,
        user_id,
        can_change_info=True,
        can_delete_messages=True,
        can_restrict_members=True,
        can_pin_messages=True,
        can_invite_users=True,
        can_promote_members=False
    )

    update.message.reply_text("User promoted to admin.")

# Command handler for /demote
def demote(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.message.reply_to_message.from_user.id

    context.bot.promote_chat_member(
        chat_id,
        user_id,
        can_change_info=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_invite_users=False,
        can_promote_members=False
    )

    update.message.reply_text("Admin rights revoked from user.")

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('promote', promote))
dispatcher.add_handler(CommandHandler('demote', demote))

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()