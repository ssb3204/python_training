n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
ls = [[0 for _ in range(200)] for _ in range(200)]

for i in range(n):
    for j in range(x[i],x[i]+8):
        for k in range(y[i],y[i]+8):
            ls[j+100][k+100]=1
sum=0
for i in ls:
    for j in i:
        if j==1:
            sum+=1

print(sum)