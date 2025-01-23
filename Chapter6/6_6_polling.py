#Exercise 6.6 Polling - Page 105
#Make a list of people who should take the favorite languages poll.

participants = ['rachel', 'diego', 'elli', 'ruca', 'austin', 'caleb', 'bruce']

#Loop through the list of people who should take hte poll. If they have already taken the poll, print a message
#Thanking them for responding. If they have not yet taken the poll, print a message telling them to take the poll.

poll = {'rachel': 'c#',
        'diego': 'python',
        'elli': 'java',
        'bruce': 'scratch'}

for participant in participants:
    if participant in poll.keys():
        print(f'{participant.title()}, thank you for taking the poll!')
    
    if participant not in poll.keys():
        print(f'{participant.title()}, please take the poll.')

print('\n')

for name, language in poll.items():
    if name in participants:
        print(f"{name.title()}'s favorite language is {language.title()}.")