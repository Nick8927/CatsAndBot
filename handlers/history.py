from .actions import history

def show_history(bot, message):
    """Показ истории действий"""
    if history:
        bot.send_message(message.chat.id, "\n".join(history))
    else:
        bot.send_message(message.chat.id, "История пока пустая 😺")
