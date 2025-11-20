n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def in_dex(x,y):
    return 0<=x and x<n and 0<=y and y<m

x,y=0,0
arr[x][y]=1
d=0

for i in range(2,m*n+1):
    nx,ny=x+dx[d],y+dy[d]
    if not in_dex(nx,ny) or arr[nx][ny]!=0:
        d=(d+1)%4
    x,y=x+dx[d],y+dy[d]
    arr[x][y]=i    

for i in arr:
    for j in i:
        print(j,end=" ")
    print()