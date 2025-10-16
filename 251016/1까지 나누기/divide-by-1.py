a=int(input())


cnt=0
i=1
while(1):
    a=a/i
    cnt+=1
    if a<=1:
        print(cnt-1)
        break
    i+=1