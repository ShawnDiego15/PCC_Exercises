#Exercise 3.8: Seeing The World - Page 46

#Think of at least 5 places in the world you'd like to visit.
#Store the locations in a list. Make sure they are not in alphabetical order.
#Print your list in its original order.
destinations = ['japan', 'korea', 'alaska', 'hawaii', 'oregon']
print(destinations)
print("-----------------------------------\n")

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(destinations))
print("-----------------------------------\n")

#Show that your list is still in its original order by printing it.
print(destinations)
print("-----------------------------------\n")

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(destinations, reverse=True))
print("-----------------------------------\n")

#Show that your list is still in its original order by printing it again.
print(destinations)
print("-----------------------------------\n")

#Use reverse() to change the order of your list. Print the list to show that the order has changed.
destinations.reverse()
print(destinations)
print("-----------------------------------\n")

#Use reverse() to change the order of your list again. Print the list again to show the original order.
destinations.reverse()
print(destinations)
print("-----------------------------------\n")

#Use sort() to change your list so its stored in alphabetical order. Print the list to show the order changed.
destinations.sort()
print(destinations)
print("-----------------------------------\n")

#Use sort() to change your list so its stored in reverse alphaetical order. Print the list show the change.
destinations.sort(reverse=True)
print(destinations)
print("-----------------------------------\n")