N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

dis=[]
mx=0
# Please write your code here.
for i in range(N):
    dis=[]
    for j in range(N):
        if i==j:
            num=P[i]//2 + S[i]
            dis.append(num)
        else:
            num=P[j]+S[j]
            dis.append(num)

    dis.sort()
    total=0
    cnt=0
    for j in range(N):
        total+=dis[j]
        if total<=B:
            cnt+=1
        else:
            mx=max(cnt,mx)

            break
print(mx)