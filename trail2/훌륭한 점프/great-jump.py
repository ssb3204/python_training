n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
start=arr[0]
start_ind=0
min_ls=[start]

while(True):  
    min_num_val=101
    for i in range(start_ind+1,min(start_ind+k,n-1)+1):
        if min_num_val>arr[i]:
            min_num_val=arr[i]
            min_num=i
    start_ind=min_num
    min_ls.append(arr[start_ind])
    if start_ind==n-1:
        break

print(max(min_ls))