n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.
ls=[0 for _ in range(101)]
all=False

for i in range(n):
    for j in range(x1[i],x2[i]+1):
        ls[j]+=1
        if ls[j]==n-1:
            all=True

if all:
    print("Yes")
else:
    print("No")