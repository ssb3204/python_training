n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

total=0
# Please write your code here.
for i in range(1,n+1):
    starting_index=arr[i]
    max_total=0
    for j in range(m):
        max_total+=arr[starting_index]
        starting_index=arr[starting_index]
    
    if total<max_total:
        total=max_total

print(total)
    