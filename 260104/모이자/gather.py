import sys
n = int(input())
A = list(map(int, input().split()))
min=sys.maxsize

for i in range(n):
    sum=0
    for j in range(n):
        sum=sum+A[j]*abs(i-j)
    if min>sum:
            min=sum   
print(min)
