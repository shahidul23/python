import os
#only read file

# file = open("C:\Python\File IO\demo.txt", "r")
# data = file.read()
# print(data)
# print(type(data))
# file.close()

#read spacific caracter
# file = open("C:\Python\File IO\demo.txt", "r")
# data = file.read(5)
# print(data)
# file.close()

#read line by line
# file = open("C:\Python\File IO\demo.txt", "r")
# data = file.readline()
# print(data)
# file.close()

#Write and read a file
# file = open("C:\Python\File IO\demo.txt", "w")
# file.write("This is Shahidul islam \nI am a python developer\nand I am learning file IO")
# file.close()

# f = open("C:\Python\File IO\demo.txt", "r")
# data = f.read()
# print(data)
# f.close()

#file append
# file = open("C:\Python\File IO\demo.txt", "a")
# file.write("\nI am a python Engineer\nand I am learning file IO")
# file.close()

# f = open("C:\Python\File IO\demo.txt", "r")
# data = f.read()
# print(data)
# f.close()

# line by line read using for loops
# file = open("C:\Python\File IO\demo.txt", "r")
# data = file.readlines()
# file.close()

# for el in data:
#     print(el)

# read file using r+ mode
# file = open("C:\Python\File IO\demo.txt", "r+")
# file.write("My name is")
# print(file.read())
# file.close()

#using with method 
with open("C:\Python\File IO\demo.txt", "r") as file:
    print(file.read())
    file.close()

file = open("C:\Python\File IO\simple.txt", "w")
file.write("Hello, Python!")
file.close()

#delete a file
# os.remove("C:\Python\File IO\simple.txt")
