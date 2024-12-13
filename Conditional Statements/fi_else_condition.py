age = int(input("Enter your age: "))

if age > 0 and age <= 18 :
    print("You Can Vote")
    print("You Can Drive")
elif age >= 19 and age <= 33:
    print("You Should Maride")
elif age >= 34 and age <=40:
    print("You Got Baby")
else:
    print("You are Invalide")           