N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

maxnum=0
total=0
# Please write your code here.
for i in ranges:
    maxnum=max(maxnum,max(i))

for i in range(-2,1002):
    work=0
    for j in ranges:
        if i<j[0]:
            work+=C
        elif j[0]<=i<=j[1]:
            work+=G
        elif j[1]<i:
            work+=H
        
    if total<work:
        total=work
    if i>maxnum+1:
        break
print(total)