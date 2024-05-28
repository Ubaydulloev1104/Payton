import math #инпортируем модуль math 
m=0 #для номер к
def DigitN(K,n):#Определение функции
    q = K
    i = 0
    while q >= 1:#цикл q>0 или q>1
        r = q % 10 
        q = int(q/10)
        i += 1
        if i == n:
            return r
    return -1
for i in range(0,5):#цикл от 0 до 5
    x=int(input("Введите значения к="))
    n=int(input("Введите значения n=")) 
    m=m+1#k1,k2,k3,..k5
    print("k",m,"=",x,": N=",n,":",DigitN(x,n))#визив функции
