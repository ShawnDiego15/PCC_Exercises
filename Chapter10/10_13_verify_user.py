# Exercise 10-13; Verify User; Page 208

# The final listing for *remember_me.py* assumes either that the user has already entered their username or that the program is running for the first time. 
#   We should modify it in case the current user is not the person who last used the program.
# Before printing a welcome back message in `greet_user()`, ask the user if this is the correct username. 
#   If it's not, call `get_new_username()` to get the correct username.

import json

def get_stored_username():
    """Get stored username if available"""
    filename = "json_files/username.json"

    try:
        with open (filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'json_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        while True:
            response = input(f"Is {username} the correct name? Please respond 'y' or 'n': ")
            if response == 'y':
                print(f"Welcome back, {username}!")
                break
            elif response == 'n':
                username = get_new_username()
                print(f"Welcome, {username}! We have stored your data for next time.")
                break
            else:
                print(f"Please ensure your response is 'y' or 'n'. You previously input '{response}'.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()