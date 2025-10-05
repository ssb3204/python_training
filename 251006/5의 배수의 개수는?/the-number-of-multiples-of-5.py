lf = [list(map(int,input().split())) for _ in range(4)]
sum=0
for i in range(4):
    for j in range(4):
        if lf[i][j]%5==0:
            sum+=1
print(sum)