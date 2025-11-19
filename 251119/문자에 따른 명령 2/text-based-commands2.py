dirs = list(input())
x,y=0,0
dx,dy=[0,1,0,-1],[1,0,-1,0]
d=0
# Please write your code here.
for i in range(len(dirs)):
    if dirs[i]=="L":
        d-=1
    elif dirs[i]=="R":
        d+=1
    elif dirs[i]=="F":
        x,y= x+dx[d],y+dy[d]
        
print(x,y)