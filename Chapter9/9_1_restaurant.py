# Exercise 9-1; Page 162; Restaurant
#   Make a class called Restaurant.
#   The __init__() method for Restuarant should store two attributes: a restaurant_name and a cuisine_type.
#   Make a method called describe_restaurant() that prints these two pieces of information, 
#       and a method called open_restaurant() that prints a message indicating the restaurant is open.
#   Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    """A class representing a model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine type of a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is open!")

restaurant = Restaurant('Olive Garden', 'Italian')

print(f"{restaurant.restaurant_name} is the name of the restaurant.")
print(f"{restaurant.cuisine_type} is the type of food they serve.")

restaurant.describe_restaurant()
restaurant.open_restaurant()