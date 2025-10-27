ls=list(map(int,input().split()))
sum=0
su=0
for i in range(1,11):
    if i%2==0:
        sum+=ls[i-1]
    if i%3==0:
        su+=ls[i-1]

print(f"{sum} {su/3:.1f}")