n, m = map(int, input().split())
arr = list(map(int, input().split()))



cnt=0
now=0
# Please write your code here.
while(now<n):
    if arr[now]==1:
        cnt+=1
        now+=2*m+1
    else:
        now+=1



print(cnt)