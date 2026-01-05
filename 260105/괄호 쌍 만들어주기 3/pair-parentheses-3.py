A = input()
n=len(A)
# Please write your code here.
cnt=0
for i in range(n):
    if A[i]=='(':
        for j in range(i+1,n):
            if A[j]==')':
                cnt+=1
        
print(cnt)
        