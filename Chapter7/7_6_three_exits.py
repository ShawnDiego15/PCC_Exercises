#Exercise 7-6; Page 124; Three Exits
#Write different versions of either exercise 7-4 or 7-5 that do each of the following at least once:
#Use a conditional text in the while statement to stop the loop.
#Use an active variable to control how long the loops runs.
#Use a break statement to exit the loop when the user esnters a 'quit' value
#Also, add in statements to prevent errors if another string is input that is not quit. - Not done but could be worth looking into.

#Use a conditional text in the while statement to stop the loop.
prompt = "\nWhat is your age?"
prompt += "\nEntering 'quit' will end the program.\n"

age = 0
ticket_total = 0
while age != "quit":
    age = input(prompt)

    if age != "quit":
        age = int(age)

        if age < 3:
            ticket_price = 0
            print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
            ticket_total += ticket_price
            print(f"Your total cost of tickets is ${ticket_total}")
        elif age >= 3 and age < 12:
            ticket_price = 10
            print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
            ticket_total += ticket_price
            print(f"Your total cost of tickets is ${ticket_total}")
        else:
            ticket_price = 15
            print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
            ticket_total += ticket_price
            print(f"Your total cost of tickets is ${ticket_total}")

#Use an active variable to control how long the loops runs.
prompt = "\nWhat is your age?"
prompt += "\nEntering 'quit' will end the program.\n"

age = 0
ticket_total = 0
active = True
while active == True:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            ticket_price = 0
            print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
            ticket_total += ticket_price
            print(f"Your total cost of tickets is ${ticket_total}")
        elif age >= 3 and age < 12:
            ticket_price = 10
            print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
            ticket_total += ticket_price
            print(f"Your total cost of tickets is ${ticket_total}")
        else:
            ticket_price = 15
            print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
            ticket_total += ticket_price
            print(f"Your total cost of tickets is ${ticket_total}")

#Use a break statement to exit the loop when the user esnters a 'quit' value
prompt = "\nWhat is your age?"
prompt += "\nEntering 'quit' will end the program.\n"

age = 0
ticket_total = 0
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        ticket_price = 0
        print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
        ticket_total += ticket_price
        print(f"Your total cost of tickets is ${ticket_total}")
    elif age >= 3 and age < 12:
        ticket_price = 10
        print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
        ticket_total += ticket_price
        print(f"Your total cost of tickets is ${ticket_total}")
    else:
        ticket_price = 15
        print(f"\nSince you are {age} years old, your ticket is ${ticket_price}.")
        ticket_total += ticket_price
        print(f"Your total cost of tickets is ${ticket_total}")