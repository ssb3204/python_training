n = int(input())
blocks = [int(input()) for _ in range(n)]
total=0
# Please write your code here.
for i in blocks:
    total+=i

total=total//n

dif=0
for i in range(n):
    if blocks[i]<total:
        dif+=abs(blocks[i]-total)

print(dif)