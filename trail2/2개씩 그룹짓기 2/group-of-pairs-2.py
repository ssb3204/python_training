import sys

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
cnt=sys.maxsize

for i in range(n):
    a=abs(arr[i]-arr[i+n])
    cnt=min(a,cnt)

print(cnt)