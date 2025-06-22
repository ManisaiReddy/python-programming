# Data Structures in python

"""
Lists
Tuple
Set
Dictionary
"""

# List -> List are sequences,ordered collection of items, stored in a position accessed by index

# List Methods

fruits = ["Mango","Apple", "Guva"]
fruits.append("Grapes")
print(fruits)
fruits1 = fruits.copy()
fruits.clear()
print(fruits)
print(fruits1)
print(fruits1.count("Mango"))
fruits1.extend(["Custard","Seasonal Mango","Mango"])
print(fruits1)
print(fruits1.index("Mango"))
fruits1.insert(1,[1,2,3])
print(fruits1)
fruits1.pop(1)
fruits1.remove("Mango")
fruits1.reverse()
fruits1.sort()
print(fruits1)

