#Exercise 6.10 Favorite Numbers - Page 112
#Modify the program from Exercise 6.2 so each person can have more than one favorite number.
#Then print each person's name along with their favorite numbers.

favorite_numbers = {
    'diego': [3, 7, 11, 13],
    'austin': [69, 420, 710],
    'abbi': [420, 7, 50],
    'rachel': [7, 13, 24],
    'sam': [710, 512, 361]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)