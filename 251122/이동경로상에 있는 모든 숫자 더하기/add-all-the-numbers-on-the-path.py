N, T = map(int, input().split())
str = list(input())
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def in_dex(x,y):
    return 0<=x and x<N and y<N and 0<=y

dx=[-1,0,1,0]
dy=[0,1,0,-1]

d=0
x,y=N//2,N//2
sum=board[x][y]

for i in range(T):
    if str[i]=="R":
        d=(d+1)%4
    elif str[i]=="L":
        d=(d-1)%4
    else:
        nx,ny=x+dx[d],y+dy[d]
        if not in_dex(nx,ny):
            continue
        x,y=x+dx[d],y+dy[d]
        sum+=board[x][y]

print(sum)