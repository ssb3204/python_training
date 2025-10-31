a=int(input())

ls=[[0 for _ in range(a)]for _ in range(a)]

for i in range(a):
    for j in range(a):
        if i==0 or j==0:
            ls[i][j]=1
        else:
            ls[i][j]=ls[i-1][j]+ls[i][j-1]+ls[i-1][j-1]


for i in ls:
    for j in i:
        print(j,end=" ")
    print()