k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

total=0
for x in arr[0]:
    ls=[]
    num=x
    for y in arr:
        for i in y:
            if y.index(num) < y.index(i):
                ls.append(i)
    for i in arr[0]:
        if ls.count(i)==k:
            total+=1

print(total)
