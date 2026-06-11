n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]


total=0
# Please write your code here.
pairs.sort()
for i in range(m):
    cnt=0
    a=sorted(pairs[i])
    for j in range(m):
        b=sorted(pairs[j])
        if a==b:
            cnt+=1
        if total<cnt:
            total=cnt

print(total)