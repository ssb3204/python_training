a=[0]*4
b=[]

for _ in range(2):
    sum=0
    ls=list(map(int,input().split()))
    for i in range(4):
        a[i]+=ls[i]
        sum+=ls[i]
    b.append(sum)

for i in b:
    print(f"{i/4:.1f}",end=" ")
print()
num=0
for i in a:
    print(f"{i/2:.1f}",end=" ")
    num+=i
print()
print(f"{num/8:.1f}")