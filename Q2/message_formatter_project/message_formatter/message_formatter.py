def mystic_border(func):
    """
    Decorator that adds a mystical rune border around the message.
    """
    def wrapper(message):
        border = "🔮" * (len(message) + 8)
        result = func(message)
        return f"{border}\n🔮  {result}  🔮\n{border}"
    return wrapper


def spellbound(func):
    """
    Decorator that adds magical spell emojis around the message.
    """
    def wrapper(message):
        result = func(message)
        return f"✨✨ {result} ✨✨"
    return wrapper
