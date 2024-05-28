import math as m
x=int(input("Вводите значение x = "))
y=int(input("Вводите значение y = "))
z=int(input("Вводите значение z = "))
a=((m.sqrt(x-1))-(y**(1./3.)))/(1+((x**2)/2)+((y**2)/4))
b=x*(m.atan(z)+(m.e**-(x+3)))
print("Ответ; a=",a,"b=",b)
