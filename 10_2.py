fay=open("films.txt","a") #Открытие файла c режим a(дозаписи)
m=input(str("Введите текст:"))
fay.write("\n"+m)
fay.close()#закрытие файла
p=input("Поиска;")
with open("films.txt") as file:#Открытие файла
    for i in file:#проверка 
        if p in i:
            print("Результат поиска:",i,end="")
