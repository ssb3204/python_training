N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
ls=[]
# Please write your code here.
def in_range(j):
    if j>=0 and j<=N-1:
        return True
    else:
        return False

for i in range(N):
    for j in range(i-K,i+K+1):
        if in_range(j) and i!=j:
            if num[i]==num[j]:
                ls.append(num[i])
                break


cnt={}
for i in ls:
    cnt[i]=cnt.get(i,0)+1

if cnt:
    max_cnt = max(cnt.values())
    result=0
    for i,j in cnt.items():
        if j==max_cnt:
            if i>result:
                result=i
else:
    result=0

print(result)
