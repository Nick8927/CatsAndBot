import os
from keyboards.main_menu import main_menu

def start(update, context):
    """приветствие"""
    photo_path = os.path.join("media", "cat.jpg")

    if os.path.exists(photo_path):
        with open(photo_path, "rb") as photo:
            update.message.reply_photo(photo, caption="Привет! Я твой кот 🐾")
    else:
        update.message.reply_text("Привет! Я твой кот 🐾")

    update.message.reply_text(
        "Выбери, что сделать:",
        reply_markup=main_menu
    )
