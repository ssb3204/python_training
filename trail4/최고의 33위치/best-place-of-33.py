n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
mn=0
# Please write your code here.
for i in range(0,n-2):
    for j in range(0,n-2):
        num=0
        for x in range(3):
            for y in range(3):
                if grid[i+x][j+y]==1:
                    num+=1
        mn=max(mn,num)
print(mn)