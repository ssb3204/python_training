a=int(input())
cnt=1
for i in range(a):
    for j in range(a):
        if cnt>=a:
            cnt=1
        print(cnt*2,end=" ")
        cnt+=1
    print()