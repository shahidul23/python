num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Therd Number: "))

if num1 > num2 and num1 > num3:
    grater = num1
elif num2 > num3:
    grater = num2 
else:
    grater = num3
print("The Grater number is: ", grater)            