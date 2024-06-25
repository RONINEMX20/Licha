import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Command handler for /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your bot. Send me a message or use /help to see available commands.')

# Command handler for /help
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Available commands:\n/start - Start the bot\n/help - Show this help message')

# Handler for unknown commands
def unknown_command(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, I didn't understand that command. Use /help to see available commands.")

# Handler for regular text messages
def text_message(update: Update, context: CallbackContext):
    update.message.reply_text(f'You said: {update.message.text}')

# Handler for inline queries
def inline_query(update: Update, context: CallbackContext):
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id='1', title='Caps', input_message_content=InputTextMessageContent(query.upper())
        ),
        InlineQueryResultArticle(
            id='2', title='Bold', input_message_content=InputTextMessageContent(f'*{query}*'), parse_mode='Markdown'
        )
    ]
    update.inline_query.answer(results)

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_command))

# Register handler for unknown commands/messages
dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))

# Register inline query handler
dispatcher.add_handler(InlineQueryHandler(inline_query))

# Main function to start the bot
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()