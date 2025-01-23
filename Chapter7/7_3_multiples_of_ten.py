#Exercise 7.3 - Multiples of 10 - Page 117
#Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input("Please input a number and I will tell you if it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"Yes, {number} is a multiple of 10!")
else:
    print(f"No, {number} is not a multiple of 10.")