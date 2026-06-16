a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
ls=[False for _ in range(101)]
cnt=0

for i in range(a,b):
    if ls[i]==False:
        ls[i]=True
for j in range(c,d):
    if ls[j]==False:
        ls[j]=True
for k in ls:
    if k:
        cnt+=1

print(cnt)