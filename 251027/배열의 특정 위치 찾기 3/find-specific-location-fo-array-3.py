ls=list(map(int,input().split()))
sum=0
for i in range(len(ls)):
    if ls[i]==0:
        for j in range(i-3,i):
            sum+=ls[j]
        break
    
print(sum)