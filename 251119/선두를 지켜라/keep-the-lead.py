n, m = map(int, input().split())

ls1=[0 for _ in range(20)]
ls2=[0 for _ in range(20)]
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

is_A=False
is_B=False
cnt=0
for i in range(now):
    if ls1[i]>ls2[i]:
        is_A=True
        if is_B==True:
            is_B=False
            cnt+=1
    elif ls1[i]<ls2[i]:
        is_B=True
        if is_A==True:
            is_A=False
            cnt+=1

print(cnt)

