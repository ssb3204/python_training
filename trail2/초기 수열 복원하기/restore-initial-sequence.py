n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(1,n+1):
    prev=i
    ls=[prev]
    for j in range(n-1):
        ls.append(arr[j]-prev)
        prev=arr[j]-prev

    if len(ls)==len(set(ls)) and all(1<=j<=n for j in ls):
        for k in ls:
            print(k,end=" ")
        break