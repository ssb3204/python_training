ls=list(map(int,input().split()))

a=[0]*9

for i in ls:
    if i==0:
        break
    if i<10:
        continue
    else:
        a[(i//10)-1]+=1
    

for i in range(9):
    print(f"{i+1} - {a[i]}")