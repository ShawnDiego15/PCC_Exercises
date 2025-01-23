# Exercise 10-4; Guest Book; Page 193

# Write a while loop that prompts users for their name.
#   When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt.
#   Make sure each entry appears on a new line in the file.

filename = 'text_files/guest_book.txt'

while True:
    guest_name = input("What is your name? Entering 'quit' will end the program. ")

    if guest_name == 'quit':
        break
    else:
        with open(filename, 'w') as file_object:
            file_object.write(f"{guest_name.capitalize()}\n")
            print(f"Welcome, {guest_name.capitalize()}! We have recorded your visit in the guest book.")