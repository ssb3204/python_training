a=int(input())


cnt=0
i=1
while(1):
    a=a//i
    cnt+=1
    if 1>=a:
        print(cnt)
        break
    i+=1