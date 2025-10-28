ls=list(map(int,input().split()))
a=[0]*6
for i in range(len(ls)):
    a[ls[i]-1]+=1

for i in range(6):
    print(f"{i+1} - {a[i]}")
