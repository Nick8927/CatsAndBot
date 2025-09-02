import os


history = []


def handle_action(update, context):
    """выполняет действие, если пользователь написал в чате"""
    text = update.message.text

    if "Погладить" in text:
        history.append("Погладил кота")
        photo_path = os.path.join("media", "cat1.jpg")
        with open(photo_path, "rb") as photo:
            update.message.reply_photo(photo, caption="Кот доволен 😺")

    elif "Обнять" in text:
        history.append("Обнял кота")
        photo_path = os.path.join("media", "cat2.jpg")
        with open(photo_path, "rb") as photo:
            update.message.reply_photo(photo, caption="Кот мурчит 🐾")
