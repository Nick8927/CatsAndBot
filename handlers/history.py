from .actions import history


def show_history(update, context):
    """Показ истории действий"""
    if history:
        update.message.reply_text("\n".join(history))
    else:
        update.message.reply_text("История пока пустая 😺")
