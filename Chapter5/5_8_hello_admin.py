#Page 89
#Make a list of 5 or more usernames, including the name 'admin'.
#You are writing code to greet each user after they log in.
#Loop trhough the list and print a greeting to each user.
#If the username is 'admin', print a special greeting.
#Otherwise, print a generic greeting.

usernames = ['user1', 'user2', 'user3', 'user4', 'user5', 'admin']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in.")