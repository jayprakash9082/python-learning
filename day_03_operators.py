# What is operators:
"""Definition:
Operators are symbols that perform operations on variables or values.

"""

#Arithmetic operators:
"""Definition
Arithmetic operators are used to perform mathematical operations like addition,subtraction,multiplication,division etc.
There are 7 types of arithmetic operator.

addition         -   +
subtraction      -   -
multiplication   -   *
division         -   /
Floor division   -   //
modulus          -   %
Exponentiation   -   **  
"""

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

a = 10 
b = 5
c = 2
print(10 + 5 * 2)

x = 10
y = 5 
z = 2 
print((10 + 5) * 2)

s = 20
t = 4

print(20 / 4)

a = 20
b = 6
print(20 // 6)

a = 20 
b = 6
print(20 % 6)

a = 2
b = 4
print(2 ** 4)

a = 15
b = 4
print(a / b)

a = 15
b = 4
print(a // b)

a = 7
print(a % 2)


a = 5 
b = 10
c = 2 
d = 2

print(5 + 10 / 2 ** 2)

# Assignment operators: 
"""Definition:
Assignment operators are used to assign values to variables
=       -      Equals to
+=      -      Add and assign
-=      -      Subtract and assign
*=      -      Multiply and assignA
/=      -      Divide and assign
//=     -      Floor divide and assign
%=      -      modulus and assign
**=     -      Exponentiation and assign
"""

a = 20      # initial value
a = 40      # reassigning the  new value

print(a)   # Output: 40, because the value of 'a' was reassigned from 20 to 40

# =========================
# PRACTICE QUESTIONS
# =========================

a = 10 
a += 5
print(a)

b = 20
b -= 7
print(b)

c = 3
c *= 4
print(c)

d = 16
d /= 4
print(d)

e = 17
e //= 3
print(e)

f = 10
f %= 3
print(f)

g = 2
g **= 3
print(g)

y = 8
y *= 2
y //= 3
print(y)

z = 5
z += 2
z *= 3
print(z)

a = 10
a += 5 * 2
print(a)

b = 20
b -= 3 ** 2
print(b)

c = 4
c *= 2 + 3
print(c)

d = 50
d //= 3 + 2
print(d)

f = 100
f %= 7 + 3
print(f)


x = 10
x += 5
x *= 2
print(x)

z = 6
z //= 2
z += 4
print(z)

a = 3
a *= 2
a **= 3
print(a)

a = 5
a += 3 * 2
a **= 2
print(a)

b = 10
b -= 4 + 2
b *= 3
print(b)

c = 8
c //= 2 + 2
c += 3 ** 2
print(c)

d = 6
d *= 2 + 3
d -= 4 // 2
print(d)

e = 9
e %= 4 + 1
e **= 2
print(e)


#Comparison operator 
"""
Definition:
Comparison Operator also called relational operator are used to compare two values.
It always provide boolean result that is true and false.
Comparison operators are as follow:
1.  ==       -       Equal tp
2.  !=       -       Not equal to 
3.  >        -       Greater than 
4.  <        -       Less than
5.  >=       -       Greater than equal to 
6.  <=       -       Less than equal to 
"""
a = 10
b = 5
print(a == b)
print(a != b)
print(a > b )
print(a < b)
print(a >=b )
print(a <= b)

a = "A"
b = "C"
print(a == b)
print(a != b)

print(ord(a))
print(ord(b))

# =========================
# PRACTICE QUESTIONS
# =========================

a = 10 
b = 10
print(a == b )

print(5 != 3)

print(8 > 12)

print(7 <= 7)

print(15 >= 10)

A = "A"
a = "a"
print("A" < "a")

print(ord(A))
print(ord(a))

print(3 + 2 == 5)

print(10 - 4 > 3)

print(6 * 2 != 12)

print(9 // 2 == 4)

a = 10
a += 5
print(a == 15)

b = 20 
b -= 3*2
print(b > 10)

c = 4 
c *= 2+1
print(c == 12 )

d = 15
d //= 4
print(d <=3)

e  = 5 
e **= 2
print(e != 25 )

f = 10
f += 5*2
print(f >= 20)

x = 8
x &=3          #here is bitwise  Operator not Moduls
print( x == 2)

print(8 % 3)

y = 6 
y -= 2 
y *=3
print(y < 15)

z = 10
z //= 3
print(z == 3)

a = 2
a += 2
a **= 2
a //= 5
print(a == 5)

# Logical operators 
"""Definition:
Logical operators in python are used to combine multiple conditions and return a Boolean result (True or false)
There are 3 types of logical operator
. and    - Return True if both condition are True.
. or     - Return true if atleast onecondition is true.
. not    - Reverse the boolean value. """

# =========================
# PRACTICE QUESTIONS
# =========================

print(123 > 130)

print((456 == 456)!= (235 == 236))

print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)

print(True and bool(0))

print(10 > 5 and 3 < 1)

a = 5 
a += 3
print(a == 8)

print(not(5==5))

x= 10
print(x % 3 == 1)

print(bool(" "))

a = 4
b = 2
print(a * b > a + b)

print(7 // 2 == 3 and 5 > 4)

a = 6
a -= 2
print(a >= 4)

print(not bool([]))

a = 10
a += 5 * 2
print(a == 20 and a > 15)

b = 8
b %= 3
print(b == 2 or b == 1)


c = 3
c **= 2
print(c < 10 and not c == 9)

d = 20
d //= 3
print(d == 6 and d < 7)

print(bool("") and bool("Python"))

x = 5
y = 0
print(x and y or 10)

a = 4
a *= 2
a -= 3
print(a == 5 or a > 10)

z = 6
z //= 4
print(z == 1 and bool(z))

print(bool([]) or (5 and 0) or "Hi")


