N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
mn=0
# Please write your code here.

for i in range(N):
    for j in range(i+1,min(i+K+1,N)):
        if num[i]==num[j]:
            if mn<num[i]:
                mn=num[i]

if mn==0:
    print("-1")
else:
    print(mn)