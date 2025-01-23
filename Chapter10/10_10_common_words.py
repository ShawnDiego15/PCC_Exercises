# Exercise 10-10; Common Words; Page 202

# Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you’d like to analyze. 
# Download the text files for these works, or copy the raw text from your browser into a text file on your computer.

# You can use the count() method to find out how many times a word or phrase appears in a string. 
# For example, the following code counts the number of times 'row' appers in a string:
line = "Row, row, row your boat"
print(line.count('row'))
print(line.lower().count('row'))

# Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted.

# Write a program that reads the files you found at Project Gutenberg and determines how many times the word ‘the’ appears in each text. 
# This will be an approximation because it will also count words such as ‘then’ and ‘tehre’. 
# Try counting ‘the ‘, with a space in the string, and see how much lower your count is.

def word_the_counter(filename):
    """Count the times 'the' appears in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        the_words = contents.count('the')
        print(f"The file {filename} says 'the' {the_words} times.")

def word_the_space_counter(filename):
    """Count the times 'the ' appears in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        the_words_space = contents.count('the ')
        print(f"The file {filename} says 'the ' {the_words_space} times.")

filenames = ['text_files/alice.txt', 'text_files/project_hail_mary.txt', 'text_files/little_women.txt', 'text_files/moby_dick.txt']
for filename in filenames:
    word_the_counter(filename)
    word_the_space_counter(filename)