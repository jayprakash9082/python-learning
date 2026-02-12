#Tuple:
"""
A tuple in Python is an ordered collection of elements that cannot be changed after it is created.

It is written using round brackets().
"""

a = (12,2,3,4,5,5,5,5,6,155,True)

index = a.index(5)
print(index)

count = a.count(5)
print(count)


#Set 
"""Intoduction
A Set is an unordered collection of unique elements
"""
s = {1,2,3,4,5}


print(s)

A = {1,2,3,4,5}
B = {4,5,6,7,8}

union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)
symmetric_diff = A.symmetric_difference(B)

print(union_set)                #print(A | B)
print(intersection_set )        #print(A & b)
print(difference_set)           #print(A - B)
print(symmetric_diff)           #print(A ^ B)