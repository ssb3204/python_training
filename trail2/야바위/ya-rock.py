n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

total=0

# Please write your code here.
for i in range(3):
    ls=[0,0,0]
    ls[i]+=1
    max_total=0
    for j in range(n):
        tmp=ls[a[j]-1]
        ls[a[j]-1]=ls[b[j]-1]
        ls[b[j]-1]=tmp
        if ls[c[j]-1]==1:
            max_total+=1
    
    if total<max_total:
        total=max_total   

print(total) 
