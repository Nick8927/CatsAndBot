import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers.start import start
from handlers.actions import handle_action
from handlers.history import show_history


load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")


def main():
    """функция запуска бота"""
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text("История выбора 📜"), show_history))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_action))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
