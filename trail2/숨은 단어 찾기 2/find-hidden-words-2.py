N, M = map(int, input().split())
arr = [input() for _ in range(N)]

cnt=0
# Please write your code here.
for i in range(N):
    for j in range(M):
        if arr[i][j]=='L':
            if j-2>=0:
                if arr[i][j-1]=='E' and arr[i][j-2]=='E':
                    cnt+=1
            if j+2<M:
                if arr[i][j+1]=='E' and arr[i][j+2]=='E':
                    cnt+=1
            if i-2>=0:
                if arr[i-1][j]=='E' and arr[i-2][j]=='E':
                    cnt+=1
            if i+2<N:
                if arr[i+1][j]=='E' and arr[i+2][j]=='E':
                    cnt+=1    


            if i-2>=0 and j-2>=0:
                if arr[i-1][j-1]=='E' and arr[i-2][j-2]=='E':
                    cnt+=1
            if i-2>=0 and j+2<M:
                if arr[i-1][j+1]=='E' and arr[i-2][j+2]=='E':
                    cnt+=1
            if i+2<N and j-2>=0:
                if arr[i+1][j-1]=='E' and arr[i+2][j-2]=='E':
                    cnt+=1
            if  i+2<N and j+2<M:
                if arr[i+1][j+1]=='E' and arr[i+2][j+2]=='E':
                    cnt+=1
print(cnt)