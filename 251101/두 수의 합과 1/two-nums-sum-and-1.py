a,b=map(int,input().split())

num=str(a+b)
cnt=0
for i in num:
    if i=="1":
        cnt+=1
print(cnt)