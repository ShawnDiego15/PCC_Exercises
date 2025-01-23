#Page 99
#Python dictionaries can be used to store actual dictionaries (or glossaries).
#Use 5 programming words you've learned since starting this book, and store their definitions.
#Then, print each word and their definition.

python_words = {
    'variable': 'A word that references a value assigned to it.',
    'list': 'A type of variable that contains multiple values sorted by an index',
    'function': 'A tool that is defined in Python that performs a certain action when called.',
    'dictionary': 'Similar to a list, except it contains values in key-value pairs.',
    'conditionals': 'Statements such as if statements, that perform a given action depending if the conditions are true/false.'
}

print(f"Variable:\n{python_words['variable']}\n")
print(f"List:\n{python_words['list']}\n")
print(f"Function:\n{python_words['function']}\n")
print(f"Dictionary:\n{python_words['dictionary']}\n")
print(f"Conditionals:\n{python_words['conditionals']}\n")