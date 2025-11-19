n, m = map(int, input().split())

ls1=[0 for _ in range(1000001)]
ls2=[0 for _ in range(1000001)]

now=1
for _ in range(n):
    direction, time = input().split()
    for _ in range(int(time)):
        if direction=="R":
            ls1[now]=ls1[now-1]+1
            now+=1
        else:
            ls1[now]=ls1[now-1]-1
            now+=1
        
now=1
for _ in range(m):
    direction, time = input().split()
    for _ in range(int(time)):
        if direction=="R":
            ls2[now]=ls2[now-1]+1
            now+=1
        else:
            ls2[now]=ls2[now-1]-1
            now+=1

x=-1
for i in range(1,now):
    if ls1[i]==ls2[i]:
        x=i
        break
print(x)

    
