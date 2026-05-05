n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

num=0
total=0
# Please write your code here.
if m==1:
    print(2*n)
else:
    for i in range(n):
        cnt=1
        for j in range(n-1):
            if grid[i][j]==grid[i][j+1]:
                cnt=cnt+1
                if cnt>=m:
                    total+=1
                    break
            else:
                cnt=1
    for j in range(n):
        cnt=1
        for i in range(n-1):
            if grid[i][j]==grid[i+1][j]:
                cnt+=1
                if cnt>=m:
                    total+=1
                    break
            else:
                cnt=1

    print(total)
