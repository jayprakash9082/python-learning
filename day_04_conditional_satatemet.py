#Conditional statement:
"""
Definition:
Conditional statement in python allow decision-making by python executes  different block of code based on given conditions.
Generally there are 3 types of variation in conditional
statements
.if              -   Execute if the condition is true.
.if-else         -   Execute if True, otherwiser False.
.if-elife-else   -   Checks multiple condition in sequence.
"""
# if condition:
#     code

age = 18

if age >= 18:
    print("You are eligible to vote")


# if condition:
#     code_if_true
# else:
#     code_if_false

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You are not eligible to vote")

# if condition1:
#     code
# elif condition2:
#     code
# else:
#     code

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# =========================
# PRACTICE QUESTIONS
# =========================

#Q1

age = int(input("Please enter your age:- "))
if age >= 18:
    print("you can drive") 
else:
    print("you can not drive")  

#Q2

num1 = int(input("Enter your first number- "))
num2 = int(input("Enter your second number- "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")  
else:
    print("Both numbers are equal") 

# #Q3

gen = input("Please tel your gender as character (M or F)-> ")

if (gen == "M") or gen == ("m"):
    print("Good morning sir")
elif (gen == "F") or gen == ("f"):
    print("Good morning mam")    
else:
    print("undefined gender")   


#Q4

num = int(input("Please tell your number-> "))

if num % 2 == 0 :
    print(f"{num} this is even number")
else:
    print(f"{num} This is odd number")    

#Q5
name = input("Please enter your name-> ") 
age  = int(input("And now enter your age-> "))

if age >= 18:
    print(f"Hello {name} you are a valid voter ")
else:
    print(f"Sorry {name} you can't vote")    


#Q6

year = int(input("Enter the year to check for leap year:- "))

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} this is not a leap year ")     

#Q7 if-elif ladder 

temp = int(input("Enter your temperature in celsius:- "))
if temp < 0:
    print("Freezing cold")
elif temp >= 0 and temp <= 10:
    print("very cold")
elif temp >= 10 and temp <= 20:
    print("Cold")
elif temp >= 20 and temp <= 30:
    print("Pleasant")
elif temp >= 30 and temp <= 40:
    print("Hot")
else:
    print("Very hot ")

#Q8 Grade system 
name= input("Enter your name:- ")
marks = int(input("please tell your marks:- "))

if marks >= 90:
    print(f"CongratulationS {name}, your grade is A ")
elif marks >= 75:
    print(f"CongratulationS {name}, your grade is  B") 
elif marks >= 50:
    print(f"Congratulations {name}, you got grade C ")
elif marks >= 36:
    print(f"{name}, you have pass and your grade  is D")
else:
    print(f"Sorry {name} , you have failed")             

#Q9 Accept Three number and print the largest number using conditional statement 

num1 = int(input("Enter your first number:- "))
num2 = int(input("Enter your second number:- "))
num3 = int(input("Enter your third number:- "))

if (num1 >= num2) and (num1 >= num3):
    print(f"{num1} is the greatest number ")
elif (num2 >= num1) and (num2 >= num3):
    print(f"{num2} is the greatest number")    
else:
    print(f"{num3} is the greatest number")    
 
#Q10 

correct_username = "Admin"
correct_password = 1234

username = input("Enter your username:- ")
password = int(input("Enter your password:- ")) 

if (username == correct_username) and (password == correct_password):
    print("Login successfull")
else:
    print("Invalid login ") 

#Q11 Number Nature checker

num = int(input("Enter your number:- "))

if num < 0 :
    print(f"{num} is a negative number")
elif num == 0:
    print(f"{num} is a zero ")  
elif (num > 0) and( num % 2 == 0 ):
    print(f"{num} is a positive even number ")  
else:
    print(f"{num} positive odd number ")         
  

#Q12 Simple calculator 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid operator")





