n=int(input("напишете n="))
k=0
while n>1:
    if n%10==3:
        k+=1
        n=n/10
print("количество 3 ровно:",k)
