N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
sum=0
num=0
is_t=True
for i in range(N):
    if arr[i]>0:
        if is_t==False:
            sum=0
            is_t=True
        sum+=1
    else:
        if is_t:
            sum=0
            is_t=False
        sum+=1
    num=max(sum,num)

print(num)