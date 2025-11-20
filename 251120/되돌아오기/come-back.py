N = int(input())

x,y=0,0
cnt=0
is_t=False

for i in range(N):
    if is_t:
        break
    m,d=input().split()
    d=int(d)

    for _ in range(d):
        if m=='N':
            y+=1
        elif m=='E':
            x+=1
        elif m=="S":
            y-=1
        elif m=='W':
            x-=1
        cnt+=1
        if x==0 and y==0:
            is_t=True
            break

print(cnt if is_t else -1)