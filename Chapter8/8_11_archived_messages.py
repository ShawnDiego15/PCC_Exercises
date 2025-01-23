# Exercise 8-11; Page 146; Archived Messages

# Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.

def show_messages(messages):
    """Print a list of messages."""
    for message in messages:
        print(f"{message}")
    
def send_messages(unsent_messages, sent_messages):
    """Print a list of messages."""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

text_messages = ['i love you', 'see you later', 'laugh out loud']
completed_messages = []

show_messages(text_messages)
send_messages(text_messages[:], completed_messages)

print("\nThe messages have now been sent, lets check our list contents below:")
print(f"List of pending messages: {text_messages}")
print(f"List of sent messages: {completed_messages}")