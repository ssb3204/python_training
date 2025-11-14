n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

max=0
# Please write your code here.
for i in segments:
    if i[0]>max:
        max=i[0]
    if i[1]>max:
        max=i[1]

ls=[0 for _ in range(max)]

for i in segments:
    for j in range(i[0],i[1]+1):
        ls[j-1]+=1
ls.sort()

print(ls[len(ls)-1])