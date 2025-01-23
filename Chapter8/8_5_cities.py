# Exercise 8-5; Page 137; Cities
#   Write a function called describe_city() that accepts the name of a city and its country.
#   The function should print a simple sentence, such as Rockport in Texas.
#   Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city_name, country_name='The USA'):
    """Print a sentence containing the city and country"""
    print(f"{city_name.title()} is located in {country_name.title()}.")

describe_city('rockport')
describe_city(city_name='norman')
describe_city('paris', country_name='france')