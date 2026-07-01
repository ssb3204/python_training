T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
cnt=0
for i in range(a,b+1):
    min_d1=1000
    min_d2=1000
    for j in range(T):
        if c[j]=='S':
            d1=abs(i-x[j])
            min_d1=min(min_d1,d1)
        elif c[j]=='N':
            d2=abs(i-x[j])
            min_d2=min(min_d2,d2)

    if min_d1<=min_d2:
        cnt+=1

print(cnt)