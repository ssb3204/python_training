n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
sum=1
num=1
for i in range(n-1):
    if arr[i]<arr[i+1]:
        sum+=1
    else:
        sum=1
    num=max(sum,num)

print(num)