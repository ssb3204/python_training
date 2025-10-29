x,y=map(int,input().split())

a=[]
b=[]
for _ in range(x):
    ls=list(map(int,input().split()))
    a.append(ls)

for _ in range(x):
    ls=list(map(int,input().split()))
    b.append(ls) 


for i,j in zip(a,b):
    for f,s in zip(i,j):
        if f==s:
            print(0.end=" ")