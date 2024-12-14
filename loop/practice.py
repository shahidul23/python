#practice 1
# i = 1
# while i <= 100:
#     print(i)
#     i+=1
# print("End loop")   

#practice 2
# i = 100
# while i>= 1:
#     print(i)
#     i -=1
# print("End Loop")    

#practice 3
# n = int(input("Enter a number: "))
# i = 1
# while i <=10:
#     print(n*i)
#     i += 1
# print("End Loop")  

#practice 4
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1
# print("End Loop") 

# i = 1
# while i <= 10:
#     print(i * i)
#     i += 1
# print("End Loop")    

#practice 5
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = 36
while i < len(tuple):
    if x == tuple[i]:
        print("Number found at inxen", i) # tuple[i]
        break
    else:
        print("Number not found")
    i += 1
print("End Loop")    