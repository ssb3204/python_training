import sys

N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here.
heights.sort()
total=sys.maxsize
for i in range(0,101):
    max_num=i+17
    cost=0

    for j in heights:
        if j<i:
            cost+=(i-j)**2
        elif j> max_num:
            cost+=(j-max_num)**2
    total=min(total,cost)

print(total)