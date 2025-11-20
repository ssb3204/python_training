commands = list(input())

# Please write your code here.
dx=[0,1,0,-1]
dy=[1,0,-1,0]

d=0
cnt=0
is_t=False
x,y=0,0

for i in commands:
    if i=="F":
        x,y=x+dx[d],y+dy[d]
    elif i=="R":
        d+=1
    elif i=="L":
        d-=1
    cnt+=1
    if x==0 and y==0:
        is_t=True
        break

print(cnt if is_t else -1)