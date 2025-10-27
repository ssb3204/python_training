ls =[0]*10
num=list(map(int,input().split()))
cnt=0
sum=0
for i in range(10):
    if num[i]!=0:
        sum+=num[i]
        cnt+=1
    else:
        break
    

print(f"{sum} {sum/cnt:.1f}")
