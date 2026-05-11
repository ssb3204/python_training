N, S = map(int, input().split())
arr = list(map(int, input().split()))

total=0
min=10000
# Please write your code here.
for i in arr:
    total+=i


for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        sum=arr[i]+arr[j]
        diff=total-sum
        if abs(S-abs(diff))<min:
            min=abs(S-abs(diff))

print(min)
        