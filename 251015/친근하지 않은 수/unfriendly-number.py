a=int(input())
cnt=a
for i in range(1,a+1):
    if i%2==0 or i%3==0 or i%5==0:
        cnt-=1
print(cnt)