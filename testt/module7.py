import random
n=int(input("Введите натуральный число n = "))
m=[random.randint(-50,50) for i in range(n)]

def f():
    s=0
    for i in range(0,n):
        if m[i] > 0:
            s = m[i] + s
    print(m)
    return("Сумма удвоенного положительного числа = " , 2*s)
