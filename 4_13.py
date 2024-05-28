import math 
a=int(input("Введите a="))
b=int(input("Введите b="))
c=int(input("Введите c="))
d=b*b-4*a*c
if d<0:
    print("Вещественные корней нет ")
elif d=0:
    print("один вещественные корень")
else:
    print("Два вещественные корня")
