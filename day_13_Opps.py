#OOp 
"""Definition:
Object-Oriented Programming is a programming paradigm based on the concept of classes and objects, where data (attributes) and behavior (methods) are encapsulated together to promote modularity, reusability, and scalability.
Encapsulation - Data ko protect karna

Abstraction  - Complex cheezein hide karna

Inheritance - Ek class dusri class ki properties le sakti hai

Polymorphism - Same method ka different behavior"""

# Imperative Approach 

a = 12 
b = 12 
print(a+b)

#Functional Approach

def addition(a, b):
    print(f"{a} + {b} = {a + b}")

try:
    num1 = int(input())
    num2 = int(input())
    addition(num1, num2)

except ValueError:
    print("Invalid input! Please enter only numbers.")


#__classes in OOP__

class  Factory:
    a = 12 # Attribute

    def hello(self):   #Method
        print("how are you")

    print("Hello how are you i am getting initialized")    

print(Factory().a)
Factory().hello()

# Objects in OOP 
class  Factory:
    a = 12 # Attribute

    def hello(self):   #Method
        print("how are you Sir")

    print("Hello how are you i am getting initialized")    

obj = Factory()  #Object 
print(obj.a)
obj.hello()

# Constructor

class  Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips 
        self.pockets = pockets
    
    def show(self):
        print(f"your object details are {self.material },{self.zips},{self.pockets}")

reebok = Factory("leather",3,2)
campus = Factory("Naylon",3,3)

reebok.show()
campus.show()

# Type of attribute 
"""
1.Class attribute - A normal variable created inside a class is a class attribute 
2.Instance attribute - A attribute creted using an instance like self.name,self.age etc . it is known as instamce attribute.  """

class Animal:
    name = "lion"  # class attribute 

    def __init__(self,age):
        self.age = age # instance attribute

    def show(delf):  # instance method 
        print("How are you")

# Using OOPs - creating student records 

class Student:    # class- blueprint or tenplate 
    def __init__(self,name,grade,percentage): # method 
        self.name = name    # Attribute
        self.grade = grade  # attribute 
        self.percentage = percentage # attrubute

    def student_details(self):  # method 
        print(f"{self.name} is in class {self.grade} and scored {self.percentage}% ")    
       

 # object - Instance of class
student1 = Student('madhav',11,90)  
# print(student1.name, student1.grade)
student2 = Student('Amar',12 ,80)  
# print(student2.name,student2.grade)

student1.student_details()
student2.student_details()        

print(student1.__dict__)

# modify object property

print(student1.percentage)
student1.percentage = 98
print(student1.percentage)


# Delete object property

print(student1.percentage)
del student1.percentage
print(student1.__dict__)

# delete object 

# del student1
# print(student1)





