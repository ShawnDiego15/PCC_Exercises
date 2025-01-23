#Page 60
#Make a list of the first 10 cubes, then use a for loop to print these.
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