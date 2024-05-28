vid=[4,2,6,7,2,2,4,5,6,7,8,7,2,3,4,1,3,4,3,5,1,2,4,3,4,5,9,8,1]
s1=min(vid)
r1=vid.index(s1)
print("a=",s1,"(",r1+1,")")
for i in range(len(vid)):
    if vid[i]==s1:
        s2=vid[i]
        r2=i+1
print("b=",s2,"(",r2,")")
