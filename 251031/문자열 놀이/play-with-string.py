a,b=input().split()

b=int(b)
a=list(a)
for i in range(b):
    ls=list(map(str,input().split()))
    if ls[0]=="1":
        t=a[int(ls[1])-1]
        a[int(ls[1])-1]=a[int(ls[2])-1]
        a[int(ls[2])-1]=t
    else:
        ls[1]=str(ls[1])
        ls[2]=str(ls[2])
        for j in range(len(a)):
            if a[j]==ls[1]:
                a[j]=ls[2]
    
    for j in a:
        print(j,end="")
    print()

