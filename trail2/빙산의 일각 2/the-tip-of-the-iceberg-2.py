n = int(input())
h = [int(input()) for _ in range(n)]

one_block=False
total=0
mn=max(h)

for _ in range(mn):
    cnt=0
    one_block=False
    for i in range(n):
        if h[i]!=0:
            one_block=True
        elif one_block==True and h[i]==0:
            cnt+=1
            one_block=False

    if one_block==True and i+1==n:
        cnt+=1

    if total<cnt:
        total=cnt

    for j in range(n):
        h[j]-=1
        if h[j]<0:
            h[j]=0

    if not any(h):
        break

print(total)