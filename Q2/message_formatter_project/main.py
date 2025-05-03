from message_formatter.message_formatter import mystic_border, spellbound

@spellbound
@mystic_border
def format_message(msg):
    return msg

if __name__ == "__main__":
    print(format_message("Welcome to the Wizarding World!"))
    print()
    print(format_message("You have been granted a new spell."))
