m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
dom=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

total=0
cal_date=0
if m1>m2:
    for i in range(m2+1,m1):
        total+=dom[i]
    cal_date=(d1-1)+dom[m2]-(d2-1)+total
    print(days[-cal_date%7])
elif m1<m2:
    for i in range(m1+1,m2):
        total+=dom[i]
    cal_date=(dom[m1]-d1)+d2+total
    print(days[cal_date%7])
else:
    cal_date=d2-d1
    print(days[cal_date%7])