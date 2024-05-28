import math 
x=int(input("Введите а="))
if x>0:
    d=math.sin(x)**2
else:
    d=1-(2*math.sin(x*x))
print("ответ=",d)
