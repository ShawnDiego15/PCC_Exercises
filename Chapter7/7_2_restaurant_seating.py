#Exercise 7.2 Restaurant Seating - Page 117
#Write a program that asks the user how many people are in their dinner group.
#If the answer is more than eight, print a message saying they will have to wait for a table.
#Otherwise, report that the table is ready.

party_size = input("How many people are in your party today? ")
party_size = int(party_size)

if party_size > 8:
    print("\nYou will need to wait a few mintues for your table.")
else:
    print("\nYour table is ready!")