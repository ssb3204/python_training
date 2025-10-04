a=int(input())


for _ in range(a):
    x,y = map(int,input().split())
    sum=0
    for i in range(x,y+1):
        if i%2==0:
            sum+=i
    print(sum)