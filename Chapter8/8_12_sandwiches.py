# Exercise 8-12; Page 150; Sandwiches

#   Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
#   and it should print a summary of the sandwich that's being ordered.
# Call the function three times, using a different number of arguments each time.

def make_sandwich(*ingredients):
    """Print a summary of an ordered sandwich"""
    print("Ordering a sandwich with the following:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich('ham')
make_sandwich('turkey', 'cheese')
make_sandwich('cheese', 'ham', 'turkey', 'lettuce')