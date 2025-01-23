#Exercise 6.4 Glossary 2 - Page 105
#Clean up code from exercies 6.3 by replacing your series of print() calls with a loop that runs through each
#of the keys and values. Add five more Python terms to your glossary and then re-output.

python_words = {
    'variable': 'A word that references a value assigned to it.',
    'list': 'A type of variable that contains multiple values sorted by an index',
    'function': 'A tool that is defined in Python that performs a certain action when called.',
    'dictionary': 'Similar to a list, except it contains values in key-value pairs.',
    'conditionals': 'Statements such as if statements, that perform a given action depending if the conditions are true/false.',
}

for key, value in python_words.items():
    print(f"{key.title()}: {value}")

python_words.update({'set': 'A list of unique values that will not output repeat values.', 
                     'key': 'Used in a dictionary to indicate what the item is.', 
                     'value': 'Used in a dictionary to indicate a value associated with a specific item.', 
                     'loop': 'A broad term for a type of operation that performs a repeat action based on conditions.',
                     'user': 'The person using the application you built.'})

print("\n")

for key, value in python_words.items():
    print(f"{key.title()}: {value}")