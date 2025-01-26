# Exercises from Python Crash Course

This file shows the solutions I have created for the exercises from the Python Crash Course, 2nd Edition book by Eric Matthes. All solutions were created within VSCode. 

Each solution is located within the folder for the respective chapter the exercise is from.

Starting in chapter 12, the chapters shift into projects. 

This file will be built upon as I continue to work through the book.

## Chapter 2
This chapter focused on vairables and simple data types.

### Exercise 2.1: Simple Message
Assign a Message to a variable, and then print that message.

#### *2_1_simple_message.py*
```
print("Assign a Message to a variable, and then print that message.")
message = "This is the sentence assigned to the variable message."
print(message)
```

### Exercise 2.2: Simple Messages
Assign a message to variable, and print that message. Then change the value of the variable to a new message, and print the new message.

#### *2_2_simple_messages.py*
```
print("Assign a message to variable, and print that message. Then change the value of the variable to a new message, and print the new message.")
message = "This is the first message"
print(message)

message = "This is the second message"
print (message)
```

### Exercise 2.3: Personal Message
Use a variable to represent a person's name, and print a message ot that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"

#### *2_3_personal_message.py*
```
name = "diego"
print(f"Hello {name.title()}, would you like to learn some Python today?")
print("-----------------------------------")

name = "diego"
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)
```

### Exercise 2.4: Name Cases
Use a variable to represent a peron's name, and then print that person's name in lowercase, uppercase, and title case.

#### *2_4_name_cases.py*
```
full_name = "diego dominguez"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())
print("-----------------------------------")

lower_name = full_name.lower()
print(lower_name)
upper_name = full_name.upper()
print(upper_name)
title_name = full_name.title()
print(title_name)
```

### Exercise 2.5: Famous Quote
Find a quote from a famous person you admire. Print the quote and the name of its author. Include quotation marks.

#### *2_5_famous_quote.py*
```
print('"No mattter where life takes me, find me with a smile." - Mac Miller')
print("-----------------------------------")

quote = '"Life goes on, days get brighter."'
print(f"{quote} - Mac Miller")
```

### Exercise 2.6: Famous Quote 2
Repeat Exercise 2.5, but this time, represent the famous person's name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

#### *2_6_famous_quote_2.py*
```
famous_person = "Mac Miller"
message = f'"No matter where life takes me, find me with a smile." - {famous_person.title()}'
print(message)
```

### Exercise 2.7: Stripping Names
Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip()

#### *2_7_stripping_names.py*
```
name = "\tDiego Dominguez\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
```

### Exercise 2.8: Number Eight
Write addition, subtraction, multiplication, and division operations that result in the number 8.

#### *2_8_number_eight.py*
```
print(2 + 6)
print(10 - 2)
print(2 * 4)
print(24 / 3)
```

### Exercise 2.9: Favorite Number
Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.

#### *2_9_favorite_number.py*
```
favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)
```

## Chapter 3
This chapter focused on the introduction of lists.

### Exercise 3.1: Names
Store the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.

#### *3_1_names.py*
```
friends = ["rachel", "caleb", "hunter", "jeremy", "destinee"]

print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())
print(friends[4].title())
```

### Exercise 3.2: Greetings
Start with the list you used in Exercise 3.1, but instead of just printing each person's name, print a message to them. The text of each message shuold be the same, but each message should be personalized with the person's name

#### *3_2_greetings.py*
```
friends = ["rachel", "caleb", "hunter", "jeremy", "destinee"]

print(f"One of my friends is {friends[0].title()}.")
print(f"One of my friends is {friends[1].title()}.")
print(f"One of my friends is {friends[2].title()}.")
print(f"One of my friends is {friends[3].title()}.")
print(f"One of my friends is {friends[4].title()}.")
```

### Exercise 3.3: My Own List
Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statments about these items, such as "I would like to own a Honda motorcycle."

#### *3_3_my_own_list.py*
```
cars = ["focus", "jeep", "civic"]

print(f"The car I currently drive is a {cars[0].title()}.")
print(f"My dream car is a {cars[1].title()}.")
print(f"The car I will probably end up driving is a {cars[2].title()}.")
```

### Exercise 3.4: Guest List
Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

#### *3_4_guest_list.py*
```
guests = ['Rachel', 'Hunter', 'Caleb']

print(f'{guests[0].title()} you are invited to Dinner!')
print(f'{guests[1].title()} you are invited to Dinner!')
print(f'{guests[2].title()} you are invited to Dinner!')
```

### Exercise 3.5: Changing Guest List
Start with the program from 3.4. Add a print() call at the end to stating the name of the guest who can't make it. Modify the list, replacing the name of the guest who can't make it with the name of the new person you are inviting. Print a second set of invitation messages, one for each person who is still in your list.

#### *3_5_changing_guest_list.py*
```
guests = ['Rachel', 'Hunter', 'Caleb']

print(f'{guests[0].title()} you are invited to Dinner!')
print(f'{guests[1].title()} you are invited to Dinner!')
print(f'{guests[2].title()} you are invited to Dinner!')

print(f'\n{guests[1].title()} can not make it to the dinner.\n')

guests[1] = 'Bryan'

print(f'{guests[0].title()} you are invited to Dinner!')
print(f'{guests[1].title()} you are invited to Dinner!')
print(f'{guests[2].title()} you are invited to Dinner!')
```

### Exercise 3.6: More Guests
Start with the program from 3.4. Add a print() call to the end of your program informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.

#### *3_6_more_guests.py*
```
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
```

### Exercise 3.7: Shrinking Guest List
Start with your program from Exercise 3.6. Add a new line that prints a message saying that you can only invite two to dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know.
Print a message to each of the two people still on your list, letting them know they're still invited.
Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.

#### *3_7_shrinking_guest_list.py*
```
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
```

### Exercise 3.8: Seeing the World
Think of at least 5 places in the world you'd like to visit. Store the locations in a list. Make sure they are not in alphabetical order. Print your list in its original order and then perform a variety of edits to the list.

#### *3_8_seeing_the_world.py*
```
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
```

### Exercise 3.9: Dinner Guests
Working with one of the programs from Exercises 3.4 - 3.7, use len() to print a message indicating the number of people.

#### *3_9_dinner_guests.py*
```
guests = ['Rachel', 'Hunter', 'Caleb']

print(f'{guests[0].title()} you are invited to Dinner!')
print(f'{guests[1].title()} you are invited to Dinner!')
print(f'{guests[2].title()} you are invited to Dinner!')

print(f"That means there are a total of {len(guests)} people invited!")
```

### Exercise 3.10: Every Function
Write a program that creates a list and then uses each function introduced in this chapter at least once.

#### *3_10_every_function.py*
```
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
```

## Chapter 4
This chapter focused on working with list objects.

### Exercise 4-1: Pizzas
Think of at least three kinds of pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

#### *4_1_pizzas.py*
```
pizzas = ['pepperoni', 'pineapple', 'bacon', 'prosciuto', 'white']
for pizza in pizzas:
    print(pizza)

print("----------------------\n")
#Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza.
#For each pizza you should have one line of output containing a simple statement.
pizzas = ['pepperoni', 'pineapple', 'bacon', 'prosciuto', 'white']
for pizza in pizzas:
    print(f"One of my favorite toppings on a pizza is {pizza}.\n")

print("----------------------\n")

#Add a line at the end of the program, outside the for loop.
#The output should consist of at least 3 lines of about the pizzas and one additional pizza.
pizzas = ['pepperoni', 'pineapple', 'bacon', 'prosciuto', 'white']
for pizza in pizzas:
    print(f"One of my favorite toppings on a pizza is {pizza}.")
    print(f"No matter where it is from, I would probably get a {pizza} on my pizza.")
    print(f"You simply can not go wrong with {pizza} on your pizza!\n")

print("I would probably like to have all of these toppings on my pizza at once.")
```

### Exercise 4-2: Animals
Think of at least 3 different animals that a common characteristic. Store these in a list, and then use a for loop to print the name of each animal.

#### *4_2_animals.py*
```
animals = ["cat", "dog", "bird", "lizard", "fish"]
for animal in animals:
    print(animal)

print("----------------\n")
#Modify your program to print a statement about each animal.
animals = ["cat", "dog", "bird", "lizard", "fish"]
for animal in animals:
    print(f"A {animal} would make a great pet!")

print("----------------\n")
#Add a sentence at the end to state what they have in common.
animals = ["cat", "dog", "bird", "lizard", "fish"]
for animal in animals:
    print(f"A {animal} would make a great pet!\n")

print("Honestly, any of these animals would make a great pet!")
```

### Exercise 4-3: Counting to Twenty
Use a for loop to print the numbers from 1 to 20, inclusive.

#### *4_3_counting_two_twenty.py*
```
for value in range (1, 21):
    print(value)

#Make these together
numbers = list(range(1, 21))
print(numbers)
```

### Exercise 4-4: One Million
Make a list of the numbers from one to one million. Then use a for loop to print hte numbers.

#### *4_4_one_million.py*
```
#millions = []
#for value in range(1, 1000001):
    #millions.append(value)

#print(millions)

millions = list(range(1, 1000001))
for value in millions:
    print(value)
```

### Exercise 4-5: Summing a Million
Make a list of the numbers from one to one million. Then use min() max() and sum().

#### *4_5_summing_a_million.py*
```
millions = list(range(1, 1000001))
print(min(millions))
print(max(millions))
print(sum(millions))
```

### Exercise 4-6: Odd Numbers
Use the third arugment of the range() function to make a list of odd numbers from 1 to 20. Then use a for loop to print each number.

#### *4_6_odd_numbers.py*
```
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
```

### Exercise 4-7: Threes
Make a list of the multiples of 3 to 30. Use a for loop to print the numbers in your list.

#### *4_7_threes.py*
```
threes = list(range(3, 31))
for number in threes:
    multiple = number * 3
    print(multiple)

print("------\n")
#Other method
threes = []
for value in range(3, 31):
    three = value * 3
    threes.append(three)

for value in threes:
    print(value)
```

### Exercise 4-8: Cubes
Make a list of the first 10 cubes, then use a for loop to print these.

#### *4_8_cubes.py*
```
cubes = list(range(1, 11))
for value in cubes:
    cube = value ** 3
    print(cube)

#Other method
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

for value in cubes:
    print(value)
```

### Exercise 4-9: Cube Comprehension
Use a list comprehension to generate a list of 10 cubes.

#### *4_9_cube_comprehension.py*
```
cubes = [value**3 for value in range(1, 11)]
print(cubes)
```

### Exercise 4-10: Slices
Create a list. 
Print the message "The first three items in the list are:"
Then use a slice to print the first three items from that program's list.
Print the message "Three items in the middle of the list are:"
Then use a slice to print three items from the middle of the program's list.
Print the message "The last three items in the list are:"
Then use a slice to print the last three items in the list.

#### *4_10_slices.py*
```
pets = ["ruca", "gina", "bruce", "ellie", "alice", "blue", "sasuke"]

#Print the message "The first three items in the list are:"
#Then use a slice to print the first three items from that program's list.
print("The first three items in the list are:")
print(pets[:3])

#Print the message "Three items in the middle of the list are:"
#Then use a slice to print three items from the middle of the program's list.
print("Three items from the middle of the list are:")
print(pets[2:5])

#Print the message "The last three items in the list are:"
#Then use a slice to print the last three items in the list.
print("The last three items in the list are:")
print(pets[-3:])
```

### Exercise 4-11: My Pizzas Your Pizzas
Start with your program from exercies page 4-1.
Make a copy of the list of pizzas, and call it friend_pizzas.
Add a new pizza to the original list
Add a new pizza to the friends list
Prove that you have two separate lists

#### *4_11_my_pizzas_your_pizzas.py*
```
pizzas = ['pepperoni', 'pineapple', 'bacon', 'prosciuto', 'white']
friend_pizzas = pizzas[:]

#Add a new pizza to the original list
pizzas.append('chicken')

#Add a new pizza to the friends list
friend_pizzas.append('beef')

#Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n")
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
```

### Exercise 4-12: More Loops
Choose a version of foods.py and write two for loops to print each list of foods.

#### *4_12_more_loops.py*
```
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friends favorite foods are:")
for food in friend_foods:
    print(food)
```

### Exercise 4-13: Buffet
A restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
Use a for loop to print each food the restuarant offers
Try to modify one of the items, and make sure that python rejects the change.
The restaurant changes its menu, replacing two of the items with different foods.
Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

#### *4_13_buffet.py*
```
foods = ("chicken", "burgers", "pasta", "salad", "soup")

#Use a for loop to print each food the restuarant offers
print("This restaurant offers:")
for food in foods:
    print(food)

#Try to modify one of the items, and make sure that python rejects the change.
#foods[0] = "sandwich"

#The restaurant changes its menu, replacing two of the items with different foods.
#Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
foods = ("sandwich", "burgers", "rice", "salad", "soup")

print("\nThe menu has changed, you can now order:")
for food in foods:
    print(food)
```

## Chapter 5
This chapter introduced if statements and provided more detail on how to effectively use them.

### 5-1: Conditional Tests
Write a series of conditional tests. Print a statement describing each test and your prediciton for the results of each test.

#### *5_1_conditional_tests.py*
```
cat = 'ruca'
print("Is cat == 'ruca'? I predict true.")
print(cat == 'ruca')

print("\nIs cat == 'gina'? I predict false.")
print(cat == 'gina')

dog = 'elli'
print("\nIs dog == 'elli'? I predict true.")
print(dog == 'elli')

print("\nIs dog == 'alice'? I predcit false.")
print(dog == 'alice')
```

### 5-2: More Conditional Tests
Create if statements for True/False for all scenarios.

#### *5_2_more_conditional_tests.py*
```
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
```

### 5-3: Alien Colors 1
Imagine an alient was just shot down in a game.
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

#### *5_3_alien_colors_1.py*
```
alien_color = 'green'

#Write an if statement to test whether the alien's color is green. If it is print a message.
if alien_color == 'green':
    print("You've earned 5 points!")


print("\n------------\n")
#Write one version of this program that passes the if test and another that fails.
alien_color = 'green'

if alien_color == 'blue':
    print("You've earned 5 points!")
```

### 5-4: Alien Colors 2
Using the same format from the 5.3 exercise, create an if-else chain.

#### *5_4_alien_colors_2.py*
```
alien_color = 'green'

#Make one version where if the color is green, the player gets 5 points. If the color is not green, they get 10 points.
if alien_color == 'green':
    print("You've earned 5 points!")
else:
    print("You've earned 10 points!")

print("\n------------\n")
#Create another version that satisfies the other condition.
alien_color = 'blue'

if alien_color == 'green':
    print("You've earned 5 points!")
else:
    print("You've earned 10 points!")
```

### 5-5: Alien Colors 3
Turn the if-else chain from exercise 5-4 into an if-elif-else chain.

If the alien is green, print a message for 5 points.
If the alien is yellow, print a message for 10 points.
If the alien is red, print a message for 15 points.
Write three versions making sure each message is printed for the appropriate alien.

#### *5_5_alien_colors_3.py*
```
alien_color = 'green'

if alien_color == 'green':
    print("You've earned 5 points!")
elif alien_color == 'yellow':
    print("You've earned 10 points!")
elif alien_color == 'red':
    print("You've earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You've earned 5 points!")
elif alien_color == 'yellow':
    print("You've earned 10 points!")
elif alien_color == 'red':
    print("You've earned 15 points!")

alien_color = 'red'

if alien_color == 'green':
    print("You've earned 5 points!")
elif alien_color == 'yellow':
    print("You've earned 10 points!")
elif alien_color == 'red':
    print("You've earned 15 points!")
```

### 5-6: Stages of Life
Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age and then:

If the person is less than 2 years old, print a message that the persion is a baby.
If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
If the person is at least 4 years old but less than 13, print a message that the person is a kid.
If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
If the person is at least 20 years old but less than 65, print a message that the person is an adult.
If the person is age 65 or older, print a message that the person is an elder.

#### *5_6_stages_of_life.py*
```
person_age = 26

if person_age < 2:
    print("This person is a baby!")
elif person_age >= 2 and person_age < 4:
    print("This person is a toddler!")
elif person_age >= 4 and person_age < 13:
    print("This person is a kid!")
elif person_age >= 13 and person_age < 20:
    print("This person is a teenager!")
elif person_age >= 20 and person_age < 65:
    print("This person is an adult!")
else:
    print("This person is an elder!")
```

### 5-7: Favorite Fruit
Make a list of your favorite fruits.
Then, write a series of independent if statements that check for certain fruits in your list.
Make a list of 3 favorite fruits.
Write 5 if statements. Each should check if the fruit is in your list and print a statement if so.

#### *5_7_facorite_fruit.py*
```
favorite_fruits = ['strawberry', 'banana', 'blueberry']

if 'strawberry' in favorite_fruits:
    print("You really like srawberries!")
if 'kiwi' in favorite_fruits:
    print("You really like kiwi!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'mango' in favorite_fruits:
    print("You really like mango!")
if 'blueberry' in favorite_fruits:
    print("You really like blueberries!")
```

### 5-8: Hello Admin
Make a list of 5 or more usernames, including the name 'admin'.
You are writing code to greet each user after they log in.
Loop trhough the list and print a greeting to each user.
If the username is 'admin', print a special greeting.
Otherwise, print a generic greeting.

#### *5_8_hello_admin.py*
```
usernames = ['user1', 'user2', 'user3', 'user4', 'user5', 'admin']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in.")
```

### 5-9: No Users
Add an if test to the program from 5_8 to make sure the list of users is not empty.
Run the program again with an empty list to confirm it works as expected.

#### *5_9_no_users.py*
```
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
```

### 5-10: Checking Usernames
Do the following to create a program that simulates how websites ensure that everyone has a unique username.
Make a list of five or more usernames.
Make another list of five usernames. Make sure one or two of these names are also in the previous list.
Loop through the new users list to see if each new username has already been used.
If it has, print a message to enter a new username. If not print a message saying its available.
Ensure the list is case senstiive.

#### *5_10_checking_usernames.py*
```
current_users = ['john', 'jake', 'diego', 'matt', 'chris']

new_users = ['John', 'riley', 'will', 'tom', 'Chris']

for user in new_users:
    if user.lower() in current_users:
        print(f"The name {user} is already taken.")
    else:
        print(f"The name {user} is avaialble.")
```

### 5-11: Ordinal Numbers
Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most end in th, except 1, 2, and 3.
Store the numbers 1-9 in a list.
Loop through the list.
Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
Your ouput should be on separate lines and say "1st 2nd 3rd 4th" and so on until "9th".

#### *5_11_ordinal_numbers.py*
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
```

## Chapter 6
This chapter introduced dictionaries and how to work with them.

## Chapter 7
This chapter introduced user input and while loops.

## Chapter 8
This chapter introduced how functions are created with Python.

## Chapter 9
This chapter introduced how classes are created and used within Python.

## Chapter 10
This chapter introduced the concepts on how to ingest and work with .txt and .json files. In addition to this, we learned how to handle exceptions to avoid errors when working with files.

### Exercise 10-11: Favorite Number
Write a program that prompts for the user's favorite number. Use `json.dump()` to store this number in a file. Write a separate program that reads in this value and prints the message, "I know your favorite number! It's ____."

#### *10_11_1_favorite_number.py*
```
import json

favorite_number = input("What is your favorite number? ")

filename = 'json_files/favorite_number.json'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print(f"We have stored {favorite_number} as your favorite number!")
```

#### *10_11_2_favorite_number.py*
```
import json

filename = 'json_files/favorite_number.json'

with open(filename) as f:
    favorite_number = json.load(f)

print(f"Your favorite number is {favorite_number}!")
```

### Exercise 10-12: Favorite Number Remembered
Combine the two programs from Excercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user's favorite number and store it in a file. Rune the program twice to see that it works.

#### *10_12_favorite_number_remembered.py*
```
import json

def get_fav_number():
    """Retrieve a users favorite number."""
    favorite_number = input("What is your favorite number? ")
    filename = 'json_files/favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def display_fav_number():
    """Print the users favorite number."""
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"You're favorite number is {favorite_number}!")
    else:
        favorite_number = get_fav_number()
        print(f"We have stored {favorite_number} as your favorite number!")

def get_stored_number():
    """Retrieve a stored number if possible."""
    filename = 'json_files/favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number
    
display_fav_number()
```

### Exercise 10-13: Verify User
The final listing for *remember_me.py* assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in `greet_user()`, ask the user if this is the correct username. If it's not, call `get_new_username()` to get the correct username.

#### *10_13_verify_user.py*
```
import json

def get_stored_username():
    """Get stored username if available"""
    filename = "json_files/username.json"

    try:
        with open (filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'json_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        while True:
            response = input(f"Is {username} the correct name? Please respond 'y' or 'n': ")
            if response == 'y':
                print(f"Welcome back, {username}!")
                break
            elif response == 'n':
                username = get_new_username()
                print(f"Welcome, {username}! We have stored your data for next time.")
                break
            else:
                print(f"Please ensure your response is 'y' or 'n'. You previously input '{response}'.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

## Chapter 11
Within this chapter, we learned how to automate testing of our code, specifically certain classes and functions.

### 11-1 City, Country; Page 215
Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form *City, Country*, such as *Santiago, Chile*. Store the function in a module called *city_functions.py*.

#### *city_functions.py*
```
def format_city(city_name, country_name):
    """Format the name of a city."""
    formatted_city = f"{city_name}, {country_name}"
    return formatted_city.title()
```

Create a file called *test_cities.py* that tests the function you just wrote (rememeber that you need to import `unittest` and the function you want to test). Write a method called `test_city_country()` to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string. Run *test_cities.py*, and make sure the `test_city_country()` passes.

#### *test_cities.py*
```
import unittest
from city_functions import format_city

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city = format_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
```

### 11-2 Population; Page 216
Modify your function so it requires a third parameter, `population`. It should now return a single string of the form *City, Country - population xxx*, such as *Santiago, Chile - population 5000000*. Run *test_cities.py* again. Make sure `test_city_country()` fails this time.

#### *city_functions.py*
```
def format_city(city_name, country_name, population):
    """Format the name of a city."""
    formatted_city = f"{city_name}, {country_name} - population {population}"
    return formatted_city.title()
```

Modify the function so the `population` parameter is optional. Run `test_city_country()` again, and make sure `test_city_country()` passes again.

#### *city_functions.py*
```
def format_city(city_name, country_name, population=''):
    """Format the name of a city."""
    if population:
        formatted_city = f"{city_name}, {country_name} - population {population}"
    else:
        formatted_city = f"{city_name}, {country_name}"
    return formatted_city.title()
```

Write a second test called `test_city_country_population()` that verifies you can call your function with the values 'santiago', 'chile', and 'population=5000000'. Run *test_cities.py* again, and make sure the new test passes.

#### *test_cities.py*
```
import unittest
from city_functions import format_city

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city = format_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - Population 5000000' work?"""
        formatted_city = format_city('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()
```

### 11-3 Employee; Page 221
Write a class called `Employee`. The `__init__()` method should take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called `give_raise()` that adds $5000 to the annual salary by default but also accepts a different raise amount.

#### *employee.py*
```
class Employee:
    """Represent an Employee."""

    def __init__(self, first_name, last_name, salary):
        """Set the emplyoees name and salary."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise, with the default being 5000"""
        self.salary += amount
```

Write a test case for `Employee`. Write two test methods, `test_give_default_raise()` and `test_give_custom_raise()`. Use the `setUp()` method so you don't have to create a new employee instance in each test method. Run your test case, and make sure both tests pass.

#### *test_employee.py*
```
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test the Employee class."""

    def setUp(self):
        """Create an Employee to use for testing."""
        self.test_employee = Employee('Ruca', 'Pancake', 10000)

    def test_give_default_raise(self):
        """Test the default raise for an employee."""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 15000)

    def test_give_custome_raise(self):
        """Test the customer raise for an employee"""
        self.test_employee.give_raise(25000)
        self.assertEqual(self.test_employee.salary, 35000)

if __name__ == '__main__':
    unittest.main()
```

**Note:** Some takeaways to remember when building out classes and test cases from this exercise.
1. Start the test cases with importing `unittest` and the module and class you are wishing to test.
2. Do not forget to pass the argument `unittest.TestCase` to the test class.
3. Start with `setUp()` where you will provide the values needed to create the instance of the class.
4. All test methods will then start with `self.` when referencing specific values or methods.
    1. For now, the general rule appears to be to plan to have `self.instance_name` prefixing all fields/methods BESIDES the `assert()` method of choice.
5. Lastly, do not forget the `if __name__` block.

## Chapter 12
In this chapter, we began working on a game, Alien Invasion, using Pygame. Chapter 12 focused on building out our ship. The ship is allowed to move from one side of the screen to the other, and also can shoot a bullet up the screen.

### 12-1: Blue Sky; Page 238
Make a Pygame window with a blue background.

#### *blue_sky.py*
```
import sys

import pygame

class ExerciseGame:
    """A model of a game for this exercise."""

    def __init__(self):
        """Initialize the Exercise Game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise Game")

        # Set BG color
        self.bg_color = (135, 206, 235)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    eg = ExerciseGame()
    eg.run_game()
```

### 12-2: Game Character; Page 238
Find a bitmap image of a game character you like or convert an image to a bitmap. Make a class that draws the character at the center of the screen and match the background color of the image to the background color of the screen, or vice versa.

#### *game_character.py*
```
import sys

import pygame

from character import Character

class ExerciseGame:
    """A model of a game for this exercise."""

    def __init__(self):
        """Initialize the Exercise Game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise Game")

        # Set BG color
        self.bg_color = (135, 206, 235)

        # Create Character
        self.character = Character(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.character.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    eg = ExerciseGame()
    eg.run_game()
```

#### *character.py*
```
import pygame

class Character:
    """A class to manage the character."""

    def __init__(self, eg_game):
        """Initialize the character and set their starting position."""
        self.screen = eg_game.screen
        self.screen_rect = eg_game.screen.get_rect()

        # Load the character image and get its rect.
        self.image = pygame.image.load('chapter12_exercises/images/game_character.bmp')
        self.rect = self.image.get_rect()

        # Start character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
```

### 12-3 Pygame Documentation; Page 246
We're far enough into the game that you might want to look at some of the Pygame documetation. The Pygame home page is at *https://www.pygame.org/*, and the home page for the documentation is at *https://www.pygame.org/docs/*. Just skim the documentation for now. You won't need it to complete this project, but it will help if you want to modify Alien Invasion or make your own game afterward.

### 12-4 Rocket; Page 246
Make a game that begins with a rocket in the center of the screen. Allow the player to move the rocket up, down, left or right using the four arrow keys. Make sure the rocket never moves beyond any edge of the screen.

#### *rocket_game.py*
```
import sys

import pygame

from rocket_settings import Settings
from rocket import Rocket

class RocketGame:
    """Overall class for the RocketGame"""

    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self)

    def run_game(self):
        """Run the game."""
        while True:
            """Check events within the game."""
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    rg = RocketGame()
    rg.run_game()
```

#### *rocket.py*
```
import pygame

class Rocket:
    """Class representing the Rocket for RocketGame"""

    def __init__(self, rg_game):
        self.screen = rg_game.screen
        self.settings = rg_game.settings

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('chapter12_exercises/images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = rg_game.screen.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

#### *rocket_settings.py*
```
class Settings:
    """A class to store all settings for Rocket Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Ship Settings
        self.rocket_speed = 1.5
```

***NOTE:*** Something to take away from this exercise is how you visualize the axis. Since (0, 0) is the top left corner, going up is actually decreasing the Y and vice versa for going down. In addition to this, there are a number of lines that need to change or be added when working on an additional axis.

### 12-5 Keys; Page 246
Make a Pygame file that creates an empty screen. In the event loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run the program and press various keys to see how Pygame responds.

#### *keys.py*
```
import sys

import pygame

from keys_settings import Settings

class KeysGame:
    """A class representing the Keys Game."""
    
    def __init__(self):
        """Initialize the Keys Game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Keys Game")

    def run_game(self):
        """Run the game."""
        while True:
            """Check events within the game."""
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            print(event.key)
            print(f"The event key for space is {event.key} while the value of pygame.K_SPACE is {pygame.K_SPACE}.")
        else:
            print(event.key)

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    kg = KeysGame()
    kg.run_game()
```

#### *keys_settings.py*
```
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
```

***NOTE:*** The `event.key` attribute maps to what appears to be a numerical ID. For example, space is 32. The actual keys such as `pygame.K_SPACE` also map to a numerical value that is identical to the `event.key`. This explains how `event.key == pygame.K_SPACE` would work. This is demonstrated in this exercise by pressing space and viewing the output.

### 12-6 Sideways Shooter; Page 253
Write a game that places a ship on the left side of the screen and allows the player to move the ship up and down. Make the ship fire a bullet that travels right across the screen when the player presses the space-bar. Make sure bullets are deleted once they disappear off the screen.

#### *sideways_shooter.py*
```
import sys

import pygame
from ss_settings import Settings
from jet import Jet
from missile import Missile

class SidewaysShooter:
    """Main class for the Sideways Shooter game"""

    def __init__(self):
        """Initialze the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideways Shooter")

        self.jet = Jet(self)
        self.missiles = pygame.sprite.Group()

    def run_game(self):
        """Main Loop to Run the Game."""
        while True:
            self._check_events()
            self.jet.update()
            self._update_missiles()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.jet.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_missile()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.jet.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = False

    def _fire_missile(self):
        """Create a new missile and add it to the missiles group."""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _update_missiles(self):
        """Update position of missiles and get rid of old missiles."""
        # Update missile positions.
        self.missiles.update()

        # Get rid of missiles that have disappeared.
        for missile in self.missiles.copy():
            if missile.rect.left >= self.screen.get_rect().right:
                self.missiles.remove(missile)

    def _update_screen(self):
        """"Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.jet.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()

        # Make the most recently drawn screen visible
        pygame.display.flip()
            


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()
```

#### *jet.py*
```
import pygame

class Jet:
    """A class to manage the jet."""

    def __init__(self, ss_game):
        """Initialze the jet and set it's starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the Jet Image and get its rect
        self.image = pygame.image.load('chapter12_exercises/images/jet.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = ss_game.screen.get_rect()

        # Start each new Jet at the left center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the jet's vertical position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the Jets position based on the movement flag."""
        # Update the jets y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.jet_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.jet_speed

        # Update the rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

#### *missile.py*
```
import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    """A class to manage missiles fired from the jet."""
    
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.missile_color

        # Create a missile rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.missile_width, self.settings.missile_height)
        self.rect.midright = ss_game.jet.rect.midright

        # Store the missiles position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the missiles to the right on the screen."""
        # Update the decimal position of the missile.
        self.x += self.settings.missile_speed
        # Update the rect position
        self.rect.x = self.x

    def draw_missile(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

#### *ss_settings.py*
```
class Settings:
    """A class to store all settings for Sideways Shooter"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.bg_color = (230, 230, 230)

        # Jet Settings
        self.jet_speed = 1.5

        # Missile Settings
        self.missile_speed = 1.0
        self.missile_width = 15
        self.missile_height = 3
        self.missile_color = (60, 60, 60)
        self.missiles_allowed = 3
```

## Chapter 13
In this chapter, we continue working on our Alien Invasion game. In this chapter we focus on building out the enemy of the game, the Aliens. The aliens appear in a 'fleet' and begin working their way down the screen and will disappear as bulets hit them.

### 13-1 Stars; Page 264
Find an image of a star. Make a grid of stars appear on the screen.

#### *star.py*
```
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the sky."""

    def __init__(self, sg_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = sg_game.screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('chapter13_exercises/images/star.png')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact vertical position.
        self.y = float(self.rect.y)
```

#### *star_settings.py*
```
# Settings for Star Game

class Settings:
    """A class to store all settings for Star Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```

#### *stars_game.py*
```
# Star Game

import sys

import pygame

from star_settings import Settings
from star import Star

class StarGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star Game")

        self.stars = pygame.sprite.Group()

        self._create_sky()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _create_sky(self):
        """Create the sky of stars."""
        # Create an star and find the number of stars in a row.
        # Spacing between each star is equal to two star widths.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit on the screen.
        available_space_y = (self.settings.screen_height - (2 * star_height))
        number_rows = available_space_y // (2 * star_height) 

        # Create the full sky of stars.
        for row_number in range(number_rows):
            # Create an star and place it in the row.
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create an star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)
        

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    sg = StarGame()
    sg.run_game()
```

### 13-2 Better Stars; Page 264
You can make a more realistic star pattern by introducing randomness when you place each star. Recall that you can get a random number like this:

```
from random import randint
random_number = randint(-10, 10)
```

This code returns a random integer between -10 and 10. Using your code in Exercise 13-1, adjust each star's position by a random amount.

#### *star_game.py*
```
# Star Game

import sys

import pygame

from star_settings import Settings
from star import Star
from random import randint

class StarGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star Game")

        self.stars = pygame.sprite.Group()

        self._create_sky()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _create_sky(self):
        """Create the sky of stars."""
        # Create an star and find the number of stars in a row.
        # Spacing between each star is equal to two star widths.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit on the screen.
        available_space_y = (self.settings.screen_height - (2 * star_height))
        number_rows = available_space_y // (2 * star_height) 

        # Create the full sky of stars.
        for row_number in range(number_rows):
            # Create an star and place it in the row.
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create an star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number

        # Randomize Position
        star.rect.x += randint(-5, 5)
        star.rect.y += randint(-5, 5)

        self.stars.add(star)
        

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    sg = StarGame()
    sg.run_game()
```

### 13-3 Raindrops; Page 268
Find an image of a raindrop and create a grid of raindrops. Make the raindrops fall toward the bottom of the screen until they disappear.
As part of an extra item, I'll have the raindrops appears somewhat randomly on the screen.

#### *raindrop_game.py*
```
# Raindrop Game

import sys
import pygame

from raindrop_settings import Settings
from raindrop import Raindrop
from random import randint

class RaindropGame:
    """Overall class for the Raindrop Game"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop Game")

        self.raindrops = pygame.sprite.Group()

        self._fill_sky()

    def run_game(self):
        """Start the main loop for the game."""
        while True:    
            self._check_events()
            self.raindrops.update()
            self._update_screen()

    def _check_events(self):
        """Check keydown events, only looking to catch if 'esc' is entered."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _fill_sky(self):
        """Create a sky of raindrops."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - (raindrop_width)
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * raindrop_height) 

        # Create the full sky of raindrops.
        for row_number in range(number_rows):
            # Create an raindrop and place it in the row.
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create an raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.y = 2 * raindrop.rect.height * row_number
        raindrop.rect.y = raindrop.y

        # Randomize Position
        raindrop.rect.x += randint(-10, 10)
        raindrop.rect.y += randint(-10, 10)

        self.raindrops.add(raindrop)

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    rd = RaindropGame()
    rd.run_game()
```

#### *raindrop.py*
```
import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rd_game):
        """Initialize a raindrop."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and get its rect.
        self.image = pygame.image.load('chapter13_exercises/images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new Raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the Raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.drop_speed
        self.rect.y = self.y
```

#### *raindrop_settings.py*
```
# Settings for Raindrop Game

class Settings:
    """A class to store all settings for Raindrop Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Raindrop Settings
        self.drop_speed = 1
```

Takeaway from this exercise is to focus on the rect x and y's we are working with. I encountered an issue where all raindrops were appearing in one row (or, only one row was appearing). This was resolved by making changes to `_create_raindrop()`.

### 13-4 Steady Rain; Page 268
Modify your code in Exercise 13-3 so when a row of rain-drops disappears off the bottom of the screen, a new row appears at the top of the screen and begins to fall.

#### *raindrop_game.py*
```
# Raindrop Game

import sys
import pygame

from raindrop_settings import Settings
from raindrop import Raindrop
from random import randint

class RaindropGame:
    """Overall class for the Raindrop Game"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop Game")

        self.raindrops = pygame.sprite.Group()

        self._fill_sky()

    def run_game(self):
        """Start the main loop for the game."""
        while True:    
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        """Check keydown events, only looking to catch if 'esc' is entered."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _fill_sky(self):
        """Create a sky of raindrops."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - (raindrop_width)


        self.number_raindrops_x = available_space_x // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * raindrop_height) 

        # Create the full sky of raindrops.
        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create an raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.y = 2 * raindrop.rect.height * row_number
        raindrop.rect.y = raindrop.y

        # Randomize Position
        raindrop.rect.x += randint(-10, 10)
        raindrop.rect.y += randint(-10, 10)

        self.raindrops.add(raindrop)

    def _create_row(self, row_number):
        """Create a single row of raindrops."""
        for raindrop_number in range(self.number_raindrops_x):
            self._create_raindrop(raindrop_number, row_number)

    def _update_raindrops(self):
        """Update the Raindrops."""
        self.raindrops.update()

        make_new_drops = False
        for raindrop in self.raindrops.copy():
            if raindrop.check_edges():
                self.raindrops.remove(raindrop)
                make_new_drops = True

        # Make a new row as needed.
        if make_new_drops:
            self._create_row(0)

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    rd = RaindropGame()
    rd.run_game()
```

#### *raindrop.py*
```
import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rd_game):
        """Initialize a raindrop."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and get its rect.
        self.image = pygame.image.load('chapter13_exercises/images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new Raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the Raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if raindrop is at the bottom of the screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.top > screen_rect.bottom:
            return True
        else:
            return False

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.drop_speed
        self.rect.y = self.y
```

### 13-5 Sideways Shooter Part 2
Try to develop Sideways Shooter from exercise 12-6 to the same point we've brought Alien Invasion. Add a fleet of enemies, and make them move sideways towards the ship. Or, write code that places aliens at random positions along the right side of the screen and then sends them toward the ship. Also, write code that makes the aliens dissapear when they're hit.

For my example, I am using bats as the enemy. Additional items I've added were:
- Bats remove themselves from the screen upon reaching the border.
- Bullets pass through the bats all the way to the edge of the screen.

#### *sideways_shooter.py*
```
# Main file for Sideways Shooter game

import sys

import pygame
from ss_settings import Settings
from jet import Jet
from missile import Missile
from bat import Bat
from random import random

class SidewaysShooter:
    """Main class for the Sideways Shooter game"""

    def __init__(self):
        """Initialze the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.jet = Jet(self)
        self.missiles = pygame.sprite.Group()
        self.bats = pygame.sprite.Group()

    def run_game(self):
        """Main Loop to Run the Game."""
        while True:
            self._check_events()
            self._create_bat()
            self.jet.update()
            self._update_missiles()
            self.bats.update()
            self._remove_bats()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.jet.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_missile()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.jet.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = False

    def _fire_missile(self):
        """Create a new missile and add it to the missiles group."""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _update_missiles(self):
        """Update position of missiles and get rid of old missiles."""
        # Update missile positions.
        self.missiles.update()

        # Get rid of missiles that have disappeared.
        for missile in self.missiles.copy():
            if missile.rect.left >= self.screen.get_rect().right:
                self.missiles.remove(missile)

        self._check_missile_bat_collisions()

    def _remove_bats(self):
        """Remove a bat that has reached the end of the screen."""
        for bat in self.bats.copy():
            if bat.rect.right <= self.screen.get_rect().left:
                self.bats.remove(bat)

    def _check_missile_bat_collisions(self):
        """Check if any missiles have collided with bats."""
        collisions = pygame.sprite.groupcollide(self.missiles, self.bats, False, True)


    def _create_bat(self):
        """Create a bat."""
        if random() < self.settings.bat_frequency:
            bat = Bat(self)
            self.bats.add(bat)
            print(len(self.bats))

    def _update_screen(self):
        """"Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.jet.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()

        self.bats.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()
            


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()
```

#### *jet.py*
```
# Exercise 12-6; Sideways Shooter

# Main File for the Jet Class

import pygame

class Jet:
    """A class to manage the jet."""

    def __init__(self, ss_game):
        """Initialze the jet and set it's starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the Jet Image and get its rect
        self.image = pygame.image.load('chapter12_exercises/images/jet.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = ss_game.screen.get_rect()

        # Start each new Jet at the left center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the jet's vertical position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the Jets position based on the movement flag."""
        # Update the jets y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.jet_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.jet_speed

        # Update the rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

#### *missile.py*
```
# Exercise 12-6; Sideways Shooter;

# Main file for Missle class.

import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    """A class to manage missiles fired from the jet."""
    
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.missile_color

        # Create a missile rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.missile_width, self.settings.missile_height)
        self.rect.midright = ss_game.jet.rect.midright

        # Store the missiles position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the missiles to the right on the screen."""
        # Update the decimal position of the missile.
        self.x += self.settings.missile_speed
        # Update the rect position
        self.rect.x = self.x

    def draw_missile(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

#### *bat.py*
```
import pygame
from pygame.sprite import Sprite
from random import randint

class Bat(Sprite):
    """A class for the enemy of the Sideways Shotoer game."""

    def __init__(self, ss_game):
        """Initialize a bat."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the bat image and get its rect.
        self.image = pygame.image.load('chapter13_exercises/images/bat.png')
        self.rect = self.image.get_rect()

        # Start each bat at a random position on the right side of the screen.
        self.rect.left = self.screen.get_rect().right

        bat_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, bat_top_max)

        # Store each bats horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bats left."""
        self.x -= self.settings.bat_speed
        self.rect.x = self.x
```

#### *ss_settings.py*
```
# Exercise 12-6 Sideways Shooter

# Settings file for Sideways Shooter

class Settings:
    """A class to store all settings for Sideways Shooter"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Jet Settings
        self.jet_speed = 1.5

        # Missile Settings
        self.missile_speed = 1.5
        self.missile_width = 15
        self.missile_height = 3
        self.missile_color = (60, 60, 60)
        self.missiles_allowed = 5

        # Bat Settings
        self.bat_speed = 0.5
        self.bat_frequency = 0.008

```
