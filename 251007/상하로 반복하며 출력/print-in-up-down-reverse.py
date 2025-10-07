a=int(input())
l=[[0]*a for _ in range(a)]

for i in range(a):
    for j in range(a):
        if i%2==0:
            l[j][i]=j+1
        else:
            l[j][i]=a-j

for i in range(a):
    for j in range(a):
        print(l[i][j],end="")
    print()