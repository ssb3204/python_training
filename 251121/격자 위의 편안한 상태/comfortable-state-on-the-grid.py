n, m = map(int, input().split())
ls =[[0 for _ in range(n)] for _ in range(n)]

# Please write your code here.
def in_dex(x,y):
    return 1<=x and x<=n-2 and 1<=y and y<=n-2


def check(x,y):
    cnt=0
    if in_dex(x,y):
        if ls[x+1][y]==1:
            cnt+=1
        if ls[x][y+1]==1:
            cnt+=1
        if ls[x-1][y]==1:
            cnt+=1
        if ls[x][y-1]==1:
            cnt+=1
        if cnt==3:
            return 1
        else:
            return False


for i in range(m):
    x,y=map(int,input().split())
    x=x-1
    y=y-1
    ls[x][y]=1
    if check(x,y):
        print(1)
    else:
        print(0)
