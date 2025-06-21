# operators are used to perform specific operations on variables and values
# we have
"""
 Arithematic 
 Assignment
 Comparision
 Bitwise
 Logical
 Identity
 Membership
"""

x = 4
y = 2

# Arithematic operators +, - , *, /, //, %, **
print("Here are the arithematic operators")
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x//y)
print(x**y)


# Assignment operators
print("Here are the assignment operators")

z= 5
print(z)
x+=z
print(x)
x-=z
print(x)
x*=z
print(x)
x/=z
print(x)
x%=z
print(x)
x//=z
print(x)
x**=z
print(x)

# comparision operators
print("Here are the comparision operators")
print(x>z)
print(x<z)
print(x<=z)
print(x>=z)
print(x==z)
print(x!=z)


# Identity operators

print("Here are the Identity operators")

vehicles = ["cars","bikes","jeep","TATA ACE"]

travels =  vehicles

print(vehicles is not travels)

# Membership operators

fruits = ["apples","bananas"]
print("bananas" not in fruits)


# Bitwise operators

# and, or, not, xor, <<, >>
print("Bitwise operators")
print(1 & 13)

print( 1 | 13)

a =1
b=2
print( ~b)

print( 1 ^ 12)

print(4>>2)
print(4<<1)

print("here are the logical operators")

animal = "cow"

godAnimal = "cow"

print( a>b and b<1)
print( a>b or a<b)
print(not b<a)