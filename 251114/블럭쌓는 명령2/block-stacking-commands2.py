n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
max=0
ls=[0 for _ in range(n)]

for i in commands:
    for j in range(i[0],i[1]+1):
        ls[j-1]+=1

ls.sort()
print(ls[len(ls)-1])