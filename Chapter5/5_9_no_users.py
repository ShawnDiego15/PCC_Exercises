#Page 89
#Add an if test to the program from 5_8 to make sure the list of users is not empty.
#Run the program again with an empty list to confirm it works as expected.

usernames = ['user1', 'user2', 'user3', 'user4', 'user5', 'admin']

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in.")
else:
    print("We need to find some users!")

print("\n------------\n")

usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in.")
else:
    print("We need to find some users!")