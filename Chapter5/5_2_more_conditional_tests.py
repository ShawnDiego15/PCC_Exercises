#Page 78
#Create if statements for True/False for all scenarios.

#Tests for equality and inequality with strings.
pasta = 'spaghetti'
print('The statement will be true below.')
print(pasta == 'spaghetti')
print('The statement will be false below.')
print(pasta == 'penne')

print("\n---------------\n")
#Tests using the lower() method.
business = 'GAP'
print('The statement below will be true.')
print(business.lower() == 'gap')
print('The statement below wil be false.')
print(business.lower() == 'old navy')

print("\n---------------\n")
#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.
number = 100

print('The statement below will be true.')
print(number == 100)
print('The statement below will be false.')
print(number == 50)

print('\nThe statement below will be true.')
print(number != 50)
print('The statement below will be false.')
print(number != 100)

print('\nThe statement below will be true.')
print(number > 50)
print('The statement below will be false.')
print(number > 150)

print('\nThe statement below will be true.')
print(number < 150)
print('The statement below will be false.')
print(number < 50)

print('\nThe statement below will be true.')
print(number <= 101)
print('The statement below will be false.')
print(number <= 99)

print('\nThe statement below will be true.')
print(number >= 99)
print('The statement below will be false.')
print(number >= 101)

print("\n---------------\n")
#Tests using the AND keyword and the OR keyword.
car_0 = '4wd'
car_1 = 'suv'

print('The statement below will be true.')
print(car_0 == '4wd' and car_1 == 'suv')
print('The statement below will be false.')
print(car_0 == '4wd' and car_1 == 'sedan')

print('\nThe statement below will be true.')
print(car_0 == '4wd' or car_1 == 'sedan')
print('The statement below will be false.')
print(car_0 == 'electric' or car_1 == 'sedan')

print("\n---------------\n")
#Test whether an item is in a list.
pets = ['ruca', 'gina', 'bruce', 'elli']

print('The statement below will be true.')
print('ruca' in pets)
print('The statement below will be false.')
print('alice' in pets)

print("\n---------------\n")
#Test whether an item is not in a list.
glasses = ['pint', 'wine', 'mug']

print('The statement below will be true.')
print('martini' not in glasses)
print('The statement below will be false.')
print('pint' not in glasses)