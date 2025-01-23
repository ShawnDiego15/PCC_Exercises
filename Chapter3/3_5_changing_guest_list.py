#Exercise 3.5: Changing Guest List - Page 42
#Start with the program from 3.4. Add a print() call at the end to stating the name of the guest who can't make it.
#Modify the list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

guests = ['Rachel', 'Hunter', 'Caleb']

print(f'{guests[0].title()} you are invited to Dinner!')
print(f'{guests[1].title()} you are invited to Dinner!')
print(f'{guests[2].title()} you are invited to Dinner!')

print(f'\n{guests[1].title()} can not make it to the dinner.\n')

guests[1] = 'Bryan'

print(f'{guests[0].title()} you are invited to Dinner!')
print(f'{guests[1].title()} you are invited to Dinner!')
print(f'{guests[2].title()} you are invited to Dinner!')