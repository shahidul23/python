
#practice 1
# with open('C:\Python\File IO\practice.txt', 'w') as f:
#     f.write('Hi Everyone\nwe are learning File I/O\nusing Java\nI like programming in Java')

#practice 2
# with open('C:\Python\File IO\practice.txt', 'r') as f:
#     data = f.read()
#     print(data)

# new_data = data.replace("Java", "Python")
# print(new_data)
# with open('C:\Python\File IO\practice.txt', 'w') as f:
#     f.write(new_data)

    
# with open('C:\Python\File IO\practice.txt', 'r') as f:
#     data = f.read()
#     print(data)

#Practice 3
# word = "learning"
# with open('C:\Python\File IO\practice.txt', 'r') as f:
#     data = f.read()
#     if data.find(word) != -1:
#         print("Found")
#     else:
#         print("Not Found")


#Practice 4
# def check_for_word(word):
#     with open('C:\Python\File IO\practice.txt', 'r') as f:
#         data = f.read()
#         if data.find(word) != -1:
#             return True
#         else:
#             return False

# data = check_for_word("learning")
# print(data)

#Practice 5
# def check_for_word():
#     word = "learning"
#     with open('C:\Python\File IO\practice.txt', 'r') as f:
#         data = f.read()
#         if data.find(word) != -1:
#             print("Found")
#         else:
#             print("Not Found")

# check_for_word() 

#Practice 6
# def check_for_line():
#     word = "learning"
#     with open('C:\Python\File IO\practice.txt', 'r') as f:
#         data = f.readlines()
#         len_no = 1
#         for line in data:
#             if line.find(word) != -1:
#                 print(len_no)
#             len_no +=1    
# check_for_line()

#Practice 7
# def check_for_line():
#     word = "programming"
#     line_no = 1
#     data = True
#     with open('C:\Python\File IO\practice.txt', 'r') as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()  # Output: -1

#practice 8
with open("C:\Python\File IO\simple.txt", "w") as f:
    f.write("2,3,5,6,8,67,43,23,12,67,78")

# def read_file():
#     with open("C:\Python\File IO\simple.txt", "r") as f:
#         data = f.read()
#         num = ""
#         for i in range(len(data)):
#             if data[i] == ",":
#                 print(int(num))
#                 num = ""
#             else:
#                 num += data[i]

# read_file()   

def readOneByOne():
    count = 0
    with open("C:\Python\File IO\simple.txt", "r") as f:
        data = f.read()
        num = data.split(",")
        for val in num:
            if int(val) % 2 == 0:
                count += 1
    print(count)
readOneByOne()  # Output: 4
               