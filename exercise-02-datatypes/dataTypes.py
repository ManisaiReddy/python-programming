#a data type tells the interpreter what kind of value you're working with 
# Python has the following data types built-in by default, in these categories:
"""
Text Type:	str

Numeric Types:	int, float, complex

Sequence Types:	list, tuple, range

Mapping Type:	dict

Set Types:	set, frozenset

Boolean Type:	bool

Binary Types:	bytes, bytearray, memoryview

None Type:	NoneType

"""

# String
collegeName = "BITS"
print(collegeName, type(collegeName))

# numeric types

busNo = 24
attendancePercentage = 72.7
classVoltage = 10 + 5j

print(type(busNo), busNo)
print(type(attendancePercentage),attendancePercentage)
print(type(classVoltage), classVoltage.imag, classVoltage.real)
""" 
Note:

complex number is the combination of real and imaginary part

here classVoltage is the complex type

10-> 10.0 -> real
5 -> 5.0 -> imaginary

In engineering j is repleaced with i(current)
In python 5j = squrt(5)

"""
# Sequence types (list, tuple, range)
# list

deptNo = [101, 102, 103, 104, 105]

#tuple

hallTno = (0o4123, 0o4124, 0o4125)
print(hallTno)


# range

yearsOfStudy= range(3)
print(yearsOfStudy)

#Dictionary

studentsInfo={
    "name":"Manisai",
    "year":"4",
    "deptNo":"101",
    # "name":"Manisai" ignored by dictionary
}
print(type(studentsInfo), studentsInfo)

# set
# takes only uniques
studentIds = {1,2,3,5,2,1}
print(type(studentIds), studentIds)

# frozenset for immutability

newStudentIds = frozenset([1,2,3,5,2,1])
# newStudentIds.add(10) it is immutable 
print(type(newStudentIds), newStudentIds)

# none
backLogs = None
print(backLogs,type(backLogs))


# boolean
areTheyPassed = True
print(areTheyPassed, type(areTheyPassed))

# bytes
# Immutable 
asciValues = bytes([65])
print(asciValues)


# bytearray
# mutable version of bytes
newAsciiValues = bytearray([65])
newAsciiValues.append(66)
print(newAsciiValues)

# memoryview

# way to access memory of bytes, bytearrys, and other binary obj without copying!
ba = bytearray([1, 2, 3, 4, 5])
mv = memoryview(ba)

print(mv[1])        # 2
mv[1] = 99
print(ba)           # bytearray(b'\x01c\x03\x04\x05')


import math
print(math.pi)
print(math.sqrt(4))
import random
print(random.choice([1.0,2.0,3.0]))
name = 'Manisai'
print(name)
print(name[0])
print(len(name))
print(name[-1])
print(name[0:3])
print(name+'Reddy')
print(name*2)
# name[0]='A'
print(name.find('ai'))
print(name.replace('a','z'))

substr = 'kaa,bbb,ccc,ddd'
print(substr.split(','))
print(substr.upper())
print(substr.lower())
print(substr.capitalize())
print(name.isalpha())
line = ' aaa,bbb,ccccc,dd '
print(line.rstrip())
print(dir(name))