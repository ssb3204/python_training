a = list(map(int, input().split()))

# Please write your code here.
a.sort()

print(max(a[1] - a[0], a[2] - a[1]) - 1)