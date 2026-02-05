#Q1
# a = int(input())

# for i in range(1,a+1,1):
#     print(i,end=" ")

#Q2  

# a = int(input())
# total = 0

# for i in range(1,a+1,):
#     total = total + i

# print(total)

#Q3 

# n = int(input())

# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(i)

#Q4 

# text = "aeiou"
# count = 0

# for i in text:
#     count = count + 1

# print(count)    

#Q5 

# n = int(input())
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

#Q 6 

# n = int(input())

# for i in range(1,11):
#     if i % 2 != 0:
#         print(f"{n} * {i} = {n *i}")

#Q7 
a = "naman"
b =""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]


if b == a:
    print("Your string is pallindrome")

else:
    print("Its not a palindome")
