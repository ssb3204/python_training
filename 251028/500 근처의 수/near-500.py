ls=list(map(int,input().split()))

max_v=0
min_v=1000

for i in ls:
    if i<500 and i>max_v:
        max_v=i
    if i>500 and i<min_v:
        min_v=i

print(max_v,min_v,sep=" ")