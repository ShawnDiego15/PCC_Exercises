#Exercise 3.10: Every Function - Page 46
#Write a program that creates a list and then uses each function introduced in this chapter at least once.

#Making the original list
cats = ['ruca', 'bruce', 'gina', 'yui', 'oliver']
print(cats)
print("-----------------------------------\n")

#Appending an item to the end of the list
cats.append('boots')
print(cats)
print("-----------------------------------\n")

#Changing a name on the list to a new one
cats[4] = 'stevie'
print(cats)
print("-----------------------------------\n")

#Inserting a new name into a specific spot on the list
cats.insert(1, 'cheeto')
print(cats)
print("-----------------------------------\n")

#Delete an item from a specific spot on the list
del cats[1]
print(cats)
print("-----------------------------------\n")

#Pop the last item on the list to re-use the value.
popped_cat = cats.pop()
print(f"{popped_cat.title()} was removed from the list.")
print(cats)
print("-----------------------------------\n")

#Pop an item in a specified location on the list ot re-use the value.
fattest_cat = cats.pop(2)
print(f"{fattest_cat.title()} is the fattest cat and removed from the list.")
print(cats)
print("-----------------------------------\n")

#Remove a list item based on the value.
cats.remove('yui')
print(cats)
print("-----------------------------------\n")

#Re-using a value that is removed from a list.
calebs_cat = 'bruce'
cats.remove(calebs_cat)
print(cats)
print(f"{calebs_cat.title()} was removed because he has separation anxiety from Gina.")
print("-----------------------------------\n")

#Repopulating the cats list.
cats.append('boots')
cats.append('bruce')
cats.append('marley')
cats.append('gina')
print(cats)
print("-----------------------------------\n")

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(cats))
print("-----------------------------------\n")

#Show that your list is still in its original order by printing it.
print(cats)
print("-----------------------------------\n")

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(cats, reverse=True))
print("-----------------------------------\n")

#Show that your list is still in its original order by printing it again.
print(cats)
print("-----------------------------------\n")

#Use reverse() to change the order of your list. Print the list to show that the order has changed.
cats.reverse()
print(cats)
print("-----------------------------------\n")

#Use reverse() to change the order of your list again. Print the list again to show the original order.
cats.reverse()
print(cats)
print("-----------------------------------\n")

#Use sort() to change your list so its stored in alphabetical order. Print the list to show the order changed.
cats.sort()
print(cats)
print("-----------------------------------\n")

#Use sort() to change your list so its stored in reverse alphaetical order. Print the list show the change.
cats.sort(reverse=True)
print(cats)
print("-----------------------------------\n")