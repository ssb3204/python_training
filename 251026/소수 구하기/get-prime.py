a=int(input())

for i in range(1,a+1):
    cnt=0
    for j in range(1,i):
        if i%j==0:
            cnt+=1
    if cnt==1:
        print(i,end=" ")
