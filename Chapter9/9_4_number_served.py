# Exercise 9-4; Page 167; Number Served
#   Start with your program from Exercise 9-1.
#   Add an attribute called number_served with a default value of 0.
#   Create an instance called restaurant from this class.
#   Print the number of customers the restaurant has served, then change this value and print it again.

#   Add a method called set_number_served() that lets you set the number of customers that have been served.
#   Call this method with a new number and print the value again.

#   Add a method called increment_number_served() that lets you increment the number of customers who've been served.
#   Call this method with any number you like that could represent how many customers were served in a day of business.

#   As a self-added exercise, ensure the number of people served cannot be reduced.
#   In addition, create a method that allows the number of people to be reset upon the end of a business day.

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


my_restaurant = Restaurant('Oliver Garden', 'Italian')
print(f"{my_restaurant.restaurant_name} has served {my_restaurant.number_served} people!")

my_restaurant.number_served = 25
print(f"{my_restaurant.restaurant_name} has served {my_restaurant.number_served} people!")

my_restaurant.set_number_served(30)
print(f"{my_restaurant.restaurant_name} has served {my_restaurant.number_served} people!")

print("Below is a test to validate the logic is in place to avoid the number of customers served from reducing.")
my_restaurant.set_number_served(20)

my_restaurant.increment_number_served(50)
print(f"{my_restaurant.restaurant_name} has served {my_restaurant.number_served} people!")

print("Below is a test to validate the logic is in place to avoid the number of customers served from reducing.")
my_restaurant.set_number_served(-10)

# As an added exercise, the describe_restaurant() method was updated to help streamline the descriptions and code.

print(my_restaurant.describe_restaurant())

# Ensuring the daily count is reset.
my_restaurant.reset_daily_served()