n=input("Ввидите предложение!;")
m=0
s=0
k=0
k1=-1
for char in n:
    m=char
    if m==s:
        print("Да,есть одинаковых соседних символов(",s,s,")порядковые номер индекса=",k1,"и",k1+1)
        k=k+1
        break
    else:
        s=m
        k1=k1+1
if k<1:
    print("Не найдено одинаковых соседних символов !")
