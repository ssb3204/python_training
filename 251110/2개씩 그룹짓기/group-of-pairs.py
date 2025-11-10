n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
ls=[]
for i in range(len(nums)//2):
    sum=nums[i]+nums[len(nums)-1-i]
    ls.append(sum)

ls.sort()
print(ls[len(ls)-1])