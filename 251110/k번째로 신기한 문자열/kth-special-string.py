n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
ls=[]
for i in str:
    if i.startswith(t):
        ls.append(i)

ls.sort()
print(ls[k-1])