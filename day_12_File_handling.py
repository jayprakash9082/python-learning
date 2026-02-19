# File Handling:
"""File handling is the process of performing operations such as reading, writing, and updating files using a programming language.
When we want to Handle the file we use file hendling"""

p = open('day_12_File_handling.py')
print(p.read())

r = open("Python.txt",'w')

r.write("Hello this is jay prakash and i am learning python ")

r.close()

r = open("Python.txt",'a')

r.write("And now i am appending some content inside the file")

r.close()
