x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

# Please write your code here.
ls=[[True for _ in range(2001)]for _ in range(2001)]
n=2
for i in range(n):
    for j in range(x1[i],x2[i]):
        for k in range(y1[i],y2[i]):
            ls[j+1000][k+1000]=False

for j in range(x1[2],x2[2]):
    for k in range(y1[2],y2[2]):
        ls[j+1000][k+1000]=True


sum=0
for i in ls:
    for j in i:
        if j==False:
            sum+=1

print(sum)