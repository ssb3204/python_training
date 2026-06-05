n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

realm=max(max(l),max(r))
ls=[0 for _ in range(realm+1)]
ok=False
total=0
cnt=0
# Please write your code here.
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            ok=False
            ls=[0 for _ in range(realm+1)]
            for x in range(n):
                if x!= i and x!=j and x!=k:
                    for y in range(l[x],r[x]+1):
                        ls[y]+=1

            if max(ls)<=1:
                ok=True
                total+=1
            else:
                ok=False




print(total)