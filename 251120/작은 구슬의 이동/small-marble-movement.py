n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dx=[0,1,-1,0]
dy=[1,0,0,-1]

def in_dex(x,y):
    return 0<x and x<=n and 0<y and y<=n

def check_dir(d):
    if d=='R':
        return 0
    elif d=='L':
        return 3
    elif d=='U':
        return 2
    elif d=='D':
        return 1

d=check_dir(d)

for _ in range(t):
    x,y=r+dx[d],c+dy[d]
    if not in_dex(x,y):
        d=3-d
        continue
    r,c=r+dx[d],c+dy[d]
    

print(r,c,sep=" ")
