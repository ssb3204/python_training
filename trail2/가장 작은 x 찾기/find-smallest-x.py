n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.
for i in range(1,10000):
    num=i
    in_range=False
    for j in range(n):
        num*=2
        if a[j]<=num<=b[j]:
            in_range=True
            continue
        else:
            in_range=False
            break
    if in_range:
        print(i)
        break

