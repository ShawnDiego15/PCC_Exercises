#Exercise 3.7: Shrinking Guest List - Page 43
#Start with your program from Exercise 3.6. Add a new line that prints a message saying that you can only invite two to dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list.
#Each time you pop a name from your list, print a message to that person letting them know.
#Print a message to each of the two people still on your list, letting them know they're still invited.
#Use del to remove the last two names from your list, so you have an empty list.
#Print your list to make sure you actually have an empty list at the end of your program.
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

#Start of 3.7:
print("\nUnfortunately, we can now only invite two people.\n")

uninvited_guest = guests.pop()
print(f'I am sorry, but we had to uninvite {uninvited_guest.title()}.')
uninvited_guest = guests.pop(2)
print(f'I am sorry, but we had to uninvite {uninvited_guest.title()}.')
uninvited_guest = guests.pop()
print(f'I am sorry, but we had to uninvite {uninvited_guest.title()}.')
uninvited_guest = guests.pop(0)
print(f'I am sorry, but we had to uninvite {uninvited_guest.title()}.\n')

print(f'{guests[0].title()} you are still invited to Dinner!')
print(f'{guests[1].title()} you are still invited to Dinner!\n')

del guests[0]
del guests[0]
print(guests)