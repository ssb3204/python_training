a=int(input())
cnt=0
while(1):
    if a==1:
        print(cnt)
        break
    if a%2!=0:
        a=a*3+1
    else:
        a=a/2
        
    cnt+=1