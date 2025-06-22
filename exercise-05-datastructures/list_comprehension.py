# List comprehension
"""
List comprehension is used to create a new list by iterating over a existing list items, it has shorter syntax
syntax:

new_list = [expression for items in iterable if condition]

"""

squares = [x**2 for x in range(1,6)]
print(squares)

# List comprehension by condition get even numbers from 1 - 1o

even_numbers = [x for x in range(1,11) if x%2==0]
print(even_numbers)

# Nested list comprehension, it creates list of pairs of numbers

pairs = [(x,y) for x in range(1,3) for y in range(2,4)]
print(pairs)