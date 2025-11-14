n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

ls=[0 for _ in range(101)]

for i in segments:
    for j in range(i[0],i[1]+1):
        ls[j-1]+=1
ls.sort()

print(ls[len(ls)-1])