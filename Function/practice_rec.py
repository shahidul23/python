#practice 1
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)

# num = int(input("Enter the Nth number: "))
# print("Sum of first", num, "natural numbers is", sum(num))

#practice 2

# def print_list(list, idx=0):
#     if idx == len(list):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# list = ['a', 'b', 'c', 'd', 'e']
# print_list(list)

#practice 3
def List_print(list, idx):
    if idx < len(list):
        print(list[idx])
        List_print(list, idx+1)

contrys = ["Bangladesh", "India","Japan", "Chine", "Botan", "Canada"]
List_print(contrys, 0)