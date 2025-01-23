#Exercise 6.8 Pets - Page 112
#Make several dictionaries, where each dictionary represents a different pet.
#In each dictionary, include the kind of animal and the owner's name. 
#Store these dictionaries in a list callled pets.
#Next, loop through your list and as you do, print everything you know about each pet.

pet_0 = {'name': 'ruca', 'species': 'cat', 'owner': 'diego'}
pet_1 = {'name': 'elli', 'species': 'dog', 'owner': 'rachel'}
pet_2 = {'name': 'alice', 'species': 'dog', 'owner': 'austin'}
pet_3 = {'name': 'tempest', 'species': 'lizard', 'owner': 'bryan'}
pet_4 = {'name': 'bruce', 'species': 'cat', 'owner': 'caleb'}

pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['species']} and is owned by {pet['owner'].title()}.")