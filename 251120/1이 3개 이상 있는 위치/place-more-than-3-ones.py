n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def in_dex(x,y):
    return 0<=x and x<n and 0<=y and y<n

total=0
for i in range(n):
    for j in range(n):
        cnt=0
        for x,y in zip(dx,dy):
            nx,ny=i+x,j+y
            if in_dex(nx,ny) and grid[nx][ny]==1:
                cnt+=1
        if cnt>=3:
            total+=1

print(total)