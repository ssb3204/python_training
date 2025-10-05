a,b = map(int,input().split())

lf=[list(map(int,input().split())) for _ in range(a)]
ls=[list(map(int,input().split())) for _ in range(a)]

for i in range(a):
    for j in range(b):
        if lf[i][j]==ls[i][j]:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()