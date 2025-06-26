# Conditional statements
"""
conditional statements are used for decision making and execute the program when they are true
They are:
if statement
else statement
elif statement
nested if statements
"""

# if statements
"""
if statements are used for decision making and executes the block of code inside it when the condition is true

"""

x = 10
if x>5:
    print("Hey there 10 is greater than 5")
    
    
# else statement

"""
else statement is used as a fallback action for the if statement
when we need possible outcome we use it
"""

if x%2 == 0:
    print(f"{x} is a even number")
else:
    print(f"{x} is not an even number i.e odd")

# elif

"""
elif stands for else if
It is used to check the multiple conditions within a block to get desired outcome
It is more cleaner avoiding the nested if statements
"""

grade = 70
if grade<= 60:
    print("Got B+")
elif grade == 70:
    print("Got A+")
elif grade >= 70:
    print("Got O")


# nested if statements

"""
nested if statements : stements inside another if statements
control over more complex conditions
"""

if grade>=70:
    print("entered first if block")
    if grade<70:
        print("entered into nested")