n = int(input())
arr = list(input().split())


cnt=0
ls=arr.copy()
# Please write your code here.
for i in range(n):
    now=chr(ord('A')+i)
    for j in range(n):
        if arr[j]==now:
            where=ord(arr[j])-ord('A')
            if j>where:
                for k in range(j,where,-1):
                    tmp=arr[k]
                    arr[k]=arr[k-1]
                    arr[k-1]=tmp
                    cnt+=1
            else:
                for k in range(j,where):
                    tmp=arr[k]
                    arr[k]=arr[k+1]
                    arr[k+1]=tmp
                    cnt+=1
            break
print(cnt)