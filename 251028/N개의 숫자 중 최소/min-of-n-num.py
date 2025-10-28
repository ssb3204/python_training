n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()

print(a[0],a.count(a[0]),sep=" ")