sum=0
for i in range(4):
    ls=list(map(int,input().split()))
    for j in range(i):
        print(ls[j],end=" ")
        sum+=ls[j]
print(sum)
