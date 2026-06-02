N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
mn=0
# Please write your code here.

P.sort()

for i in range(N):
    cnt=0
    total=0
    for j in range(N):
        if i==j:
            total+=P[j]/2
            if total<=B:
                cnt+=1
                if mn<cnt:
                    mn=cnt
            else:
                if mn<cnt:
                    mn=cnt
                break
        else:
            total+=P[j]
            if total<=B:
                cnt+=1
                if mn<cnt:
                    mn=cnt
            else:
                if mn<cnt:
                    mn=cnt
                break
        

print(mn)