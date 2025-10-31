a=int(input())

ls=[[" " for _ in range(a)] for _ in range(a)]

for i in range(a):
    for j in range(i+1):
        if j==0 or j==i:
            ls[i][j]=1
        else:
            ls[i][j]=ls[i-1][j-1]+ls[i-1][j]


for i in ls:
    for j in i:
        print(j,end=" ")
    print()
