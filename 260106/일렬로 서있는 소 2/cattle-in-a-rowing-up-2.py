N = int(input())
A = list(map(int, input().split()))
cnt=0
# Please write your code here.
for i in range(N):
    a=A[i]
    for j in range(i+1,N):
        if a<=A[j] and j !=N+1:
            b=A[j]
            for k in range(j+1,N):
                if b<=A[k]:
                    cnt+=1

print(cnt)