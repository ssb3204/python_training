n, m = map(int, input().split())

ls1=[0 for _ in range(1000001)]
ls2=[0 for _ in range(1000001)]
# Process A's movements

now=1

for _ in range(n):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        ls1[now]=ls1[now-1]+vi
        now+=1
now=1
for _ in range(m):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        ls2[now]=ls2[now-1]+vi
        now+=1

rank=[]
cnt=1
for i in range(1,now):
    if ls1[i]>ls2[i]:
        rank.append(1)
    elif ls1[i]<ls2[i]:
        rank.append(2)
    else:
        rank.append(3)

for i in range(len(rank)-1):
    if rank[i]!=rank[i+1]:
        cnt+=1

print(cnt)


