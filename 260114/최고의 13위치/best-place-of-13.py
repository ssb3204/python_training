n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ma=0
# Please write your code here.
for i in range(n):
    for j in range(n-2):
        ma= max(ma,grid[i][j]+grid[i][j+1]+grid[i][j+2])
    
print(ma)