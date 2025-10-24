a=int(input())
ls=[[0]*a for i in range(a)]

for i in range(0,a):
    for j in range(a):
        if i%2==0:
            ls[j][i]=j+1
        else:
            ls[j][i]=a-j

for i in ls:
    print("".join(map(str, i)))