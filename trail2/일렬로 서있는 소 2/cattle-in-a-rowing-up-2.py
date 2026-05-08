N = int(input())
A = list(map(int, input().split()))
cnt=0
# Please write your code here.
for i in range(len(A)):
    fir = A[i]
    for j in range(i+1,len(A)):
        sec=A[j]
        for k in range(j+1,len(A)):
            thr= A[k]
            if fir <= sec <=thr:
                cnt+=1

print(cnt)