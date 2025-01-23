#Page 89
#Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#Make a list of five or more usernames.
#Make another list of five usernames. Make sure one or two of these names are also in the previous list.
#Loop through the new users list to see if each new username has already been used.
#If it has, print a message to enter a new username. If not print a message saying its available.
#Ensure the list is case senstiive.

current_users = ['john', 'jake', 'diego', 'matt', 'chris']

new_users = ['John', 'riley', 'will', 'tom', 'Chris']

for user in new_users:
    if user.lower() in current_users:
        print(f"The name {user} is already taken.")
    else:
        print(f"The name {user} is avaialble.")
