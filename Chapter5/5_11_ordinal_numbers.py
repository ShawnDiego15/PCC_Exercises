#Page 89
#Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most end in th, except 1, 2, and 3.
#Store the numbers 1-9 in a list.
#Loop through the list.
#Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
#Your ouput should be on separate lines and say "1st 2nd 3rd 4th" and so on until "9th".

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