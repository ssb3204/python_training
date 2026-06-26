m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
months=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]


total=0
cnt=0

if m1<m2:
    for i in range(m1+1,m2):
        total+=months[i]
    dates=(months[m1]-d1)+d2+total
    for i in range(1,dates+1):
        if days[i%7]==A:
            cnt+=1
else:
    dates=abs(d2-d1)
    if d2>d1:
        for i in range(1,dates+1):
            if days[i%7]==A:
                cnt+=1
    else:
        for i in range(1,dates+1):
            if days[-i%7]==A:
                cnt+=1

print(cnt)