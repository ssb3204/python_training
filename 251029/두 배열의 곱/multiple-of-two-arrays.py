a=[]
b=[]

for _ in range(3):
    ls=list(map(int,input().split()))
    a.append(ls)
e=input()
for _ in range(3):
    ls=list(map(int,input().split()))
    b.append(ls)
k=0
for i,j in zip(a,b):
    num=([x*y for x,y in zip(i,j)])
    print(*num,end=" ")
    print()