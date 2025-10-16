a=int(input())


cnt=0
i=1
while(1):
    if a<=1:
        print(cnt)
        break
    a=a/i
    cnt+=1
    
    i+=1