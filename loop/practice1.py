# WAP to find the sum of first n natural numbers.(useing while loop)
# num = int(input("Enter a number: "))

# i =1 
# sum = 0
# while i <= num:
#     sum += i
#     i += 1
# print(f"Natural Number is {num} and sum of the natural Number is {sum}")   

#WAN to find factorial of first n natural numbers.(using for loop)
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")