ls =[0]*10
num=list(map(int,input().split()))
for i in range(10):
    if num[i]!=0:
        ls[i]=num[i]
    else:
        break
    
ls.reverse()

for i in ls:
    if i!=0:
        print(i,end=" ")