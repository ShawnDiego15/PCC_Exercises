#Exercise 7-8; Page 127; No Pastrami
#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
#Add code to the beginning stating the Deli has ran out of Pastrami.
#Then use a while loop to remove all occurences of pastrami from sandwich orders.
#Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami', 'turkey', 'pastrami', 'grilled cheese', 'italian', 'pastrami', 'ham', 'pastrami']
finished_sandwiches = []

print("Unfortunately, the Deli has ran out of Pastrami.")
pastrami = 0
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    pastrami += 1

#As an added item, display the number of pastrami sandwiches we needed to remove.
print(f"There were {pastrami} pastrami sandwiches we could not complete. Please place another order.")
#Allow users to create an additional order that is not a pastrami sandwich.
order = ""
while pastrami > 0:
    order = input("Please place another order. ")
    pastrami -= 1
    sandwich_orders.append(order)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("We have made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())