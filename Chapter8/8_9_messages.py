# Exercise 8-9; Page 146; Messages

# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    """Print a list of messages."""
    for message in messages:
        print(f"{message}")

text_messages = ['i love you', 'see you later', 'laugh out loud']
show_messages(text_messages)