ls = list(map(int,input().split()))
sum=0
cnt=0
for i in ls:
    if i>=250:
        break
    else:
        sum+=i
        cnt+=1

print(f"{sum} {sum/cnt:.1f}")