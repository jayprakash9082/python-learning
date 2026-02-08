# Functions:
"""Definition:
A function is a reusable block of code that performs a specific task.
It runs only when it is called, and it can take inputs (parameters) and return an output
def function_name(parameters):
    # code block
    return result
"""
#Ex 1 
# def hello():
#     print("Thsi is Hello function and i am doing Hello!")
# hello()    

#Parameters:
#Parameters are variables listed in a function definition that receive values when the function is called.
# Arguments:
# Arguments are the actual values that are passed to a function when it is called.

# Positional argument 
def sum(a,b):
    print(f"the sum of your number is {a+b}")
sum(5,2)

# Default argument
def Hello(name,age):
    print(f"Your name is {name} and your age is {age}")

Hello(age = 21 ,name = "prakash")

# keyword Argument 
def add(a,b=10):  # here 10 is default parameter 
    print(f"the sum of your number is {a+b} ")

add(10,11)    # here 11 is default argument

#Q1 

def pallindrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print(f"{st} it is pallindrome")   
    else:
        print(f"{st} is not a pallindrome")

pallindrome("naman")
pallindrome("prakash")

def hello():  # Here we are using return function
    return "Hello how are you"
print(hello())

# =========================
# PRACTICE QUESTIONS
# =========================

#Q1 Write a function to check whether a number is even or odd

def oddEven(a):
    if a % 2 == 0:
        print("this is even")
    else:
        print("this is odd")    
oddEven(7)        

#Q2 Take an integer and print the sum of its digits.

def sum_of_n(n):
    total = 0 
    for i in range(1,n+1,1):
        total = total + i
    return total
result = sum_of_n(5)
print(result)  

#Q3 Check whether a given number is positive, negative, or zero.

def check_number(n):

    if n == 0:
        return " zero "
    elif n < 0:
        return "negative"
    else:
        return " positive "

num = int(input())
result = check_number(num)
print(result)

#Q4 Count how many digits are in a given number.

def digit(n):
    num = n 
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count 
n = int(input())
ans=digit(n)
print(ans) 

#Q5 Write a program to reverse a number using a while loop.

def rev_num(a):
    rev = 0

    while a > 0:
        rev = rev * 10 + a %10
        a = a// 10
    return rev 

a = int(input())
final_result = rev_num(a)   
print(final_result)     

#Q6 Check whether a number is a palindrome (without converting to string).

def palindrome(a):
    original = a
    rev = 0 
    if a == 0:
       print("It is palindromic number")
    while a > 0:
        rev = rev * 10 + a % 10
        a = a // 10 
    if original == rev:
     print("it is palindromic number ")
    else:
        print("it is not a palindromic number")    

a = int(input())
palindrome(a)

#Q7 Find the factorial of a number using a function.

def factorial_num(n):
    if n == 0:
        return "Factorial of zero is not allowed"
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

n = int(input())
result = factorial_num(n)
print(result)




