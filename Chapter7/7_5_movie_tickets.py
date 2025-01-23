#Exercise 7-5; Page 123; Movie Tickets
#A movie theatre charges different ticket prices depeonding on a person's age.
#If a person is under the age of 3, the ticket is free;
#If they are between 3 and 12 the ticket is $10
#If they are over age 12, the ticket is $15.
#Write a loop in which you ask users their age and then tell them the cost of their movie ticket.
#As an independent extra task, try ot write this up so that the total could be displayed as well.
#Do not forget to have a way to end the loop.

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