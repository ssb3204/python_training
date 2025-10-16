a,b,c=map(int,input().split())

is_t=True

for i in range(a,b+1):
    if i%c==0:
        is_t =False

if is_t:
    print("YES")
else:
    print("NO")