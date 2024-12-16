#practice 1
nums = ["Barisal", "Chattogram", "Dhaka", "Khulna", "Mymensingh", "Rajshahi", "Sylhet"]
heroes = ["Thor", "Ironman", "Captain America", "Black Widow", "Hulk", "Spiderman", "Doctor Strange"]

# def print_len(list):
#     print(len(list))


# print_len(nums)
# print_len(heroes)


#practice 2
# def print_item(items):
#     for item in items:
#         print(item, end=",")

# print_item(nums)
# print_item(heroes)

#practice 3
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *=i
#     return(fact)

# numbers = int(input("Enter a factorial Number:"))
# print(factorial(numbers))

#practice 4
# def convertUsdToInr(Dlr):
#     Inr = float(Dlr*125.25 )
#     print(f"{Dlr} USD = {Inr} BDT")

# vle = int(input("Enter amount:"))
# convertUsdToInr(vle)

def odd_event(num):
    if num % 2 != 0:
        print("Odd")
    else:
        print("Even")
num = int(input("Enter a Number:"))
odd_event(num)



    


