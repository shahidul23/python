#print 1 to n Recursive function
# def print_numbers(n):
#     if n==0:
#         return
#     print(n)
#     print_numbers(n-1)

# num = int(input("Enter Number of N:"))
# print_numbers(num)

#practice 2
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
num = int(input("Enter Number of N:"))
print(fact(num))  # Output: 3628800
