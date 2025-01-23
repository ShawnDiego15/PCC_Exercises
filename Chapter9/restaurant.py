# This file contains the class for Restaurant.

class Restaurant:
    """A class representing a model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine type of a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        restaurant_desc = f"The restaurant {self.restaurant_name} serves {self.cuisine_type} food. They have served {self.number_served} customers today."
        return restaurant_desc

    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is open!")

    def set_number_served(self, num_served):
        """
            Allow a user to set the number of customers served.
            Ensure the number of customers served cannot be reduced.
        """
        if num_served >= self.number_served:
            self.number_served = num_served
        else:
            print("You cannot un-serve a customer on a business day!")

    def increment_number_served(self, num_served):
        """
            Allow a user to add to the number of customers served.
            Ensure the number of customers served cannot be reduced.
        """
        if num_served > 0:
            self.number_served += num_served
        else:
            print("You cannot serve a negative number of customers!")

    def reset_daily_served(self):
        """Reset the number of customers served as the day has ended."""
        print(f"The day is over and {self.restaurant_name} served {self.number_served} customers.")
        self.number_served = 0
        print(f"We have reset the number of customers served to {self.number_served} to end the day.")