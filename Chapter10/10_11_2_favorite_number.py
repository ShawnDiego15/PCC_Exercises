# Chapter 10; Exercise 10-11; Favorite Number; Page 208

# Write a program that prompts for the user's favorite number. 
# Use `json.dump()` to store this number in a file. 
# Write a separate program that reads in this value and prints the message, "I know your favorite number! It's ____."

# Open and read favorite number

import json

filename = 'json_files/favorite_number.json'

with open(filename) as f:
    favorite_number = json.load(f)

print(f"Your favorite number is {favorite_number}!")