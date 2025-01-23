#Exercise 6.9 Favorite Places - Page 112
#Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary.
#Store one to three favorite places of each person.
#Loop through the dictionary, and print each person's name and their favorite places.

favorite_places = {
    'diego': ['pool', 'river', 'lake'],
    'rachel': ['parents house', 'concert', 'coffee shop'],
    'caleb': ['salon', 'home', 'club']
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")