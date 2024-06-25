import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /chatstatus
def chat_status(update: Update, context: CallbackContext):
    chat = update.effective_chat

    # Get basic information about the chat
    chat_id = chat.id
    chat_title = chat.title
    chat_type = chat.type
    chat_members_count = chat.get_members_count()
    chat_administrators_count = chat.get_administrators_count()

    message = f"Chat Title: {chat_title}\n"
    message += f"Chat ID: {chat_id}\n"
    message += f"Chat Type: {chat_type}\n"
    message += f"Members Count: {chat_members_count}\n"
    message += f"Administrators Count: {chat_administrators_count}\n"

    update.message.reply_text(message)

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handler
dispatcher.add_handler(CommandHandler('chatstatus', chat_status))

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()