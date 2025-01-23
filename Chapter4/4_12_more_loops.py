#Page 65
#Choose a version of foods.py and write two for loops to print each list of foods.
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