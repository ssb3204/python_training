a,b=map(int,input().split())

for i in range(1,10):
    num=b
    for j in range(a,b+1,2):
        if j==b:
            print(f"{num} * {i} = {num*i}")
        else:
            print(f"{num} * {i} = {num*i}",end=" / ")
            num-=2