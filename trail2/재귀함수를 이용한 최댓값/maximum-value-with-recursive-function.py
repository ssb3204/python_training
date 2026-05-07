n = int(input())
arr = list(map(int, input().split()))
mn=0
# Please write your code here.
def f(n):
    if n==0:
        return max(arr[n],mn)
    
    return max(f(n-1),arr[n-1])

num=f(n)
print(num)
        