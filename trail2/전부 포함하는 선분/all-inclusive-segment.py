n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

ls=[]
total=101


# Please write your code here.
for i in range(n):
    x=[]
    y=[]
    for j in range(n):
        if i==j:
            continue
        x.append(segments[j][0])
        y.append(segments[j][1])
    l=max(y)-min(x)
    if total>l:
        total=l
    

print(total)
