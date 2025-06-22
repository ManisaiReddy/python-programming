# Tuple Data structure
"""
tuple is an ordered collections of items
It is created by declaring parenthesis ()
When you create a tuple it's context cannot be changed, i.e they are immutable
They can hold both heterogeneous and homogeneous items
They are great for fixed data collections
"""

numbers = (1,2,3,1,34)
print(numbers.count(1))
print(numbers.index(3))

# Passing list and tuple to function
"""
When you pass a list we are actualy passing reference to a function
It will directly change the list
They are mutable
"""

def my_fun(food):
    food.append("Guva")
    for x in food:
        print(x)
        
        
fruits = ["mango","banana"]
my_fun(fruits)
print(fruits)

# Passing Tuple to a function
"""
when you pass a tuple to the function actually you are passing value to it
Tuples are immutable and you are trying to change the values of tuple inside the function
It will return new tuple for num object, but the original tuple remains constant
"""
def get_modified(num):
    num+=(10,)
    for x in num:
        print(x)
get_numbers = (1,2,3)
get_modified(get_numbers)
print(get_numbers)

