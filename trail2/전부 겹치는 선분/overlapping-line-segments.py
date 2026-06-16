n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.
ls=[0 for _ in range(101)]
th=False
for i in range(n):
    for j in range(x1[i],x2[i]+1):
        ls[j]+=1
        if ls[j]==n:
            th=True
if th:
    print("Yes")
else:
    print("No")