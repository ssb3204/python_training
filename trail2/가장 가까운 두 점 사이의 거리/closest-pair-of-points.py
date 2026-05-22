n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

total=1000000
# Please write your code here.
for i in range(n):
    for j in range(i+1,n):
        total=min(total,(x[i]-x[j])**2+(y[i]-y[j])**2)

print(total)