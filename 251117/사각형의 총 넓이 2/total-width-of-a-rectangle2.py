n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
ls=[[0 for _ in range(200)]for _ in range(200)]

for i in range(n):
    for j in range(x1[i],x2[i]):
        for k in range(y1[i],y2[i]):
            ls[j+100][k+100]=1
sum=0
for i in ls:
    for j in i:
        if j==1:
            sum+=1

print(sum)