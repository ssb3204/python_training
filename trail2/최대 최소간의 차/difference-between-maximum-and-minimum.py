import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()

min_num=arr[0]
max_num=arr[-1]
total=sys.maxsize
for i in range(10001):
    cost=0
    for j in arr:
        if i+k<j:
            cost+=abs(j-(i+k))
        elif j<i:
            cost+=i-j
    if total>cost:
        total=cost


print(total)