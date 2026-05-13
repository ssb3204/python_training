N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

min=10000
# Please write your code here.
for i in range(N):
    for j in range(N-T+1-i):
        total=arr[j:j+T+i]
        cnt=0
        for k in total:
            cnt+=abs(k-H)
        if min>cnt:
                min=cnt   
        

print(min)