import sys

n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
total=sys.maxsize
for i in range(n):
    cnt=0
    num=0
    for j in range(i,n+i):
        cnt+=a[j%n]*num
        num+=1
    if total>cnt:
        total=cnt
print(total)
