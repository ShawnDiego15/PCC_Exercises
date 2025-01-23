#Exercise 6.11 Cities - Page 112
#Make a dictionary called cities. Use the name of three cities as keys in your dictionary.
#Create a dictionary of information about each city and include 
#   the country that the city is in, approximate population, and one fact about that city.
#Print the name of each city and all of the information you have stored about it.

cities = {
    'austin': {
        'country': 'america',
        'population': '1 million',
        'fact': 'I live here!'
    },
    'london': {
        'country': 'england',
        'population': '800 thousand',
        'fact': 'my friend Chris is from here!'
    },
    'tortola': {
        'country': 'british virgin islands',
        'population': '5 thousand',
        'fact': 'we vacationed here in 2022!'
    }
}

for city, city_info in cities.items():
    print(f"\n{city.title()} has a population of {city_info['population']} and is located in {city_info['country'].title()}. "
          f"Fun fact about {city.title()}: {city_info['fact'].capitalize()}")