n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dx=[0,-1,0,1]
dy=[-1,0,1,0]

def in_dex(x,y):
    return 0<=x and x<n and 0<=y and y<n

x,y=n-1, n-1
grid[x][y]=n*n
d=0

for i in range(n*n-1,0,-1):
    nx,ny=x+dx[d],y+dy[d]
    if not in_dex(nx,ny) or grid[nx][ny]!=0:
        d=(d+1)%4
    x,y=x+dx[d],y+dy[d]
    grid[x][y]=i    

for i in grid:
    for j in i:
        print(j,end=" ")
    print()