# Exercise 9-2; Page 162; Three Restaurants
#   Start with your class from Exercise 9-1.
#   Create three different instances from the class, and call describe_restaurant() for each instance.

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

restaurant_1 = Restaurant('Olive Garden', 'Italian')

restaurant_2 = Restaurant('Red Lobster', 'Seafood')

restaurant_3 = Restaurant('Los Comales', 'Mexican')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()