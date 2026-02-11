# Data Structure:
"""Data structure helps us decide how data is kept and how fast we can find or use it.
Types of data structure
1 List
2 Tuple
3 Dictionary
4 Set
"""

# List 
"""A Before starting we need to understand some of the
terminology.

Mulable      - Mutability refers to whether an object's valuecan be changed after creation. And List allows this
Duplicates   - we know data structures are used to storemultiple values so duplicates means same value occuringmultiple time. List allows this
Ordered      - List maintains ordered data structure maintainsthe sequence of elements as they were inserted. This means you can access elements using their position(index).
Heterogenous - List have heterogenous nature that means we can have multiple data types inside the list.
"""

# a = [12,13,14,18,25,28.2]

#First way using index 
# for i in range(len(a)):
#     print(a[i])

#2nd way directly on values 

# for i in a:
#     print(i)

#Q1 Print positive and negative elements of an list
# a = [20,-30,50,-29,49,59,-69]

# print("These are positive number")

# for i in a:
#     if i >=0:
#         print(i)

# print("These are negative numbers")

# for i in a:
#     if i < 0:
#         print(i)

#Q2 Mean of list element 

# l = [12,435,67,89,23,25,69]
# total = 0
# for i in l:
#     total = total + i

# print(total/len(l))

#Q3 Find the greatest element and print its index too.

# l =[555,259,695,999,1004,2006,13,25,100,105,12]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i 

# print(f"Your greatest number is { largest} at index {index}")       
    
#Q4 Find the second largest number.

# l = [ 99,69,29,109,209,68,1008,10009,1009]

# largest = l[0]

# sec_largest= l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest 
#         largest = i
#     elif i >sec_largest:
#         sec_largest = i

# print(largest,sec_largest)

#Q5 check if list is shorted  or not 

a =  [ 12,13,14,15,16] 

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not shorted")
        break 
else:
    print("your list is sorted")    