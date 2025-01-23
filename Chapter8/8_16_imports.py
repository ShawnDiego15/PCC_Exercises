# Exercise 8-16; Page 155; Imports

# Using a program you wrote that has one function in it, store that function in a separate file.
# Import the function into your main program file, and call the function using each of these approaches:

#   import module_name
import books

books.favorite_book('Hunger Games')

#   from module_name import function_name
from books import favorite_book

favorite_book('Shiloh')

#   from module_name import function_name as fn
from books import favorite_book as fb

fb('Of Mice and Men')

#   import module_name as mn
import books as bk

bk.favorite_book('Bible')

#   from module_name import *
from books import *

favorite_book('Newspaper')