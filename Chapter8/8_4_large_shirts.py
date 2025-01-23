# Exercise 8-4; Page 137; Large Shirts
#   Modify the make_shirt() function so that shirts are large by default with a message that reads I Love Python.
#   Make a large shirt and medium shirt with the default message
#   Make a shirt of any size with a different message.

def make_shirt(shirt_size='large', shirt_text='I love Python'):
    """Print a sentence describing a custom shirt"""
    print(f"This shirt says '{shirt_text}' and is printed on a {shirt_size} shirt!")

make_shirt()
make_shirt(shirt_size='medium')

make_shirt(shirt_size='small', shirt_text='I love Cats!')