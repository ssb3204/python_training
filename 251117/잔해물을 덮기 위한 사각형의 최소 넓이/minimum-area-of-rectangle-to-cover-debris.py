x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

ls=[[0 for _ in range(2000)]for _ in range(2000)]

for j in range(x1[0],x2[0]):
    for k in range(y1[0],y2[0]):
        ls[j+1000][k+1000]=1

for j in range(x1[1],x2[1]):
    for k in range(y1[1],y2[1]):
        ls[j+1000][k+1000]=2

min_x=2000
min_y=2000
max_x=0
max_y=0

sum=0
for i in range(2000):
    for j in range(2000):
        if ls[i][j]==1:
            if i<min_x:
                min_x=i
            elif i>max_x:
                max_x=i
            if j<min_y:
                min_y=j
            elif j>max_y:
                max_y=j
if not any(1 in i for i in ls):
    print(0)
else:
    sum=(max_x-min_x+1)*(max_y-min_y+1)
    print(sum)