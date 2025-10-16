cnt=0
while(1):
    if cnt==3:
        break
    a=int(input())
    if a%2==0:
        print(a//2)
    else:
        continue
    cnt+=1