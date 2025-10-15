sum=0
for _ in range(10):
    a=int(input())
    if 200>=a and a>=0:
        sum+=a

print(f"{sum} {sum/10:.1f}")