sum=0
cnt=0
for _ in range(10):
    a=int(input())
    if 200>=a and a>=0:
        sum+=a
        cnt+=1

print(f"{sum} {sum/cnt:.1f}")