n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ls=[]
sum=0
num=0
for i in range(n-1):
    if arr[i]==arr[i+1]:
        num+=1
    else:
        num=0
    sum=max(sum,num)

print(sum+1)
        