#Page 65
#Start with your program from exercies page 4-1.
#Make a copy of the list of pizzas, and call it friend_pizzas.
pizzas = ['pepperoni', 'pineapple', 'bacon', 'prosciuto', 'white']
friend_pizzas = pizzas[:]

#Add a new pizza to the original list
pizzas.append('chicken')

#Add a new pizza to the friends list
friend_pizzas.append('beef')

#Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n")
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)