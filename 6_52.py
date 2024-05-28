n=int(input("Введите число "))
if n==2:
    print("Это простое число")
if n<=1 or n%2==0 or n%3==0 or n%5==0 or n%7==0:
     print("Это сложное число")
else:
    print("Это простое число")
