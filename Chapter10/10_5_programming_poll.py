# Exercise 10-5; Programming Poll; Page 193

# Write a while loop that asks people why they like programming.
#   Each time someone enters a reason, add their reason to a file that stores all the responses.

filename = 'text_files/programming_poll.txt'

while True:
    response = input("Why do you like programming? Entering 'quit' will end the program. ")

    if response == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{response.capitalize()}\n")
            print("Thank you, your response has been recorded.\n")