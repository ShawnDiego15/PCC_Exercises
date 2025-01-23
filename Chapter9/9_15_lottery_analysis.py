# Exercise 9-15; Lottery Analysis; Page 181

# You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
#   Make a list or tuple called my_ticket.
#   Write a loop that keeps pulling numbers until your ticket wins.
#   Print a message rerpoting how many times the loop had to run to give you a winning ticket.

from random import choice

def get_winning_ticket(lottery):
    """Return a winning ticket from a set of possiblities."""
    winning_values = []

    while len(winning_values) < 4:
        pulled_value = choice(lottery)
    
        if pulled_value not in winning_values:
            winning_values.append(choice(lottery))

    return winning_values

def check_ticket(played_ticket, winning_values):
    """Check all values in a winning ticket against a played ticket."""
    for element in played_ticket:
        if element not in winning_values:
            return False
        
    return True

def make_random_ticket(lottery):
    """Return a random ticket from a set of possible values."""
    ticket = []

    while len(ticket) < 4:
        pulled_value = choice(lottery)

        if pulled_value not in ticket:
            ticket.append(pulled_value)

    return ticket

lottery = ['A', 'B', 'C', 'D', 'E', 51, 42, 39, 21, 13, 7, 3, 29, 34, 69]
winning_values = get_winning_ticket(lottery)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(lottery)
    won = check_ticket(new_ticket, winning_values)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_values}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_values}")