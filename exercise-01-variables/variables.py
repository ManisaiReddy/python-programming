"""
Variables are containers for storing data values
No need for explicit declaration of type
Can be assigned values at run time and can even change to any type

"""

x = 21
print(x)

"""

Variable name can be a single character or combination of characters
we have some rules that will followed to write most efficient python programing
Use camel, pascal, or snake casing for writing variable names
Don't start variable naming with number, but can end up or even in middle of name should be accepted
use alpha numerics only ( A-z, a-z, 0-9, _)
Always try to name declarative naming for variable naming (i.e give a perfect naming situable for the program)
"""
# single word variable
age = 23
#camel casing 
studentAge = 24
#pascal casing
StudentPercentage = 52.3
# snake casing
student_id = 121

print(age)
print(studentAge)
print(StudentPercentage)
print(student_id)


"""
 Many values to Many variables 
 Python allows you to assign values to multiple variables in one line
"""
deptNo, hodId, branch = 101, 122, 'ECE'
print(deptNo)
print(hodId)
print(branch)


# Make sure the number of variables matches the number of values, or else you will get an error
"""
we can also assign one value to the multiple variables
And you can assign the same value to multiple variables in one line
"""

deptNo=deptName=dept= 102
print(deptNo)
print(deptName)
print(dept)


isOkay = False

def makeHappy():
    global isOkay
    isOkay = True
    print(isOkay)
# print(makeHappy())
makeHappy()
print(isOkay)

# value type
a = 10
b = a
b = 30

print(a)
print(b)

# reference type

list1 = [1,2,4]
list2 = list1
list1.append(8)
print(list1)
print(list2)

# shadowing built in 


len = 10

print(len("hello"))