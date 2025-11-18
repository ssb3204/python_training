N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
ls=[[0,i] for i in range(1,N+1)]

is_t=False
num=1
while True:
    if is_t or num>M:
        break
    
    for i in ls:
        if i[1]==student[num-1]:
            i[0]+=1
        if i[0]==K:
            print(i[1])
            is_t=True
            break
    num+=1

if is_t==False:
    print(-1)
