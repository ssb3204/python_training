N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
arr.sort()
total=0
for i in range(N):
    ls=[arr[i],arr[i]+K]
    cnt=0
    for j in range(N):
        if ls[0]<=arr[j]<=ls[1]:
            
            cnt+=1
    if total<cnt:
        total=cnt

print(total)