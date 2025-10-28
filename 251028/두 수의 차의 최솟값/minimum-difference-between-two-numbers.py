a=int(input())
ls=list(map(int,input().split()))
min_v=100
for i in range(a-1):
    if min_v>ls[i+1]-ls[i]:
        min_v=ls[i+1]-ls[i]

print(min_v)