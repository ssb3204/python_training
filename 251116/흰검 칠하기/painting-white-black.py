n = int(input())
commands = []

for _ in range(n):
    a=input().split()
    if not a:
        break
    if len(a)!=2:
        break
    commands.append(tuple(a))
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
MAX=200050
ls=[[0,0, "none"] for _ in range(MAX)]

now=MAX//2

for i in range(n):
    a=int(x[i])
    b=dir[i]
    if b=="R":
        for j in range(now,now+a):
            ls[j][0]+=1
            ls[j][2]="black"
        now+=a-1
    elif b=="L":
        for j in range(now,now-a,-1):
            ls[j][1]+=1
            ls[j][2]="white"
        now=now-a+1

        
b,w,g=0,0,0
for i in ls:
    if i[2]=="none":
        continue
    if i[0]>=2 and i[1]>=2:
        g+=1
    elif i[2]=="black":
        b+=1
    elif i[2]=="white":
        w+=1

print(w,b,g,sep=" ")