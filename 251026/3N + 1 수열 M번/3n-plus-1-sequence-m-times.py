a=int(input())

for i in range(a):
    b=int(input())
    cnt=0
    while(b!=1):
        if b%2==0:
            b/=2
            cnt+=1
        else:
            b=b*3+1
            cnt+=1
    print(cnt)