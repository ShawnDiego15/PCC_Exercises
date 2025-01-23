# Exercise 8-1; Page 131; Favorite Book
# Write a function called favorite_book() that accepts a paramter, title.
# The function should print a message stating the favorite book.
# Call the function making sure to include a book title as an argument in the function call.

def favorite_book(title):
    """Display a sentence stating your favorite book."""
    print(f"My favorite book is {title.title()}.")

favorite_book("the Hunger games")