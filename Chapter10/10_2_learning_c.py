# Exercise 10-2; Learning C; Page 191

# You can use the replace() method to replcae any word in a string with a different word.
# Here is an example showing how to replacec 'dog' with 'cat' in a sentence.
message = "I really like dogs."
print(message.replace('dog', 'cat'))

# NOTE: This does change the actual message variable, and instead needs to be its own variable or used within the print method.

# Read each line from the file you jsut created, learning_python.txt, and replace the word Python with the name of another language, such as C.
# Print each modified line to the screen.

print('\n---------------------------------\n')

filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

learning_topics = ''
for line in lines:
    learning_topics += line.strip()
    learning_topics += '\n'

print(learning_topics.replace('python', 'C'))