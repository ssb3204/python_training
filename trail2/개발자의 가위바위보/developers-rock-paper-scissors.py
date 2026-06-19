N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# Please write your code here.
case=[(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]

total=0

for s,r,p in case:
    win=0
    answer=[(s,p),(r,s),(p,r)]

    for i in range(N):
        if (a[i],b[i]) in answer:
            win+=1
    
    if total<win:
        total=win

print(total)