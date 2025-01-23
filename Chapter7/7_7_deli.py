#Exercise 7-7; Page 127; Deli
#Make a list called sandwich_orders and fill it with names of various sandwiches.
#Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order.
#As each sandwich is made, move it ot the list of finished sandwiches.
#After all sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['pastrami', 'turkey', 'grilled cheese', 'italian', 'ham']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("We have made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())