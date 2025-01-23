#Exercise 7-4; Page 123; Pizza Toppings
#Write a loop that prompts the user to enter a series of pizza topppings until they enter a 'quit' value.
#As they enter each topping, print a message saying you'll add that topping to their piza.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEntering 'quit' will end the program.\n"

active = True
while active == True:
    message = input(prompt)

    if message != 'quit':
        print(f"We will add {message} to your pizza!")
    else:
        active = False

#An alternative way to accomplish this could be:

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEntering 'quit' will end the program.\n"

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(f"We will add {message} to your pizza!")