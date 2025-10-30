a=int(input())

ls=[[0 for _ in range(a)] for _ in range(a)]
cnt=1
for i in range(a):
    for j in range(a):
        ls[j][i]=cnt
        cnt+=1
    

for i in ls:
    for j in i:
        print(j,end=" ")
    print()