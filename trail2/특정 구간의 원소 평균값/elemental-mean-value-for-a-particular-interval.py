n = int(input())
arr = list(map(int, input().split()))

cnt=0
# Please write your code here.
for i in range(n):
    for j in range(i,n):
        total=0
        for k in range(i,j+1):
            total+=arr[k]
        
        l=j-i+1

        if total%l !=0:
            continue
        avg=total//l

        if avg in arr[i:j+1]:
            cnt+=1

print(cnt)