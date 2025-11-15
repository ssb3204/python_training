n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
MAX=10000
ls=[[0, "none"] for _ in range(MAX)]

now=MAX//2

for i in range(n):
    a=int(x[i])
    b=dir[i]
    if b=="R":
        for j in range(now,now+a):
            ls[j][0]+=1
            ls[j][1]="black"
        now+=a-1
    else:
        for j in range(now,now-a,-1):
            ls[j][0]+=1
            ls[j][1]="white"
        now=now-a+1

        
b,w,g=0,0,0
for i in ls:
    if i[0]==0:
        continue
    if i[0]>=4:
        g+=1
    elif i[1]=="black":
        b+=1
    elif i[1]=="white":
        w+=1

print(w,b,g,sep=" ")