# Exercise 8-10; Page 146; Sending Messages

# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves
#   each message to a new list called sent_messages as it's printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.

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
send_messages(text_messages, completed_messages)

print("\nThe messages have now been sent, lets check our list contents below:")
print(f"List of pending messages: {text_messages}")
print(f"List of sent messages: {completed_messages}")