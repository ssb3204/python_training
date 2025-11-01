a,b=map(str,input().split())
cnt=0
for i in range(int(a)):
    c=input()
    if b==c:
        cnt+=1

print(cnt)