n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
min=101
max=-101
for i in segments:
    if i[0]<0 and i[0]<min:
        min=i[0]
    if i[1]<0 and i[1]<min:
        min=i[1]
    if i[0]>=0 and i[0]>max:
        max=i[0]
    if i[1]>=0 and i[1]>max:
        max=i[1]

ls=[0 for _ in range(max+1)]

for i in segments:
    if min<0:
        a=i[0]+abs(min)
        b=i[1]+abs(min)
    else:
        a=i[0]
        b=i[1]
    for j in range(a,b):
        ls[j]+=1
ls.sort()

print(ls[len(ls)-1])