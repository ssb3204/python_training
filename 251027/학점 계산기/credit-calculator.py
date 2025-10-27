a=int(input())
sum=0

b=list(map(float,input().split()))
for i in b:
    sum+=i

print(f"{sum/a:.1f}")
if sum/a>=4.0:
    print("Perfect")
elif sum/a>=3.0:
    print("Good")
else:
    print("Poor")