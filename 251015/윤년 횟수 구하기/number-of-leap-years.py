a=int(input())

cnt=0

for i in range(1,a):
    if i%100!=0 and i%400==0:
        cnt+=1
    elif i%4==0:
        cnt+=1

print(cnt)