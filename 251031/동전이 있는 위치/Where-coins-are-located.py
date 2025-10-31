a,b=map(int,input().split())

ls=[[0 for _ in range(a)] for _ in range(a)]

for i in range(b):
    x,y=map(int,input().split())
    ls[x-1][y-1]=1


for i in ls:
    for j in i:
        print(j,end=" ")
    print()