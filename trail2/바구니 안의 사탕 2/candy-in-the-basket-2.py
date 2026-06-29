N, k = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
def in_range(i):
    return 0<=i<len(ls)


max_range=max(pos)
total=0
ls=[0 for _ in range(max_range)]

for i in range(N):
    ls[pos[i]-1]+=candy[i]

for i in range(len(ls)):
    cnt=0
    for j in range(i-k,i+k+1):
        if in_range(j):
            cnt+=ls[j]
        else:
            continue
    if total<cnt:
        total=cnt
print(total)