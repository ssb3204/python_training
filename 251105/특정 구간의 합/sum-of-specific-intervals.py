n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
def f(a,b):
    global arr
    global sum
    for i in range(a-1,b):
        sum+=arr[i]
    return sum


for i in range(m):
    sum=0
    a,b=map(int,input().split())
    print(f(a,b))


