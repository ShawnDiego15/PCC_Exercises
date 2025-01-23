#Exercise 7-9; Page 127; Dream Vacations
#Write a program that pools users about their dream vacation.
#Include a block of code that prints the results of hte poll.

dream_vacations = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your dream vacation? ")

    dream_vacations[name] = response

    repeat = input("Would you like anyone else to respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\n----Poll Results ----")
for name, response in dream_vacations.items():
    print(f"{name.title()} would like to go to {response}.")