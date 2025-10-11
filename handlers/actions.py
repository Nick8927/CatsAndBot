import os

history = []

def handle_action(bot, message):
    """Выполняет действие, если пользователь написал в чате"""
    text = message.text

    if "Погладить" in text:
        history.append("Погладил кота")
        photo_path = os.path.join("media", "cat1.jpg")
        if os.path.exists(photo_path):
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo, caption="Кот доволен 😺")
        else:
            bot.send_message(message.chat.id, "Кот доволен 😺")

    elif "Обнять" in text:
        history.append("Обнял кота")
        photo_path = os.path.join("media", "cat2.jpg")
        if os.path.exists(photo_path):
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo, caption="Кот мурчит 🐾")
        else:
            bot.send_message(message.chat.id, "Кот мурчит 🐾")
