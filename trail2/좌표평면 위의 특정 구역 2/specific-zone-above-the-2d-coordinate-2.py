n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]


total=1600000000
# Please write your code here.
for i in range(n):
    lx=[]
    ly=[]
    for j in range(n):
        if i!=j:
            lx.append(x[j])
            ly.append(y[j])

    total=min(total,(max(lx)-min(lx))*(max(ly)-min(ly)))

print(total)