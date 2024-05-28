b=int(input("Введите радиус круга= "))
a=int(input("Введите сторна квадра= "))
a=a*a
b=b**2*3.14
if a<b:
    print('Круг')
else:
    print('Квадрат')
