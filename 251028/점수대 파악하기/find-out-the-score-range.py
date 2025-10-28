ls=list(map(int,input().split()))
a=[0]*10

for i in ls:
    if i ==0:
        break
    if i<10:
        continue
    a[(i//10)-1]+=1

for i in range(10,0,-1):
    print(f"{i*10} - {a[i-1]}") 