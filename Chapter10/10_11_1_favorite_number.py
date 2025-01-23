# Exercise 10-11; Favorite Number; Page 208

# Write a program that prompts for the user's favorite number. 
# Use `json.dump()` to store this number in a file. 
# Write a separate program that reads in this value and prints the message, "I know your favorite number! It's ____."

# Prompt and Store favorite number

import json

favorite_number = input("What is your favorite number? ")

filename = 'json_files/favorite_number.json'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print(f"We have stored {favorite_number} as your favorite number!")