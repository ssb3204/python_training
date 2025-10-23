a= int(input())
cnt=9
for i in range(a):
    for j in range(a):
        if cnt<=0:
            cnt=9
        print(cnt,end="")
        cnt-=1
    print()