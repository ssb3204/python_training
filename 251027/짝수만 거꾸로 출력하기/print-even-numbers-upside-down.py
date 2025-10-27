a=int(input())

ls=list(map(int,input().split()))

ls.reverse()

for i in ls:
    if i%2==0:
        print(i,end=" ")