s1=str(input("Введите S1 строку: "))
s2=str(input("Введите S2 строку: "))
n1=int(input("Введите N1 строку: "))
n2=int(input("Введите N2 строку: "))
a=len(s2)
a1=a-n2
s=s1[0:n1]+s2[a1:a]
print("Ответ: ",s)
