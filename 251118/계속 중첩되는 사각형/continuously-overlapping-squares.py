n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
ls=[["none" for _ in range(201)] for _ in range(201)]

for i in range(n):
    if i%2==0:
        for j in range(x1[i],x2[i]):
            for k in range(y1[i],y2[i]):
                ls[j+100][k+100]="red"
    else:
        for j in range(x1[i],x2[i]):
            for k in range(y1[i],y2[i]):
                ls[j+100][k+100]="blue"

sum=0
for i in ls:
    for j in i:
        if j=="blue":
            sum+=1

print(sum)