n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
total=0

# Please write your code here.
def in_range(a,b):
    return 0<=a<n and 0<=b<n 


for i in range(n):
    for j in range(n):
        for k in range(2*n):
            cost=k*k+(k+1)*(k+1)
            if cost>n*n*m:
                break

            gold = 0
            for dx in range(-k,k+1):
                for dy in range(-k,k+1):
                    if abs(dx)+abs(dy)<=k:
                        x,y=dx+i,dy+j
                        if in_range(x,y):
                            gold+=grid[x][y]
        
        
            if gold*m>=cost:
                total=max(total,gold)
print(total)