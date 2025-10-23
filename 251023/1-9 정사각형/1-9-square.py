a=int(input())
cnt=1
for i in range(a):
    for _ in range(a):
        if cnt>=10:
            cnt=1
        print(cnt,end="")
        cnt+=1
    print()