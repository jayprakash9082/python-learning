# Dictionry 
"""Definition:
A dictionary in Python is a mutable data structure that stores data in key value pairs where each key is unique.

"""
# d = {1:"Hello",2:56}
# print(type(d))
# print(d)

# d = {"name":"jp" , "age" : 23}
# print(d["name"])

# d={10: 100,20:200,30:300,40:400}
# d[10] = 1000   #Updating
# d[50] = 500    #creating
# del d[30]     # deleting
# print(d)


# d={10: 100,20:200,30:300,40:400}

# for i in d.values():
#     print(i)
    


# d={10: 100,20:200,30:300,40:400}

# d.clear()

#Q1  Write a Python script to merge two Python dictionaries? 

# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600 }

# for i in d2:
#     d1[i] = d2[i]
    
# print(d1)   

#Q2Y Write a Python program to sum all the values in a dictionary?


d1 = {1:10,2:20,3:30,4:40,5:50}
total = 0

for i in d1.values():
    total = total+ i
print(total)    

