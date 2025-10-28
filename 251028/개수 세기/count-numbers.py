a,b=map(int,input().split())

ls=list(map(int,input().split()))
cnt=0
for i in ls:
    if i==b:
        cnt+=1

print(cnt)