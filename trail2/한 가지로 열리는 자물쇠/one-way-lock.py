N = int(input())
a, b, c = map(int, input().split())

cnt=0
# Please write your code here.
for i in range(1,N+1):
    if i>a+2 or i<a-2:
        for j in range(1,N+1):
            if j>b+2 or j<b-2:
                for k in range(1,N+1):
                    if k>c+2 or k<c-2:
                        cnt+=1


print((N*N*N)-cnt)