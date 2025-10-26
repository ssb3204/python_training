a=int(input())

for i in range(1,a+1):
    cnt=1
    for j in range(i,a+1):
        if j==a:
            print(f"{i} * {cnt} = {i*cnt}")
        else:
            print(f"{i} * {cnt} = {i*cnt}",end=" / ")
        cnt+=1