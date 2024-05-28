a=open("10.txt","w")#Открытие файла для Запись.
k=0
import random as r #ипортируем модуль random
print("началние символи:")
for i in range(10):#цикл для заполнения сул.чис.
    b=r.randint(0,1)
    a.write(str(b)+"\n")
    print(b)
a.close()#Закрытие файла
#Открытие файла для Чтение и Запись.
with open('10.txt','r') as ff,open('101.txt','w') as fx:
    for s in ff:
        if int(s)==k: 
            fx.write(str(1)+"\n")#Запись 1
        else:
            fx.write(str(0)+"\n")#Запись 0
with open('101.txt','r') as re:#Открытие файла для Чтение
    print("Замененные символы")
    for line in re:
        print(line, end="")
