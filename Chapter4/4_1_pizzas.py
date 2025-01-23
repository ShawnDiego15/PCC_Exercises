#Page 56
#Think of at least three kinds of pizza. 
#Store these pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['pepperoni', 'pineapple', 'bacon', 'prosciuto', 'white']
for pizza in pizzas:
    print(pizza)

print("----------------------\n")
#Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza.
#For each pizza you should have one line of output containing a simple statement.
pizzas = ['pepperoni', 'pineapple', 'bacon', 'prosciuto', 'white']
for pizza in pizzas:
    print(f"One of my favorite toppings on a pizza is {pizza}.\n")

print("----------------------\n")

#Add a line at the end of the program, outside the for loop.
#The output should consist of at least 3 lines of about the pizzas and one additional pizza.
pizzas = ['pepperoni', 'pineapple', 'bacon', 'prosciuto', 'white']
for pizza in pizzas:
    print(f"One of my favorite toppings on a pizza is {pizza}.")
    print(f"No matter where it is from, I would probably get a {pizza} on my pizza.")
    print(f"You simply can not go wrong with {pizza} on your pizza!\n")

print("I would probably like to have all of these toppings on my pizza at once.")