ls =[0]*10
num=list(map(int,input().split()))
cnt=0
sum=0
for i in range(10):
    if num[i]==0:
        break
        
    elif num[i]%2==0:
        sum+=num[i]
        cnt+=1

print(f"{cnt} {sum}")