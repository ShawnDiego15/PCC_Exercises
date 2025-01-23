# Exercise 9-14; Lottery; Page 181

# Make a list or tuple containing a series of 10 numbers and five letters.
#   Randomly select four numbers or letters from the list and print a message saying
#       that any ticket matching these four numbers or letters wins a prize.  

from random import choice

lottery = ['A', 'B', 'C', 'D', 'E', 51, 42, 39, 21, 13, 7, 3, 29, 34, 69]

winning_values = []

while len(winning_values) < 4:
    pulled_value = choice(lottery)
    
    if pulled_value not in winning_values:
        winning_values.append(choice(lottery))

print(f"If your values for the lottery are: {winning_values}, congratulations you win!")