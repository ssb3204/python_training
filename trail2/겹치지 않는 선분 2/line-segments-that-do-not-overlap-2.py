from fractions import Fraction

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

ls=[]
cnt=0
# Please write your code here.
for i in range(n):
    a= Fraction(1,lines[i][1]-lines[i][0])
    b= Fraction(-(a)*lines[i][0])
    ls.append((a,b))


for i in range(n):
    for j in range(n):
        if i==j:
            continue
        a1,b1 = ls[i]
        a2,b2 = ls[j]
        if a1==a2:
            continue
        
        y = (a2*b1-a1*b2)/(a2-a1)
        if 0<=y<=1:
            break
    else:
        cnt+=1

print(cnt)