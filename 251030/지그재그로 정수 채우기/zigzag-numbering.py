n, m = map(int, input().split())

ls=[[0 for _ in range(m)] for _ in range(n)]

cnt=0
# Please write your code here.
for i in range(m):
    for j in range(n):
        if i%2==0:
            ls[j][i]=cnt
            cnt+=1
        else:
            ls[n-j-1][i]=cnt
            cnt+=1

for i in ls:
    for j in i:
        print(j,end=" ")
    print()
