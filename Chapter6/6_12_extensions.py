#Exercise 6.12 Extensions - Page 112
#Use one of the example programs from this chapter, and extend it by adding new keys and values
#Changing the context of the program or improving the formatting of the output.

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#We can revise the output to change the language if there is only one favorite.

#NOTE: NOT COMPLETE