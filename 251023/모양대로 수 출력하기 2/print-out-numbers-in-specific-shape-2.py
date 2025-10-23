a=int(input())
cnt=2
for i in range(a):
    for j in range(a):
        if cnt>=10:
            cnt=2
        print(cnt,end=" ")
        cnt+=2
    print()