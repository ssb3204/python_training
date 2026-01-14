n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

for i in range(n):
    for j in range(n):
        print(gird[i][j])