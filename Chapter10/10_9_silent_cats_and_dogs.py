# Exercise 10-9; Silent Cats and Dogs; Page 202

# Modify your except block in Exercise 10-8 to fail silently if either file is missing.

def read_files(filename):
    """Read and output the resutls of a text file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

filenames = ['text_files/dogs.txt', 'text_files/cats.txt', 'text_files/gerbils.txt']
for filename in filenames:
    read_files(filename)