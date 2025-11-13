m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
dom=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
s=0
for i in range(m1+1):
    s+=dom[i]

s+=d1
f=0
for i in range(m2+1):
    f+=dom[i]
f+=d2


print(f-s)