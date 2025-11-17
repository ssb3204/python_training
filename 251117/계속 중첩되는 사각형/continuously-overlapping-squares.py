n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
ls=[[0 for _ in range(200)] for _ in range(200)]

for i in range(n):
    if i%2==0:
        for j in range(x1[0],x2[0]):
            for k in range(y1[0],y2[0]):
                ls[j+100][k+100]=1
    else:
        for j in range(x1[1],x2[1]):
            for k in range(y1[1],y2[1]):
                ls[j+100][k+100]=2

sum=0
for i in ls:
    for j in i:
        if j==2:
            sum+=1

print(sum)