n, k = map(int, input().split())
x = []
c = []

arr=[]
total=0
max=0
cntmax=0

for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

for i in x:
    if i>max:
        max=i

for i in range(max):
    arr.append(0)

for i in range(len(x)):
    if c[i]=='G':
        arr[x[i]-1]+=1
    elif c[i]=='H':
        arr[x[i]-1]+=2

if k>max:
    for i in arr:
        cntmax+=i
    print(cntmax)
else:
    for i in range(max-k):
        for j in range(i,i+k+1):
            total+=arr[j]
            if cntmax< total:
                cntmax=total
        total=0
    print(cntmax)