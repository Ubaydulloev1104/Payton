from collections import Counter
n = input("Вводите значение(n<=9999) n= ").strip()
if any(count == 3 for digit, count in Counter(n).most_common()):
    print("Да,это число ",n ," содержит ровно три одинаковые цифры ")
else:
    print("Нет,это число",n, " не содержит три одинаковые цифры ") 

