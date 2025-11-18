n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
sum=0
num=0
for i in range(n):
    if arr[i]>t:
        sum+=1
    else:
        sum=0
    num=max(sum,num)

print(num)