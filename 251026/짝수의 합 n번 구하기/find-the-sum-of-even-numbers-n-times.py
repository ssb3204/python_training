a=int(input())

for i in range(a):
    b,c=map(int,input().split())
    sum=0
    for j in range(b,c+1):
        if j%2==0:
            sum+=j
    print(sum)