from keyboards.main_menu import main_menu


def start(update, context):
    """"""
    update.message.reply_text(
        "Привет! Я твой кот 🐾",
        reply_markup=main_menu
    )
