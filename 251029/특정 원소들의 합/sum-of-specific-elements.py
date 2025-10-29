sum=0
for i in range(1,5):
    ls=list(map(int,input().split()))
    for j in range(i):
        sum+=ls[j]
print(sum)
