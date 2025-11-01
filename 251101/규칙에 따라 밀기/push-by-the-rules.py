a=list(input())
b=list(input())

for i in b:
    if i=="L":
        c=a[:1]
        m=a[1:]
        a=m+c
    else:
        c=a[-1:]
        m=a[:-1]
        a=c+m

for i in a:
    print(i,end="")