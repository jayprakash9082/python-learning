# Data type
"""Definition:
Data types define the type of data that can be stored in a variable.
They tell us what kind of value a variable holds."""

# types of data type 
"""
Integer -> this is used to store numbers in variable.
Float   -> this is used to  store decimal point value and fraction. 
Complex -> This is used to store imaginary numbers like 32j, where 'j' is the imaginary unit.
String -> This is used to store text data enclosed in single or double quotes.
Boolean -> This is used to store True and False values.

And more 

"""
a = 225          # this is integer
print(type(a))   

b = 1.5          # this is float
print(type(b))

c = 34j              # this is complex 
print(type(c))     #j is imaginary 

d = " Jayprakash"
print(type(d))       # this is string 

e = True
print(type(e))           # this is bool 


# String indexing

a = "Jayprakash"

print(a[0])
print(a[1])

"""There are two types of String indexing are there.
1 positive indexing -> starts from 0 , 1,2...
2 Negative indexing -> starts from last -1,-2,-3...
"""

# String Slicing
""" Definition:
String slicing means extracting a specific part (substring) of a string using an index range.

> string[start : end : step]
"""

st="Jayprakash"
print(st[0:10:1])

# Type conversion 
"""Definition:
Type conversion means changing one data type into another data type.
eg. int()->float()->str()->bool()
"""
a=12
a = str(a)
print(type(a))
print(a) #==> "12" (a will be converted to string)

a = 10          # int
b = float(a)   # int → float
c = str(b)     # float → str
d = bool(c)    # str → bool

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


# there are two types of Type conversion
# Implicit
""" Definition:
Implicit type conversion means Python automatically converts one data type into another.
"""
# eg - a = 12
# print(a/2)

a = 12
print(a/2)      #==> 6.0 (a convert into float )

# Explicit 
""" Definition:
Explicit type conversion means converting one data types to Another data types manually using Type casting function
Common Type Casting Functions:
int()
float()
str()
bool()
list()
tuple()
set()
"""
x = 1
x = float(x)
x = str(x)
x = bool(x)

print(x)

#Input and Output
""" input:
Input means that data given to the program by the user.
We use the input() function to take input from the user.
"""
name = input("Please enter your name")
print(f"Welcome back {name}")

Age = int(input("tell me your age "))
print(Age)



"""Output:
It means the data that the program displays to the user.
 """

name="Jayprakash"
print("Hello!", name)

name2 = "prakash"
age2 =23
city = "mumbai"

print(f"Hello my name is {name2} my age is {age2} and i'am from {city}") 
# Here i'am using Formated string (f{}),
 