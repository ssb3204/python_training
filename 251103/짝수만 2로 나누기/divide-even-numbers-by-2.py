n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def f(a):
    return a//2

for i in arr:
    if i%2==0:
        print(f(i),end=" ")
    else:
        print(i,end=" ")