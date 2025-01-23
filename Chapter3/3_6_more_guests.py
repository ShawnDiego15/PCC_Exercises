#Exercise 3.6: More Guests - Page 42
#Start with the program from 3.4. Add a print() call to the end of your program informing people that you found a bigger table.
#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list.
guests = ['Rachel', 'Hunter', 'Caleb']

print(f'{guests[0].title()} you are invited to Dinner!')
print(f'{guests[1].title()} you are invited to Dinner!')
print(f'{guests[2].title()} you are invited to Dinner!')

print("\nWe found a bigger table, we will need to send more invitations.\n")

guests.insert(0, 'Sam')
guests.insert(2, 'Austin')
guests.append('Jeremy')

print(f'{guests[0].title()} you are invited to Dinner!')
print(f'{guests[1].title()} you are invited to Dinner!')
print(f'{guests[2].title()} you are invited to Dinner!')
print(f'{guests[3].title()} you are invited to Dinner!')
print(f'{guests[4].title()} you are invited to Dinner!')
print(f'{guests[5].title()} you are invited to Dinner!')