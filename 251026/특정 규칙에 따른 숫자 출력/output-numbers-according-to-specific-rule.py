a=int(input())

cnt=1
for i in range(a,0,-1):
    for j in range(a-i):
        print(" ",end=" ")
    for j in range(i,0,-1):
        if cnt==10:
            cnt=1
        print(cnt,end=" ")
        cnt+=1
    print()