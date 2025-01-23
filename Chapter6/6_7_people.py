#Exercise 6.7 People - Page 112
#Start with the program from Exercise 6.1
#Make two new dictionaries representing different people, and store all three dictionaries in a list called poeple.
#Loop through your list of people and pring everything you know about each person.

person_0 = {'first_name': 'diego', 'last_name': 'dominguez', 'age': 26, 'city': 'austin'}
person_1 = {'first_name': 'leslie', 'last_name': 'martinez', 'age': 34, 'city': 'portland'}
person_2 = {'first_name': 'barbara', 'last_name': 'pash', 'age': 60, 'city': 'rockport'}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"{full_name} is {person['age']} years old and lives in a city named {person['city'].title()}.")