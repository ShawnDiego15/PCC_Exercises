#Page 60
#Make a list of the multiples of 3 to 30. Use a for loop to print the numbers in your list.
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