# loops:
"""Definition:
Loops are used to repeat a block of code multiple times instead of writing it again and again.
There are 2 types of loops in python. For loop and While loop.

For loop: A for loop runs the same code again and again for each item in a sequence range().

While loop: A while loop is used to repeat a block of code as long as a given condition remains true.
"""

# For loop 


a  = range(1,21,1)

for i in a :
    print(i)

for i in range(20,0,-1):
    print(i)  

for i in range(5,51,5):
    print(i)  

n = int(input("which table you want to print:- "))  

for i in range(n,n*10+1,n):
    print(i)

# loops for strings

a = "PRAKASH" 
print(len(a))
for i in range(0,len(a),1):
    print( a[i] )

a = "Jay prakash"
for i in a:
    print(i)

#Break Continue else

for i in range(1,21,1):
    if i == 15:
        break       # break   
    print(i)
   
for i in range(1,16,1):
    if i == 11:
        continue      #Continue            
    print(i)   

for i in range(1,21):
    if i == 45:
        print("Break Statement is executed")    
    print(i)
else:
    print("break statement is not executed")        

# =========================
# PRACTICE QUESTIONS
# =========================

#Q1 Accept an integer and Print hello world n times

n = int(input("plese tell your number:- "))

for i in range(n):
    print("Hello world")

#Q2 Print natural number up to n.

n = int(input("please tell your number:- "))

for i in range(1,n+1):
    print(i)

#Q3 Reverse for loop. Print n to 1.

n = int(input("Enter the number:- "))

for i in range(n,0,-1):
    print(i)

#Q4 Take a number as input and print its table.

n = int(input("which table you want:- "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i} ")

#Q5 Sum up to n terms

n = int(input("Please tell your number:- "))
sum = 0
for i in range(1,n+1,1):
    sum = sum + i

print(f" sum of {n} is :", sum)

#Q6 Factorial of a number 

n = int(input("Please tell your factorial number:- "))
fact = 1
for i in range(1,n+1):
    fact = fact * i 

print(f"factorial of {n} is: ",fact)    

#Q7 Print the sum of all even & odd numbers in a range separately

n = int(input("Please enter your number:- "))
even = 0
odd = 0
for i in range (1,n+1):
    if i % 2 == 0:
        even = even + i 
    else:
        odd = odd + i

print(f"your even and odd sum are {even},{odd}")   

#Q8 Print all the factors of a number

n = int(input("Enter your number:- "))

for i in range(1,n+1):
    if n % i == 0:
        print(i)

#Q9  Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself Ex - 6 = 1, 2, 3 =

n = int(input("Enter your number:- "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("Your number is a perfect number")         
else:
    print("Your number is not a perfect number")

#Q10 Check wether the number is prime or not.

n = int(input("Check your number is prime or not:- "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("Your number is prime")
else:
    print("your number is not  prime")       

#Q11 Reverse a string without using in build functions.

a = "PRAKASH"
for i in range(len(a)-1,-1,-1):
    print(a[i])


        