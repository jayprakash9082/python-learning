#Exception Handling
"""Exception Handling is a mechanism in Python that allows a program to detect, handle, and respond to runtime errors so that the program does not crash unexpectedly.
Try      - wrap the block of code that might cause an exception.
Except   - Handle the exception if it occurs.
else     - Run code only if no exception occurs 
Finally  - Run code no matter what whether there's an exception or not.
Raise    - Manually throw an exception.
"""
"""There are three main types of errors in Python:
1.Syntax Errors
2.Runtime Errors (Exceptions)
3.Logical Errors
"""
a = int(input("Tell your number :- "))

try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an error as {err}")

else:
    print("Good there is no exception")

finally:
    print("I will run no matter what") 

print("Ok i have done the division")

# Raise
age = int(input("Tell your age:- "))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club ")

except Exception as err:
    print(f"An error occurs as {err}")


print("The club will start soon")    