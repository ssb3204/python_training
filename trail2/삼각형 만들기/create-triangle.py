n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

total=0

for i in range(n):
    xi,yi = points[i]
    xmax=0
    ymax=0
    for j in range(n):
        if i==j:
            continue
        xj,yj =points[j]
        if yi==yj:
            xmax=max(xmax,abs(xj-xi))
        if xi==xj:
            ymax=max(ymax,abs(yj-yi))
    
    total=max(total,xmax*ymax)

print(total)