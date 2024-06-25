import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

# In-memory storage for sections (for demonstration purposes)
sections = []

# Command handler for /add_section
def add_section(update: Update, context: CallbackContext):
    if context.args:
        section_name = ' '.join(context.args)
        if section_name not in sections:
            sections.append(section_name)
            update.message.reply_text(f"Section '{section_name}' added.")
        else:
            update.message.reply_text(f"Section '{section_name}' already exists.")
    else:
        update.message.reply_text("Please provide a section name to add.")

# Command handler for /list_sections
def list_sections(update: Update, context: CallbackContext):
    if sections:
        section_list = '\n'.join(sections)
        update.message.reply_text(f"Sections:\n{section_list}")
    else:
        update.message.reply_text("No sections added yet.")

# Command handler for /remove_section
def remove_section(update: Update, context: CallbackContext):
    if context.args:
        section_name = ' '.join(context.args)
        if section_name in sections:
            sections.remove(section_name)
            update.message.reply_text(f"Section '{section_name}' removed.")
        else:
            update.message.reply_text(f"Section '{section_name}' does not exist.")
    else:
        update.message.reply_text("Please provide a section name to remove.")

# Initialize the Updater and Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('add_section', add_section))
dispatcher.add_handler(CommandHandler('list_sections', list_sections))
dispatcher.add_handler(CommandHandler('remove_section', remove_section))

# Main function
def main():
    updater.start_polling()
    logging.info("Bot started polling.")
    updater.idle()

if __name__ == '__main__':
    main()