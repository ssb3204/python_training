ls=[0]*5

for i in range(3):
    a,b=map(str,input().split())
    if a=="Y" and int(b)>=37:
        ls[0]+=1
    elif a=="N" and int(b)>=37:
        ls[1]+=1
    elif a=="Y" and int(b)<37: 
        ls[2]+=1
    else:
        ls[3]+=1

if ls[0]>=2:
    ls[4]="E"
else:
    ls[4]=0

for i in ls:
    print(i,end=" ")