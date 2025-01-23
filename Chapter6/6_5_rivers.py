#Exercise 6.5 Rivers - Page 105
#Make a dictionary containing three major rivers and the country each river runs through.
#Use a loop to print a sentence about each river.
#Use a loop to print the name of each river.
#Use a loop to print the name of each country.

rivers = {'mississippi': 'america',
          'nile': 'egypt',
          'amazon': 'brazil'}

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title}.\n")

for river in rivers.keys():
    print(f"{river.title()}\n")

for country in rivers.values():
    print(f"{country.title()}\n")