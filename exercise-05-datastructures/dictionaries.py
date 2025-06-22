# Dictionaries 
"""
Dictionaries are mutable
They are unordered collections of items
We can change, add, or delete dictionaries for dynamic modifications
We map items in dictionary by key
Key is the unique one and dictionaries are fast due to mapping!

"""

person = {
    "name":"manisai",
    "age": 25,
    "city": "Hyderabad"
}

print(person)

# Creating a empty dict
empty_dict = {}
print(empty_dict)

# Creating a new dictionary using dict 
new_person =dict(name="manisai", age=25, city="hyderabadi")
print(new_person)

# Accessing dicitionary values

print(new_person["name"])

# using get method -> returns none if the key is not found

print(new_person.get("age"))

# Adding new key value pair

new_person["sex"]="male"
print(new_person)

new_person["age"]=24
print(new_person)

# Deleting key value pairs in dictionary
# Using del key word we can delte key value pair and it doesnot return the deleted item

del person["city"]
print(person)


# Deleting key value pairs in dictionaries by pop method
# Pop method will return the deleted key value pair

x = new_person.pop("sex")
print(x)
print(new_person)


# Iterating through keys in dictionaries

for key in person:
    print(key)
    
    
# Using iterable person.keys()

for key in person.keys():
    print(key)
    
#  Iterating through values in dictionaries

for value in person.values():
    print(value)
    
# Iterating through key value pairs 

for key,value in person.items():
    print (f"hey {key} there is : {value}")

"""
Dictionary Methods:

Dictionaries come with several built-in methods:

clear(): Removes all items from the dictionary.

copy(): Returns a shallow copy of the dictionary.

fromkeys(iterable, value): Returns a new dictionary with keys from iterable and values set to value.

get(key, default): Returns the value for key if key is in the dictionary; otherwise, returns default.

items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.

keys(): Returns a view object that displays a list of all the keys in the dictionary.

pop(key, default): Removes the item with the specified key and returns its value. If the key is not found, returns default.

popitem(): Removes and returns a (key, value) pair from the dictionary.

setdefault(key, default): Returns the value of key if key is in the dictionary; if not, inserts key with a value of default and returns default.

update([other]): Updates the dictionary with the key-value pairs from other, overwriting existing keys.

values(): Returns a view object that displays a list of all the values in the dictionary.

"""