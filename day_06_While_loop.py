# While loop:
""" Definition:
A while loop is a control flow statement in programming that repeatedly executes a block of code as long as a given condition remains true.
The condition is checked before each iteration, and the loop stops when the condition becomes false

WHILE battery < 100:
    charging ON

"""

# =========================
# PRACTICE QUESTIONS
# =========================

#Q1

a = 1 

while a <= 30:
    print(a)
    a = a + 1 

#Q2

a = int(input())

while a > 0:
    print(a % 10)
    a = a // 10 

#Q3 

a = int(input())
rev = 0 
while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(rev)    

#Q4 Palindromic number 

a = int(input())
copy = a 
rev = 0 
while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(rev)    

if copy == rev:
    print(" Pallindromic number")
else:
    print("Not a palindromic number")    
