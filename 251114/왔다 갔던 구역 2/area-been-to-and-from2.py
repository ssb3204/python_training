n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
ls=[0 for _ in range(n*20)]
now=n*10
for i in range(n):
    if dir[i]=="R":
        for j in range(now,now+int(x[i])):
            ls[j]+=1
        now=now+int(x[i])
    elif dir[i]=="L":
        for j in range(now-1,now-int(x[i])-1,-1):
            ls[j]+=1
        now=now-int(x[i])
cnt=0
for i in ls:
    if i>=2:
        cnt+=1

print(cnt)