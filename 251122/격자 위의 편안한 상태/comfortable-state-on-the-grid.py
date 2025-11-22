n, m = map(int, input().split())
ls =[[0 for _ in range(n)] for _ in range(n)]

# Please write your code here.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if ls[nx][ny] == 1:
                cnt += 1

    return cnt == 3




for i in range(m):
    x,y=map(int,input().split())
    x=x-1
    y=y-1
    ls[x][y]=1
    if check(x,y):
        print(1)
    else:
        print(0)
