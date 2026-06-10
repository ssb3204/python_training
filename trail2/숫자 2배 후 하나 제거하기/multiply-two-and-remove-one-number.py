import sys
n = int(input())
arr = list(map(int, input().split()))

mn= sys.maxsize
total=0
# Please write your code here.
for i in range(n):
    total=0
    ls=arr.copy()
    ls[i]*=2
    
    for j in range(n):
        dls=ls.copy()
        del dls[j]
        total=0
        for k in range(n-2):
            total+=abs(dls[k]-dls[k+1])
        if mn>total:
            mn=total

print(mn)