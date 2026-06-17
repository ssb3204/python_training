N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.
ls=[None for _ in range(11)]
cnt=0
for i in range(N):
    
    if ls[pigeon[i]]==None:
        ls[pigeon[i]]=position[i]
    elif ls[pigeon[i]]==1 and position[i]==0:
        ls[pigeon[i]]=position[i]
        cnt+=1
    elif ls[pigeon[i]]==0 and position[i]==1:
        ls[pigeon[i]]=position[i]
        cnt+=1

print(cnt)



