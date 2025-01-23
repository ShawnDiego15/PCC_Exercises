# Exercise 9-10; Imported Restaurant; Page 180

# Using your latest Restaurant class, store it in a module.
#   Make a separate file that imports Restaurant.
#   Make a Restaurant instance and call one of Restaurant's methods to show that the import statement is working properly.

from restaurant import Restaurant

my_restaurant = Restaurant("Diego's Food Truck", "Tacos")

print(my_restaurant.describe_restaurant())

my_restaurant.open_restaurant()

my_restaurant.set_number_served(25)

print(my_restaurant.describe_restaurant())

my_restaurant.increment_number_served(55)

print(my_restaurant.describe_restaurant())

my_restaurant.reset_daily_served()

print(my_restaurant.describe_restaurant())