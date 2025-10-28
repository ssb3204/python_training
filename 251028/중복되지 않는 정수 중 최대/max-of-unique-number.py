n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max_v=0
is_t=False
for i in nums:
    if nums.count(i)==1:
        is_t=True
        if max_v<i:
            max_v=i

if is_t:
    print(max_v)
else:
    print(-1)