m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
dom=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum=0
if m1!=m2:
    sum+=dom[m1]-d1+d2+1

    for i in range(m1+1,m2):
        sum+=dom[i]
else:
    if d2!=d1:
        sum+=d2-d1+1
    else:
        sum+=1

print(sum)