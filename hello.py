import os
import datetime
from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    # Get the current time
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    # Send a message with the current time to the user
    update.message.reply_text(f"The current time is {current_time}")

# Get the bot token from an environment variable
TOKEN = '5832451246:AAH20GMJ0o7QWzXuTltjBOtQbYIdUOQ8bFY'

# Create the Updater and Dispatcher objects
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Create a CommandHandler for the /start command
start_handler = CommandHandler('start', start)

# Add the CommandHandler to the Dispatcher
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()
updater.idle()
