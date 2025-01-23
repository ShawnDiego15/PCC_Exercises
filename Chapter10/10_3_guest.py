# Exercise 10-3; Guests; Page 193

# Write a program that prompts the user for their name.
# When they respond, write their name to a file called guest.txt

guest_name = input("What is your name? ")

filename = 'text_files/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(guest_name)