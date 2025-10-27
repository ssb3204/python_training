ls=list(map(int,input().split()))

for i in ls:
    if i!=0:
        if i%2!=0:
            print(i+3,end=" ")
        else:
            print(i//2,end=" ")
    else:
        break
