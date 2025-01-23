# Exercise 8-6; Page 142; City Names
#   Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this: "City, Country"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city_name, country_name):
    """Return a Formatted version of a City and Country Name"""
    location_format = f"{city_name}, {country_name}"
    return location_format.title()

location_1 = city_country('paris', 'france')
print(location_1)
location_2 = city_country('santiago', 'chile')
print(location_2)
location_3 = city_country('mexico city', 'mexico')
print(location_3)
