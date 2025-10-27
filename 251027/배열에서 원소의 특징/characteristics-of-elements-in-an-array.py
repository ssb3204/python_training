ls=list(map(int,input().split()))


for i in range(1,10):
    if ls[i]%3==0:
        print(ls[i-1])
        break