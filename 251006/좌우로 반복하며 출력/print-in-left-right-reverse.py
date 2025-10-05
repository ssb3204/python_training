a=int(input())
l=[]

for i in range(1,a+1):
    l.append(i)

for i in range(a):
    for j in range(a):
        print(l[j],end="")
    l.reverse()
    print()