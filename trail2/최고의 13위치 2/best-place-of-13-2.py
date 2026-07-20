n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

total=0
# Please write your code here.
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for x in range(n-2):
                if i==k and abs(j-x)<3:
                    continue
                cnt=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[k][x]+arr[k][x+1]+arr[k][x+2]
                total=max(total,cnt)

print(total)