# Exercise 11-1 & 11-2; Page 215/216

def format_city(city_name, country_name, population=''):
    """Format the name of a city."""
    if population:
        formatted_city = f"{city_name}, {country_name} - population {population}"
    else:
        formatted_city = f"{city_name}, {country_name}"
    return formatted_city.title()