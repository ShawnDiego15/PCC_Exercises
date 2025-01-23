#Page 68
#A restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
foods = ("chicken", "burgers", "pasta", "salad", "soup")

#Use a for loop to print each food the restuarant offers
print("This restaurant offers:")
for food in foods:
    print(food)

#Try to modify one of the items, and make sure that python rejects the change.
#foods[0] = "sandwich"

#The restaurant changes its menu, replacing two of the items with different foods.
#Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
foods = ("sandwich", "burgers", "rice", "salad", "soup")

print("\nThe menu has changed, you can now order:")
for food in foods:
    print(food)