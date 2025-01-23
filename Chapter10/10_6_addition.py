# Exercise 10-6; Addition; Page 201

# One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
# When you try to convert the input to an int, you’ll get a ValueError. 
# Write a program that prompts for two numbers. Add them together and print the result. 
# Catch the TypeError if either input value is not a number, and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text instead of a number. 

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add a letter!")
    else:
        print(answer)