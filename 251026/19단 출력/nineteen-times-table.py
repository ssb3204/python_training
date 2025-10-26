for i in range(1,20):
    line=2
    for j in range(1,20):
        if j==19 or line==1:
            print(f"{i} * {j} = {i*j}")
        else:
            print(f"{i} * {j} = {i*j}",end=" / ")
        line-=1
        if line==0:
            line=2