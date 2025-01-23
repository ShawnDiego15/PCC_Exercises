# Exercise 9-13; Dice; Page 181

# Make a class Die with one attribute called sides, which has a default value of 6.
#   Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
#   Make a 6-sided die and roll it 10 times.
#   Then, make a 10 and 20-sided die and roll each 10 times.

# As an added feature, the roll_dice method will congratulate on a max roll.

# We will also add a new method, roll_max which will count the number of times it taxes to roll a max on a given die.

from random import randint

class Die:
    """A class representing a model of a die."""

    def __init__(self, sides):
        """Initialize a die with specified number of sides."""
        self.sides = sides

    def roll_dice(self):
        """Roll the Die."""
        roll_num = randint(1, self.sides)

        if roll_num == self.sides:
            print(f"{roll_num}. A Max Roll!")
        else:
            print(f"{roll_num}")

    def roll_max(self):
        "Roll the Die until you hit a max roll."
        active = True
        num_rolls = 0
        while active == True:
            roll_num = randint(1, self.sides)
            num_rolls += 1

            if roll_num == self.sides:
                print(f"Congrats, you rolled a max roll on a {self.sides}-sided die in {num_rolls} tries!")
                active = False
            else:
                active = True

print("\nWe will now roll a 6 sided die 10 times.\n")
six_sided = Die(6)

num_roll = 0

while num_roll < 10:
    six_sided.roll_dice()
    num_roll += 1

print("\nWe will now roll a 10 sided die 10 times.\n")
ten_sided = Die(10)

num_roll = 0

while num_roll < 10:
    ten_sided.roll_dice()
    num_roll += 1

print("\nWe will now roll a 20 sided die 10 times.\n")
twenty_sided = Die(20)

num_roll = 0

while num_roll < 10:
    twenty_sided.roll_dice()
    num_roll += 1

print("\nWe will now roll until we hit a max on each cube.\n")

six_sided.roll_max()
ten_sided.roll_max()
twenty_sided.roll_max()