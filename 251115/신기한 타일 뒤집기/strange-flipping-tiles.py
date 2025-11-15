n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
MAX=20000
ls=[["none"] for _ in range(MAX)]

now=MAX//2

for i in range(n):
    a=int(x[i])
    b=dir[i]
    if b=="R":
        for j in range(now,now+a):
            ls[j]="black"
        now+=a-1
    elif b=="L":
        for j in range(now,now-a,-1):
            ls[j]="white"
        now=now-a+1

        
b,w=0,0
for i in ls:
    if i=="none":
        continue
    if i=="black":
        b+=1
    elif i=="white":
        w+=1

print(w,b,sep=" ")