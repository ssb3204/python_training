a=int(input())

cnt=a

for i in range(1,a+1):
    if i%100==0 and i%400!=0:
        cnt-=1
    elif i%4!=0:
        cnt-=1

print(cnt)