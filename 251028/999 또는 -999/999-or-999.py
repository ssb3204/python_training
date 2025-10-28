ls=list(map(int,input().split()))
min_v=999
max_v=-999
for i in ls:
    if i==999 or i==-999:
        break
    if i>max_v:
        max_v=i
    if i<min_v:
        min_v=i

print(max_v,min_v,sep=" ")