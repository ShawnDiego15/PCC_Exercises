# Exercise 10-8; Cats And Dogs; Page 202

# Make two files, cats.txt and dogs.txt. 
# Store at least three names of cats in the first file and three names of dogs in the second file. 
# Write a program that tries to read these files and print the contents of the file to the screen. 
# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 
# Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

def read_files(filename):
    """Read and output the resutls of a text file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(contents)

filenames = ['text_files/dogs.txt', 'text_files/cats.txt', 'text_files/gerbils.txt']
for filename in filenames:
    read_files(filename)