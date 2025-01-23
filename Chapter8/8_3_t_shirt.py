# Exercise 8-3; Page 137; T-Shirt
#   Write a function called make_shirt() that acepts a size and the text of a message that should be printed on a shirt
#   The function should print a sentence summarizing the size of the shirt and the message printed on it.
#   Call the function once using positional arguments to make a shirt. 
#   Call the function a second time using kayword arguments.

def make_shirt(shirt_size, shirt_text):
    """Print a sentence describing a custom shirt"""
    print(f"This shirt says '{shirt_text}' and is printed on a {shirt_size} shirt!")

make_shirt('large', 'I love cats!')
make_shirt(shirt_size='small', shirt_text='I love dogs!')