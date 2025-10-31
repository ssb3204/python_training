ls=[[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        if i==0 or j==0:
            ls[i][j]=1
        else:
            ls[i][j]=ls[i-1][j]+ls[i][j-1]

for i in ls:
    for j in i:
        print(j,end=" ")
    print()