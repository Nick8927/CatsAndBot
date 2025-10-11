# import os
# from keyboards.main_menu import main_menu
#
# def start(update, context):
#     """приветствие"""
#     photo_path = os.path.join("media", "cat.jpg")
#
#     if os.path.exists(photo_path):
#         with open(photo_path, "rb") as photo:
#             update.message.reply_photo(photo, caption="Привет! Я твой кот 🐾")
#     else:
#         update.message.reply_text("Привет! Я твой кот 🐾")
#
#     update.message.reply_text(
#         "Выбери, что сделать:",
#         reply_markup=main_menu
#     )

import os
from telegram import Update
from telegram.ext import ContextTypes
from keyboards.main_menu import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда приветствия"""
    photo_path = os.path.join("media", "cat.jpg")

    if os.path.exists(photo_path):
        with open(photo_path, "rb") as photo:
            await update.message.reply_photo(photo, caption="Привет! Я твой кот 🐾")
    else:
        await update.message.reply_text("Привет! Я твой кот 🐾")

    await update.message.reply_text(
        "Выбери, что сделать:",
        reply_markup=main_menu
    )
