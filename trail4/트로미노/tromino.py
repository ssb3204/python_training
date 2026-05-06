n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
total=0

for i in range(n-1):
    for j in range(m-1):
        box=[grid[i][j],grid[i+1][j],grid[i][j+1],grid[i+1][j+1]]
        total=max(sum(box)-min(box),total)


for i in range(n):
    for j in range(m-2):
        linetotal=grid[i][j+0]+grid[i][j+1]+grid[i][j+2]
        total=max(total,linetotal)

for i in range(n-2):
    for j in range(m):
        linetotal=grid[i+0][j]+grid[i+1][j]+grid[i+2][j]
        total=max(total,linetotal)


print(total)