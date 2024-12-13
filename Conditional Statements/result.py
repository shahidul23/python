result = int(input("Enter your result: "))

if result > 0 and result <33:
    grade = 'F'
elif result >=33 and result < 45:
    grade = 'D'
elif result >=45 and result < 55:
    grade = 'B'
elif result >= 55 and result < 65:
    grade = 'B+'
elif result >=65 and result < 80:
    grade = 'A'
elif result >= 80 and result <=100:
    grade = 'A+'
else:
    print("Your Result Invalide")   
print("Your Grate is :", grade)     

