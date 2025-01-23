# Exercise 10-12; Favorite Number Remembered; Page 208

# Combine the two programs from Excercise 10-11 into one file. 
# If the number is already stored, report the favorite number to the user. 
# If not, prompt for the user's favorite number and store it in a file. 
# Run the program twice to see that it works.

import json

def get_fav_number():
    """Retrieve a users favorite number."""
    favorite_number = input("What is your favorite number? ")
    filename = 'json_files/favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def display_fav_number():
    """Print the users favorite number."""
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"You're favorite number is {favorite_number}!")
    else:
        favorite_number = get_fav_number()
        print(f"We have stored {favorite_number} as your favorite number!")

def get_stored_number():
    """Retrieve a stored number if possible."""
    filename = 'json_files/favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number
    
display_fav_number()