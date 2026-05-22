n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]
total=0
# Please write your code here.

ls=[0 for _ in range(1000)]
for i in range(n):
    for j in range(a[i],b[i]):
        ls[j]+=1

s=ls[:]

for i in range(n):
    ls=s[:]
    for j in range(a[i],b[i]):
        ls[j]-=1
    cnt=0
    for k in ls:
        if k!=0:
            cnt+=1
    total=max(total,cnt)

print(total)