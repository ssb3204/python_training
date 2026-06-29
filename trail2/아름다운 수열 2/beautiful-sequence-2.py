N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
cnt=0
# Please write your code here.
for i in range(N-M+1):
    ls=[]
    for j in range(M):
        ls.append(A[i+j])
    ls.sort()
    if B==ls:
        cnt+=1
    
print(cnt)