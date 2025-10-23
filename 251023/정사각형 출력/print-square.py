a=int(input())
cnt=1
for i in range(a):
    for _ in range(a):
        print(cnt,end=" ")
        cnt+=1
    print()