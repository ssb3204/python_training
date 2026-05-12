n, k = map(int, input().split())
arr = list(map(int, input().split()))
max=0
total=0
# Please write your code here.
for i in range(n-k+1):
    for j in range(i,i+k):
        total+= arr[j]
        if total>max:
            max=total
    total=0

print(max)