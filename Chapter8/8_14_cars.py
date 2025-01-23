# Exercise 8-14; Page 150; Cars

# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs,
#   such as a color or an option feature.
# Your function should work for a call like the below:
#   car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that's returned to make sure all the information was stored correctly.

def make_car(manufacturer, model, **car_info):
    """Store data about a car in a dictionary"""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)