ls=list(map(int,input().split()))
sum=0
for i in range(len(ls)):
    if ls[i]==0:
        for j in range(i-3,i):
            print(j,end="")
            sum+=j

print(sum)